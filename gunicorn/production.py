bind = "unix:/tmp/tutelage.sock"
workers = 3
daemon = True
pidfile = "/var/run/gunicorn/tutelage.pid"
loglevel = "error"
proc_name = "tutelage"
worker_class = "gevent"
debug = False
logfile = "/var/log/gunicorn/tutelage.log"
user = "gunicorn"
group = "gunicorn"

