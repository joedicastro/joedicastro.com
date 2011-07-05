title: Mover todos los archivos del mismo tipo de un arbol de directorios a la vez
date: 2011-04-26 23:17
tags: python, script, mover, copiar, borrar, linux, windows

A veces tenemos la necesidad de **mover (o copiar o borrar)** varios ficheros 
del mismo tipo a la vez, pero estos no "cuelgan" de un solo directorio, si no 
que se encuentran repartidos dentro una jerarquía de subdirectorios. En este 
caso los típicos comandos para mover/copiar/borrar archivos no nos sirven, ni 
siquiera los útiles comodines nos resuelven el problema.  ¿Como lo hacemos 
entonces?

Por ejemplo, si tenemos una estructura de directorios como esta:

    :::text
    raiz
    ├── dir_1
    │   ├── imagen_1.jpg
    │   ├── pdf_1.pdf
    │   ├── texto_1.txt
    │   └── texto_2.txt
    ├── dir_2
    │   ├── imagen_2.jpg
    │   ├── imagen_3.gif
    │   └── texto_3.txt
    ├── dir_3
    │   ├── doc_1.doc
    │   ├── pdf_2.pdf
    │   ├── pdf_3.pdf
    │   ├── pdf_4.pdf
    │   ├── texto_4.txt
    │   └── texto_5.txt
    ├── dir_4
    │   ├── subdir_1
    │   │   └── imagen_4.png
    │   ├── subdir_2
    │   │   ├── pdf_5.pdf
    │   │   └── texto_7.txt
    │   ├── doc_2.doc
    │   └── texto_6.txt
    └── dir_5


Y queremos mover todos los ficheros `.txt` al `dir_5` que tenemos vacío, ¿Como 
lo hacemos? Bueno, en el caso de **Linux** (y UNIX) podemos hacerlo en una sola 
operación gracias al siempre útil y versátil `find` con el siguiente comando 
(ejecutado desde el directorio raíz):

    :::bash
    find . -type f -name *.txt -exec mv {} ./dir_5 \;


Este comando nos encontraría todos los archivos con la extensión `.txt` dentro 
de todos los directorios y subdirectorios y los iría moviendo uno a uno al 
`dir_5`. Es un comando rápido y efectivo. Genéricamente, el comando sería así:

    :::bash
    find directorio_origen -type f -name *.EXT -exec mv {} ./directorio_destino \;


donde `EXT` sería la extensión del tipo de archivo que queremos mover. Se puede 
emplear esta variante para copiar los archivos en vez de moverlos:

    :::bash
    find directorio_origen -type f -name *.EXT -exec cp {} ./directorio_destino \;


Y esta otra para eliminarlos (¡emplear con cuidado!):

    :::bash
    find directorio_origen -type f -name *.EXT -exec rm -f {} \;


Partiendo de la idea de hacer algo equivalente en **Python**, he creado un 
script que hace algo similar a esto, sin la necesidad de teclear todo el comando 
(y con el riesgo a equivocarse y liarla parda) y que también sirve para que los 
no trabajen habitualmente con la consola no necesiten recordar (o anotar) esos 
comandos.

La parte principal del script **move_by_ext.py** es la siguiente:

    :::python
    def find_and_process(args, count=0, log=""):
        """Find the files by file extension and process (move/copy/remove) them."""
    
        def process(the_path, the_file):
            """Process each file."""
            processed = 0
            src_file = os.path.join(the_path, the_file)
            dst_file = os.path.join(args.dst, the_file)
            if args.rm:
                os.remove(src_file)
                processed = 1
            else:
                if not os.path.exists(dst_file): # not replace if already exists 
                    if args.cp:
                        shutil.copy2(src_file, dst_file)
                    else:
                        shutil.move(src_file, dst_file)
                    processed = 1
            return processed
    
        if not os.path.exists(args.dst):
            os.mkdir(args.dst)
        for path, directories, files in os.walk(args.src):
            for fil in files:
                # ignore files without extension (can have the same name as the ext)
                file_ext = fil.split('.')[-1] if len(fil.split('.')) > 1 else None
                # ignore dots in given extensions
                extensions = [ext.replace('.', '') for ext in args.ext]
                if file_ext in extensions:
                    count += process(path, fil)
    
        opt = int("{0}{1}".format(int(args.rm), int(args.cp)), 2)
        log = "Files {0}: {1}".format({0:"moved", 1:"copied", 2:"removed"}[opt], count)
        return log

Este script nos permite realizar las mismas operaciones que los comandos 
anteriores y además tiene dos ventajas adicionales:

* **Permite emplear varias extensiones a la vez**, lo que nos permite
mover/copiar/borrar distintos tipos de archivo en una sola operación.
Por ejemplo si queremos mover todos los tipos de imagen de la estructura de 
directorios anterior, podríamos hacerlo indicándole que emplee las extensiones 
`.jpg`, `.gif` y `.png` en la misma operación. El comando sería el siguiente 
(las extensiones pueden llevar o no el punto, funciona exactamente igual), 
ejecutado desde el directorio raíz:


    `python move_by_ext.py jpg .gif png -d ./dir_5`

* **Funciona en Windows**. A diferencia del comando para Linux, este se puede 
emplear en Windows sin necesidad de instalar ningún entorno que nos simule un 
shell Linux (como [Cygwin](http://www.cygwin.com/)) y solo es necesario tener 
instalado Python 2.7

La sintaxis del script es muy sencilla y se puede ver reflejada en la ayuda del 
mismo:

    :::console
    $ python move_by_ext.py -h
    usage: move_by_ext.py ext [-s SRC] [-d DST] [-c | -r] [--help]
    
    Move (or copy/remove) all files selected by extension into a directory tree to
    a destination directory.
    
    positional arguments:
      ext                the extension(s) of the files to process. To use more
                         than one extension, separate them with a space
    
    optional arguments:
      -h, --help         show this help message and exit
      -s SRC, --src SRC  the source path. Current dir if none is provided
      -d DST, --dst DST  the destination path. Current dir if none is provided
      -c, --copy         copy all the files with the given extension(s) to the
                         destination directory.
      -r, --remove       remove all the files with the given extension(s). Use
                         with caution! remove also in the subdirectories
      -v, --version      show program's version number and exit


El script completo puede encontrarse en mi [repositorio][0].

  [0]: https://bitbucket.org/joedicastro/python-recipes/src/tip/src/move_by_ext.py
