title: Sincronizar dos directorios con Fabric y Rsync
date: 2011-07-06 22:02
tags: python, fabric, rsync, sincronizar


Anteriormente habíamos visto como [sincronizar un directorio remoto y uno local 
empleando solamente FTP][0]. Ahora vamos a ver la forma de hacerlo empleando 
[ssh][1] y [rsync][2]. Para ello vamos a utilizar otra vez **Python** y una 
herramienta muy valiosa para cualquier [sysadmin][3] que se precie como es 
[fabric][4] (que descubrí gracias a Manuel Viera en [esta pregunta en majibu][5]).
Evidentemente realizar la sincronización con rsync esta a años luz de hacerlo 
con FTP, la velocidad de sincronización, el tiempo empleado y la cantidad de 
datos a mover son mucho menores. FTP es algo que debería utilizarse únicamente 
cuando no disponemos de acceso via SSH.

 [0]: http://joedicastro.com/sincronizar-una-carpeta-local-y-una-remota-a-traves-de-ftp-lftp-mirror.html
 [1]: http://es.wikipedia.org/wiki/Ssh
 [2]: http://es.wikipedia.org/wiki/Rsync
 [3]: http://es.wikipedia.org/wiki/Administrador_de_sistemas
 [4]: http://fabfile.org/
 [5]: http://python.majibu.org/preguntas/11/libreria-para-emplear-con-ssh

La gran ventaja de **fabric** es que nos permite ahorrarnos el tener que 
implementar el acceso SSH con [paramiko][6] y la entrada de opciones y 
argumentos con *argparse*. Gracias a esto los scripts necesarios son mucho más 
cortos y limpios y su utilización es bastante más sencilla. Fabric ya incorpora 
una función para emplear rsync, `rsync_project`, dentro de su modulo de proyectos 
contribuidos `fabric.contrib.project`

 [6]: http://www.lag.net/paramiko/

Una forma de implementar esta sincronización en ambas direcciones empleando esta 
función predefinida sería esta:

    :::python
    from fabric.api import env, hosts, local
    from fabric.contrib.project import rsync_project

    env.host_string = "username@host"
    REMOTE_PATH = "/your/remote/path"
    LOCAL_PATH = "/your/local/path"

    @hosts(env.host_string)
    def rsync_up(dlt="yes"):
        rsync_project(REMOTE_PATH, LOCAL_PATH + "/", 
                      delete= True if dlt == "yes" else False)

    def rsync_down(dlt="yes"):
        local("rsync -pthrvz {0}:{1}/ {2} {3}".
              format(env.host_string, REMOTE_PATH, LOCAL_PATH, 
              "--delete" if dlt == "yes" else ""))

Y luego solo tendríamos que llamar a la función deseada:


    :::console
    # "Para sincronizar de remoto a local"
    $ fab rsync_down


> Hay que tener en cuenta un detalle con fabric. Cuando se le pasa un parámetro, 
> este es siempre convertido a una cadena. Luego al pasarle `True` o `False` no 
> se convierte en un valor booleano, sino una cadena `"True"`o `"False"`. De ahí 
> que compruebe si el parámetro coincide con `"yes"` en vez de un valor booleano.

El problema con la función rsync predefinida de fabric es que esta pensada 
únicamente para subir archivos a un servidor remoto, es decir, es una 
sincronización en una sola dirección, por eso implemento la sincronización en 
sentido contrario sin emplearla y empleando `local`. La autentificación de la 
sesión SSH puede realizarse especificando la contraseña dentro del propio fichero, 
pero va en contra del sentido común emplear un método tan inseguro como este. Lo 
lógico es emplear autorizaciones de sesiones SSH sin contraseña por medio de una 
[clave pública][7].

 [7]: http://es.wikipedia.org/wiki/Criptograf%C3%ADa_asim%C3%A9trica
 
Podríamos prescindir de la librería incorporada dentro de fabric y tendríamos 
algo como esto:

    :::python
    from fabric.api import env, local

    env.host_string = "username@host"
    REMOTE_PATH = "/your/remote/path"
    LOCAL_PATH = "/your/local/path"

    def _rsync(source, target, delete):
        """Process the _rsync command."""
        output = local("rsync -pthrvz {0}/ {1} {2}".
                       format(source, target, "--delete" if delete == "yes" else ""))

    def up(dlt='yes'):
        """Sync from local to remote."""
        _rsync(LOCAL_PATH, ":".join([env.host_string, REMOTE_PATH]), dlt)

    def down(dlt='yes'):
        """Sync from remote to local."""
        _rsync(":".join([env.host_string, REMOTE_PATH]), LOCAL_PATH, dlt)


