title: Fabric & Rsync para realizar Backups
date: 2011-07-13 20:21
tags: python, fabric, rsync, backup, sincronizar

En el [anterior articulo][1] empleaba [fabric][2] y [rsync][3] para sincronizar 
un directorio local y uno remoto en ambas direcciones. Además le añadía las 
funcionalidades de [logger][4] y [notify][5] para proporcionar información sobre 
el proceso durante y después de su ejecución. Y comenzaba el articulo recordando 
a [lftp-mirror][6], el script que había creado para realizar la sincronización a 
través de FTP. Pero **lftp-mirror** realiza algo más que la sincronización, pues 
también permite realizar el archivado del directorio local en ficheros 
comprimidos y lanzar varias tareas en una sola ejecución.

  [1]: http://joedicastro.com/sincronizar-dos-directorios-con-fabric-y-rsync.html
  [2]: http://fabfile.org/
  [3]: http://es.wikipedia.org/wiki/Rsync
  [4]: http://joedicastro.com/logger-informes-legibles-para-tus-scripts-python.html
  [5]: http://joedicastro.com/notificaciones-de-escritorio-en-ubuntu-desde-python.html
  [6]: http://joedicastro.com/sincronizar-una-carpeta-local-y-una-remota-a-traves-de-ftp-lftp-mirror.html
  
Ahora he añadido esta funcionalidad al fichero **fabric** creado anteriormente.
Así empleando este fichero podemos realizar el Backup periódico de varios 
servidores en una sola operación y de forma completamente automática (basta con 
programar su ejecución). Se sincronizan los dos directorios y se crea un archivo 
comprimido del directorio local por cada día de la semana. De este modo siempre 
tenemos una copia del estado del directorio remoto de los últimos siete días. Y 
al final del proceso en nuestro correo, un email con el informe del resultado por 
cada una de las tareas ejecutadas.

En este fichero, **rsync_fabric.py**, disponemos de tres posibles tareas:

    :::console
    $ fab -l

         A Fabric file for sync two directories (remote ⇄ local) with rsync.

    Available commands:

        backup  Sync from remote to local & archive the local directory.
        down    Sync from remote to local.
        up      Sync from local to remote.

Con la primera realizamos el backup (sincronización + archivado) y 
con las siguientes solo la sincronización desde o hacia el servidor. Una de las 
ventajas de fabric es que nos permite concatenar tareas fácilmente desde la 
línea de comandos, así podemos lanzar varias sincronizaciones de forma 
simultanea. Para poder realizar esto, creo una configuración de sincronización 
por defecto y después creo una función para cada una las tareas adicionales que 
simplemente redefinen los valores de estas variables globales. Por ejemplo:

    :::python
    # Variables globales de sincronización predefenidas
    env.host_string = "username@example.com"
    env.remote = "/my_directory"
    env.local = "/home/my_user/backups/my_directory"

    # Redefinimos estas variables para otra configuración de sincronización. Por 
    # supuesto, pueden tratarse de servidores distintos.
    def _databases():
        global env
        env.host_string = "username@example.com"
        env.remote = "/databases"
        env.local = "/home/my_user/backups/databases"

Veamos ejemplos de como podemos utilizar estas tareas:


    :::console
    # "Si queremos sincronizar el contenido local hacia el remoto, por ejemplo 
    # para subir los ficheros al servidor por primera vez. Empleando los valores 
    # por defecto. El modificador -w lo empleo para que no se detenga en los 
    # errores, que de ocurrir, los veremos luego en el informe final."
    $ fab -w up
    [localhost] local: rsync -pthrvz --delete /home/my_user/backups/my_directory/ 
     username@example.com:my_directory

    Done.
    # "Pero también podemos especificar una tarea distinta a la por defecto de 
    # este modo. Sincronizando desde el servidor a nuestro directorio local las 
    # bases de datos."
    $ fab -w down:databases
    [localhost] local: rsync -pthrvz --delete username@example.com:databases/ 
    /home/my_user/backups/databases

    Done.
    # "Y por supuesto, podemos realizar varias tareas a la vez."
    $  fab -w down backup:databases
    [localhost] local: rsync -pthrvz --delete username@example.com:my_directory/ 
    /home/my_user/backups/my_directory
    [localhost] local: rsync -pthrvz --delete username@example.com:databases/ 
    /home/my_user/backups/databases

    Done.

