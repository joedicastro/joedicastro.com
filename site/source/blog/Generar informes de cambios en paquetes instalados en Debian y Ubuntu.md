titLe: Generar informes de cambios en paquetes instalados en Debian y Ubuntu.
date: 2011-05-06 22:55
tags: python, script, paquetes, linux, Debian, Ubuntu, dpkg

Una de las políticas de seguridad que tengo con mis sistemas **Linux**, es 
además de efectuar respaldos periódicos (diarios) del contenido del directorio 
`/home` (en mi caso siempre es una partición o disco independiente), es siempre 
guardar también una lista de los paquetes instalados en los mismos. 
Prácticamente nunca hago una copia completa de la partición o disco de de 
sistema, y aunque si hago una copia de los directorios más importantes, prefiero 
tener siempre una relación actualizada de los paquetes instalados en cada 
maquina.

*[paquetes]: En sistemas *NIX se denomina así a los programas

En sistemas Linux [Debian][0] y otras distribuciones derivadas ([Ubuntu][1], 
[Mint][2], [Mepis][3], [Knoppix][4], ...) obtener esta lista es realmente 
sencillo, pues solo es necesario ejecutar este comando:

    :::console
    dpkg -l > lista_paquetes.txt


Y con eso, se generaría una lista de los paquetes instalados[^nota] en el 
sistema en el fichero *lista_paquetes.txt*. Y mantener actualizado este fichero 
es tan sencillo como programar (via `crontab` por ejemplo) la ejecución de este 
comando con un sencillo [script][6] [shell][5]. Y así lo he realizado durante 
años, hasta que quise tener aun más información.

  [0]: http://debian.org
  [1]: http://ubuntu.com
  [2]: http://www.linuxmint.com/
  [3]: http://www.mepis.org/
  [4]: http://www.knoppix.org/
  [5]: http://es.wikipedia.org/wiki/Shell_de_UNIX
  [6]: http://es.wikipedia.org/wiki/

Entonces me interesó conocer también los cambios que se producen en los 
paquetes, es decir nuevas (des)instalaciones y actualizaciones. Es lógico pensar 
que si uno mismo es el que las realiza, pues ya sabe esta información de primera 
mano. Pero la memoria es frágil y no demasiado confiable, además ¿que ocurre 
cuando en una misma maquina tienen permisos para administrar los paquetes más de 
un usuario? 

Se pueden conocer estos cambios de los paquetes en el tiempo de varios modos, 
desde acudir a los logs de **dpkg** en `/var/log/dpkg.log` y examinarlos con 
algún analizador de logs (o el más sencillo e inmediato comando `less`) hasta 
consultarlos de una manera más sencilla y gráfica con el gestor de paquetes 
**Synaptic** (en el menú *Archivo -> Histórico*). Pero me interesaba automatizar 
esto, para conocer esos cambios poco después de que se produjeran y lo lógico 
era emplear el mismo script shell que empleaba para generar la lista de paquetes 
instalados. Así lo hice entonces, combinando los comandos `awk`, `grep`, `diff` 
y `mail` con el comando del principio para obtener la lista, tenia los cambios 
en mi buzón de correo al poco tiempo de producirse. Y ha funcionado 
perfectamente hasta ahora.

Pero desde que me introduje en el lenguaje **Python**, he ido migrando poco a 
poco los scripts [bash][7] que tengo para reescribirlos en este lenguaje. Y 
recientemente le ha tocado a este. Ha sido muy fácil y la verdad es que el 
resultado aunque funcionalmente es el mismo, me ha permitido entregar unos 
informes más elegantes y fáciles de interpretar de un golpe de vista. 

  [7]: http://es.wikipedia.org/wiki/Bash

Ahora, cuando se realiza algún cambio en los paquetes del sistema, de forma 
automática, por mi o por otro usuario autorizado, yo recibo en mi correo un 
informe similar a este:

    :::diff
    SCRIPT =========================================================================
    dpkg_diff (ver. 0.1)
    http://code.joedicastro.com/python-recipes

    Changes of packages installed on yourmachine
     ===============================================================================

    START TIME =====================================================================
                                                         Thursday 05/05/11, 10:30:01
     ===============================================================================


    INSTALLED PACKAGES LIST FILE ___________________________________________________

    /your/path/to/package_list.txt


    CHANGES DIFF ___________________________________________________________________

    --- previous Wed May  4 22:59:51 2011
    +++ current  Thu May  5 10:30:01 2011
    @@ -34,1 +34,1 @@
    -ii  apt                 0.7.25.3ubuntu9.3
    +ii  apt                 0.7.25.3ubuntu9.4
    @@ -36,2 +36,2 @@
    -ii  apt-transport-https 0.7.25.3ubuntu9.3
    -ii  apt-utils           0.7.25.3ubuntu9.3
    +ii  apt-transport-https 0.7.25.3ubuntu9.4
    +ii  apt-utils           0.7.25.3ubuntu9.4

    END TIME =======================================================================
                                                         Thursday 05/05/11, 10:30:01
     ===============================================================================


