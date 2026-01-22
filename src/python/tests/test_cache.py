"""
Tests for the cache module.

This module contains unit tests for:
- MemoryCache
- DiskCache
- CacheEntry
- CacheStats
- Caching decorators
- Cache key generation utilities
"""

import sys
import time
from pathlib import Path

import pytest

# Add the src directory to the path for imports
src_path = Path(__file__).parent.parent / "src"
if str(src_path) not in sys.path:
    sys.path.insert(0, str(src_path))

from cache import (
    CacheEntry,
    CacheStats,
    DiskCache,
    MemoryCache,
    cached,
    clear_all_caches,
    generate_config_hash,
    generate_floor_cache_key,
    get_calculation_cache,
    get_render_cache,
)

# =============================================================================
# CACHE ENTRY TESTS
# =============================================================================


class TestCacheEntry:
    """Tests for CacheEntry dataclass."""

    def test_creation(self):
        """Test creating a cache entry."""
        entry = CacheEntry(value="test", created_at=time.time())
        assert entry.value == "test"
        assert entry.hits == 0
        assert entry.expires_at is None

    def test_is_expired_no_expiry(self):
        """Test is_expired when no expiry set."""
        entry = CacheEntry(value="test", created_at=time.time())
        assert entry.is_expired() is False

    def test_is_expired_future(self):
        """Test is_expired when expiry is in the future."""
        entry = CacheEntry(
            value="test",
            created_at=time.time(),
            expires_at=time.time() + 3600,
        )
        assert entry.is_expired() is False

    def test_is_expired_past(self):
        """Test is_expired when expiry is in the past."""
        entry = CacheEntry(
            value="test",
            created_at=time.time() - 100,
            expires_at=time.time() - 50,
        )
        assert entry.is_expired() is True

    def test_access_increments_hits(self):
        """Test that access() increments hit counter."""
        entry = CacheEntry(value="test", created_at=time.time())
        assert entry.hits == 0
        entry.access()
        assert entry.hits == 1
        entry.access()
        assert entry.hits == 2

    def test_access_returns_value(self):
        """Test that access() returns the cached value."""
        entry = CacheEntry(value={"key": "value"}, created_at=time.time())
        result = entry.access()
        assert result == {"key": "value"}


# =============================================================================
# CACHE STATS TESTS
# =============================================================================


class TestCacheStats:
    """Tests for CacheStats dataclass."""

    def test_default_values(self):
        """Test default statistics values."""
        stats = CacheStats()
        assert stats.hits == 0
        assert stats.misses == 0
        assert stats.evictions == 0
        assert stats.total_entries == 0

    def test_hit_rate_no_accesses(self):
        """Test hit rate with no accesses."""
        stats = CacheStats()
        assert stats.hit_rate == 0.0

    def test_hit_rate_all_hits(self):
        """Test hit rate with all hits."""
        stats = CacheStats(hits=10, misses=0)
        assert stats.hit_rate == 1.0

    def test_hit_rate_all_misses(self):
        """Test hit rate with all misses."""
        stats = CacheStats(hits=0, misses=10)
        assert stats.hit_rate == 0.0

    def test_hit_rate_mixed(self):
        """Test hit rate with mixed hits and misses."""
        stats = CacheStats(hits=7, misses=3)
        assert stats.hit_rate == 0.7

    def test_reset(self):
        """Test resetting statistics."""
        stats = CacheStats(hits=10, misses=5, evictions=3, total_entries=20)
        stats.reset()
        assert stats.hits == 0
        assert stats.misses == 0
        assert stats.evictions == 0
        # Note: total_entries is not reset by reset()
        assert stats.total_entries == 20

    def test_str_representation(self):
        """Test string representation."""
        stats = CacheStats(hits=5, misses=5, evictions=2, total_entries=10)
        str_rep = str(stats)
        assert "hits=5" in str_rep
        assert "misses=5" in str_rep
        assert "50.00%" in str_rep


# =============================================================================
# MEMORY CACHE TESTS
# =============================================================================