No empleo contraseña alguna, ni en el fichero ni en la línea de comandos, podría 
hacerse perfectamente, pero prefiero emplear una clave [RSA][7] [pública][8] 
autorizada para las sesiones SSH en el servidor. Es bastante más seguro y cómodo. 
En los ejemplos no se ve la salida de *rsync*, pues es capturada (así como los 
erores) para ser mostrada a posteriori en los informes. 

  [7]: http://es.wikipedia.org/wiki/RSA
  [8]: http://es.wikipedia.org/wiki/Criptograf%C3%ADa_asim%C3%A9trica
  
Un ejemplo de informe sería el siguiente:

    :::text
    START TIME =====================================================================
                                                        miércoles 13/07/11, 19:48:55
    ================================================================================

    SCRIPT =========================================================================
    fab (ver. Unknown)
    Fabric Rsync
    http://joedicastro.com

    Syncing username@example.com:databases to /home/my_user/backups/databases
    ================================================================================

    RSYNC OUTPUT ___________________________________________________________________

    receiving file list ... done

    sent 20 bytes  received 825 bytes  153.64 bytes/sec
    total size is 827.76M  speedup is 979595.42


    ROTATE COMPRESSED COPIES _______________________________________________________

    Created file:

    /home/my_user/backups/databases_13jul2011_19:49_mié.tar.gz

    Deleted old file:

    databases_13jul2011_19:37_mié.tar.gz


    DISK SPACE USED ================================================================
                                                                            1.60 GiB
    ================================================================================

    END TIME =======================================================================
                                                        miércoles 13/07/11, 19:50:02
    ================================================================================


Que como podemos ver, ha tardado poco más de un minuto en sincronizar 827.56 
Megabytes y el total de espacio ocupado por el directorio y los siete archivos 
comprimidos es de 1.60 Gibibytes (1,72 Gigabytes). 
  
  
## Ventajas

Las ventajas de sincronizarlo con **rsync + ssh** vs **ftp**, como ya comenté en el 
anterior articulo son enormes. Se ahorra muchísimo tiempo y ancho de banda, lo 
que ayuda a no saturar la red y no tener que planificar con tanto cuidado las 
ventanas de backup. Por ejemplo he realizado unas pruebas y para las mismas 
condiciones: **mismo servidor, mismo directorio, mismo horario y condiciones de 
red; la sincronización remoto → local a través de FTP emplea entre 35 y 45 
minutos y cuando lo hacemos a través de rsync emplea entre 2 y 4 minutos**. Ahí 
es nada, estamos hablando de un proceso ~13 veces más rápido. 

## Código

