title: Sincronizar Bitbucket y GitHub
date: 2012-04-26 21:15
tags: mercurial, hg, repositorio, bitbucket, github, python

Para mis proyectos empleo generalmente [mercurial][hg] (hg) como sistema de
control de versiones, porque está hecho en Python y me parece más elegante y
agradable de usar que [git][git], aunque empleo git para algunas tareas, como
gestionar los plugins de [Vim][vim]. Del mismo modo, el emplear hg como 
[DCVS][dcvs] me llevaba de forma natural a emplear [Bitbucket][bb] como
alojamiento para mis repositorios públicos. 

  [hg]: http://mercurial.selenic.com/
  [git]: http://git-scm.com/
  [vim]: http://www.vim.org
  [dcvs]: http://es.wikipedia.org/wiki/Programas_para_control_de_versiones
  [bb]: http://bitbucket.org
  

Siempre me ha gustado **Bitbucket**, su estilo sencillo, pero muy potente y creo que
tiene algunas características que son superiores a las de sus rivales (el [diff
side-by-side][diff], por ejemplo[^gt]). Pero también tengo claro que si hay algún
alojamiento de código en la red que destaca sobre todos los demás es [GitHub][gh],
"todo" el mundo está allí y de algún modo, estás "obligado" a estar. **GitHub**
tiene algunas características muy potentes y en ciertos aspectos es muy superior
a Bitbucket, aunque me sigue gustando más el *feeling* de este último. 

  [gh]: http://github.com
  [diff]: http://blog.bitbucket.org/2011/12/08/pull-requests-with-side-by-side-diffs/
  [^gt]: Bueno, algunos rivales como [Gitorius][gts], también soportan esta característica

  [gts]: http://gitorious.org/
        

## Hg != Git 

Me planteé entonces hace unos días que lo mejor era mantener una replica de mis
repositorios alojados en Bitbucket en GitHub, como dice el refrán, *Nunca tengas
todos tus huevos en una misma cesta*. El problema es que aunque Bitbucket soporta 
repositorios tanto en mercurial como en git (para competir con GitHub), GitHub
solo soporta repositorios en Git. Y dado el éxito que tienen, dudo mucho que
tengan intención alguna de soportar otro sistema de versiones distinto a Git. 

Técnicamente es posible mantener un repositorio con los dos dcvs a la vez, pero
maldita la gracia que me hacía, ademas de que no es nada aconsejable por el
incremento de tamaño en disco que esto supondría. Entonces, ¿como hacer para poder
alojar un repositorio mantenido con mercurial en un alojamiento que solo soporta
Git? La solución, **hg-git**.

### hg-git

[hg-git][hgg] es un plugin para mercurial que permite sincronizar el repositorio
local en hg con un repositorio en git, admitiendo tanto *push* como *pull* y sin
perdidas de información. Gracias a este plugin, podemos alojar el repositorio en
los dos sitios a la vez, empleando solo mercurial para gestionarlo.

  [hgg]: http://hg-git.github.com/ 
  

Instalarlo es muy fácil (desde `easy_install` o `pip`) y emplearlo también.
Primero necesitas habilitarlo en el fichero `~/.hgrc`, así como la extensión 
bookmarks que necesita para trabajar.

    [extensions]
    hgext.bookmarks =
    hggit = 

A continuación tienes que ir a tu repositorio y asignarle un `bookmark` a la
rama que tengas por defecto (suele ser `default`) o a `tip` con el nombre de
`master` (el nombre de las ramas por defecto en git), es decir:

    :::console
    $ hg bookmark -r default master -f

Y luego emplearlo es tan sencillo como si fuera un repositorio de mercurial, por
ejemplo un push:

    :::console
    $ hg push git+ssh://git@github.com/joedicastro/joedicastro.com.git


## Sincronizar el repositorio con Bitbucket y GitHub

Ahora, lo que tampoco me apetecía era tener que andar haciendo un push cada vez
para cada alojamiento, lo ideal es que cada vez que hiciera un push a un
sitio se sincronizara también el otro de forma automática. La solución
pasa por emplear los *paths* para definir alias para los repositorios remotos y
un *hook* para automatizar la sincronización. 