class TestMemoryCache:
    """Tests for MemoryCache class."""

    def test_set_and_get(self):
        """Test basic set and get operations."""
        cache = MemoryCache()
        cache.set("key1", "value1")
        assert cache.get("key1") == "value1"

    def test_get_nonexistent_key(self):
        """Test getting a key that doesn't exist."""
        cache = MemoryCache()
        assert cache.get("nonexistent") is None

    def test_get_with_default(self):
        """Test getting with a default value."""
        cache = MemoryCache()
        assert cache.get("nonexistent", default="default") == "default"

    def test_has_key(self):
        """Test has() method."""
        cache = MemoryCache()
        cache.set("key1", "value1")
        assert cache.has("key1") is True
        assert cache.has("nonexistent") is False

    def test_delete_key(self):
        """Test deleting a key."""
        cache = MemoryCache()
        cache.set("key1", "value1")
        assert cache.delete("key1") is True
        assert cache.get("key1") is None
        assert cache.delete("key1") is False  # Already deleted

    def test_clear(self):
        """Test clearing the cache."""
        cache = MemoryCache()
        cache.set("key1", "value1")
        cache.set("key2", "value2")
        cache.clear()
        assert cache.size == 0
        assert cache.get("key1") is None

    def test_size(self):
        """Test size property."""
        cache = MemoryCache()
        assert cache.size == 0
        cache.set("key1", "value1")
        assert cache.size == 1
        cache.set("key2", "value2")
        assert cache.size == 2

    def test_max_size_eviction(self):
        """Test that entries are evicted when max size is reached."""
        cache = MemoryCache(max_size=3)
        cache.set("key1", "value1")
        cache.set("key2", "value2")
        cache.set("key3", "value3")
        cache.set("key4", "value4")  # Should evict key1 (LRU)
        assert cache.size == 3
        assert cache.get("key1") is None  # Was evicted
        assert cache.get("key4") == "value4"

    def test_lru_eviction_order(self):
        """Test that LRU eviction follows access order."""
        cache = MemoryCache(max_size=3)
        cache.set("key1", "value1")
        cache.set("key2", "value2")
        cache.set("key3", "value3")
        # Access key1 to make it recently used
        cache.get("key1")
        # Add key4, should evict key2 (oldest accessed)
        cache.set("key4", "value4")
        assert cache.get("key1") == "value1"  # Still there
        assert cache.get("key2") is None  # Was evicted

    def test_ttl_expiration(self):
        """Test TTL expiration."""
        cache = MemoryCache()
        cache.set("key1", "value1", ttl=0.1)
        assert cache.get("key1") == "value1"
        time.sleep(0.15)
        assert cache.get("key1") is None  # Expired

    def test_default_ttl(self):
        """Test default TTL."""
        cache = MemoryCache(default_ttl=0.1)
        cache.set("key1", "value1")
        assert cache.get("key1") == "value1"
        time.sleep(0.15)
        assert cache.get("key1") is None

    def test_stats_tracking(self):
        """Test that statistics are tracked correctly."""
        cache = MemoryCache()
        cache.set("key1", "value1")
        cache.get("key1")  # Hit
        cache.get("key1")  # Hit
        cache.get("nonexistent")  # Miss
        assert cache.stats.hits == 2
        assert cache.stats.misses == 1

    def test_cleanup_expired(self):
        """Test cleanup_expired method."""
        cache = MemoryCache()
        cache.set("key1", "value1", ttl=0.1)
        cache.set("key2", "value2")  # No TTL
        time.sleep(0.15)
        removed = cache.cleanup_expired()
        assert removed == 1
        assert cache.get("key1") is None
        assert cache.get("key2") == "value2"

    def test_various_value_types(self):
        """Test caching various value types."""
        cache = MemoryCache()
        cache.set("string", "hello")
        cache.set("int", 42)
        cache.set("float", 3.14)
        cache.set("list", [1, 2, 3])
        cache.set("dict", {"a": 1, "b": 2})
        cache.set("none", None)

        assert cache.get("string") == "hello"
        assert cache.get("int") == 42
        assert cache.get("float") == 3.14
        assert cache.get("list") == [1, 2, 3]
        assert cache.get("dict") == {"a": 1, "b": 2}
        # Note: None values need special handling
        assert cache.get("none") is None


