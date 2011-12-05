title: Convertir ficheros djvu a pdf en Linux
date: 2011-12-3
tags: script, python, djvu, pdf, linux


Tengo por costumbre almacenar mis documentos escaneados en el formato 
[djvu][djvu], que fue expresamente creado para esa tarea y que otorga la mejor 
calidad posible en el menor espacio. Es el formato perfecto para documentos 
complejos sobre los que no se va a realizar un [OCR][ocr] (aunque también lo soporta). Además es un formato abierto, por lo que nos garantiza que podrá seguir 
empleándose en un futuro. Pero a veces necesito compartir estos ficheros con 
otros y para evitarme problemas suelo convertirlos a un formato más conocido y 
difundido como [PDF][pdf].

  [djvu]: http://es.wikipedia.org/wiki/DjVu
  [pdf]: http://es.wikipedia.org/wiki/Pdf
  [ocr]: http://es.wikipedia.org/wiki/Reconocimiento_%C3%B3ptico_de_caracteres
  

Para realizar esta conversión empleo desde hace años (la primera versión es del 
2009) un sencillo script en python. Ahora que he necesitado una conversión 
masiva de documentos de un formato al otro, he modificado el script para hacer 
esto más sencillo y he decidido compartirlo con cualquiera que pueda necesitarlo. 

### Los requisitos previos

Está diseñado para funcionar en Linux y necesita de la instalación de dos 
pequeños programas que son los que realmente realizan la conversión. Estos dos 
programas son `ddjvu` y `tiff2pdf`. Además de tener instalado **Python** en una 
versión *2.7* o superior. Estos dos programas vienen en los repositorios de 
prácticamente todas las distribuciones importantes dentro de los paquetes 
[djvulibre][djl] y [libtiff][ltf].

  [djl]: http://djvu.sourceforge.net/
  [ltf]: http://libtiff.maptools.org

En el caso de no tenerlos instalados, la instalación de los mismos es muy 
sencilla, para distribuciones basadas en Debian/Ubuntu:

    :::console
    $ apt-get install djvulibre-bin libtiff-tools

`ddjvu` nos extrae las páginas que conforman el documento *.djvu* a un archivo intermedio en formato *.tiff* y `tiff2pdf` nos lo convierte en *.pdf*.
 
### Modo de empleo

Emplearlo es muy sencillo, como se puede ver en la ayuda del mismo:

    :::console
    $ djvu2pdf -h
    usage: djvu2pdf [-h] [-d | -z] [-v] file [file ...]

    Converts a djvu file into a pdf file

    positional arguments:
      file           The djvu file

    optional arguments:
      -h, --help     show this help message and exit
      -d             no compression. Best quality but big files.
      -z             zip compression. More quality, more size.
      -v, --version  show program's version number and exit

Básicamente llamandalo desde python y poniendo a continuación el nombre del 
fichero/s es lo único que necesitamos para ejecutarlo, por ejemplo:

    :::console
    $ ls
    documento.djvu  documento_2.djvu
    $ python djvu2pdf.py documento.djvu documento_2.djvu
    $ ls
    documento.djvu  documento.pdf  documento_2.djvu  documento_2.pdf

Opcionalmente tenemos las opciones `-d` y `-z`, que nos sirven para especificar 
si queremos no emplear compresión en el *.pdf* (por defecto emplea compresión 
[jpeg][jpeg]) o emplear compresión [zip][zip], respectivamente. Si no empleamos compresión, la calidad final será la mejor posible, pero los archivos serán muy grandes. En cambio, empleando *zip*, tenemos unos ficheros ligeramente mayores a cambio de una calidad muy buena. Aunque la compresión *zip* puede dar problemas 
con algunos visores y lectores de ebooks.

  [jpeg]: http://es.wikipedia.org/wiki/Jpeg
  [zip]: http://es.wikipedia.org/wiki/Formato_de_compresi%C3%B3n_ZIP
  
  
### El script, djvu2pdf.py

El contenido del scipt es el que sigue. Este está disponible, actualizado siempre 
a la última versión, en mi [repositorio][repo]

  [repo]: https://bitbucket.org/joedicastro/python-recipes/src/tip/src/djvu2pdf.py
  
    :::python
    #!/usr/bin/env python
    # -*- coding: utf8 -*-

    """
        djvu2pdf.py: Converts a .djvu file into a .pdf file
    """

    #==============================================================================
    # This Script does exactly as the description above says.
    #==============================================================================

    #==============================================================================
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
    #==============================================================================

    __author__ = "joe di castro <joe@joedicastro.com>"
    __license__ = "GNU General Public License version 3"
    __date__ = "03/12/2011"
    __version__ = "0.3"

    try:
        import sys
        import os
        from argparse import ArgumentParser
        from subprocess import Popen, PIPE
    except ImportError:
        # Checks the installation of the necessary python modules
        print((os.linesep * 2).join(["An error found importing one module:",
        str(sys.exc_info()[1]), "You need to install it", "Stopping..."]))
        sys.exit(-2)


    def check_execs(*progs):
        """Check if the programs are installed, if not exit and report."""
        for prog in progs:
            try:
                Popen([prog, '--help'], stdout=PIPE, stderr=PIPE)
            except OSError:
                msg = 'The {0} program is necessary to run the script'.format(prog)
                sys.exit(msg)
        return


    def arguments():
        """Defines the command line arguments for the script."""
        main_desc = """Converts a djvu file into a pdf file"""

        parser = ArgumentParser(description=main_desc)
        parser.add_argument("file", nargs="+", help="The djvu file")
        group = parser.add_mutually_exclusive_group()
        group.add_argument("-d", dest="qlty", action="store_const", const="-d",
                            help="no compression. Best quality but big files.")
        group.add_argument("-z", dest="qlty", action="store_const", const="-z",
                            help="zip compression. More quality, more size.")
        parser.add_argument("-v", "--version", action="version",
                            version="%(prog)s {0}".format(__version__),
                            help="show program's version number and exit")
        return parser


    def process(command, fname):
        """Process the external commands and report the errors."""
        errors = Popen(command, stderr=PIPE).stderr.readlines()
        for line in errors:
            print("{0}: {1}".format(fname.upper(), line.rstrip(os.linesep)))


    def main():
        """Main section."""
        args = arguments().parse_args()
        djvu_files = args.file

        for djvu in djvu_files:
            if not os.path.exists(djvu):
                print("ERROR: cannot open '{0}' (No such file)".format(djvu))
            else:
                djvu_filename = djvu.split(".djvu")[0]
                tiff = '{0}.tif'.format(djvu_filename)
                pdf = '{0}.pdf'.format(djvu_filename)
                process(['ddjvu', '-format=tiff', djvu, tiff], tiff)
                if os.path.exists(tiff):
                    quality = args.qlty if args.qlty else "-j"
                    process(['tiff2pdf', quality, '-o', pdf, tiff], pdf)
                    os.remove(tiff)


    if __name__ == "__main__":
        check_execs('ddjvu', 'tiff2pdf')
        main() 
  
