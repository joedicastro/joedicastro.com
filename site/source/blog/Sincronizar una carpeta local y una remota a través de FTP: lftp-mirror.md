title: Sincronizar una carpeta local y una remota a través de FTP: lftp-mirror
date: 2010-12-19 14:58
tags: linux, python, script, lftp, ftp mirror, sincronizar, lftp-mirror, ftp sync, ftp



A veces tenemos la necesidad de subir (o bajar) contenido a un servidor
y posteriormente tener actualizados los cambios que se produzcan en uno
(o ambos) de los lados. Es decir tener sincronizados el directorio
remoto y el local. Esto es relativamente fácil cuanto tenemos acceso via
 [consola][1] y [ssh][2] al servidor y podemos utilizar programas tan
 potentes como [rsync][3]. ¿Pero que ocurre cuando el único método del
 que disponemos para intercambiar ficheros con el servidor es a través
 del protocolo [FTP][4], como ocurre con muchos servidores web?

   [1]: http://es.wikipedia.org/wiki/L%C3%ADnea_de_comandos
   [2]: http://es.wikipedia.org/wiki/Ssh
   [3]: http://es.wikipedia.org/wiki/Rsync
   [4]: http://es.wikipedia.org/wiki/Ftp

Bien, en ese caso, tenemos un pequeño problema. El protocolo **FTP**
aunque perfectamente valido para las funciones para las que fue
originalmente creado, la transferencia de archivos, no contempla este
caso. La solución manual y menos efectiva es volver a transferir todos
los archivos cada vez que se produce un cambio, solución nada
recomendable a nada que el tamaño de estos empiece a ser superior a
decenas de Megabytes. También podríamos ir comprobando manualmente que
ficheros han cambiado y transferir únicamente estos, algo también muy
poco recomendable si el número de archivos es elevado. Afortunadamente
algunos clientes gráficos de **FTP** nos permiten comprobar que ficheros
 son distintos en uno y otro lado y luego transferir únicamente estos,
 lo cual ya es un método bastante más efectivo y adecuado. Aunque si se
 trata de directorios con muchos archivos y una estructura jerárquica
 compleja (muchos directorios y subdirectorios) el proceso es bastante
 lento pues ha de ir comprobando en un lado y en el otro las diferencias
  entre los archivos (fecha, tamaño y atributos únicamente)
recorriendolos todos. ¿Pero que ocurre si queremos realizar esta
operación de forma periódica y automática? entonces esta solución
tampoco es valida, pues necesitaríamos un programa de línea de comandos
o un script para realizarlo.


Por suerte para nosotros, esta solución también está disponible a través
 de varios programas y scripts para consola, entre los cuales el mejor
 es [**lftp**][5] de **Alexander V. Lukyanov**. Este fantástico programa
  es una navaja suiza para todo aquello que necesitemos hacer a través
  de **FTP**, siendo uno de los mejores clientes **FTP**, si no el
mejor, que existen. Y una de las innumerables posibilidades que ofrece
 es precisamente la de **sincronizar dos directorios con la opción
 mirror** (espejar). De esta manera podemos mantener perfectamente
 sincronizados dos directorios de forma automática. **Nos permite hacer
 la sincronización en ambas direcciones, remoto → local y local →
 remoto**.

   [5]: http://lftp.yar.ru/

Como ya he mencionado es muy potente y repleto de opciones y permite muchas más
operaciones más allá de la sincronización entre directorios. Por este motivo
**he creado un [script][6] en [Python][7] que empleando lftp, se centra
únicamente en la sincronización entre directorios a través de FTP y añade
algunas nuevas funcionalidades, [lftp-mirror][8].**

   [6]: http://es.wikipedia.org/wiki/Script
   [7]: http://es.wikipedia.org/wiki/Python
   [8]: http://code.joedicastro.com/lftp-mirror/wiki/Leer_en_espanol

## ¿Que ventajas aporta este script?

  * **Proporciona un log detallado y legible** que graba en un fichero en disco
y **que puede ser enviado por correo electrónico** a una o varias direcciones
empleando el servidor de correo local o uno externo.
  * **Permite crear una copia comprimida por día de la semana del directorio
local sincronizado**. Esto nos permite tener el directorio actualizado y una
copia de seguridad por cada uno de los últimos 7 días, para poder revertir algún
 cambio o borrado accidental.
  * **Se centra únicamente en la sincronización (mirror)** entre directorios, 
  obviando las otras opciones que nos ofrece lftp
  * **Nos proporciona** (en el log) **el tamaño del espacio ocupado en el disco 
  duro por el directorio local y las copias de seguridad.**
  * **Permite tres modos de ejecución distintos,** lo que lo convierte en muy 
  versátil:
    * **Como tarea programada**. En este modo los parámetros de la sincronización 
    se incluyen directamente dentro del script y solo es necesario programar su 
    ejecución para automatizar el proceso. Es ideal para la sincronización 
    periódica de un único directorio/servidor **FTP**
    * **Interactivo.** En este modo los parámetros se introducen directamente 
    como argumentos en la línea de comandos. Es ideal para ejecutar una 
    sincronización puntual manual
    * **Importando los parámetros desde un fichero de configuración.** Este modo 
    es similar al primero, con la diferencia de que en este caso los parámetros 
    los tomamos de un fichero de configuración externo. Este fichero que podemos 
    crear nosotros mismos (se sirve uno de ejemplo) nos permite establecer 
    múltiples operaciones de sincronización que se ejecutaran de manera 
    secuencial una detrás de otra.
  * **En sistemas operativos que lo soporten nos muestra notificaciones 
  emergentes** a través de la librería libnotify de la ejecución del script y 
  su correcta finalización. Por ejemplo, a través de las notificaciones 
  emergentes de [**Ubuntu**][9]. Muy útil para conocer cuando se está ejecutando 
  una tarea programada sin salida por consola.
  * Si empleamos los modos de ejecución no interactivos, **emplea [base64][10] 
  para una mínima protección de la contraseñas de acceso** a los servidores 
  **FTP** y evitar almacenarlas las mismas en texto claro. No es una fuerte 
  medida de seguridad, pero es lo mínimo que deberíamos tener en cuenta.

   [9]: http://es.wikipedia.org/wiki/Ubuntu
   [10]: http://es.wikipedia.org/wiki/Base64