# =============================================================================
# DISK CACHE TESTS
# =============================================================================


class TestDiskCache:
    """Tests for DiskCache class."""

    @pytest.fixture
    def cache_dir(self, tmp_path):
        """Create a temporary cache directory."""
        return tmp_path / "cache"

    def test_set_and_get(self, cache_dir):
        """Test basic set and get operations."""
        cache = DiskCache(cache_dir)
        cache.set("key1", "value1")
        assert cache.get("key1") == "value1"

    def test_get_nonexistent_key(self, cache_dir):
        """Test getting a key that doesn't exist."""
        cache = DiskCache(cache_dir)
        assert cache.get("nonexistent") is None

    def test_get_with_default(self, cache_dir):
        """Test getting with a default value."""
        cache = DiskCache(cache_dir)
        assert cache.get("nonexistent", default="default") == "default"

    def test_has_key(self, cache_dir):
        """Test has() method."""
        cache = DiskCache(cache_dir)
        cache.set("key1", "value1")
        assert cache.has("key1") is True
        assert cache.has("nonexistent") is False

    def test_delete_key(self, cache_dir):
        """Test deleting a key."""
        cache = DiskCache(cache_dir)
        cache.set("key1", "value1")
        assert cache.delete("key1") is True
        assert cache.get("key1") is None
        assert cache.delete("key1") is False

    def test_clear(self, cache_dir):
        """Test clearing the cache."""
        cache = DiskCache(cache_dir)
        cache.set("key1", "value1")
        cache.set("key2", "value2")
        cache.clear()
        assert cache.size == 0
        assert cache.get("key1") is None

    def test_size(self, cache_dir):
        """Test size property."""
        cache = DiskCache(cache_dir)
        assert cache.size == 0
        cache.set("key1", "value1")
        assert cache.size == 1
        cache.set("key2", "value2")
        assert cache.size == 2

    def test_persistence(self, cache_dir):
        """Test that data persists across cache instances."""
        cache1 = DiskCache(cache_dir)
        cache1.set("key1", "value1")

        # Create new cache instance with same directory
        cache2 = DiskCache(cache_dir)
        assert cache2.get("key1") == "value1"

    def test_ttl_expiration(self, cache_dir):
        """Test TTL expiration."""
        cache = DiskCache(cache_dir)
        cache.set("key1", "value1", ttl=0.1)
        assert cache.get("key1") == "value1"
        time.sleep(0.15)
        assert cache.get("key1") is None

    def test_cleanup_expired(self, cache_dir):
        """Test cleanup_expired method."""
        cache = DiskCache(cache_dir)
        cache.set("key1", "value1", ttl=0.1)
        cache.set("key2", "value2")
        time.sleep(0.15)
        removed = cache.cleanup_expired()
        assert removed == 1
        assert cache.get("key1") is None
        assert cache.get("key2") == "value2"

    def test_complex_values(self, cache_dir):
        """Test caching complex values."""
        cache = DiskCache(cache_dir)
        complex_value = {
            "nested": {"a": 1, "b": [1, 2, 3]},
            "list": [{"x": 1}, {"y": 2}],
        }
        cache.set("complex", complex_value)
        retrieved = cache.get("complex")
        assert retrieved == complex_value

    def test_stats_tracking(self, cache_dir):
        """Test statistics tracking."""
        cache = DiskCache(cache_dir)
        cache.set("key1", "value1")
        cache.get("key1")  # Hit
        cache.get("nonexistent")  # Miss
        assert cache.stats.hits == 1
        assert cache.stats.misses == 1


# =============================================================================
# CACHING DECORATOR TESTS
# =============================================================================


