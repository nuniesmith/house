"""
Caching utilities for floor plan generation.

This module provides caching mechanisms to avoid redundant calculations
and improve performance when generating multiple floor plans or formats.
"""

import hashlib
import json
import logging
import pickle
import time
from collections.abc import Callable
from dataclasses import dataclass
from functools import wraps
from pathlib import Path
from typing import Any, TypeVar

logger = logging.getLogger(__name__)

# Type variable for generic function return types
T = TypeVar("T")


@dataclass
class CacheEntry:
    """A single cache entry with metadata."""

    value: Any
    created_at: float
    expires_at: float | None = None
    hits: int = 0

    def is_expired(self) -> bool:
        """Check if this cache entry has expired."""
        if self.expires_at is None:
            return False
        return time.time() > self.expires_at

    def access(self) -> Any:
        """Access the cached value and increment hit counter."""
        self.hits += 1
        return self.value


@dataclass
class CacheStats:
    """Statistics for cache performance monitoring."""

    hits: int = 0
    misses: int = 0
    evictions: int = 0
    total_entries: int = 0

    @property
    def hit_rate(self) -> float:
        """Calculate the cache hit rate."""
        total = self.hits + self.misses
        if total == 0:
            return 0.0
        return self.hits / total

    def reset(self) -> None:
        """Reset all statistics."""
        self.hits = 0
        self.misses = 0
        self.evictions = 0

    def __str__(self) -> str:
        return (
            f"CacheStats(hits={self.hits}, misses={self.misses}, "
            f"hit_rate={self.hit_rate:.2%}, evictions={self.evictions}, "
            f"entries={self.total_entries})"
        )


class MemoryCache:
    """
    In-memory cache for expensive calculations.

    Features:
    - TTL (time-to-live) support
    - Maximum size with LRU eviction
    - Statistics tracking
    - Thread-safe operations (basic)

    Example usage:
        >>> cache = MemoryCache(max_size=100, default_ttl=300)
        >>> cache.set("room_area_123", 450.5)
        >>> area = cache.get("room_area_123")
    """

    def __init__(
        self,
        max_size: int = 1000,
        default_ttl: float | None = None,
    ):
        """
        Initialize the cache.

        Args:
            max_size: Maximum number of entries before eviction
            default_ttl: Default time-to-live in seconds (None = no expiry)
        """
        self._cache: dict[str, CacheEntry] = {}
        self._max_size = max_size
        self._default_ttl = default_ttl
        self._stats = CacheStats()
        self._access_order: list[str] = []

    def get(self, key: str, default: Any = None) -> Any:
        """
        Get a value from the cache.

        Args:
            key: Cache key
            default: Value to return if key not found or expired

        Returns:
            Cached value or default
        """
        entry = self._cache.get(key)

        if entry is None:
            self._stats.misses += 1
            return default

        if entry.is_expired():
            self._stats.misses += 1
            self._evict(key)
            return default

        self._stats.hits += 1
        self._update_access_order(key)
        return entry.access()

    def set(
        self,
        key: str,
        value: Any,
        ttl: float | None = None,
    ) -> None:
        """
        Set a value in the cache.

        Args:
            key: Cache key
            value: Value to cache
            ttl: Time-to-live in seconds (None uses default)
        """
        # Evict if at capacity
        while len(self._cache) >= self._max_size:
            self._evict_lru()

        effective_ttl = ttl if ttl is not None else self._default_ttl
        expires_at = time.time() + effective_ttl if effective_ttl else None

        self._cache[key] = CacheEntry(
            value=value,
            created_at=time.time(),
            expires_at=expires_at,
        )
        self._update_access_order(key)
        self._stats.total_entries = len(self._cache)

    def delete(self, key: str) -> bool:
        """
        Delete a key from the cache.

        Args:
            key: Cache key to delete

        Returns:
            True if key was deleted, False if not found
        """
        if key in self._cache:
            self._evict(key)
            return True
        return False

    def clear(self) -> None:
        """Clear all entries from the cache."""
        self._cache.clear()
        self._access_order.clear()
        self._stats.total_entries = 0

    def has(self, key: str) -> bool:
        """Check if a key exists and is not expired."""
        entry = self._cache.get(key)
        if entry is None:
            return False
        if entry.is_expired():
            self._evict(key)
            return False
        return True

    @property
    def stats(self) -> CacheStats:
        """Get cache statistics."""
        return self._stats

    @property
    def size(self) -> int:
        """Get current number of entries."""
        return len(self._cache)

    def _evict(self, key: str) -> None:
        """Evict a specific key."""
        if key in self._cache:
            del self._cache[key]
            self._stats.evictions += 1
            self._stats.total_entries = len(self._cache)
        if key in self._access_order:
            self._access_order.remove(key)

    def _evict_lru(self) -> None:
        """Evict the least recently used entry."""
        if self._access_order:
            lru_key = self._access_order.pop(0)
            self._evict(lru_key)

    def _update_access_order(self, key: str) -> None:
        """Update the access order for LRU tracking."""
        if key in self._access_order:
            self._access_order.remove(key)
        self._access_order.append(key)

    def cleanup_expired(self) -> int:
        """
        Remove all expired entries.

        Returns:
            Number of entries removed
        """
        expired_keys = [key for key, entry in self._cache.items() if entry.is_expired()]
        for key in expired_keys:
            self._evict(key)
        return len(expired_keys)


