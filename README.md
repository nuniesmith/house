# Construction Management Suite - Docker Deployment

This guide provides instructions for containerizing and deploying the Construction Management Suite using Docker and Docker Compose.

## 📋 Prerequisites

- Docker Engine 20.10 or later
- Docker Compose 2.0 or later
- Git (for cloning the repository)

## 🏗️ Project Structure

```
construction-management-suite/
├── Dockerfile              # Container definition
├── docker-compose.yml      # Multi-container orchestration
├── nginx.conf              # Nginx web server configuration
├── .dockerignore           # Files to exclude from Docker build
├── index.html              # Main application shell
├── dashboard.html          # Dashboard page
├── calculator.html         # Cost calculator
├── scheduler.html          # Project scheduler
├── bunker.html            # Bunker blueprints
├── house.html             # Farmhouse blueprints
├── cabin.html             # Cabin blueprints
├── bunker.md              # Bunker construction guide
├── house.md               # Farmhouse construction guide
├── cabin.md               # Cabin construction guide
├── main.js                # Main application logic
└── js/
    └── modules/
        └── marked.js       # Markdown parser
```

## 🚀 Quick Start

### Option 1: Using Docker Compose (Recommended)

1. **Clone or prepare your project files:**
   ```bash
   # Ensure all your HTML, JS, CSS, and MD files are in the project directory
   ls -la
   # Should show: index.html, dashboard.html, calculator.html, etc.
   ```

2. **Start the application:**
   ```bash
   docker-compose up -d
   ```

3. **Access the application:**
   - Open your browser and navigate to: `http://localhost:8080`
   - The Construction Management Suite welcome screen should appear

4. **Stop the application:**
   ```bash
   docker-compose down
   ```

### Option 2: Using Docker directly

1. **Build the image:**
   ```bash
   docker build -t construction-management-suite .
   ```

2. **Run the container:**
   ```bash
   docker run -d \
     --name construction-app \
     -p 8080:80 \
     construction-management-suite
   ```

3. **Access the application:**
   - Navigate to: `http://localhost:8080`

## 🔧 Configuration Options

### Environment Variables

The application can be configured using environment variables in the `docker-compose.yml`:

```yaml
environment:
  - NGINX_HOST=localhost
  - NGINX_PORT=80
```

### Port Configuration

To change the external port, modify the `docker-compose.yml`:

```yaml
ports:
  - "3000:80"  # Application will be available on port 3000
```

### Volume Mounts for Development

For development with live file updates, uncomment the volume mount in `docker-compose.yml`:

```yaml
volumes:
  - ./:/usr/share/nginx/html:ro
```

This allows you to edit files locally and see changes immediately without rebuilding.

## 🌐 Production Deployment

### Option 1: Basic Production Setup

1. **Build for production:**
   ```bash
   docker-compose -f docker-compose.yml up -d --build
   ```

2. **Use environment-specific configuration:**
   ```bash
   # Create production environment file
   echo "NGINX_HOST=your-domain.com" > .env
   echo "NGINX_PORT=80" >> .env
   
   docker-compose --env-file .env up -d
   ```

### Option 2: With Reverse Proxy (Traefik)

Uncomment the Traefik service in `docker-compose.yml` for automatic SSL and routing:

```yaml
traefik:
  image: traefik:v2.10
  container_name: traefik
  # ... configuration
```

### Option 3: Behind External Load Balancer

For deployment behind external load balancers (AWS ALB, CloudFlare, etc.):

1. **Modify nginx.conf** to trust forwarded headers:
   ```nginx
   real_ip_header X-Forwarded-For;
   set_real_ip_from 10.0.0.0/8;
   ```

2. **Update security headers** for your domain:
   ```nginx
   add_header Content-Security-Policy "default-src 'self' https://your-domain.com;...";
   ```

## 🔍 Monitoring and Logging

### View Application Logs

```bash
# View real-time logs
docker-compose logs -f construction-app

# View nginx access logs
docker-compose exec construction-app tail -f /var/log/nginx/construction_access.log

# View nginx error logs
docker-compose exec construction-app tail -f /var/log/nginx/construction_error.log
```

### Health Checks

The container includes a health check endpoint:

```bash
# Check container health
docker-compose ps

# Manual health check
curl http://localhost:8080/health
```

## 🐛 Troubleshooting

### Common Issues

1. **Port already in use:**
   ```bash
   # Check what's using port 8080
   lsof -i :8080
   
   # Use a different port
   docker-compose down
   # Edit docker-compose.yml to change port mapping
   docker-compose up -d
   ```

2. **Files not loading:**
   ```bash
   # Check if all required files are present
   docker-compose exec construction-app ls -la /usr/share/nginx/html/
   
   # Check nginx configuration
   docker-compose exec construction-app nginx -t
   ```

3. **Permission issues:**
   ```bash
   # Fix file permissions
   docker-compose exec construction-app chmod -R 755 /usr/share/nginx/html
   ```

### Performance Optimization

1. **Enable additional caching:**
   ```nginx
   # Add to nginx.conf
   location ~* \.(html|js|css)$ {
       expires 24h;
       add_header Cache-Control "public, must-revalidate";
   }
   ```

2. **Optimize Docker image size:**
   ```dockerfile
   # Use multi-stage build for smaller images
   FROM nginx:alpine AS production
   COPY --from=build /app/dist /usr/share/nginx/html
   ```

## 📊 Scaling

### Horizontal Scaling

```yaml
# In docker-compose.yml
services:
  construction-app:
    deploy:
      replicas: 3
    ports:
      - "8080-8082:80"
```

### Load Balancing

Use the included Traefik configuration or external load balancers:

```yaml
# Traefik labels for load balancing
labels:
  - "traefik.enable=true"
  - "traefik.http.services.construction.loadbalancer.server.port=80"
```

## 🔒 Security

### HTTPS Setup

For production, always use HTTPS:

1. **With Traefik (automatic):**
   ```yaml
   labels:
     - "traefik.http.routers.construction.tls.certresolver=letsencrypt"
   ```

2. **With external SSL termination:**
   - Configure your load balancer for SSL
   - Update nginx.conf to handle forwarded headers

### Security Headers

The nginx configuration includes security headers:
- X-Frame-Options
- X-XSS-Protection  
- X-Content-Type-Options
- Content-Security-Policy

## 📈 Maintenance

### Updates

1. **Update application:**
   ```bash
   # Pull latest changes
   git pull
   
   # Rebuild and restart
   docker-compose up -d --build
   ```

2. **Update base image:**
   ```bash
   # Update nginx base image
   docker-compose pull
   docker-compose up -d --force-recreate
   ```

### Backup

```bash
# Backup application data (if using volumes)
docker run --rm -v construction-data:/data -v $(pwd):/backup alpine tar czf /backup/construction-backup.tar.gz /data

# Backup configuration
cp docker-compose.yml nginx.conf /path/to/backup/
```

## 🎯 Next Steps

1. **Domain Setup:** Configure your domain to point to the server
2. **SSL Certificate:** Set up HTTPS using Let's Encrypt or your certificate provider
3. **Monitoring:** Add application monitoring with tools like Prometheus/Grafana
4. **CI/CD:** Set up automated deployment pipelines
5. **Backup Strategy:** Implement automated backups for any user data

## 🆘 Support

For issues with the Docker deployment:

1. Check the troubleshooting section above
2. Review container logs: `docker-compose logs`
3. Verify all required files are present in the project directory
4. Ensure Docker and Docker Compose are properly installed

The application should be accessible at `http://localhost:8080` and display the Construction Management Suite welcome screen with options to launch the full application or access specific tools.# house
