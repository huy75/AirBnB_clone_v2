#!/usr/bin/python3
# Fabfile to distribute an archive to a web server.
from os import path
from fabric.api import env, put, run, sudo

env.hosts = ["35.227.45.0", "35.237.153.115"]
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'


def do_deploy(archive_path):
    """Distributes an archive to a web server.
    Args:
        archive_path (str): The path of the archive to distribute.
    Returns:
        If the file doesn't exist at archive_path or an error occurs - False.
        Otherwise - True.
    """
    if not path.exists(archive_path):
        return False

    base_name = path.basename(archive_path)
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

        cmd = "mv /data/web_static/releases/{}/web_static/* \
        /data/web_static/releases/{}/"
        sudo(cmd.format(name, name))

        run("rm -rf /data/web_static/releases/{}/web_static/")

        """ Delete the symbolic link from the web server """
        run("rm -rf /data/web_static/current")
        """
        Create a new the symbolic link on the web server,
        linked to the new version of the code
        """
        run("ln -s /data/web_static/releases/{} /data/web_static/current"
            .format(name))
        run("service nginx restart")
        return True
    except:
        return False
