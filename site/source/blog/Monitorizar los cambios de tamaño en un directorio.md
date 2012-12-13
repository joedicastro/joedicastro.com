title: Monitorizar los cambios de tamaño en un directorio
date: 2011-05-17 21:52
tags: python, script, tamaño, directorio, monitor, linux

Cuando administramos varias maquinas UN*X nos puede interesar el tener 
controlados los cambios de tamaño en algunos directorios determinados, para 
poder observar pautas de comportamiento o ver cambios inesperados, para 
solucionar los problemas cuando o antes de que se produzcan. Y aunque hay varias
 formas de realizar esto, incluso con demonios que monitorizan los cambios en 
tiempo real (incrond, inotify, dnotify, gamin, watch, ...), puede que una 
solución más sencilla nos sea suficiente para directorios no críticos. Para 
instalaciones no complejas nos puede servir, por ejemplo, para no tener que 
lidiar con las [quotas de disco][0] (no siempre es una buena opción). O para 
evitar que por ejemplo una mala configuración en la rotación de los logs de una 
maquina acaben agotando el espacio disponible para la partición de sistema (caso
 real que me he encontrado más de una vez). 

*[UN*X]: Linux, Unix, Solaris, BSD, etc

  [0]: http://en.wikipedia.org/wiki/Disk_quota

Para poder monitorizar los cambios de tamaño de un directorio (y subdirectorios)
 he creado un sencillo script **Python** que registra los cambios en la ruta que
  le proporcionemos y luego envía un informe por correo al buzón del usuario 
local. Los datos de los directorios los registra en un fichero oculto (su 
nombre empieza por un `.`) binario de tipo [pickle][1] y el informe se guarda 
a su vez en un archivo de texto con el mismo nombre que el script, pero 
terminado en `.log`. 
 
  [1]: http://docs.python.org/library/pickle.html#module-pickle

El informe que genera nos muestra por un lado tantos los nuevos directorios, 
como los directorios que se han eliminado con la cifra del espacio en disco que 
ocupan (o liberan). Por otro lado también nos informa de los directorios que han 
cambiado de tamaño, mostrándonos en que porcentaje se han 
incrementado/decrementado y la cantidad de espacio que ha variado. Aquí podemos 
ver un ejemplo de uno de estos informes.

    :::text
    SCRIPT =========================================================================
    dir_size_monitor (ver. 0.2)
    http://joedicastro.com

    Changes in size of directories for .. on yourmachine
    ================================================================================

    START TIME =====================================================================
                                                          Tuesday 05/17/11, 21:10:48
    ================================================================================

    NEW DIRECTORIES ________________________________________________________________

       799.72 KiB   ./src/test/bibendum
         1.14 MiB   ./src/test/condimentum
         2.31 MiB   ./src/test/laoreet
       204.28 KiB   ./src/test/risus
         2.90 MiB   ./src/test/torquent


    DELETED DIRECTORIES ____________________________________________________________

       383.79 KiB   ./src/test/adipiscing
         5.38 MiB   ./src/test/consequat
       847.72 KiB   ./src/test/etiam
       938.93 KiB   ./src/test/maecenas
         3.55 MiB   ./src/test/tincidunt
         2.33 MiB   ./src/test/viverra


    CHANGED DIRECTORIES ____________________________________________________________

        34.79 %     55.5 MiB   ./src
        34.82 %     55.5 MiB   ./src/test
       -99.97 %     15.3 MiB   ./src/test/odio
       -99.97 %     15.6 MiB   ./src/test/tellus


    THRESHOLD VALUES _______________________________________________________________

    The directories whose size differences are less than any of these values are ignored:

    Percentage:     10 %
    Size:        10.00 MiB


    .. STATISTICS __________________________________________________________________

          78 directories
      215.04 MiB


    END TIME =======================================================================
                                                          Tuesday 05/17/11, 21:10:48
    ================================================================================


Opcionalmente podemos establecer dos valores de umbral para que se ignoren todos 
los cambios que estén por debajo de estas dos cifras. Para desactivarlos 
simplemente hay que dejarlos a cero. Estas cifras se refieren por un lado al 
porcentaje de diferencia mínimo que deseamos establecer para que se nos informe 
y por otro a la cantidad mínima (expresada en bytes) de espacio en disco que se 
ha incrementado/decrementado en ese directorio. Pueden funcionar los dos a la 
vez, por lo que se han de cumplir las dos condiciones, o solamente uno dejando 
el otro a cero.

Si programamos este script para que se ejecute cada cierto tiempo, podemos tener 
una idea aproximada de los cambios producidos en el. Y digo aproximada porque 
este nos muestra únicamente los cambios registrados entre dos *instantáneas* 
tomadas, una en la ejecución anterior y otra en la ejecución actual. Y por lo 
tanto no esperemos obtener la relación de todos los cambios producidas entre 
ellas. Para conocer algo a ese nivel de detalle es mejor emplear uno de los 
servicios en tiempo real que mencionaba al principio. Dicho esto, es evidente 
que en la primera ejecución no tiene sentido informar de nada y de hecho hasta 
la segunda ejecución no empezara a generar informes.

