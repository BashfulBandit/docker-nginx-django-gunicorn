# Sample Gunicorn configuration file.

###########################################################
#                       Debugging                         #
###########################################################
# 
# Restart workers when code changes.
reload = True
# reload_engine
# 
# The implementation that should be used to power reload.
reload_engine = 'auto'
# reload_extra_files
# 
# Extends reload option to also watch and reload on additional files (e.g., templates, configurations, specifications, etc.).
reload_extra_files = []
# spew
# 
# Install a trace function that spews every line executed by the server.
# 
# This is the nuclear option.
spew = False
# check_config
# 
# Check the configuration.
check_config = False

###########################################################
#                       Logging                           #
###########################################################
# 
# accesslog
# 
# The Access log file to write to.
accesslog = '-'
# disable_redirect_access_to_syslog
# 
# Disable redirect access logs to syslog.
disable_redirect_access_to_syslog = False
# access_log_format
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'
# errorlog
errorlog = '-'
# loglevel
loglevel = 'info'
# capture_output
capture_output = False
# logger_class
# 
# The logger you want to use to log events in Gunicorn.
logger_class = 'gunicorn.glogging.Logger'
# logconfig
# 
# The log config file to use. Gunicorn uses the standard Python logging module’s Configuration file format.
logconfig = None
# logconfig_dict
# 
# The log config dictionary to use, using the standard Python logging module’s dictionary configuration format. This option takes precedence over the logconfig option, which uses the older file configuration format.
# 
# Format: https://docs.python.org/3/library/logging.config.html#logging.config.dictConfig
logconfig_dict = {}
# syslog_addr
# 
# Address to send syslog messages.
syslog_addr = 'udp://localhost:514'
# syslog
# 
# Send Gunicorn logs to syslog.
syslog = False
# syslog_prefix
# 
# Makes Gunicorn use the parameter as program-name in the syslog entries.
syslog_prefix = None
# syslog_facility
# 
# Syslog facility name
syslog_facility = 'user'
# enable_stdio_inheritance
# 
# Enable inheritance for stdio file descriptors in daemon mode.
# 
enable_stdio_inheritance = False
# statsd_host
# 
# host:port of the statsd server to log to.
statsd_host = None
# statsd_prefix
# 
# Prefix to use when emitting statsd metrics (a trailing . is added, if not provided).
statsd_prefix = None
###########################################################
#                       Process Naming                    #
###########################################################
# proc_name
# 
# A base to use with setproctitle for process naming.
proc_name = None
# default_proc_name
# 
# Internal setting that is adjusted for each type of application.
default_proc_name = 'gunicorn'
###########################################################
#                           SSL                           #
###########################################################
# keyfile
# 
# SSL key file
keyfile = None
# certfile
# 
# SSL certificate file
certfile = None
# ssl_version
# 
# SSL version to use (see stdlib ssl module’s)
ssl_version = 2
# cert_reqs
# 
# Whether client certificate is required (see stdlib ssl module’s)
cert_reqs = 0
# ca_certs
# 
# CA certificates file
ca_certs = None
# suppress_ragged_eofs
# 
# Suppress ragged EOFs (see stdlib ssl module’s)
suppress_ragged_eofs = True
# do_handshake_on_connect
# 
# Whether to perform SSL handshake on socket connect (see stdlib ssl module’s)
do_handshake_on_connect = False
# ciphers
# 
# Ciphers to use (see stdlib ssl module’s)
ciphers = 'TLSv1'
###########################################################
#                         Security                        #
###########################################################
# limit_request_line
# 
# The maximum size of HTTP request line in bytes.
limit_request_line = 4094
# limit_request_fields
# 
# Limit the number of HTTP headers fields in a request.
limit_request_fields = 100
# limit_request_field_size
# 
# Limit the allowed size of an HTTP request header field.
limit_request_field_size = 8190
###########################################################
#                         Server Hooks                    #
###########################################################
def post_fork(server, worker):
    server.log.info("Worker spawned (pid: %s)", worker.pid)

def pre_fork(server, worker):
    pass

def pre_exec(server):
    server.log.info("Forked child, re-executing.")

def when_ready(server):
    server.log.info("Server is ready. Spawning workers")