class DiskCache:
    """
    Disk-based cache for persistent caching across runs.

    Useful for caching generated images or expensive calculations
    that should persist between program executions.

    Example usage:
        >>> cache = DiskCache(cache_dir=Path("./cache"))
        >>> cache.set("floor_plan_hash", png_bytes)
        >>> data = cache.get("floor_plan_hash")
    """

    def __init__(
        self,
        cache_dir: Path | str,
        default_ttl: float | None = None,
    ):
        """
        Initialize the disk cache.

        Args:
            cache_dir: Directory to store cache files
            default_ttl: Default time-to-live in seconds
        """
        self._cache_dir = Path(cache_dir)
        self._cache_dir.mkdir(parents=True, exist_ok=True)
        self._default_ttl = default_ttl
        self._metadata_file = self._cache_dir / "_metadata.json"
        self._metadata = self._load_metadata()
        self._stats = CacheStats()

    def _load_metadata(self) -> dict[str, dict]:
        """Load cache metadata from disk."""
        if self._metadata_file.exists():
            try:
                with self._metadata_file.open() as f:
                    return json.load(f)
            except (json.JSONDecodeError, OSError):
                return {}
        return {}

    def _save_metadata(self) -> None:
        """Save cache metadata to disk."""
        try:
            with self._metadata_file.open("w") as f:
                json.dump(self._metadata, f, indent=2)
        except OSError as e:
            logger.warning(f"Failed to save cache metadata: {e}")

    def _get_cache_path(self, key: str) -> Path:
        """Get the file path for a cache key."""
        # Use hash to avoid filesystem issues with special characters
        key_hash = hashlib.md5(key.encode()).hexdigest()
        return self._cache_dir / f"{key_hash}.cache"

    def get(self, key: str, default: Any = None) -> Any:
        """Get a value from the cache."""
        meta = self._metadata.get(key)
        if meta is None:
            self._stats.misses += 1
            return default

        # Check expiration
        if meta.get("expires_at") and time.time() > meta["expires_at"]:
            self._stats.misses += 1
            self.delete(key)
            return default

        cache_path = self._get_cache_path(key)
        if not cache_path.exists():
            self._stats.misses += 1
            return default

        try:
            with cache_path.open("rb") as f:
                value = pickle.load(f)
            self._stats.hits += 1
            return value
        except (pickle.PickleError, OSError) as e:
            logger.warning(f"Failed to load cache entry {key}: {e}")
            self._stats.misses += 1
            return default

    def set(
        self,
        key: str,
        value: Any,
        ttl: float | None = None,
    ) -> None:
        """Set a value in the cache."""
        cache_path = self._get_cache_path(key)

        effective_ttl = ttl if ttl is not None else self._default_ttl
        expires_at = time.time() + effective_ttl if effective_ttl else None

        try:
            with cache_path.open("wb") as f:
                pickle.dump(value, f)

            self._metadata[key] = {
                "created_at": time.time(),
                "expires_at": expires_at,
                "path": str(cache_path),
            }
            self._save_metadata()
            self._stats.total_entries = len(self._metadata)
        except (pickle.PickleError, OSError) as e:
            logger.warning(f"Failed to cache entry {key}: {e}")

    def delete(self, key: str) -> bool:
        """Delete a key from the cache."""
        if key not in self._metadata:
            return False

        cache_path = self._get_cache_path(key)
        try:
            if cache_path.exists():
                cache_path.unlink()
        except OSError as e:
            logger.warning(f"Failed to delete cache file {cache_path}: {e}")

        del self._metadata[key]
        self._save_metadata()
        self._stats.evictions += 1
        self._stats.total_entries = len(self._metadata)
        return True

    def clear(self) -> None:
        """Clear all cache entries."""
        for key in list(self._metadata.keys()):
            self.delete(key)
        self._metadata.clear()
        self._save_metadata()

    def has(self, key: str) -> bool:
        """Check if a key exists and is not expired."""
        meta = self._metadata.get(key)
        if meta is None:
            return False
        if meta.get("expires_at") and time.time() > meta["expires_at"]:
            self.delete(key)
            return False
        return self._get_cache_path(key).exists()

    @property
    def stats(self) -> CacheStats:
        """Get cache statistics."""
        return self._stats

    @property
    def size(self) -> int:
        """Get current number of entries."""
        return len(self._metadata)

    def cleanup_expired(self) -> int:
        """Remove all expired entries."""
        now = time.time()
        expired_keys = [
            key
            for key, meta in self._metadata.items()
            if meta.get("expires_at") and now > meta["expires_at"]
        ]
        for key in expired_keys:
            self.delete(key)
        return len(expired_keys)


