#!/usr/bin/env python
# -*- coding: utf8 -*-

"""
    fabfile.py: A fabric script for _gen my personal blog
"""

#==============================================================================
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
#==============================================================================

__author__ = "joe di castro <joe@joedicastro.com>"
__license__ = "GNU General Public License version 3"
__date__ = "17/06/2012"
__version__ = "0.6"

import os
import re
from fabric.api import *
from fabric.contrib.project import rsync_project
from fabric.contrib.console import confirm

PELICAN_REPOSITORY = "git://github.com/getpelican/pelican.git"
PROD = "joedicastro.com"
PROD_PATH = "/home/joedicastro/webapps/joedicastro"
LOCAL_WEB = os.path.join("~/www", PROD)
ROOT_PATH = os.path.abspath(os.path.dirname(__file__))
BLOG_PATH = os.path.join(ROOT_PATH, "site/source/blog")
ENV_PATH = os.path.join(ROOT_PATH, "env")
PELICAN = os.path.join(ROOT_PATH, "pelican")
CONFIG_FILE = os.path.join(ROOT_PATH, "site/pelican.conf.py")
OUTPUT = os.path.join(ROOT_PATH, "site/output")
env.user = "joedicastro"


def _escape(filename):
    """Escape spaces in unix filenames to local commands."""
    return filename.replace(" ", r"\ ")


def _valid_HTML():
    """Remove the obsolete rel="" and rev="" links in footnotes."""
    for path, dirs, files in os.walk(OUTPUT):
        for fil in files:
            if fil[-5:] == ".html":
                local("sed -i {0} -r -e 's/re[l|v]=\"footnote\"//g' {0}".
                      format(os.path.join(path, _escape(fil))))


def _make_env():
    """Make a virtual enviroment"""
    local("virtualenv {0}".format(ENV_PATH))


def _del_env():
    """Delete a virtual enviroment."""
    local("rm -rf {0}".format(ENV_PATH))


def _clone_pelican():
    """Clone Pelican from repository."""
    local("git clone {0}".format(PELICAN_REPOSITORY))
    with lcd(PELICAN):
        local("git checkout 9543ce0")
        local("git reset --hard")


def _install():
    """Install Pelican in the virtual enviroment."""
    with lcd(PELICAN):
        local("{0}/bin/python setup.py install".format(ENV_PATH))


def _install_mkd():
    """Install Markdown in the virtual enviroment."""
    local("{0}/bin/pip install markdown==2.0.3".format(ENV_PATH))


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


def _clean_unwanted():
    "Remove no wanted files & folders."
    local("rm -rf {0}/author".format(OUTPUT))
    local("rm -rf {0}/drafts".format(OUTPUT))
    local("rm {0}/index?.html".format(OUTPUT))
    local("rm {0}/index??.html".format(OUTPUT))


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
    _install_mkd()


def regen():
    """Regenerate the site from source."""
    _clean()
    _gen()
    _clean_unwanted()
    _valid_HTML()
    _local_deploy()


@hosts(PROD)
def publish():
    """Publish into remote web server with rsync."""
    regen()
    _browse()
    if confirm("¿Estas seguro de querer publicarlo?"):
        rsync_project(PROD_PATH, OUTPUT + "/", delete=True)


def _edit(mkd_path, new):
    """Edit a markdown file."""
    local("tmux new-window 'vim {0}'".format(_escape(mkd_path)))
    local("firefox {0}{1} 2>/dev/null &".format(OUTPUT, "/drafts" if new else
                                                        "/archives.html"))
    _gen(True)


def _get_status(mkd_file):
    """Get the draft status of a source markdown file."""
    with open(mkd_file, 'r') as f:
        if re.search("status: draft", f.read()):
            return True
        return False


def _get_mkd_files():
    """Get a list of the source markdown files of the blog."""
    mkds = []
    for path, dirs, files in os.walk(os.path.join(ROOT_PATH, BLOG_PATH)):
        for fil in sorted(files):
            if fil[-3:] == ".md":
                fpath = os.path.join(path, fil)
                title = fil[:-3]
                draft = _get_status(fpath)
                mkds.append({'path': fpath, 'title': title, 'draft': draft})
    return mkds


def _print_list(lst, header, draft):
    """Print a list of markdown files filtered by their draft status."""
    print("{0}{1}".format(header, os.linesep))
    for f in lst:
        if f['draft'] == draft:
            print("{0:3} | {1}".format(lst.index(f) + 1, f['title']))
    print(os.linesep)


def edit():
    """Choose a markdown article to edit or create a new one."""
    markdown_files = _get_mkd_files()
    _print_list(markdown_files, "Articulos publicados", False)
    _print_list(markdown_files, "Borradores", True)

    request = "Elige un articulo o crea uno nuevo (n):{0}".format(os.linesep)
    error = "¡Error! El valor introducido no es valido.{0}".format(os.linesep)
    while True:
        choice = raw_input(request)
        try:
            chosen = markdown_files[int(choice) - 1]
            _edit(chosen['path'], True if chosen['draft'] else False)
            break
        except IndexError:
            print(error)
        except ValueError:
            if choice == 'n':
                new = raw_input("Introduce el nombre:{0}".format(os.linesep))
                _edit(os.path.join(BLOG_PATH, new + ".md"), True)
                break
            print(error)


def img4web(delete=False, source=""):
    """Optimize .jpg & .png images and copy them into source pictures dir."""
    local("./img4web.py -d {0} {1} {2}".
          format(os.path.join(ROOT_PATH, "site/source/pictures"),
                 "--delete" if delete else "",
                 "-s {0}".format(source) if source else ""))


def commit(message):
    """Make a commit to the local mercurial repository."""
    local("hg commit -m '{0}'".format(message))


def push():
    """Make a push to the remote mercurial repository."""
    local("hg push bitbucket")


def blinks():
    """Check the webpage for broken links."""
    local("wget --spider --no-parent -r -nd -o blinks.txt {0}".format(PROD))
    local("vim blinks.txt")