El código del fichero fabric es el siguiente:

    :::python
    #!/usr/bin/env python
    # -*- coding: utf8 -*-

    import os
    import glob
    import tarfile
    import time
    from get_size import get_size as _get_size
    from get_size import best_unit_size as _best_unit_size
    from logger import Logger as _logger
    from notify import notify as _notify
    from fabric.api import env, local

    LOG = _logger()

    #===============================================================================
    # RSYNC HOSTS
    #===============================================================================

    # Your default host. No need any more if only wants a host.
    env.host_string = "username@host"
    env.remote = "/your/remote/path"
    env.local = "/your/local/path"

    # If wants to use various hosts, then define the previous variables like this, 
    # one function per host. 
    def _host_1():
        """Host variables for host_1."""
        global env
        env.host_string = "username@host_1"
        env.remote = "/your/remote/path/in/host_1"
        env.local = "/your/local/path/for/host_1"

    def _host_2():
        """Host variables for host_2."""
        global env
        env.host_string = "username@host_2"
        env.remote = "/your/remote/path/in/host_2"
        env.local = "/your/local/path/for/host_2"

    # ...
    #
    # def _host_n():
    #     """Host variables for host_n."""
    #     global env
    #     env.host_string = "username@host_n"
    #     env.remote = "/your/remote/path/in/host_n"
    #     env.local = "/your/local/path/for/host_n"

    #===============================================================================
    # END RSYNC HOSTS
    #===============================================================================

    def _log_start():
        """Create the Start time info block for the log."""
        # Init the log for multiple hosts. Do not repeat the previous logs.
        if LOG.get():
            LOG.__init__()
        LOG.time("Start time")

    def _log_end(task):
        """Create the End time info block and send & write the log."""
        _notify("Rsync", "Ended" , "ok")
        LOG.time("End time")
        LOG.free(os.linesep * 2)
        LOG.write(True)
        LOG.send("Fabric Rsync ({0})".format(task))

    def _check_local():
        """Create local directory if no exists."""
        if not os.path.exists(env.local):
            os.mkdir(env.local)

    def _rsync(source, target, delete):
        """Process the _rsync command."""
        _log_start()
        LOG.header("Fabric Rsync\nhttp://joedicastro.com",
                   "Syncing {0} to {1}".format(source, target))
        _notify("Rsync", "Start syncing {0} to {1}".format(source, target), "info")
        out = local("rsync -pthrvz {2} {0}/ {1}".
                    format(source, target, "--delete" if delete == "yes" else ""),
                    capture=True)
        _notify("Rsync", "Finished synchronization", "ok")
        LOG.list("Rsync Output", out)
        if out.failed:
            LOG.list("Rsync Errors", out.stderr)

    def _compress(path):
        """Compress a local directory into a gz file.

        Creates a file for each weekday, an removes the old files if exists"""
        os.chdir(os.path.join(path, os.pardir))
        dir2gz = os.path.basename(path)
        old_gzs = glob.glob('{0}*{1}.tar.gz'.format(dir2gz, time.strftime('%a')))
        gz_name = "{0}_{1}.tar.gz".format(dir2gz, time.strftime('%d%b%Y_%H:%M_%a'))
        gz_file = tarfile.open(gz_name, "w:gz")
        gz_file.add(path, arcname=dir2gz)
        gz_file.close()
        output = os.linesep.join(['Created file:', '', os.path.join(os.getcwd(),
                                                                    gz_name)])
        for old_gz in old_gzs:
            os.remove(old_gz)
            output += os.linesep.join([os.linesep, 'Deleted old file:', '', old_gz])
        return output

    def _archive():
        """Archive the local directory in a gz file for each weekday."""
        _notify('Rsync', 'Compressing folder...', 'info')
        LOG.list('Rotate compressed copies', _compress(env.local))
        _notify("Rsync", "Finished compression", "ok")

    def _get_diskspace():
        """Get the disk space used by the local directory and archives."""
        gz_size = sum([_get_size(gz) for gz in glob.glob('{0}*.gz'.
                                                         format(env.local))])
        log_size = _get_size(LOG.filename) if os.path.exists(LOG.filename) else 0
        local_size = _get_size(env.local)
        size = _best_unit_size(local_size + gz_size + log_size)
        LOG.block('Disk space used', '{0:>76.2f} {1}'.format(size['s'], size['u']))

    def up(server=None, dlt='yes'):
        """Sync from local to remote."""
        globals()["_" + server]() if server else None
        _rsync(env.local, ":".join([env.host_string, env.remote]), dlt)
        _log_end(server)

    def down(server=None, dlt='yes', archive=False):
        """Sync from remote to local."""
        globals()["_" + server]() if server else None
        _check_local()
        _rsync(":".join([env.host_string, env.remote]), env.local, dlt)
        if not archive:
            _log_end(server)

    def backup(server=None):
        """Sync from remote to local & archive the local directory."""
        down(server, archive=True)
        _archive()
        _get_diskspace()
        _log_end(server)


El fichero siempre actualizado puede ser encontrado en el repositorio *Python Recipes* que está alojado en [github][gh] con el nombre `rsync_fabfile.py` 

  [gh]: http://github.com/joedicastro/python-recipes
  
