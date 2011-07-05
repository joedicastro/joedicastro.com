title: Conocer el tamaño de un directorio con Python
date: 2011-05-16 21:05
tags: python, script, linux, IEC, tamaño, directorio, fichero


Aunque conocer el tamaño de un directorio en sistemas como Linux es algo 
trivial, solo es necesario emplear el comando `du`, si queremos hacer lo mismo 
con **Python** -sin hacer uso de este comando- la cosa ya no es tan sencilla. 
Sobre todo si lo que queremos es una solución que nos devuelva tanto el tamaño 
de un fichero como el de un directorio. Cuando me encontré con esta necesidad lo 
primero que hice fue buscar en Internet para conocer alguna solución previa 
(reinventar la rueda no siempre es lo mejor) y me encontré con esto:

    :::python
    def get_dir_size(the_path):
        """Get size of a directory tree in bytes."""
        path_size = 0
        for path, dirs, files in os.walk(the_path):
            for fil in files:
                filename = os.path.join(path, fil)
                path_size += os.path.getsize(filename)
        return path_size


Esta solución nos daría el tamaño en bytes de un directorio. Pero esta solución,
 que encontré en varios sitios, presentaba dos problemas:

* **No da un tamaño exacto**. Esto se debe a que no tiene en cuenta las carpetas 
y ficheros ocultos (los que empiezan con un `.` en Linux) y los ficheros 
especiales `..` (que apuntan al directorio superior). Además tampoco tiene en 
cuenta los enlaces simbólicos. Por está razón la salida de esta función no 
coincide con el espacio que nos reporta el comando UN*X `du -bs`

*[UN*X]: Linux, Unix, Solaris, BSD, etc
    

* **No funciona para un solo fichero**. Solo trabaja cuando lo ejecutamos sobre 
un directorio, al hacerlo sobre un solo fichero nos dará como resultado siempre 0.

Teniendo en cuenta este punto de partida, elaboré una función que solucionara 
estos dos problemas y que devolviera el tamaño exacto de un directorio o 
fichero. Esta es la **función que nos da el resultado correcto**:

    :::python
    def get_size(the_path):
        """Get size of a directory tree or a file in bytes."""
        path_size = 0
        for path, directories, files in os.walk(the_path):
            for filename in files:
                path_size += os.lstat(os.path.join(path, filename)).st_size
            for directory in directories:
                path_size += os.lstat(os.path.join(path, directory)).st_size
        path_size += os.path.getsize(the_path)
        return path_size


El resultado de esta función es el mismo que el que nos devuelve el comando 
Linux `du -bs`. Además tiene en cuenta los enlaces simbólicos y no los sigue. 
Luego buscando una **solución ligeramente más rápida** (aunque menos elegante y 
*pythonica*) y que siguiera dando resultados precisos, cree una variante basada 
en el empleo de generadores. 

    :::python
    def get_size_fast(the_path):
        """Get size of a directory tree or a file in bytes."""

        def get_sizes(the_path):
            """Make a generator of individual file & directory sizes."""
            if not os.path.islink(the_path):
                if os.path.isdir(the_path):
                    for file_or_dir in os.listdir(the_path):
                        path = os.path.join(the_path, file_or_dir)
                        if os.path.isfile(path):
                            yield os.lstat(path).st_size
                        else:
                            for size in get_sizes(path):
                                yield size
                yield os.lstat(the_path).st_size
            else:
                yield os.lstat(the_path).st_size

        return sum(get_sizes(the_path))


### Obtener el tamaño del directorio en la mejor unidad posible ###

