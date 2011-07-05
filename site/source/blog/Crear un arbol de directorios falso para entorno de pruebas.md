title: Crear un arbol de directorios falso para entorno de pruebas
date: 2011-04-27 20:52
tags: script, python, Lorem Ipsum

A veces, para realizar pruebas con nuestros propios programas o para, por 
ejemplo, hacer pruebas con programas de Backup o FTP, necesitamos crear un 
entorno de pruebas que nos permita hacer todo tipo de operaciones sin comprometer 
la seguridad de nuestros datos reales. Una practica habitual es hacer copias de 
directorios de nuestros propios archivos y trabajar sobre ellos. Es algo que 
creo se debería dejar únicamente para la última fase de las pruebas, cuando en 
teoría ya todo funciona. Confundir ubicaciones y malograr los datos reales es 
más fácil de lo que pueda parecer, sobre todo si se comparte el mismo sistema de 
archivos. Otra veces lo que necesitamos es generar una estructura de directorios 
totalmente aleatoria, con sus correspondientes archivos de forma temporal. 

He creado un script **Python** que hace precisamente esto último, generar una 
jerarquía completa de directorios, de forma aleatoria, con sus correspondientes 
archivos de texto para simular una estructura de directorios real. Cuando le 
estaba dando vueltas a como generar de forma aleatoria los nombres de los 
archivos y que al mismo tiempo fuera multiplataforma (respetando los caracteres 
no permitidos según el sistema de archivos) me acorde de [Lorem Ipsum][0]. El 
texto que se lleva empleando desde los tiempos de la imprenta para generar 
borradores y que aún se emplea en diseño gráfico para los contenidos de prueba 
(al igual que en la web). No solo hacía de este modo un guiño a esta veterana 
prueba de maquetación, si no que me solucionaba la papeleta de generar los 
nombres de directorios y archivos. Al estar compuesto de "palabras" en latín 
(solo caracteres del alfabeto) me olvidaba de las incompatibilidades entre 
plataformas y sistemas de archivo. Un homenaje y un problema resuelto en un solo 
paso.

  [0]: http://es.wikipedia.org/wiki/Lorem_ipsum

Cuando me disponía ya a crear un modo de extraer palabras aleatorias del texto 
original de Lorem Ipsum, pensé que seguro que no era el primero al que se le 
ocurría hacer esto con Python, así que después de una pequeña búsqueda en el 
[PyPI][1], di con el magnifico proyecto de James Hales, 
[Lorem-Ipsum-Generator][2]. Importando el modulo de este proyecto en mi script, 
tenía medio trabajo hecho.

*[PyPI]: Python Package Index
   
   [1]: http://pypi.python.org/pypi
   [2]: http://code.google.com/p/lorem-ipsum-generator/

El script, al que llamo **test_dir_tree**, genera una estructura de directorios 
de entre 7 y 39 directorios (estos parámetros pueden ser fácilmente cambiados en 
el script), con sus correspondientes archivos. El número de archivos se decide 
en función del número de directorios y se reparten también de forma aleatoria 
entre los mismos. Como he comentado, los nombres tanto de directorios como 
ficheros proceden de Lorem Ipsum. El tamaño de los archivos oscila entre 3 y 512 
Kbytes, para no ocupar demasiado espacio en disco. Son archivos de texto 
normales en los cuales el contenido está formado a su vez por párrafos 
aleatorios de Lorem Ipsum.

No es necesario ningún parámetro para ejecutar el script:

    :::console
    python test_dir_tree.py