class TestCachedDecorator:
    """Tests for the @cached decorator."""

    def test_basic_caching(self):
        """Test basic function caching."""
        call_count = 0
        cache = MemoryCache()

        @cached(cache=cache)
        def expensive_function(x):
            nonlocal call_count
            call_count += 1
            return x * 2

        result1 = expensive_function(5)
        result2 = expensive_function(5)

        assert result1 == 10
        assert result2 == 10
        assert call_count == 1  # Only called once due to caching

    def test_different_arguments(self):
        """Test that different arguments produce different cache keys."""
        cache = MemoryCache()

        @cached(cache=cache)
        def add(a, b):
            return a + b

        assert add(1, 2) == 3
        assert add(3, 4) == 7
        assert add(1, 2) == 3  # From cache

    def test_keyword_arguments(self):
        """Test caching with keyword arguments."""
        cache = MemoryCache()

        @cached(cache=cache)
        def greet(name, greeting="Hello"):
            return f"{greeting}, {name}!"

        result1 = greet("World")
        result2 = greet("World", greeting="Hello")
        result3 = greet("World", greeting="Hi")

        assert result1 == "Hello, World!"
        assert result2 == "Hello, World!"
        assert result3 == "Hi, World!"

    def test_cache_with_ttl(self):
        """Test caching with TTL."""
        call_count = 0
        cache = MemoryCache()

        @cached(cache=cache, ttl=0.1)
        def get_time():
            nonlocal call_count
            call_count += 1
            return call_count

        result1 = get_time()
        result2 = get_time()
        assert result1 == result2 == 1

        time.sleep(0.15)
        result3 = get_time()
        assert result3 == 2  # Cache expired, function called again

    def test_cache_clear_method(self):
        """Test that decorated function has cache_clear method."""
        cache = MemoryCache()

        @cached(cache=cache)
        def func(x):
            return x

        func(1)
        func(2)
        assert cache.size > 0

        func.cache_clear()  # type: ignore[attr-defined]
        assert cache.size == 0

    def test_custom_key_function(self):
        """Test caching with custom key function."""
        cache = MemoryCache()

        def custom_key(x, y):
            return f"sum_{x + y}"

        @cached(cache=cache, key_func=custom_key)
        def add(x, y):
            return x + y

        # These should share the same cache entry
        result1 = add(1, 4)  # key: sum_5
        result2 = add(2, 3)  # key: sum_5

        assert result1 == 5
        assert result2 == 5
        # Both calls return the first cached value (5 from 1+4)


# =============================================================================
# CONFIG HASH TESTS
# =============================================================================


class TestConfigHash:
    """Tests for config hash generation."""

    def test_generate_config_hash_basic(self):
        """Test basic config hash generation."""
        config = {"key": "value", "nested": {"a": 1}}
        hash1 = generate_config_hash(config)
        assert isinstance(hash1, str)
        assert len(hash1) == 16

    def test_generate_config_hash_deterministic(self):
        """Test that same config produces same hash."""
        config = {"key": "value", "nested": {"a": 1}}
        hash1 = generate_config_hash(config)
        hash2 = generate_config_hash(config)
        assert hash1 == hash2

    def test_generate_config_hash_different_configs(self):
        """Test that different configs produce different hashes."""
        config1 = {"key": "value1"}
        config2 = {"key": "value2"}
        hash1 = generate_config_hash(config1)
        hash2 = generate_config_hash(config2)
        assert hash1 != hash2

    def test_generate_config_hash_order_independent(self):
        """Test that key order doesn't affect hash."""
        config1 = {"a": 1, "b": 2}
        config2 = {"b": 2, "a": 1}
        hash1 = generate_config_hash(config1)
        hash2 = generate_config_hash(config2)
        assert hash1 == hash2

    def test_generate_floor_cache_key(self):
        """Test floor cache key generation."""
        config = {"rooms": [{"label": "Bedroom"}]}
        key = generate_floor_cache_key("main", config, "png")
        assert "floor_main_png_" in key
        assert len(key) > 20  # Has hash suffix

    def test_generate_floor_cache_key_different_floors(self):
        """Test that different floors produce different keys."""
        config = {"rooms": []}
        key1 = generate_floor_cache_key("main", config, "png")
        key2 = generate_floor_cache_key("basement", config, "png")
        assert key1 != key2

    def test_generate_floor_cache_key_different_formats(self):
        """Test that different formats produce different keys."""
        config = {"rooms": []}
        key1 = generate_floor_cache_key("main", config, "png")
        key2 = generate_floor_cache_key("main", config, "svg")
        assert key1 != key2


# =============================================================================
# GLOBAL CACHE TESTS
# =============================================================================


