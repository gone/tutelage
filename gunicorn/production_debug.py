bind = "unix:/tmp/tutelage.sock"
workers = 3
daemon = False
pidfile = "/var/run/gunicorn/tutelage_debug.pid"
loglevel = "debug"
proc_name = "tutelage"
worker_class = "gevent"
debug = True
user = "gunicorn"
group = "gunicorn"