Donde se puede ver la información que nos indica el script que ha generado el 
correo, la maquina en la que se han realizado los cambios, la localización del 
fichero con la relación de todos los paquetes instalados en el sistema, la fecha 
y hora de la ejecución del script y el [diff][8] con la relación de cambios en 
los paquetes en formato [Unified format][9]. En este ejemplo podemos ver como se 
han actualizado tres paquetes en esa maquina. No nos dice la hora en que se 
efectuó la modificación (podemos verlo en el log de `dpkg`) pero si podemos 
saber que se efectuó entre dos intervalos de ejecución del script, información 
que será más que suficiente la mayoría de las veces. Para datos concretos, ir al 
log y filtrarlo con `grep` y en segundos sabremos la respuesta. Si además como 
es mi caso, ejecutamos el script cada 12 o 24 horas, pues será fácil saber 
cuando se han realizado los cambios.

  [8]: http://es.wikipedia.org/wiki/Diff
  [9]: http://en.wikipedia.org/wiki/Diff#Unified_format

Un fragmento de código de la parte principal del script es el siguiente:

    :::python
    def pretty_diff(diff):
        """Better format for package lines in diff."""
        pkg = {} # diff's packages lines

        # Get columns info for diff package lines
        for idx, line in enumerate(diff):
            if not findall("^-{3}|^\+{3}|^@{2}", line):
                # split the line in columns and remove the description column
                cols = split("\s{2,}", line, 3)[:3]
                # A nested dict, for each line index we have a dict that contains 
                # the package line columns: 's' (status), 'n' (name) & 'v' (version)
                # and the width of the name column: w(width)
                pkg[idx] = {'s':cols[0], 'n':cols[1], 'v':cols[2], 'w':len(cols[1])}

        # maximum width in packages' name column for all lines
        mxw = max((pkg[index]['w'] for index in pkg))

        # Replace each package line for a prettier one (more legible) 
        for i in range(len(diff)):
            if i in pkg:
                diff[i] = ("{0} {1} {2}".format(pkg[i]['s'], pkg[i]['n'] + " " *
                                                (mxw - pkg[i]['w']), pkg[i]['v']))
        return diff


    def main(old=""):
        """Main section"""

        # The path to store the debian packages list file
        pkg_lst_file = "./package_list.txt"

        # Start logging
        log = Logger()
        url = "http://code.joedicastro.com/python-recipes"
        head = "Changes of packages installed on {0}".format(platform.node())
        log.header(url, head)
        log.time("Start time")

        # Read the old file and clean the list
        if os.path.exists(pkg_lst_file):
            old = open(pkg_lst_file, 'r').readlines()
            old_date = time.ctime(os.stat(pkg_lst_file).st_mtime)

        # Get the current list of debian packages installed on system 
        current = Popen(["dpkg", "-l"], stdout=PIPE).stdout.readlines()

        # First, save the list file
        with open(pkg_lst_file, 'w') as out:
            out.writelines(current)
            curr_date = time.ctime(os.stat(pkg_lst_file).st_mtime)

        # Compare both lists
        if old:
            file_path = os.path.realpath(pkg_lst_file)
            diff = [ln for ln in unified_diff(old, current, fromfile="previous",
                                              tofile="current ",
                                              fromfiledate=old_date,
                                              tofiledate=curr_date, n=0,
                                              lineterm="")]

            # If there are differences write the log to disk and send mail
            if diff:
                log.list("Installed packages list file", file_path)
                log.list("Changes diff", pretty_diff(diff))
                log.time("End time")
                log.write(True)
                # Send mail to current system user. For other options, see logger 
                # module info
                log.send("Debian packages changes")



Este script hace uso del modulo logger, que comento en este [artículo][10]. 

  [10]: http://joedicastro.com/logger_informes_legibles_para_tus_scripts_python

Para obtener la versión más reciente del script y del modulo logger, consultar 
mi [repositorio][repo].

  [repo]: http://code.joedicastro.com/python-recipes

  [^nota]: Es una relación de los programas instalados empleando el sistema de 
    paqueteria de Debian, los programas instalados manualmente vía compilación 
    u otros medios no aparecerán en ella. 
