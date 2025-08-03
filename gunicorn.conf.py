import os

# Server Socket
bind = f"0.0.0.0:{os.environ.get('PORT', 5000)}"
backlog = 2048

# Worker Processes
workers = int(os.environ.get('WEB_CONCURRENCY', 1))
worker_class = 'sync'
worker_connections = 1000
timeout = 30
keepalive = 2

# Restart Workers
max_requests = 1000
max_requests_jitter = 50

# Logging
accesslog = '-'
errorlog = '-'
loglevel = 'info'

# Process naming
proc_name = 'professor_website'

# Server mechanics
preload_app = True
daemon = False
pidfile = None
user = None
group = None
tmp_upload_dir = None

# SSL
keyfile = None
certfile = None