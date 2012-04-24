title: Comprobar si un programa está instalado con Python
date: 2011-04-28 14:04
tags: python idiom, script, python

Cuando creamos un script en **Python**, sobre todo aquellos orientados a 
ejecutarse en la línea de comandos, a veces necesitamos echar mano de un 
programa externo que no siempre viene por defecto instalado en el sistema. Por 
ejemplo, en el script que empleo en 
[optimizar imágenes para la web](http://joedicastro.com/optimizar_imagenes_para_la_web) 
empleo los programas externos *pngcrush* y *jpegtran*. ¿Como comprobamos 
entonces si el programa está instalado? Desde luego es siempre mejor 
comprobarlo y avisar al usuario, que dejar que arroje un feo error.

Una forma de comprobar si el programa está instalado es capturando la excepción 
cuando se produzca con las sentencias `try` y `except`, incluyendo la llamada al 
ejecutable dentro de ellas y devolver un mensaje de error avisando de la 
necesidad de la presencia de este ejecutable. Pero al igual que en el ejemplo 
anterior, yo prefiero comprobar esto incluso antes de ejecutar cualquier otro 
código dentro del script. Para ello empleo el [conocido truco][0] que nos 
permite ejecutar cierto código solo cuando es ejecutado como script y no cuando 
es importado como módulo:

    :::python
    if __name__ == "__main__":
       chequeo_ejecutable()
       main()


Donde `main()` es la función principal donde albergaríamos el código fundamental 
del script. Es un conocido [Python Idiom][1] que me sirve perfectamente para 
esta tarea. De hecho lo empleo habitualmente en todos mis scripts para separar 
el código principal de las funciones. 

  [0]: http://ibiblio.org/g2swap/byteofpython/read/module-name.html
  [1]: http://python.net/~goodger/projects/pycon/2007/idiomatic/handout.html

Comprobar en Linux si existe el ejecutable es realmente sencillo (siempre y 
cuando conozcamos el nombre exacto del ejecutable) con este código:

    :::python
    #!/usr/bin/env python
    # -*- coding: utf8 -*-
    
    import sys
    from subprocess import Popen, PIPE
    
    def check_execs(*progs):
        """Check if the programs are installed, if not exit and report."""
        for prog in progs:
            try:
                Popen([prog, '--help'], stdout=PIPE, stderr=PIPE)
            except OSError:
                msg = 'The {0} program is necessary to run this script'.format(prog)
                sys.exit(msg)
        return
    
    def main():
        # Incluir aquí el código fundamental del script
        pass
    
    if __name__ == "__main__":
        check_execs('python')
        main()


Si no existiera el ejecutable que le pasamos a la función `check_execs()` 
entonces se detendrá el script y nos dirá que necesitamos instalarlo para 
ejecutar el script. Hacerlo así nos evita cualquier tipo de manipulación previa 
antes de darnos cuenta de que nos falta un elemento esencial para ejecutarlo al 
completo. Esta función funciona porque en Linux los ejecutables normalmente 
están colgando de una ruta del PATH. En Windows, por ejemplo, la cosa cambia.

Si queremos que el script sea multiplataforma y que nos funcione tanto en 
sistemas \*NIX como en Windows entonces necesitamos una función algo más 
compleja. En Windows un ejecutable no necesita colgar del PATH y es muy 
frecuente que no sea así. Al mismo tiempo en Windows podemos tener el sistema de 
ficheros repartido en varias unidades de disco, y necesitamos explorar todas 
ellas para buscar nuestro ejecutable. Aunque lo más frecuente es que se 
encuentre en la unidad C: y la función se detiene en cuanto encuentra el primer 
ejecutable, el hecho de realizar está búsqueda hace que el proceso sea más lento 
en Windows que en Linux. 

La función multiplataforma es la siguiente:

    :::python
    def check_execs_posix_win(progs):
        """Check if the program is installed.
    
        Returns one  dictionary with 1+n pair of key/values:
        
        A fixed key/value:
        
        "WinOS" -- (boolean) True it's a Windows OS, False it's a *nix OS
        
        for each program in progs a key/value like this:
        
        "program"  -- (str or boolean) The Windows executable path if founded else 
                                       '' if it's Windows OS. If it's a *NIX OS True
                                       if founded else False 
    
        """
        execs = {'WinOS':True if platform.system() == 'Windows' else False}
        # get all the drive unit letters if the OS is Windows
        windows_drives = findall(r'(\w:)\\',
                                 Popen('fsutil fsinfo drives', stdout=PIPE).
                                 communicate()[0]) if execs['WinOS'] else None
    
        progs = [progs] if isinstance(progs, str) else progs
        for prog in progs:
            if execs['WinOS']:
                # Set all commands to search the executable in all drives
                win_cmds = ['dir /B /S {0}\*{1}.exe'.format(letter, prog) for
                            letter in windows_drives]
                # Get the first location (usually in C:) where the executable exists
                for cmd in win_cmds:
                    execs[prog] = (Popen(cmd, stdout=PIPE, stderr=PIPE, shell=True).
                                   communicate()[0].split(os.linesep)[0])
                    if execs[prog]:
                        break
            else:
                try:
                    Popen([prog, '--help'], stdout=PIPE, stderr=PIPE)
                    execs[prog] = True
                except OSError:
                    execs[prog] = False
        return execs

En la parte de Windows (la de \*NIX es básicamente igual) esta función lo que 
hace es obtener primero las letras de las unidades de disco disponibles en el 
sistema. Luego busca el ejecutable en cada una de ellas y en cuanto encuentra 
la primera ruta al ejecutable se detiene. La función en este caso devuelve un 
diccionario donde hay una clave fija que es `WinOS` que será `True` si estamos 
en Windows y `False` en caso contrario. Luego nos devuelve una clave por cada 
uno de los programas que le mandemos comprobar. Esta clave sera booleana en el 
caso de *NIX y la ruta del programa (o una cadena vacía) en el caso de Windows.

*[booleana]: Verdadero o Falso. El nombre proviene de la Álgebra de Boole.

Las funciones y un ejemplo de su funcionamiento podéis encontrarlas en el
fichero `check_execs.py` en mi repositorio *Python Recipes* que se encuentra
alojado tanto en [bitbucket][bb] como en [github][gh].

   
   [bb]: https://bitbucket.org/joedicastro/python-recipes
   [gh]: http://github.com/joedicastro/python-recipes
     