Definir los alias con *paths* es realmente sencillo, nos vamos al fichero
`.hg/hgrc` del repositorio local y añadimos esto (e.g. el repo de este blog):

    [paths]
    github = git+ssh://git@github.com:joedicastro/joedicastro.com.git
    bitbucket = ssh://hg@bitbucket.org/joedicastro/joedicastro.com

De este modo, realizar un `push` es tan sencillo como:

    :::console
    $ hg push bitbucket

Ahora necesitamos crear el `hook` que nos sincronice los dos alojamientos. Hay
en la red varias soluciones para esto, por ejemplo [esta][morgan] y [esta][denis], 
pero ninguna de las dos acababa de convencerme, la una por emplear un script
bash que entraba muy fácilmente en un bucle infinito y la otra por necesitar
otro modulo externo, que en mi caso no acababa de funcionar. Así
que basándome en la idea del script bash del primero, decidí crearme uno en
Python que funcionara correctamente y me solucionara el problema. 

  [morgan]: http://morgangoose.com/blog/2010/09/29/github-and-bitbucket-hooks/
  [denis]: http://wiki.ddenis.com/index.php?title=Sync_BitBucket_and_GitHub
  

El código del `hook` es el siguiente:

    :::python
    #!/usr/bin/env python
    # encoding: utf-8

    """
        bb_gh_sync.py: Mercurial hook to keep synced a repo to Bitbucket & GitHub.
    """

    #==============================================================================
    # This script maintain synced a repository to booth github and bitbucket sites,
    # using only a local mercurial repository. To do this, makes use of hg-git, the
    # paths defined in my local hg repo and the environment variable given by hg, to
    # push to the site non described in the command line argument. This way, it's
    # irrelevant which site I decided to push every time, booth are done by this
    # hook.
    #===============================================================================

    #==============================================================================
    #    Copyright 2012 joe di castro <joe@joedicastro.com>
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
    __date__ = "23/04/2012"
    __version__ = "0.1"


    import os
    from tempfile import gettempdir
    from subprocess import call


    def main():
        """Main section"""

        tmp_dir = gettempdir()
        lock_file = os.path.join(tmp_dir, "bb_gh_sync.lock")

        # make sure that only runs once for each repository
        if not os.path.exists(lock_file):
            open(lock_file, "w").close()
            # if pushed to bitbucket, push to github too
            if os.environ['HG_ARGS'] == "push bitbucket":
                call(["/usr/bin/env", "hg", "push", "github"])
            # et viceversa...
            if os.environ['HG_ARGS'] == "push github":
                call(["/usr/bin/env", "hg", "push", "bitbucket"])
        else:
            os.remove(lock_file)


    if __name__ == "__main__":
        main()

Ahora solo tenemos que editar nuestro fichero `~/.hgrc` para habilitarlo y ya
estaría listo para funcionar. Editamos el fichero y le añadimos estas lineas:

    [hooks]
    post-push = $HOME/dotfiles/hg/bb_gh_sync.py

Ahora, si hacemos un push a Bitbucket, el hace automáticamente un push también a
GitHub al acabar el primero, y viceversa. De este modo, hacer un push a ambos
alojamientos es tan sencillo como:

    :::console
    $ hg push bitbucket
    pushing to ssh://hg@bitbucket.org/joedicastro/joedicastro.com
    running ssh hg@bitbucket.org 'hg -R joedicastro/joedicastro.com serve --stdio'
    searching for changes
    no changes found
    running hook post-push: $HOME/dotfiles/hg/bb_gh_sync.py
    pushing to git+ssh://git@github.com:joedicastro/joedicastro.com.git
    creating and sending data
    ["git-receive-pack 'joedicastro/joedicastro.com.git'"]
        github::refs/heads/master => GIT:198e8cc9
    running hook post-push: $HOME/dotfiles/hg/bb_gh_sync.py
    $


De este modo puedo mantener copias de los repositorios locales en ambos sitios
de manera automática y sincronizada, sin preocuparme, ni hacer un trabajo extra.
Eso si, conviene prescindir de los wikis y documentarlo todo a través de ficheros
`README.md` en formato Markdown para facilitar la integración de los dos sitios.
Lo que por otro lado también ayuda a mantenerlos actualizados de manera más sencilla.
