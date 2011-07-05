#!/usr/bin/env python
# -*- coding: utf8 -*-

"""
    fabfile.py: A fabric script for _gen my personal blog
"""

#===============================================================================
#    Copyright 2011 joe di castro <joe@joedicastro.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#===============================================================================

__author__ = "joe di castro <joe@joedicastro.com>"
__license__ = "GNU General Public License version 3"
__date__ = "28/06/2011"
__version__ = "0.2"

import os
from fabric.api import *
from fabric.contrib.project import rsync_project
from fabric.contrib.console import confirm

PELICAN_REPOSITORY = "git://github.com/ametaireau/pelican.git"
PROD = "joedicastro.com"
PROD_PATH = "/home/joedicastro/webapps/joedicastro"
LOCAL_WEB = os.path.join("~/www", PROD)
ROOT_PATH = os.path.abspath(os.path.dirname(__file__))
ENV_PATH = os.path.join(ROOT_PATH, "env")
PELICAN = os.path.join(ROOT_PATH, "pelican")
CONFIG_FILE = os.path.join(ROOT_PATH, "site/pelican.conf.py")
OUTPUT = os.path.join(ROOT_PATH, "site/output")
env.user = "joedicastro"

def _valid_HTML():
    """Remove the obsolete rel="" and rev="" links in footnotes."""
    for path, dirs, files in os.walk(OUTPUT):
        for fil in files:
            if fil[-5:] == ".html":
                local("sed -i {0} -r -e 's/re[l|v]=\"footnote\"//g' {0}".
                      format(os.path.join(path, fil.replace(" ", r"\ "))))

def _make_env():
    """Make a virtual enviroment"""
    local("virtualenv {0}".format(ENV_PATH))

def _del_env():
    """Delete a virtual enviroment."""
    local("rm -rf {0}".format(ENV_PATH))

def _clone_pelican():
    """Clone Pelican from repository."""
    local("git clone {0}".format(PELICAN_REPOSITORY))

def _install():
    """Install Pelican in the virtual enviroment."""
    with lcd(PELICAN):
        local("{0}/bin/python setup.py install".format(ENV_PATH))

def _browse():
    """Browse the local Apache site."""
    local("firefox -new-window http://localhost/joedicastro.com 2>/dev/null &")

def _gen(autoreload=False):
    """Generate the site from source."""
    local("{0}/bin/pelican {2} -s {1}".format(ENV_PATH, CONFIG_FILE,
                                              "-r" if autoreload else ""))
def _clean():
    "Remove the output folder."
    local("rm -rf {0}".format(OUTPUT))

def _local_deploy():
    """Deploy to the local apache web server."""
    local("rm -rf {0}".format(LOCAL_WEB))
    local("cp -r {0} {1}".format(OUTPUT, LOCAL_WEB))


def pull_pelican():
    """Update Pelican to last revision from repository."""
    with lcd(PELICAN):
        local("git pull")

def bootstrap():
    """Get Pelican and install it in a virtual enviroment."""
    with settings(warn_only=True):
        _del_env()
    _make_env()
    with settings(warn_only=True):
        _clone_pelican()
    _install()

def regen():
    """Regenerate the site from source."""
    _clean()
    _gen()
    _valid_HTML()
    _local_deploy()

@hosts(PROD)
def publish():
    """Publish into remote web server with rsync."""
    regen()
    _browse()
    if confirm("¿Estas seguro de querer publicarlo?"):
        rsync_project(PROD_PATH, OUTPUT + "/", delete=True)

def new(title):
    """Create a new blog article."""
    local("gedit --new-window {0}/site/source/blog/{1}.md 2>/dev/null &".
          format(ROOT_PATH, title.replace(" ", "\ ")))
    local("firefox --new-window {0}/index.html &".format(OUTPUT))
    _gen(True)

def img4web(delete=False, source=""):
    """Optimize .jpg & .png images and copy them into source pictures dir."""
    local("./img4web.py -d {0} {1} {2}".
          format(os.path.join(ROOT_PATH, "site/source/pictures"),
                 "--delete" if delete else "",
                 "-s {0}".format(source) if source else ""))
