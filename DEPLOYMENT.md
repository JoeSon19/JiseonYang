# Deployment Guide

This document provides instructions for deploying the Professor Website on Replit.

## Deployment Fixes Applied

The following fixes have been implemented to resolve deployment issues:

### 1. Simplified Run Command
- **Problem**: Complex run command `pkill python3; python main.py` causing process conflicts
- **Solution**: Created clean startup scripts (`start.py`, `wsgi.py`) for simple execution
- **Alternative commands**:
  - Direct: `python main.py`
  - Production: `gunicorn -c gunicorn.conf.py wsgi:application`
  - Simple: `python start.py`

### 2. Single Port Configuration
- **Problem**: Multiple port configurations (5000→80 and 5001→3000) conflicting with GCE Autoscale
- **Solution**: Application now uses only port 5000 with proper environment variable handling
- **Configuration**: `HOST=0.0.0.0` and `PORT=5000` (or from environment)

### 3. Health Check Endpoints
- **Problem**: Missing proper health checks causing deployment timeout
- **Solution**: Enhanced health check endpoints:
  - `/health` - Comprehensive health check with database status
  - `/ping` - Simple readiness check that returns "pong"

### 4. Production-Ready Configuration
- **Improvements**:
  - Proper error handling and logging
  - Database connection retry logic
  - Environment variable configuration
  - WSGI application setup for Gunicorn

## Deployment Options

### Option 1: Direct Flask (Development/Testing)
```bash
python main.py
```

### Option 2: Production with Gunicorn (Recommended)
```bash
gunicorn -c gunicorn.conf.py wsgi:application
```

### Option 3: Simple Startup Script
```bash
python start.py
```

## Environment Variables

The application supports the following environment variables:

- `PORT`: Server port (default: 5000)
- `HOST`: Server host (default: 0.0.0.0)
- `DATABASE_URL`: PostgreSQL database connection string
- `SECRET_KEY`: Flask secret key for sessions

## Health Check Endpoints

- **GET /health**: Returns comprehensive application health status
  ```json
  {
    "status": "healthy",
    "database": "connected",
    "application": "running",
    "timestamp": "2025-08-03 20:49:53"
  }
  ```

- **GET /ping**: Simple readiness check
  ```
  pong
  ```

## Deployment Process

1. **Ensure all files are saved**
2. **Set environment variables** if needed
3. **Use simple deployment command**: The deployment should now use `python main.py` instead of complex shell commands
4. **Verify health checks**: Access `/health` and `/ping` endpoints to confirm deployment success

## Troubleshooting

### Common Issues
1. **Process conflicts**: Use simple commands without `pkill`
2. **Port binding**: Ensure only one port configuration (5000→80)
3. **Health checks**: Verify endpoints return 200 status codes
4. **Database connection**: Check DATABASE_URL environment variable

### Verification Commands
```bash
# Test health endpoints
curl http://localhost:5000/health
curl http://localhost:5000/ping

# Check application logs
tail -f logs/application.log
```

## Notes

- The application is configured to bind to `0.0.0.0` for deployment compatibility
- Database initialization is handled automatically on startup
- Error handling includes graceful degradation for temporary database issues
- All static files are properly configured for production serving