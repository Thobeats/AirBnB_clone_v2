#!/usr/bin/python3
"""
Write a Fabric script (based on the file 2-do_deploy_web_static.py)
that creates and distributes an archive to your web servers,
using the function deploy
"""
from fabric.api import env, local, run, put
from os.path import exists
from datetime import datetime
env.hosts = ['54.237.67.242', '100.25.0.50']


def do_pack():
    """
    generates a .tgz archive from the contents of the web_static folder
    """
    # create the versions folder
    local("sudo mkdir -p versions")

    # archive name
    currentDate = datetime.now().strftime('%Y%m%d%H%M%S')
    archive = "web_static_{}.tgz".format(currentDate)

    # store in the versions folder
    storage_path = "versions/{}".format(archive)

    archivedResult = local("tar -cvzf {} web_static/".format(storage_path))
    if archivedResult.failed:
        return None
    return (storage_path)


def do_deploy(archive_path):
    """
    distributes an archive to your web servers
    """
    # check if the path exists
    if not exists(archive_path):
        return False

    try:
        # Upload the archive to the /tmp/ directory of the web server
        put(archive_path, '/tmp/')

        # get the archive file name with and without extension
        archive_filename = archive_path.split('/')[-1]
        archive_name = archive_filename.split('.')[0]

        # Uncompress the archive to the folder
        # /data/web_static/releases/<archive filename without extension>
        run("sudo mkdir -p /data/web_static/releases/{}".format(archive_name))
        run("sudo tar -xzf /tmp/{} -C /data/web_static/releases/{}"
            .format(archive_filename, archive_name))

        # Move the files from web_static into its parent folder
        run("sudo mv /data/web_static/releases/{}/web_static/* \
            /data/web_static/releases/{}"
            .format(archive_name, archive_name))

        # Remove the web_static folder
        run("sudo rm -rf /data/web_static/releases/{}/web_static"
            .format(archive_name))

        # Delete the symbolic link /data/web_static/current from the web server
        run("sudo rm -rf /data/web_static/current")

        # create new symbolic link /data/web_static/current
        run("sudo ln -sf /data/web_static/releases/{} /data/web_static/current"
            .format(archive_name))
        return True
    except Exception:
        return False



def deploy():
    """
    distributes an archive to your web servers
    """
    # check if the path exists
    archive_path = do_pack()
    if not archive_path:
        return False

    try:
        # deploy the archive
        return do_deploy(archive_path)
    except Exception:
        return False
