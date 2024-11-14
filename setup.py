import os

from setuptools import find_packages
from setuptools import setup


name = 'zc.recipe.deployment'

entry_points = '''
[zc.buildout]
default = %(name)s:Install
deployment = %(name)s:Install
configuration = %(name)s:Configuration
crontab = %(name)s:Crontab
sharedconfig = %(name)s:SharedConfig

[zc.buildout.uninstall]
default = %(name)s:uninstall
sharedconfig = %(name)s:uninstall_shared_config

''' % globals()


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()


setup(
    name=name,
    version='2.0.dev0',
    author='Jim Fulton',
    author_email='dev-zope@zope.dev',
    description='ZC Buildout recipe for Unix deployments',
    license='ZPL 2.1',
    keywords='deployment build',
    url='https://github.com/zopefoundation/' + name,
    long_description=(
        read('README.rst')
        + '\n' +
        read('CHANGES.rst')
        + '\n' +
        'Detailed Documentation\n'
        '**********************\n'
        + '\n' +
        read('src', 'zc', 'recipe', 'deployment', 'README.txt')
        + '\n' +
        'Download\n'
        '**********************\n'
    ),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Framework :: Buildout",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: Zope Public License",
    ],
    install_requires=['setuptools'],
    python_requires='>=3.8',
    extras_require={
        'test': [
            'zc.buildout',
            'zope.testing',
            'zope.testrunner',
        ]},
    entry_points=entry_points,
    package_dir={'': 'src'},
    packages=find_packages('src'),
    namespace_packages=['zc', 'zc.recipe'],
    zip_safe=False,
    include_package_data=True,
)