Estas funciones proporcionan el resultado que deseamos, pero lo entregan en una 
unidad difícilmente legible, en bytes. ¿Que ocurre si queremos verlo en 
[Mebibytes, GibiBytes][0], ... y que además sea siempre la más adecuada para una 
mejor visualización? Para responder a esta pregunta desarrolle una función que 
nos hace precisamente esto, tomar un tamaño en bytes y devolvernos el valor 
correcto en la [unidad binaria IEC][1] más adecuada:

  [0]: http://es.wikipedia.org/wiki/Prefijo_binario
  [1]: http://physics.nist.gov/cuu/Units/binary.html

    :::python
    def best_unit_size(bytes_size):
        """Get a size in bytes & convert it to the best IEC prefix for readability.

        Return a dictionary with three pair of keys/values:

        "s" -- (float) Size of path converted to the best unit for easy read
        "u" -- (str) The prefix (IEC) for s (from bytes(2^0) to YiB(2^80))
        "b" -- (int / long) The original size in bytes

        """
        for exp in range(0, 90 , 10):
            bu_size = abs(bytes_size) / pow(2.0, exp)
            if int(bu_size) < 2 ** 10:
                unit = {0:"bytes", 10:"KiB", 20:"MiB", 30:"GiB", 40:"TiB", 50:"PiB",
                        60:"EiB", 70:"ZiB", 80:"YiB"}[exp]
                break
        return {"s":bu_size, "u":unit, "b":bytes_size}


Esta función nos devuelve un diccionario con tres claves:

* `'s'`: Es el tamaño convertido a la mejor unidad IEC posible en términos de 
legibilidad.
* `'u'`: Es el prefijo IEC para el tamaño anterior.
* `'b'`: Es el tamaño original en bytes.

Para entenderla, lo mejor es mostrar algunos ejemplos:

    :::pycon
    >>> import get_size
    >>> size = get_size.best_unit_size(38467206502)
    >>> "{0:.2f} {1}".format(size['s'], size['u'])
    '35.83 GiB'
    >>> size = get_size.best_unit_size(45332)
    >>> "{0:.2f} {1}".format(size['s'], size['u'])
    '44.27 KiB'
    >>> size = get_size.best_unit_size(9878323)
    >>> "{0:.2f} {1} es igual a {2} bytes".format(size['s'], size['u'], size['b'])
    '9.42 MiB es igual a 9878323 bytes'


Y evidentemente, combinar las dos funciones en una, nos evita tener que pasar 
las dos a un mismo directorio/fichero. 

    :::python
    def get_unit_size(the_path):
        """Calculate size of a directory/file & convert it for the best IEC prefix.

        Return a dictionary with three pair of keys/values:

        "s" -- (float) Size of path converted to the best unit for easy read
        "u" -- (str) The prefix (IEC) for s (from bytes(2^0) to YiB(2^80))
        "b" -- (int / long) The original size in bytes

        """

        bytes_size = 0
        for path, directories, files in os.walk(the_path):
            for filename in files:
                bytes_size += os.lstat(os.path.join(path, filename)).st_size
            for directory in directories:
                bytes_size += os.lstat(os.path.join(path, directory)).st_size
        bytes_size += os.path.getsize(the_path)

        for exp in range(0, 90 , 10):
            bu_size = abs(bytes_size) / pow(2.0, exp)
            if int(bu_size) < 2 ** 10:
                unit = {0:"bytes", 10:"KiB", 20:"MiB", 30:"GiB", 40:"TiB", 50:"PiB",
                        60:"EiB", 70:"ZiB", 80:"YiB"}[exp]
                break
        return {"s":bu_size, "u":unit, "b":bytes_size}


Que nos devuelve un diccionario similar al anterior, lo que nos proporciona la 
posibilidad de disponer tanto del tamaño en bytes como en la mejor unidad IEC 
posible con una única función. 

Todas estas funciones con ejemplos (y además una clase que hace uso de ellas), 
se pueden encontrar en el fichero [get_size.py][2] de [mi repositorio][repo]. Si 
se ejecuta el fichero como un script puede verse una comparativa de las diversas 
funciones en rendimiento y precisión con respecto al comando `du -bs`

  [2]: https://bitbucket.org/joedicastro/python-recipes/src/tip/src/get_size.py
  [repo]: http://code.joedicastro.com
