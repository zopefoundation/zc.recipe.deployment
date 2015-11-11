Changes
*******

- Python 3 support.

1.2.0 (2014-02-04)
==================

- Added an ``on-change`` option to the configuration recipe to run a
  command when a configuration file changes.

1.1.0 (2013-11-04)
==================

- Do not touch an existing configuration file if the content hasn't
  changed.


1.0.0 (2013-04-24)
==================

- Added a ``name`` option to the ``configuration`` recipe to allow
  explicit control of generated file paths.

0.10.2 (2013-04-10)
===================

- Fix packaging bug.


0.10.1 (2013-04-10)
===================

- Fix for 0.9 -> 0.10 .installed.cfg migration


0.10.0 (2013-03-28)
===================

- Add ``etc-prefix`` and ``var-prefix`` to specify new locations of
  these entire trees.  Final versions of these paths are exported.

- Previously undocumented & untested ``etc``, ``log`` and ``run``
  settings are deprecated.  Warnings are logged if their values are
  used.

- Add ``cache-directory`` and ``lib-directory`` to the set of output
  directories.

- Add system-wide configuration, allowing locations of the "root"
  directories to be specified for an entire machine.

- Allow ``*-directory`` options (e.g. ``log-directory``) to be
  overridden by configuration data.


0.9.0 (2011-11-21)
==================

- Fixed test dependencies.

- Using Python's ``doctest`` module instead of deprecated
  ``zope.testing.doctest``.

- Added a directory option for configuration to override default etc
  directory.


0.8.0 (2010-05-18)
==================

Features Added
--------------

Added recipe for updating configuration files that may shared by
multiple applications.

0.7.1 (2010-03-05)
==================

Bugs fixed
----------

- Fixed a serious bug that cause buildouts to fail when using new
  versions of the deployment recipe with older buildouts.

- Made uninstall more tolerant of directories it's about to delete
  already being deleted.

0.7.0 (2010-02-01)
==================

Features Added
--------------

You can now specify a user for crontab entries that is different than
a deployment user.

0.6 (2008-02-01)
================

Features Added
--------------

Added the ability to specify a name independent of the section name.
Also, provide a name option for use by recipes.

Important note to recipe authors: Recipes should use the deployment
name option rather than the deployment name when computing names of
generated files.

0.5 (Mar 23, 2007)
==================

Features Added
--------------

Added recipe for generating crontab files in /etc/cron.d.

0.4 (Mar 22, 2007)
==================

Features Added
--------------

- Added setting for the logrotate configuration directories.

Bugs Fixed
----------

- The documentation gave the wrong name for the crontab-directory option.

0.3 (Feb 14, 2007)
==================

Features Added
--------------

- Added a configuration recipe for creating configuration files.

0.2.1 (Feb 13, 2007)
====================

- Fixed bug in setup file.

0.2 (Feb 7, 2007)
=================

Bugs Fixed
----------

- Non-empty log and run directories were deleated in un- and
  re-install.