class TestGlobalCaches:
    """Tests for global cache instances."""

    def test_get_calculation_cache(self):
        """Test getting calculation cache."""
        cache = get_calculation_cache()
        assert isinstance(cache, MemoryCache)

    def test_get_render_cache(self):
        """Test getting render cache."""
        cache = get_render_cache()
        assert isinstance(cache, MemoryCache)

    def test_clear_all_caches(self):
        """Test clearing all global caches."""
        calc_cache = get_calculation_cache()
        render_cache = get_render_cache()

        calc_cache.set("test", "value")
        render_cache.set("test", "value")

        clear_all_caches()

        assert calc_cache.get("test") is None
        assert render_cache.get("test") is None


# =============================================================================
# EDGE CASES AND ERROR HANDLING
# =============================================================================


class TestEdgeCases:
    """Tests for edge cases and error handling."""

    def test_memory_cache_empty_key(self):
        """Test with empty string key."""
        cache = MemoryCache()
        cache.set("", "empty key value")
        assert cache.get("") == "empty key value"

    def test_memory_cache_special_characters_in_key(self):
        """Test with special characters in key."""
        cache = MemoryCache()
        cache.set("key:with:colons", "value1")
        cache.set("key/with/slashes", "value2")
        cache.set("key with spaces", "value3")
        assert cache.get("key:with:colons") == "value1"
        assert cache.get("key/with/slashes") == "value2"
        assert cache.get("key with spaces") == "value3"

    def test_memory_cache_update_existing_key(self):
        """Test updating an existing key."""
        cache = MemoryCache()
        cache.set("key", "value1")
        cache.set("key", "value2")
        assert cache.get("key") == "value2"

    def test_disk_cache_creates_directory(self, tmp_path):
        """Test that DiskCache creates the cache directory."""
        cache_dir = tmp_path / "new" / "nested" / "cache"
        assert not cache_dir.exists()
        cache = DiskCache(cache_dir)
        assert cache_dir.exists()

    def test_config_hash_with_non_json_serializable(self):
        """Test config hash with non-JSON-serializable values."""
        from datetime import datetime

        config = {
            "datetime": datetime.now(),
            "path": Path("/some/path"),
        }
        # Should not raise, should fall back to string representation
        hash_value = generate_config_hash(config)
        assert isinstance(hash_value, str)

    def test_cache_entry_zero_ttl(self):
        """Test cache entry with zero TTL (immediately expired)."""
        entry = CacheEntry(
            value="test",
            created_at=time.time(),
            expires_at=time.time(),  # Expires immediately
        )
        # Might be expired depending on timing
        # This is mainly to ensure it doesn't crash

    def test_memory_cache_concurrent_access_pattern(self):
        """Test pattern that might occur with concurrent access."""
        cache = MemoryCache(max_size=5)

        # Simulate rapid set/get pattern
        for i in range(100):
            cache.set(f"key{i % 10}", f"value{i}")
            cache.get(f"key{(i + 1) % 10}")

        # Cache should still be functional
        assert cache.size <= 5
        cache.set("final", "value")
        assert cache.get("final") == "value"


# =============================================================================
# PERFORMANCE TESTS
# =============================================================================


class TestPerformance:
    """Performance-related tests (not actual benchmarks)."""

    def test_memory_cache_many_entries(self):
        """Test memory cache with many entries."""
        cache = MemoryCache(max_size=1000)

        # Add many entries
        for i in range(500):
            cache.set(f"key{i}", f"value{i}")

        assert cache.size == 500

        # Verify some entries
        assert cache.get("key0") == "value0"
        assert cache.get("key499") == "value499"

    def test_cache_hit_rate_tracking(self):
        """Test that hit rate is properly tracked over many operations."""
        cache = MemoryCache()

        # Pre-populate cache
        for i in range(10):
            cache.set(f"key{i}", f"value{i}")

        # 50% hits, 50% misses
        for i in range(20):
            if i % 2 == 0:
                cache.get(f"key{i // 2}")  # Hit
            else:
                cache.get(f"nonexistent{i}")  # Miss

        hit_rate = cache.stats.hit_rate
        assert 0.4 <= hit_rate <= 0.6  # Approximately 50%
