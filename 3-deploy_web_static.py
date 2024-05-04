#!/usr/bin/python3
"""
Write a Fabric script (based on the file 2-do_deploy_web_static.py)
that creates and distributes an archive to your web servers,
using the function deploy
"""
from fabric.api import env, put, run
from os.path import exists
do_pack = __import__('1-pack_web_static').do_pack
do_deploy = __import__('2-do_deploy_web_static').do_deploy
env.hosts = ['54.237.67.242', '100.25.0.50']


def deploy():
    """
    distributes an archive to your web servers
    """
    # check if the path exists
    archive_path = do_pack()
    if not exists(archive_path):
        return False

    try:
        # deploy the archive
        return do_deploy(archive_path)
    except Exception:
        return False
