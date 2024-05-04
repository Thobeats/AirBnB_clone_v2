#!/usr/bin/python3
"""
Write a Fabric script that generates a .tgz archive
from the contents of the web_static folder of your
AirBnB Clone repo, using the function do_pack.
"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """
    generates a .tgz archive from the contents of the web_static folder
    """
    # create the versions folder
    local("mkdir -p versions")

    # archive name
    currentDate = datetime.now().strftime('%Y%m%d%H%M%S')
    archive = "web_static_{}.tgz".format(currentDate)

    # store in the versions folder
    storage_path = "versions/{}".format(archive)

    archivedResult = local("tar -cvzf {} web_static/".format(storage_path))
    if archivedResult.failed:
        return False
    return (storage_path)