Una vez ejecutado el script, se genera una estructura de directorios como la de 
este ejemplo:

    :::text
    test
    ├── blandit
    │   ├── [234K]  bibendum.txt
    │   ├── [319K]  congue.txt
    │   ├── [382K]  consequat.txt
    │   └── [298K]  ligula.txt
    ├── elit
    ├── est
    │   ├── [ 22K]  condimentum.txt
    │   ├── [401K]  hac.txt
    │   ├── [139K]  nibh.txt
    │   └── [ 12K]  tincidunt.txt
    ├── habitasse
    │   ├── [359K]  etiam.txt
    │   ├── [ 59K]  facilisi.txt
    │   ├── [ 12K]  integer.txt
    │   ├── [ 23K]  metus.txt
    │   └── [ 31K]  non.txt
    ├── lacus
    │   ├── [394K]  faucibus.txt
    │   └── [ 29K]  torquent.txt
    ├── laoreet
    │   └── [424K]  eros.txt
    ├── litora
    │   └── [ 87K]  tellus.txt
    └── nostra
        ├── [349K]  curabitur.txt
        ├── [241K]  neque.txt
        ├── [3.4K]  odio.txt
        └── [ 78K]  sapien.txt


Donde el principio del contenido de uno de esos archivos de texto, sería algo así:

    :::text
    Eget. Sem turpis tempus sagittis arcu, nullam ac rutrum turpis. Sem
    fusce lacus, cum neque fermentum potenti. Est aliquam donec, leo
    amet elit dapibus ipsum. Quam pellentesque eu fusce pellentesque
    torquent netus vivamus velit at nisl. Senectus ligula, erat dictum.
    Natoque metus urna quis vivamus in duis. Cras. Massa nam. Quisque.
    Potenti, sit. Urna metus, et eu duis suspendisse per primis. Duis,
    viverra massa enim hac.
    
    Fames ut leo in a turpis proin gravida ac, auctor. Natoque
    suspendisse nisl. Dictumst mus, amet pede, eni velit velit. Elit.
    Cum. Congue pretium ad id porta in massa enim purus. Tempus, porta
    donec molestie habitasse, urna urna nam. Tempor massa sed quam sit
    nec dapibus at, duis. Leo pellentesque. Orci arcu iaculis ac, elit
    netus conubia. Penatibus platea rutrum netus suspendisse non. Purus
    consequat. Inceptos platea, tempus metus eu consectetuer feugiat,
    urna at lorem pellentesque curae. Dapibus a, scelerisque cum, auctor
     tincidunt primis. Augue nisi id per nulla, sit enim mus id eleifend
     taciti, semper est.


El script tarda muy poco en generar esta estructura, por ejemplo en un Core 2 
Duo a 2 GHz, se tardan 1.72s en generar una estructura de 71 directorios y 114 
ficheros.

Este es el núcleo central del script **test_dir_tree.py**:

    :::python
    def test_tree(path, min_dirs=7, max_dirs=79):
        """make a fake directory hierarchy with files for test purposes."""
    
        def latin_words(generator):
            """Generate a list of latin words"""
            words = generator.generate_paragraphs_plain(9).lower()
            return list(set(words.replace('.', '').replace(',', '').split()))
    
        def check_path(path):
            """If no exists a path, make it."""
            if not os.path.exists(path):
                os.mkdir(path)
    
        lorem = lipsum.MarkupGenerator()
        latins = latin_words(lorem)
    
        dirs = latins[:randrange(min_dirs, max_dirs)]
        files = [f for f in latins if f not in dirs][:len((dirs) * 3) - 3]
    
        check_path(path)
        for directory in dirs:
            check_path(os.path.join(path, directory))
    
        for fil in files:
            filename = os.path.join(path, choice(dirs), '{0}.txt'.format(fil))
            text = ''
            size = randint(3, 524288) # Files not bigger than 512 Kbytes
            sample = lorem.generate_paragraphs_plain(randrange(3, 9))
            while len(text) < size:
                text += sample + os.linesep * 2
            with open(filename, 'w') as out:
                out.write(text[:size])
    
        return dirs, files


Para obtener el script completo, acudir a mi [repositorio][3].

  [3]: https://bitbucket.org/joedicastro/python-recipes/src/tip/src/test_dir_tree.py