## ¿Para que nos puede servir este script?

Vamos a ver un ejemplo de lo más común, las **copias de seguridad de una página web**. En muchos [hosting compartidos][11] la única posibilidad de transferir archivos con el servidor es a través de una cuenta **FTP**. Empleando este script, podemos crear un directorio en local donde haremos las copias de seguridad de los ficheros de la web y luego sincronizarlo automáticamente todos los días, descargando únicamente los ficheros que han cambiado. Con esto tendremos no solo el directorio actualizado diariamente, si no que además dispondremos de una copia de seguridad por cada uno de los siete días anteriores para poder corregir cualquier problema ocurrido entre esas fechas. Configurar algo así es realmente sencillo, únicamente tendríamos que cambiar los valores incorporados dentro del script por los que necesitamos y luego programar su ejecución diaria con cron.

   [11]: http://es.wikipedia.org/wiki/Hosting#Alojamiento_compartido_.28shared_hosting.29

Para una introducción más detallada, instrucciones de ejecución, control de versiones y enlaces para la descarga, acudir al [**repositorio del script**][12]

   [12]: https://bitbucket.org/joedicastro/lftp-mirror/wiki/Leer_en_espanol

Un extracto del código de **lftp-mirror.py**:

    :::python
    def mirror(args, log):
        """Mirror the directories."""

        user = '' if args.anonymous else ' '.join(args.login)
        local, remote = os.path.normpath(args.local), os.path.normpath(args.remote)
        port = '-p {0}'.format(args.port) if args.port else ''
        include = ' --include-glob {0}'.format(args.inc_glob) if args.inc_glob else ''
        exclude = ' --exclude-glob {0}'.format(args.exc_glob) if args.exc_glob else ''

        url = 'http://code.joedicastro.com/lftp-mirror'
        msg = 'Connected to {1} as {2}{0}'.format(os.linesep, args.site, 'anonymous'
                                                  if args.anonymous
                                                  else args.login[0])
        msg += 'Mirror {0} to {1}'.format(local if args.reverse else remote,
                                          remote if args.reverse else local)
        log.header(url, msg)
        log.time('Start time')
        notify('Mirroring with {0}...'.format(args.site), 'sync')

        if not os.path.exists(local):
            os.mkdir(local)
            log.list('Created new directory', local)
        os.chdir(os.path.join(local, os.pardir))

        # create the script file to import with lftp
        scp_args = ('-vvv' + args.erase + args.newer + args.parallel + args.reverse
                    + args.del_first + args.depth_first + args.no_empty_dir +
                    args.no_recursion + args.dry_run + args.use_cache +
                    args.del_source + args.missing + args.existing + args.loop +
                    args.size + args.time + args.no_perms + args.no_umask +
                    args.no_symlinks + args.suid + args.chown + args.dereference +
                    exclude + include)

        with open('ftpscript', 'w') as script:
            lines = ('open {0}ftp://{1} {2}'.format(args.secure, args.site, port),
                     'user {0}'.format(user),
                     'mirror {0} {1} {2}'.format(scp_args,
                                                 local if args.reverse else remote,
                                                 remote if args.reverse else local),
                    'exit')
            script.write(os.linesep.join(lines))

        # mirror
        cmd = ['lftp', '-d', '-f', script.name]
        sync = Popen(cmd, stdout=PIPE, stderr={True:STDOUT, False:None}[args.quiet])
        # end mirroring

        log.list('lftp output', ''.join(sync.stdout.readlines()))

        # compress the dir and create a .gz file with date
        if not args.reverse and not args.no_compress:
            notify('Compressing folder...', 'info')
            log.list('Rotate compressed copies', compress(local))
        # end compress

        gz_size = sum([get_size(gz) for gz in glob.glob('{0}*.gz'.format(local))])
        log_size = get_size(log.filename) if os.path.exists(log.filename) else 0
        local_size = get_size(local)
        size = best_unit_size(local_size + gz_size + log_size)
        log.block('Disk space used', '{0:>76.2f} {1}'.format(size['s'], size['u']))
        log.time('End Time')
        log.free(os.linesep * 2)
        log.write(True)

        os.remove(script.name)

Para obtener el código completo, ir al [fichero fuente](https://bitbucket.org/joedicastro/lftp-mirror/src/tip/src/lftp_mirror.py).

