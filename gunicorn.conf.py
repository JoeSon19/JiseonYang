"""
Gunicorn configuration for production deployment.
Optimized for GCE Autoscale deployment with single port configuration.
"""

import os

# Server socket
bind = f"0.0.0.0:{os.environ.get('PORT', 5000)}"
backlog = 2048

# Worker processes
workers = min(4, (os.cpu_count() or 1) + 1)
worker_class = "sync"
worker_connections = 1000
timeout = 30
keepalive = 60

# Restart workers
max_requests = 1000
max_requests_jitter = 50
preload_app = True

# Logging
accesslog = "-"
errorlog = "-"
loglevel = "info"
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'

# Process naming
proc_name = "professor_website"

# Server mechanics
daemon = False
pidfile = None
user = None
group = None
tmp_upload_dir = None

# SSL (not needed for Replit deployment)
keyfile = None
certfile = None