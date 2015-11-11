##############################################################################
#
# Copyright (c) 2006 Zope Foundation and Contributors.
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

from zope.testing import renormalizing
import doctest
import getpass
import grp
import os
import pwd
import re
import stat
import unittest
import zc.buildout.testing


user = pwd.getpwuid(os.geteuid()).pw_name
group = grp.getgrgid(os.getegid()).gr_name


def ls(path):
    def perm(power, mode):
        bit = (mode & 2 ** power) << (31 - power)
        if bit:
            if power in [2, 5, 8]:
                return 'r'
            elif power in [1, 4, 7]:
                return 'w'
            else:
                return 'x'
        else:
            return '-'
    st = os.stat(path)
    if stat.S_ISDIR(st.st_mode):
        permissions = ['d']
    else:
        permissions = ['-']
    permissions = ''.join(permissions + [
        perm(power, st.st_mode) for power in reversed(range(9))])
    return '%s %s %s %s' % (permissions, user, group, path)


def setUp(test):
    zc.buildout.testing.buildoutSetUp(test)
    zc.buildout.testing.install_develop('zc.recipe.deployment', test)
    zc.buildout.testing.install('six', test)
    test.globs['user'] = getpass.getuser()
    test.globs['ls'] = ls


def test_suite():
    optionflags = (doctest.IGNORE_EXCEPTION_DETAIL |
                   doctest.NORMALIZE_WHITESPACE)
    return unittest.TestSuite((
        doctest.DocFileSuite(
            'paths.test',
            setUp=zc.buildout.testing.buildoutSetUp,
            tearDown=zc.buildout.testing.buildoutTearDown,
            checker=renormalizing.RENormalizing([
                (re.compile('/[^ ]*/sample-buildout'), 'PREFIX'),
               ]),
            optionflags = optionflags,
            ),
        doctest.DocFileSuite(
            'README.txt',
            setUp=setUp, tearDown=zc.buildout.testing.buildoutTearDown,
            optionflags = optionflags,
            checker=renormalizing.RENormalizing([
                (re.compile('\d+ \d\d\d\d-\d\d-\d\d \d\d:\d\d'), ''),

                # The ordering of these regexps is important.  If they are in a
                # different order, they will break on systems where the user
                # and group are the same (default of linux)

                (re.compile("user '%s'" % user), "user 'USER'"),
                (re.compile("group '%s'" % group), "group 'GROUP'"),
                (re.compile("%s %s" % (user, group)), "USER GROUP"),
                (re.compile(user), "USER"),

                # The order doesn't matter after this point

                (re.compile('/.*/sample-buildout'), 'PREFIX'),
                (re.compile("command not found"), "not found"),
                (re.compile("Initializing part"), "Initializing section"),
                (re.compile(
                    r"\nCouldn't find index page for 'six' "
                    r"\(maybe misspelled\?\)"
                    ), ""),

                # some shells print the line number of the error

                (re.compile('sh: 1: echoxxx: not found'),
                    'sh: echoxxx: not found'),

                # Same as zc.buildout.testing.not_found, copied since
                # older versions of buildout don't define this.
                (re.compile(r'Not found: [^\n]+/(\w|\.)+/\r?\n'), ''),
               ]),
            ),
        ))

if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