def worker_int(worker):
    worker.log.info("worker received INT or QUIT signal")

    ## get traceback info
    import threading, sys, traceback
    id2name = {th.ident: th.name for th in threading.enumerate()}
    code = []
    for threadId, stack in sys._current_frames().items():
        code.append("\n# Thread: %s(%d)" % (id2name.get(threadId,""),
            threadId))
        for filename, lineno, name, line in traceback.extract_stack(stack):
            code.append('File: "%s", line %d, in %s' % (filename,
                lineno, name))
            if line:
                code.append("  %s" % (line.strip()))
    worker.log.debug("\n".join(code))

def worker_abort(worker):
    worker.log.info("worker received SIGABRT signal")
###########################################################
#                         Server Mechanics                #
###########################################################
# preload_app
# 
# Load application code before the worker processes are forked.
preload_app = False
# sendfile
# 
# Disables the use of sendfile().
sendfile = None
# reuse_port
# 
# Set the SO_REUSEPORT flag on the listening socket.
reuse_port = False
# daemon
# 
# Daemonize the Gunicorn process.
# 
# Detaches the server from the controlling terminal and enters the background.
daemon = False
# raw_env
# 
# Set environment variable (key=value).
raw_env = []
# pidfile
# 
# A filename to use for the PID file
pidfile = None
# worker_tmp_dir
# 
# A directory to use for the worker heartbeat temporary file.
worker_tmp_dir = None
# user
# 
# Switch worker processes to run as this user.
user = None
# group
# 
# Switch worker process to run as this group.
group = None
# umask
# 
# A bit mask for the file mode on files written by Gunicorn.
umask = 0
# initgroups
# 
# If true, set the worker process’s group access list with all of the groups of which the specified username is a member, plus the specified group id.
initgroups = False
# tmp_upload_dir
# 
# Directory to store temporary request data as they are read.
tmp_upload_dir = None
# secure_scheme_headers
# 
#     {'X-FORWARDED-PROTOCOL': 'ssl', 'X-FORWARDED-PROTO': 'https', 'X-FORWARDED-SSL': 'on'}
# 
# A dictionary containing headers and values that the front-end proxy uses to indicate HTTPS requests. These tell Gunicorn to set wsgi.url_scheme to https, so your application can tell that the request is secure.
secure_scheme_headers = {'X-FORWARDED-PROTOCOL': 'ssl', 'X-FORWARDED-PROTO': 'https', 'X-FORWARDED-SSL': 'on'}
# forwarded_allow_ips
# 
# Front-end’s IPs from which allowed to handle set secure headers. (comma separate).
forwarded_allow_ips = '127.0.0.1'
# pythonpath
# 
# A comma-separated list of directories to add to the Python path.
pythonpath = None
# paste
# 
# Load a PasteDeploy config file. The argument may contain a # symbol followed by the name of an app section from the config file, e.g. production.ini#admin.
paste = None
# proxy_protocol
# 
# Enable detect PROXY protocol (PROXY mode).
proxy_protocol = False
# proxy_allow_ips
# 
# Front-end’s IPs from which allowed accept proxy requests (comma separate).
proxy_allow_ips = '127.0.0.1'
# raw_paste_global_conf
# 
# Set a PasteDeploy global config variable in key=value form.
raw_paste_global_conf = []
###########################################################
#                         Server Socket                   #
###########################################################
# bind
# 
# The socket to bind.
bind = '0.0.0.0:8000'
# backlog
# 
# The maximum number of pending connections.
backlog = 2048
###########################################################
#                      Worker Processes                   #
###########################################################
# workers
# 
# The number of worker processes for handling requests.
workers = 1
# worker_class
# 
# The type of workers to use.
worker_class = 'sync'
# threads
# 
# The number of worker threads for handling requests.
threads = 1
# worker_connections
# 
# The maximum number of simultaneous clients.
worker_connections = 1000
# max_requests
# 
# The maximum number of requests a worker will process before restarting.
max_requests = 0
# max_requests_jitter
# 
# The maximum jitter to add to the max_requests setting.
max_requests_jitter = 0
# timeout
# 
# Workers silent for more than this many seconds are killed and restarted.
timeout = 30
# graceful_timeout
# 
# Timeout for graceful workers restart.
graceful_timeout = 30
# keepalive
# 
# The number of seconds to wait for requests on a Keep-Alive connection.
keepalive = 2