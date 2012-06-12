title: Mantener la temperatura adecuada en un portátil Dell con Linux
date: 2012-06-12 10:44
tags: linux, dell, python

Los que tengáis o hayáis tenido un portátil __Dell__, sabréis que es posible
controlar la velocidad de funcionamiento de sus ventiladores de forma manual.
Existen aplicaciones para Windows, pero también es posible hacerlo desde Linux
con el paquete `i8kutils` creado por Massimo Dal Zotto. Este paquete incluye un
modulo del kernel `i8k` que necesita ser cargado al inicio y una serie de
utilidades para controlar el ventilador e informar de la temperatura y otros
valores de la [BIOS][bios].

  [bios]: https://es.wikipedia.org/wiki/Bios

Este paquete fue creado originalmente para el portátil Dell Inspiron 8000, de
ahí su nombre. Esta utilidad aprovecha el modo [SMM ][smm] de la BIOS que estaba
presente en los modelos Inspiron para controlar la velocidad de los ventiladores
(algo que también permiten otras marcas como Toshiba y Lenovo, para las que
también hay algunas utilidades). Dell también ofrece el soporte de SMM BIOS en
otras gamas y portátiles, como los de la serie Latitude o XPS. Aunque está
utilidad no funciona en algunos modelos.

  [smm]: http://es.wikipedia.org/wiki/Modo_de_Gerencia_del_Sistema

Esta utilidad funciona bajo la línea de comandos, pero al amparo del modulo del
kernel surgieron varias aplicaciones, principalmente applets para el panel de
Gnome 2, que permitían un control gráfico de los ventiladores y su temperatura.
Este control podía ser automático o manual. Yo personalmente me decanté en su
momento por emplear [Conky][conky] para mostrar las velocidades y la temperatura y
emplear un script, `i8kapplet` por Wheelspin, para controlar automáticamente la
temperatura dentro de unos rangos.

  [conky]: http://conky.sourceforge.net/


## i8kfans.py

Este era un script bash que lleva dándome servicio mucho años (el portátil ya
tiene sus siete años) pero que por la forma que tiene de controlar cuando se
debe subir/bajar la velocidad de los ventiladores, provocaba que se sucediesen
de vez en cuando continuos acelerones y frenazos en los mismos. Esto al principio
no me disgustaba, pero con los años los ventiladores hacen cada vez más ruido y
si bien el sonido constante a alta velocidad es ligeramente molesto, esos
cambios bruscos de velocidad se me han vuelto insoportables. Y dado que el
portátil se acerca al final de su vida útil, sustituir los ventiladores, aunque
es la solución adecuada, no lo veo económicamente rentable.

Yo sabía que el problema por el que esto sucedía es porque la BIOS por defecto
regula las temperaturas de los ventiladores en unos rangos predefinidos y esto
no se desactiva, de hecho trabaja conjuntamente con el script. Como los rangos
de temperatura que yo predefino son inferiores a los de la BIOS, en algunas
ocasiones los dos pelean por el control de los ventiladores y es lo que ocasiona
el problema. Pero el calor es el peor enemigo de la electrónica, y en los
portátiles esto es un factor critico. De hecho estoy seguro de que este equipo
(muy bien amortizado) me ha durado tantos años gracias a que me he preocupado de
este punto. Estoy cansado de ver morir a portátiles y discos duros en verano
porque la gente no se preocupa de este tema. Por favor, limpiad el polvo de los
ventiladores al llegar el verano, os ahorrareis muchos disgustos.

