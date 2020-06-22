import os

bind = '127.0.0.1:8090'
backlog = 2048

def get_workers():
    procs = os.sysconf('SC_NPROCESSORS_ONLN')
    if procs > 0:
        return procs * 2 + 1
    else:
        return 3
        
workers = get_workers()
# worker_class = 'egg:gunicorn#eventlet'
worker_connections = 1000
timeout = 600
keepalive = 2

debug = False
spew = False

daemon = False
pidfile = None
umask = 0
user = None
group = None
tmp_upload_dir = None

logfile = '-'
loglevel = 'info'
accesslog = '-'

proc_name = None