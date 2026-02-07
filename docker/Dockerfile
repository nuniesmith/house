# ============================================
# FloorPlan Designer - Simple Static Dockerfile
# ============================================
# Serves HTML/JS/Assets from nginx
# For personal house build planning project
# ============================================

FROM nginx:alpine

# Remove default nginx website
RUN rm -rf /usr/share/nginx/html/*

# Copy the HTML application files (includes assets subfolder)
COPY src/html/ /usr/share/nginx/html/

# Copy custom nginx configuration
COPY config/nginx.conf /etc/nginx/conf.d/default.conf

# Set proper permissions
RUN chmod -R 755 /usr/share/nginx/html

# Expose port 80
EXPOSE 80

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD curl -f http://localhost/ || exit 1

# Start nginx
CMD ["nginx", "-g", "daemon off;"]
