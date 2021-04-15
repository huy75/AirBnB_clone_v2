#!/usr/bin/python3
# Fabfile to delete out-of-date archives.
import os
from fabric.api import *

env.hosts = ['35.227.45.0', '35.237.153.115']


def do_clean(number=0):
    """
    Args:
        number (int): The number of archives to keep.
    If number is 0 or 1, keep only the most recent archive.
    If number is 2, keep the most and second most recent archives,
    etc.
    """
    number = int(number)
    number = 2 if number < 1 else number + 1
    local("ls -d -1tr versions/* | tail -n +{} | \
    xargs -d '\n' rm -f --".format(number))

    run("ls -d -1tr /data/web_static/releases/* | tail -n +{} | \
    xargs -d '\n' rm -rf --".format(number))
