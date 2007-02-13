##############################################################################
#
# Copyright (c) 2005 Zope Corporation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""Create a system deployment for an application

$Id: deployment.py 14934 2006-11-10 23:57:33Z jim $
"""

import grp, logging, os, pwd, shutil

logger = logging.getLogger('zc.recipe.deployment')

class Install:

    def __init__(self, buildout, name, options):
        self.name, self.options = name, options
        create = []

        options['run-directory'] = os.path.join(options.get('run', '/var/run'),
                                                name)
        options['log-directory'] = os.path.join(options.get('log', '/var/log'),
                                                name)
        options['etc-directory'] = os.path.join(options.get('etc', '/etc'),
                                                name)
        options['crontab-directory'] = options.get('crontab-directory',
                                                   '/etc/cron.d')
        options['rc-directory'] = options.get('rc-directory', '/etc/init.d')

    def install(self):
        options = self.options
        user = options['user']
        uid, gid = pwd.getpwnam(user)[2:4]
        created = []
        try:
            make_dir(options['etc-directory'],   0,   0, 0755, created)
            make_dir(options['log-directory'], uid, gid, 0755, created)
            make_dir(options['run-directory'], uid, gid, 0750, created)
        except Exception, e:
            for d in created:
                try:
                    shutil.rmtree(d)
                except OSError:
                    # parent directory may have already been removed
                    pass
            raise e

        return ()

    def update(self):
        pass


def uninstall(name, options):
    path = options['etc-directory']
    shutil.rmtree(path)
    logger.info("Removing %r", path)
    for d in 'log', 'run':
        path = options[d+'-directory']
        if os.listdir(path):
            logger.warn("Can't remove non-empty directory %r.", path)
        else:
            os.rmdir(path)
            logger.info("Removing %r.", path)

def make_dir(name, uid, gid, mode, created):
    uname = pwd.getpwuid(uid)[0]
    gname = grp.getgrgid(gid)[0]
    if not os.path.isdir(name):
        os.mkdir(name, mode)
        created.append(name)
        logger.info('\n    Creating %r,\n    mode %o, user %r, group %r',
                    name, mode, uname, gname)
    else:
        os.chmod(name, mode)
        logger.info('\n    Updating %r,\n    mode %o, user %r, group %r',
                    name, mode, uname, gname)

    os.chown(name, uid, gid)