# =============================================================================
# CACHING DECORATORS
# =============================================================================


def cached(
    cache: MemoryCache | DiskCache | None = None,
    key_func: Callable[..., str] | None = None,
    ttl: float | None = None,
) -> Callable[[Callable[..., T]], Callable[..., T]]:
    """
    Decorator to cache function results.

    Args:
        cache: Cache instance to use (creates new MemoryCache if None)
        key_func: Function to generate cache key from arguments
        ttl: Time-to-live for cached results

    Example:
        >>> cache = MemoryCache()
        >>> @cached(cache=cache, ttl=60)
        ... def expensive_calculation(x, y):
        ...     return x ** y
    """
    if cache is None:
        cache = MemoryCache()

    def decorator(func: Callable[..., T]) -> Callable[..., T]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> T:
            # Generate cache key
            if key_func:
                key = key_func(*args, **kwargs)
            else:
                key = _generate_cache_key(func.__name__, args, kwargs)

            # Check cache
            result = cache.get(key)
            if result is not None:
                return result

            # Calculate and cache
            result = func(*args, **kwargs)
            cache.set(key, result, ttl=ttl)
            return result

        # Add cache control methods to the wrapper
        wrapper.cache = cache  # type: ignore
        wrapper.cache_clear = cache.clear  # type: ignore

        return wrapper

    return decorator


def _generate_cache_key(func_name: str, args: tuple, kwargs: dict) -> str:
    """Generate a cache key from function name and arguments."""
    key_parts = [func_name]

    for arg in args:
        key_parts.append(_hash_value(arg))

    for k, v in sorted(kwargs.items()):
        key_parts.append(f"{k}={_hash_value(v)}")

    return ":".join(key_parts)


def _hash_value(value: Any) -> str:
    """Create a hash string for a value."""
    try:
        # Try JSON serialization first
        json_str = json.dumps(value, sort_keys=True, default=str)
        return hashlib.md5(json_str.encode()).hexdigest()[:8]
    except (TypeError, ValueError):
        # Fall back to string representation
        return hashlib.md5(str(value).encode()).hexdigest()[:8]


# =============================================================================
# CONFIG-BASED CACHE KEY GENERATION
# =============================================================================


def generate_config_hash(config: dict[str, Any]) -> str:
    """
    Generate a hash for a floor plan configuration.

    This is useful for caching generated images based on config content.

    Args:
        config: Floor plan configuration dictionary

    Returns:
        Hash string uniquely identifying the configuration
    """
    try:
        config_str = json.dumps(config, sort_keys=True, default=str)
        return hashlib.sha256(config_str.encode()).hexdigest()[:16]
    except (TypeError, ValueError) as e:
        logger.warning(f"Failed to hash config: {e}")
        return hashlib.md5(str(config).encode()).hexdigest()[:16]


def generate_floor_cache_key(
    floor_name: str,
    config: dict[str, Any],
    output_format: str = "png",
) -> str:
    """
    Generate a cache key for a floor plan output.

    Args:
        floor_name: Name of the floor (e.g., "main", "basement")
        config: Floor plan configuration
        output_format: Output format (png, svg, pdf)

    Returns:
        Cache key string
    """
    config_hash = generate_config_hash(config)
    return f"floor_{floor_name}_{output_format}_{config_hash}"


# =============================================================================
# GLOBAL CACHE INSTANCES
# =============================================================================

# Global memory cache for runtime calculations
_calculation_cache = MemoryCache(max_size=500, default_ttl=3600)

# Global memory cache for rendered images (larger, longer TTL)
_render_cache = MemoryCache(max_size=50, default_ttl=None)


def get_calculation_cache() -> MemoryCache:
    """Get the global calculation cache."""
    return _calculation_cache


def get_render_cache() -> MemoryCache:
    """Get the global render cache."""
    return _render_cache


def clear_all_caches() -> None:
    """Clear all global caches."""
    _calculation_cache.clear()
    _render_cache.clear()


# =============================================================================
# EXPORTS
# =============================================================================

__all__ = [
    "CacheEntry",
    "CacheStats",
    "DiskCache",
    "MemoryCache",
    "cached",
    "clear_all_caches",
    "generate_config_hash",
    "generate_floor_cache_key",
    "get_calculation_cache",
    "get_render_cache",
]