Pero... un momento, si estamos empleado un comando local, no empleamos 
`rsync_project` y empleamos una clave pública para el acceso SSH, entonces no 
estamos empleando **paramiko**, ¿de que nos sirve emplear fabric?. Bueno, en 
realidad `rsync_project` también emplea `local`, por lo que no emplea paramiko. 
Pero las ventajas vienen de que, por ejemplo, este mismo script se podría modificar 
fácilmente para ejecutar rsync en el servidor en vez de en nuestra maquina local, 
 empleando `run` en vez de `local`. Además podemos emplear el mismo fichero para 
 añadir varias tareas más a realizar en el servidor, aparte de la sincronización. 
Podríamos prescindir de fabric y hacer esto mismo con un script con un número 
similar de líneas, pero esto nos permite centralizar todas las tareas más comunes 
sobre ese servidor en un único fichero. Por ejemplo podríamos añadir una tarea 
para hacer un respaldo previo de una base de datos en el servidor, empleando un 
comando remoto en el servidor, luego hacer la sincronización separada de la BDD 
y el resto de ficheros y finalmente eliminar ese respaldo. Puede haber cientos 
de razones para preferir emplear fabric antes de un script independiente para 
la sincronización.

## Ejecución desatendida de la sincronización

Si queremos programar esta tarea, no sería mala idea que nos avisara de cuando 
comienza a ejecutarse y del resultado de la misma. Para ello puedo emplear 
[Logger][8] y [notify][9], para implementar esta funcionalidad.

 [8]: http://joedicastro.com/logger-informes-legibles-para-tus-scripts-python.html
 [9]: http://joedicastro.com/notificaciones-de-escritorio-en-ubuntu-desde-python.html
 
    :::python
    from logger import Logger as _logger
    from notify import notify as _notify
    from fabric.api import env, local

    env.host_string = "username@host"
    REMOTE_PATH = "/your/remote/path"
    LOCAL_PATH = "/your/local/path"

    def _rsync(source, target, delete):
        """Process the _rsync command."""
        log = _logger()
        log.header("Fabric Rsync\nhttp://code.joedicastro.com/python-recipes",
                   "Syncing {0} to {1}".format(source, target))
        log.time("Start time")
        _notify("Rsync", "Start syncing {0} to {1}".format(source, target), "info")
        output = local("rsync -pthrvz {0}/ {1} {2}".
                       format(source, target, "--delete" if delete == "yes" else ""),
                       capture=True)
        _notify("Rsync", "Finished", "ok")
        log.list("Output", output)
        if output.failed:
            log.list("Error", output.stderr)
        log.time("End time")
        log.send("Fabric Rsync")

    def up(dlt='yes'):
        """Sync from local to remote."""
        _rsync(LOCAL_PATH, ":".join([env.host_string, REMOTE_PATH]), dlt)

    def down(dlt='yes'):
        """Sync from remote to local."""
        _rsync(":".join([env.host_string, REMOTE_PATH]), LOCAL_PATH, dlt)


De esta forma, nos avisaría con una notificación en el escritorio de su inicio y 
fin, y al acabarse la sincronización, tendríamos un informe en nuestro correo 
parecido a este:

    :::text
    SCRIPT =========================================================================
    fab (ver. Unknown)
    Fabric Rsync

    Syncing username@host:/your/remote/path to /your/local/path
    ================================================================================

    START TIME =====================================================================
                                                       miércoles 06/07/11, 21:50:48
    ================================================================================

    OUTPUT _________________________________________________________________________

    receiving file list ... done
    ./
    index.php

    sent 48 bytes  received 200 bytes  45.09 bytes/sec
    total size is 99  speedup is 0.40


    END TIME =======================================================================
                                                       miércoles 06/07/11, 21:50:54
    ================================================================================


Este fichero está disponible en [mi repositorio][repo].
 
  [repo]: https://bitbucket.org/joedicastro/python-recipes/src/tip/src/rsync_fabfile.py