Así que descartado el reemplazar los ventiladores, me planteé el crear un script
que intentara hacer lo mismo pero de forma más suave, intentado reducir el
número de cambios bruscos de velocidad y fruto de ello es el siguiente script,
que está disponible tanto en [Bitbucket ][bbkt] como en [GitHub][gh]:

  [bbkt]: http://bitbucket.org/joedicastro/i8kfans
  [gh]: http://github.com/joedicastro/i8kfans

    :::python
    #!/usr/bin/env python
    # -*- coding: utf8 -*-

    """
        i8kfans.py: Adjust the fans speed in various Dell laptops (with a nvidia
        graphics card) to maintain the right temperatures. This affect both fans,
        the cpu and the gpu fan. Originally i8k was created to run in a Dell
        Inspiron 8000 laptop, but this Dell fan control via SMM BIOS is available
        in others laptops of various series (Inspiron, XPS, Latitude, etcetera),
        but not all of them are supported. Mine is an Inspiron 9400 but I tested
        this successfully in a XPS m1330 too.

        Based on a 2006 bash script by Wheelspin, `i8kapplet`. This old script
        served faithfully me for many years, but my ears couldn't stand much longer
        its random and common slow downs/speed ups. Over the years, fans have
        become more and more loud. This new script runs in a more smooth way, with
        less sudden changes.  It's cheaper than replace booth fans, don't you
        think?

        This script needs the `i8kutils` linux package installed and the `i8k`
        kernel module loaded to work.
    """


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
    __date__ = "12/06/2012"
    __version__ = "0.3"


    try:
        from os import linesep
        from subprocess import check_output, Popen, PIPE
        from sys import exit, exc_info
        from time import sleep
    except ImportError:
        # Checks the installation of the necessary python modules
        print((linesep * 2).join(["An error found importing one module:",
        str(exc_info()[1]), "You need to install it", "Stopping..."]))
        exit(-2)


    def check_execs(*progs):
        """Check if the programs are installed, if not exit and report."""
        for prog in progs:
            try:
                Popen([prog, '--help'], stdout=PIPE, stderr=PIPE)
            except OSError:
                msg = 'The {0} program is necessary to run this script'.format(prog)
                exit(msg)
        return


    def get_right_fan_speed(current_temperature, current_fan_speed, temp_triggers):
        """Get the right fan speed to use with i8kfan command.

        :current_temperature: current temperature value for the fan implied
        :current_fan_speed: current fan speed
        :temp_triggers: the threshold temperatures to trigger the fan speed change
        :returns: right fan speed or "-" (means change nothing to i8kfan)

        """
        right_fan_speed = None  # the right fan speed for the current temp
        if current_temperature >= temp_triggers[0]:
            if current_temperature >= temp_triggers[1]:
                right_fan_speed = 2
            else:
                right_fan_speed = 1
        else:
            right_fan_speed = 0
        return right_fan_speed if right_fan_speed != current_fan_speed else "-"


    def main():
        """Main section"""
        # time between temperature checks
        interval = 1
        # the temp thresholds to jump to a faster fan speed. Values greater than
        # [g|c]pu[0] set the fan speed to 1 and the ones greater than [g|c]pu[1]
        # set the speed to 2. Obviously, values minor than [g|c]pu[0] stop the fan
        gpu_temps = [45, 53]
        cpu_temps = [40, 50]

        # check if the i8k kernel module is already loaded
        if  "i8k" not in check_output("ls /proc/".split()):
            exit("The i8k kernel module is not loaded")

        while True:
            try:
                # get current values
                cpu_temp = int(check_output("i8kctl temp".split()))
                gpu_out = check_output("nvidia-smi -q -d TEMPERATURE".split())
                gpu_temp = int([s for s in gpu_out.split() if s.isdigit()][-1])
                cpu_fan, gpu_fan = [int(f) for f in check_output("i8kfan").split()]

                # get the right speed values for each fan
                cpu_rfs = get_right_fan_speed(cpu_temp, cpu_fan, cpu_temps)
                gpu_rfs = get_right_fan_speed(gpu_temp, gpu_fan, gpu_temps)

                # if any of the fans needs to change their speed, change it!
                if cpu_rfs != "-" or gpu_rfs != "-":
                    Popen("i8kfan {0} {1}".format(cpu_rfs, gpu_rfs).split(),
                          stdout=PIPE)

                # wait a moment. We want a cooler laptop, aren't we?
                sleep(interval)
            except KeyboardInterrupt:
                exit()


    if __name__ == "__main__":
        check_execs("i8kctl", "i8kfan", "nvidia-smi")
        main()

    ###############################################################################
    #                                  Changelog                                  #
    ###############################################################################
    #
    # 0.3:
    #
    # * Better documentation
    #
    # 0.2:
    #
    # * Fix an error in a function docstring due to refactorization
    # * Give appropriate credit to original idea' script
    #
    # 0.1:
    #
    # * First attempt
    #

De momento, aunque aún sufre del mismo problema inevitable por el conflicto
por el control entre el script y la BIOS, de momento he observado que se produce
con menos frecuencia y durante menos tiempo. Aunque quizás realice algunos
cambios para intentar reducir aún más esos conflictos.
