title: Pelican - Publicación y automatización
date: 2011-06-28 23:54
tags: pelican, python, markdown, restructuredtext, blog, html, rsync, fabric

Una vez que sabemos como [instalar Pelican][0] y [crear contenido][1] con él, es
hora de saber como convertir ese contenido en un blog real disponible en
internet. Es decir, saber como publicar ese contenido. Como hemos visto hasta
ahora, al constar básicamente de simples ficheros HTML, un servidor de archivos
es más que suficiente para servir el blog. Esto nos abre un gran abanico de
posibilidades, desde emplear un potente (y barato) servidor de ficheros en la
*nube* como __Amazon S3__, pasando por las páginas web estáticas que nos
permiten repositorios como __Bitbucket__ o __GitHub__, por los tradiciones
hostings compartidos (e.g.  este blog), hasta un servidor casero sencillo
montado sobre un [NAS][4]. 
 

  [0]: http://joedicastro.com/pelican-introduccion-e-instalacion.html
  [1]: http://joedicastro.com/pelican-creacion-de-contenido.html
  [4]: http://es.wikipedia.org/wiki/Network-attached_storage
  
Aún cuando es posible emplear un simple servidor de archivos para alojar el blog, 
siempre es mejor contar con un servidor web detrás (Apache, nginx, lighttpd, 
...) que nos permita hacer redirecciones para nuestras antiguas páginas si ya 
disponíamos de un blog anterior o manejar los errores HTTP [404][5] o [403][6] 
de forma personalizada. 

  [5]: http://es.wikipedia.org/wiki/Error_404
  [6]: http://es.wikipedia.org/wiki/Anexo:C%C3%B3digos_de_estado_HTTP

  
## Publicar el contenido

Publicar el contenido de una web es tan sencillo como volcar el contenido del 
directorio que nos genera Pelican (en nuestro ejemplo sería 
*myblog.com/site/output/\**) en el directorio destino de nuestro servidor web. 
Dependiendo del método que hayamos elegido para alojar nuestro blog, puede ser 
tan sencillo como una copia de archivos o emplear FTP (SFTP) ó [SSH][7] ([SCP][9], 
[Unison][8.bis] ó [rsync][8]). Aquí el tema radica no en la primera vez que 
vayamos a subir el contenido al servidor, si no en las sucesivas, a medida que 
vayamos creando contenido nuevo. No tendría ningún sentido volver a subir todo 
el contenido cada vez, si no solamente el nuevo o el que haya cambiado. Para eso 
necesitamos sincronizar los dos directorios. 

  [7]: http://es.wikipedia.org/wiki/SSH
  [8]: http://es.wikipedia.org/wiki/Rsync
  [8.bis]: http://en.wikipedia.org/wiki/Unison_%28file_synchronizer%29
  [9]: http://es.wikipedia.org/wiki/SCP

Si solamente disponemos de acceso FTP (o SFTP) a nuestro servidor, entonces 
tendremos que emplear una herramienta que nos permita la sincronización sobre 
FTP, como puede ser __lftp__. Y el proceso se puede automatizar con un script 
como el que describo en [Sincronizar una carpeta local y una remota a través de 
FTP: lftp-mirror][10]. Si disponemos de acceso a través de SSH, entonces la 
elección es clarisima, __rsync__. Más adelante explico una manera de emplearlo 
de forma automática.

  [10]: http://joedicastro.com/sincronizar-una-carpeta-local-y-una-remota-a-traves-de-ftp-lftp-mirror.html

Cualquiera de ambas soluciones nos permite subir el contenido en apenas segundos, 
(sobre todo en el caso de rsync) cuando se trata de añadir un articulo nuevo, 
por ejemplo. Y lo mismo a la hora de hacer una rectificación, es tan inmediato 
como lo pueden ser plataformas como Wordpress, Drupal y similares. Además, con 
las potentes herramientas que existen para hacer cambios múltiples en varios 
ficheros de texto a la vez, se pueden realizar tareas casi imposibles con una 
plataforma de blogs tradicional sin recurrir a consultas SQL en la BDD o a 
plugins externos. Una de estas herramientas, sin recurrir a `find`, `grep`, 
`awk` y `sed`, puede ser [regexxer][11].

  [11]: http://regexxer.sourceforge.net/


## Generar el contenido en el propio servidor

Si el alojamiento que hemos escogido nos permite instalar programas python, 
entonces tenemos la posibilidad de instalar Pelican en el servidor remoto. De 
esta formar podríamos subir únicamente los archivos markdown o reStructuredText 
al servidor y generar allí mismo el contenido web. De este modo la cantidad de 
datos a subir sería ridícula y un simple comando FTP nos serviría. Luego bien 
podríamos lanzar Pelican a través de una consola SSH o bien dependiendo del 
servidor, tener un [demonio][12] corriendo que cuando detectara un cambio en el 
sistema de ficheros lanzará un script que generara el contenido con Pelican. 

  [12]: http://es.wikipedia.org/wiki/Demonio_%28inform%C3%A1tica%29
  
