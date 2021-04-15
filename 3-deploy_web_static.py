#!/usr/bin/python3
"""
Python fabric that manages archives for web servers
"""
import os
from fabric.api import *
from datetime import datetime as dt

env.hosts = ['35.227.45.0', '35.237.153.115']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'

now = dt.now()


def do_pack():
    """Packs web_static files into .tgz file"""

    file_name = 'versions/web_static_{}.tgz'\
                .format(now.strftime("%Y%m%d%H%M%S"))

    if not os.path.isdir("versions"):
        if local("mkdir -p versions").failed:
            return None

    command = local("tar -cvzf {} web_static".format(file_name))
    if command.succeeded:
        return file_name
    return None


def do_deploy(archive_path):
    """Distributes an archive to a web server.
    Args:
        archive_path (str): The path of the archive to distribute.
    Returns:
        If the file doesn't exist at archive_path or an error occurs - False.
        Otherwise - True.
    """
    if not os.path.exists(archive_path):
        return False
    base_name = os.path.basename(archive_path)
    name = base_name.split(".")[0]
    try:
        """ Upload the archive to the /tmp/ directory of the web server """
        put(archive_path, "/tmp")

        run("mkdir -p /data/web_static/releases/{}/".format(name))
        """ Uncompress the archive on the web server """
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/"
            .format(base_name, name))

        """ Delete the archive from the web server """
        run("rm /tmp/{}".format(base_name))

        run("mv /data/web_static/releases/{}/web_static/* \
        /data/web_static/releases/{}/".format(name, name))

        run("rm -rf /data/web_static/releases/{}/web_static/".format(name))

        """ Delete the symbolic link from the web server """
        run("rm -rf /data/web_static/current")
        """
        Create a new the symbolic link on the web server,
        linked to the new version of the code
        """
        run("ln -s /data/web_static/releases/{} /data/web_static/current"
            .format(name))
        print("New version deployed!")
        return True
    except:
        return False


def deploy():
    """
    Packs and deploys a webstatic site from an archive
    Returns: Value of do_deploy, False if no archive created
    """
    archive = do_pack()
    if archive is None:
        return False
    return(do_deploy(archive))