Este es el contenido de [dir_size_monitor.py][script] es el siguiente:

  [script]: https://bitbucket.org/joedicastro/python-recipes/src/tip/src/dir_size_monitor.py

    :::python
    #!/usr/bin/env python
    # -*- coding: utf8 -*-

    """
        dir_size_monitor.py: Monitors changes in the size of dirs for a given path
    """

    #===============================================================================
    # This Script monitors the changes in disk size for the directories included in
    # a given path. It reports what directories are new or deleted. Also reports the
    # directories in which their size increases or decreases above threshold values.
    # These threshold values refer to the amount in difference of size of the 
    # directory or/and the percentage difference. These values can be overrided by 
    # setting them to zero.
    #
    # The final report is sended via email to the local user. This script is 
    # intended to run periodically (e.g. via cron) 
    #===============================================================================

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
    __date__ = "17/05/2011"
    __version__ = "0.2"

    try:
        import sys
        import os
        import platform
        import pickle
        import logger
        from get_size import best_unit_size, get_size_fast
    except ImportError:
        # Checks the installation of the necessary python modules 
        print((os.linesep * 2).join(["An error found importing one module:",
        str(sys.exc_info()[1]), "You need to install it", "Stopping..."]))
        sys.exit(-2)


    def list4log(dirs_size_dict, wpath, dirs):
        """Create a list of new or deleted directories for the log."""
        llst = []
        for ldir in sorted(dirs):
            dsz = best_unit_size(dirs_size_dict[ldir])
            llst.append(" {0:8.2f} {1}   ./{2}".
                        format(dsz['s'], dsz['u'], os.path.relpath(ldir, wpath)))
        return llst

    def diff4log(before, current, wpath, dirs, threshold_pct=0, threshold_sz=0):
        """Create a list of the directories that had size changes for the log."""
        llst = []
        for ddir in sorted(dirs):
            pct = (((current[ddir] - float(before[ddir])) / before[ddir]) * 100.0)
            diff = current[ddir] - before[ddir]
            if abs(pct) >= threshold_pct and abs(diff) > threshold_sz:
                dsz = best_unit_size(diff)
                llst.append(" {0:8.2f} % {1:8.1f} {2}   ./{3}".
                            format(pct, dsz['s'], dsz['u'], os.path.relpath(ddir,
                                                                            wpath)))
        return llst


    def main(first_exec=False):
        """Main section"""
        # The path to monitor changes in directories dir_size
        mon_pth = "/your/path/to/monitor"

        # Ignore all directories that are below these percentage or absolute value 
        # of size difference. There are optional, set to zero to override them.
        thld_pct = 20      # In percentage of difference in size for a directory
        thld_sz = 10.486E6 # In bytes of absolute value of directory size difference

        # Prepare the log
        log = logger.Logger()
        url = "http://joedicastro.com"
        head = ("Changes in size of directories for {0} on {1}".
                format(mon_pth, platform.node()))
        log.header(url, head)
        log.time("START TIME")

        # Load the last dictionary of directories/sizes if exists
        try:
            with open('.dir_sizes.pkl', 'rb') as input_file:
                bfr_dir = pickle.load(input_file)
        except (EOFError, IOError, pickle.PickleError):
            bfr_dir = {}
            first_exec = True

        # Get the current dictionary of directories/sizes
        crr_dir = {}
        for path, dirs, files in os.walk(mon_pth):
            for directory in dirs:
                dir_path = os.path.join(path, directory)
                dir_size = get_size_fast(dir_path)
                crr_dir[dir_path] = dir_size

        # First, Save the current dirs/sizes
        with open(".dir_sizes.pkl", "wb") as output_file:
            pickle.dump(crr_dir, output_file)

        # Create the list depending the status of directories
        deleted = [d for d in bfr_dir if d not in crr_dir]
        added = [d for d in crr_dir if d not in bfr_dir]
        changed = [d for d in crr_dir if d in bfr_dir if crr_dir[d] != bfr_dir[d]]


        log.list("Deleted directories", list4log(bfr_dir, mon_pth, deleted))
        log.list("New directories", list4log(crr_dir, mon_pth, added))
        log.list("Changed directories", diff4log(bfr_dir, crr_dir, mon_pth, changed,
                                                 thld_pct, thld_sz))

        # If thresholds are nonzero, then report the values 
        if thld_pct or thld_sz:
            tsz = best_unit_size(thld_sz)
            log.list("Threshold Values",
                     ["The directories whose size differences are less than any of "
                      "these values are ignored:", "",
                      "Percentage: {0:6} %".format(thld_pct),
                      "Size:       {0:6.2f} {1}".format(tsz['s'], tsz['u'])])

        # Show some statistics for the analyzed path
        mon_pth_sz = best_unit_size(get_size_fast(mon_pth))
        log.list("{0} Statistics".format(mon_pth),
                 ["{0:8} directories".format(len(crr_dir)),
                  "{0:8.2f} {1}".format(mon_pth_sz['s'], mon_pth_sz['u'])])
        log.time("END TIME")
        if not first_exec:
            log.send("Changes in size of directories")
            log.write()

    if __name__ == "__main__":
        main()


Este script necesita los módulos [get_size][2] y [logger][3] para poder 
funcionar. Solo es necesario descargar los archivos y guardarlos en el mismo 
directorio donde se aloje este script. La versión más actualizada de este script 
se puede encontrar en el repositorio *Python Recipes* alojado en [bitbucket][bb]
y en [github][gh].

  [bb]: http://bitbucket.org/joedicastro/python-recipes
  [gh]: http://github.com/joedicastro/python-recipes
  [2]: http://joedicastro.com/conocer_el_tamano_de_un_directorio_con_python
  [3]: http://joedicastro.com/logger_informes_legibles_para_tus_scripts_python