Otra posibilidad que me convence más, es de la poder instalar un repositorio en 
el servidor con un software de control de versiones, como Git o Mercurial. La 
idea sería tener un repositorio local, y al hacer un push hacia el repositorio 
remoto, a través de un *hook* activar la generación de la página con Pelican. 
Esto nos permitiría además poder tener varias copias del repositorio (por 
ejemplo en GitHub o Bitbucket) y por lo tanto de la web, haciendo "innecesarias" 
las copias de seguridad. 


## Automatizar todos los procesos

Pero lo ideal es poder automatizar todas las tareas que hemos visto hasta ahora, 
empleando unos pocos comandos para realizarlas sin esfuerzo alguno (bueno, 
a menos que tengas tú [ghostwriter][13] particular, me temo que los artículos los 
seguirás teniendo que escribir tú). Para poder realizar esto disponemos de la 
fantástica y potente herramienta [Fabric][14] (el [Capistrano][15] para Python) 
que nos permite ejecutar comandos locales o remotos en múltiples servidores. Esto 
nos permite hacer despliegues de software sin apenas esfuerzo en distintas 
máquinas, copiar ficheros o ejecutar tareas repetitivas empleado una corta 
serie de comandos. Una grandísima herramienta para administradores de sistema y 
desarrolladores.

  [13]: http://es.wikipedia.org/wiki/Negro_%28escritor%29
  [14]: http://fabfile.org
  [15]: http://en.wikipedia.org/wiki/Capistrano
  

Lo único que necesitamos es instalar **fabric** y crear un fichero llamado 
`fabfile.py` donde especificaremos las tareas que queremos programar. Para 
instalar la última versión estable de fabric, lo mejor es emplear `easy_install` 
o `pip`

    ::console
    $ pip install fabric  
  
Una vez creado el fichero `fabfile.py`, lo único que tendremos que hacer para 
ejecutar una tarea del mismo, sería escribir el comando `fab` seguido del nombre 
que le hayamos dado a la tarea (este sería el funcionamiento básico). Y la tarea 
se ejecutaría inmediatamente. 

Para comprender mejor como funciona Fabric, muestro aquí el contenido actual de 
mi fichero `fabfile.py`  
  
    ::python
    #!/usr/bin/env python
    # -*- coding: utf8 -*-

    """
        fabfile.py: A fabric script for generate my personal blog
    """

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
        local("rm  -rf {0}".format(LOCAL_WEB))
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

    @hosts("my_user@" + PROD)
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

    def img4web(delete=True, source=""):
        """Optimize .jpg & .png images and copy them into source pictures dir."""
        local("./img4web.py -d {0} {1} {2}".
              format(os.path.join(ROOT_PATH, "site/source/pictures"),
                     "--delete" if delete else "",
                     "-s {0}".format(source) if source else ""))


Ahora, veremos el funcionamiento básico que nos permite este script. Primero 
vemos las tareas que tenemos disponibles:

    ::console
    $ fab -l
        fabfile.py: A fabric script for generate my personal blog

    Available commands:

        bootstrap     Get Pelican and install it in a virtual enviroment.
        img4web       Optimize .jpg & .png images and copy them into source pict...
        new           Create a new blog article.
        publish       Publish into remote server with rsync.
        pull_pelican  Update Pelican to last revision from repository.
        regen         Regenerate the site from source.

Veamos que hacen cada una de ellas:

* ***bootstrap*** Si observamos el código, veremos que lo hace es, en este orden: 
eliminar cualquier entorno virtual previo, crear un entorno virtual nuevo, 
descargar Pelican desde el repositorio (si no lo hemos hecho anteriormente) e 
instalar Pelican dentro de este entorno virtual. Y todo esto en un solo paso, casi 
todos los comandos que explicaba en [Pelican - Introducción e Instalación][0] con 
solo  teclear `fab bootstrap`. Así de fácil. Con este comando podemos tanto crear 
una instalación de Pelican desde cero, como actualizar la instalación de Pelican 
después de actualizar este a la última versión con ***pull-pelican***. Siguiendo 
con nuestro ejemplo, lo que haría este comando es crear los directorios *env* y 
*pelican* dentro de *myblog.com* con el entorno virtual creado y pelican 
instalado.

        ::console
        $ fab bootstrap

