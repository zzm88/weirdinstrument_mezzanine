from __future__ import unicode_literals
import multiprocessing

bind = "unix:/home/root/mezzanine/weirdinstrument_mezzanine/gunicorn.sock"
workers = multiprocessing.cpu_count() * 2 + 1
errorlog = "/home/root/logs/weirdinstrument_mezzanine_error.log"
loglevel = "error"
proc_name = "weirdinstrument_mezzanine"