* ***img4web*** Este comando hace uso del script que describía en [Optimizar 
imágenes para la web][16] para hacer precisamente eso, reducir el peso de las 
imágenes que empleo en los artículos. Lo que hago es a medida que voy escribiendo 
el articulo es ir guardando las imágenes en el directorio raíz (en nuestro 
ejemplo, *myblog.com/*) y cuando lo termino, simplemente ejecuto el comando 
`fab img4web` y este me optimiza las imágenes, me guarda las optimizadas en el 
directorio de imágenes del contenido (*myblog.com/site/source/pictures/*) y me 
elimina las imágenes originales del directorio raíz. Cuando termina me muestra un 
resumen con la cantidad de imágenes procesadas y el ahorro en espacio conseguido. 
Espacio en disco ahorrado que se resume en menos ancho de banda consumido y en 
páginas web que se cargan más rápido.

        ::console
        $ fab img4web
        
  [16]: http://joedicastro.com/optimizar-imagenes-para-la-web.html
  
* ***new*** Con este creo o edito los artículos del blog. Realiza 
tres funciones: me abre una venta de Gedit con el articulo que le indico con la 
extensión `.md`, me abre una ventana de Firefox que me muestra el fichero 
*index.html* del directorio del sitio generado por Pelican 
(*myblog.com/site/output/index.html*) y finalmente me activa Pelican con la 
opción `autoreload`. Luego empleando el plugin **Grid** de Compiz, divido la 
pantalla en dos mitades y coloco a la izquierda Gedit y a la derecha Firefox. 
Esto me permite, como explicaba en [De Drupal a Pelican][17] editar el contenido 
y previsualizar el resultado casi en tiempo real, disponiendo al mismo tiempo de 
un buen corrector ortográfico. 

        ::console
        $ fab new:"Articulo de prueba"

  [17]: http://joedicastro.com/de-drupal-a-pelican.html

* ***publish*** El más importante, el que sube los artículos al servidor web. 
Publicar el contenido de la web es tan sencillo como ejecutar este comando. Lo 
que hace es regenerar el contenido (por si hubiera algún cambio sin guardar) y 
luego mostrarme el resultado en firefox. Pero el resultado que me muestra no es 
el del directorio de salida de Pelican, si no de una copia que tengo en un 
servidor Apache local. Esto me permite ver los cambios de manera más fiel a la 
versión web, puesto que hace uso del fichero .htaccess y de las reglas que tengo 
establecidas en él. Finalmente me pregunta si realmente deseo publicar el 
contenido, por si se me hubiera escapado algo. Si le digo que no, aborta la 
publicación, pero si le digo que si, me sincroniza el contenido de la carpeta 
local con la remota empleando **rsync**. De esta manera solo se transmiten los 
ficheros nuevos, se borran los que se hayan eliminado en local y **solo transmite 
la parte que haya cambiado de los archivos modificados**. Gracias a esto, 
modificar o añadir contenido es cuestión de segundos. Y sencillisimo.

        ::console
        $ fab publish
    
* ***pull_pelican*** Nos sirve para actualizar Pelican a la última revisión 
disponible en el repositorio oficial. Si después de ejecutarlo, queremos instalar 
la nueva versión en nuestro entorno virtual para poder emplearla, simplemente 
tenemos que volver a ejecutar `fab bootstrap` y todo se realizará de forma 
automática.
 
        ::console
        $ fab pull_pelican

* ***regen*** El proceso principal, es el que le pide a Pelican que genere el 
sitio web a partir de nuestro directorio de origen. También realiza varios 
procesos: primero eliminar el directorio de salida actual (para tener una copia 
fresca), genera el nuevo contenido, luego procesa los archivos para que 
validen en HTML5 y finalmente hace una copia del directorio de salida a mi 
servidor local Apache. El procesar los archivos para validar en HTML5 se debe a 
que markdown crea unos enlaces `rel = "footnote"` y `rev = "footnote"` en las notas 
al pie que se han quedado obsoletos y no son necesarios. De momento es un 
post-procesado, pero puede que finalmente modifique Pelican para que se haga en 
tiempo de generación del sitio. Aunque creo que  el rendimiento de esta manera 
sería menor que emplear el comando `sed` que ejecuta este proceso, será cuestión 
de probarlo. También se podría modificar markdown.


Con solo **6** comandos tengo automatizadas todas las tareas básicas para 
administrar y crear contenido en mi blog. Ni siquiera el potente y buenísimo 
[drush][18] de Drupal me permitía este nivel de automatización (aunque se 
acercaba bastante). De esta manera solo me tengo que preocupar de crear 
artículos y de las posibles personalizaciones que le quiera realizar al tema del 
sitio. Me olvido de todo lo demás, de todo lo que conlleva un CMS. Solo hay una 
manera de bloguear más cómoda para los que a estos les parezca algo complejo, 
servicios como Tumblr. Aunque si quieres tener el control sobre tu sitio, no 
conozco manera más cómoda y con más ventajas que esta. 

  [18]: http://drupal.org/project/drush
