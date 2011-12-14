title: Python one-liners. Potencia en una sola línea
date: 2011-05-02 22:18
tags: one-liner, linux, python, javascript

Un [one-liner](http://en.wikipedia.org/wiki/One-liner_program) propiamente dicho
 es un comando de la consola que ejecuta una determinada función en "una sola 
 línea de texto". En Python esto se consigue con una única orden de línea de 
 comandos que llama al interprete y ejecuta los argumentos que le pasemos en 
 la misma. Aunque también se les denomina así a veces a funciones lambda y 
 funciones que han sido reducidas a una sola linea de código.

Un ejemplo de python one-liner es uno de los más famosos:

    :::python
    python -m this


Y que nos devuelve el popular [Zen of Python][0]:

    :::text
    The Zen of Python, by Tim Peters
    
    Beautiful is better than ugly.
    Explicit is better than implicit.
    Simple is better than complex.
    Complex is better than complicated.
    Flat is better than nested.
    Sparse is better than dense.
    Readability counts.
    Special cases aren't special enough to break the rules.
    Although practicality beats purity.
    Errors should never pass silently.
    Unless explicitly silenced.
    In the face of ambiguity, refuse the temptation to guess.
    There should be one-- and preferably only one --obvious way to do it.
    Although that way may not be obvious at first unless you're Dutch.
    Now is better than never.
    Although never is often better than *right* now.
    If the implementation is hard to explain, it's a bad idea.
    If the implementation is easy to explain, it may be a good idea.
    Namespaces are one honking great idea -- let's do more of those!

  [0]: http://www.python.org/dev/peps/pep-0020/

Pero existen varios one-liners muy útiles que nos pueden hacer la vida más fácil 
para determinadas tareas. 

### Iniciar un servidor web y compartir un directorio

    :::python
    python -m SimpleHTTPServer


Si ejecutamos este one-liner se iniciará un servidor web en el puerto `8000` de 
nuestra dirección local (`localhost` o `127.0.0.1`) que nos servirá los archivos 
del directorio donde lo ejecutemos. Para ello solo tenemos que acceder desde 
nuestro navegador a la dirección `http://localhost:8000` o `http://127.0.0.1`. 
Para interrumpir el servicio basta con que interrumpamos el programa con 
`Ctrl+C`. Si quisiéramos emplear un puerto distinto de *8000*, por ejemplo 
*8080*, solo tenemos que indicarselo:

    :::python
    python -m SimpleHTTPServer 8080


### Iniciar un servidor SMTP

    :::python
    python -m smtpd -n -c DebuggingServer localhost:25


Con este comando iniciamos un servidor de correo SMTP. Es básico, pero puede ser 
muy útil para crear un entorno temporal de pruebas. Dependiendo de la 
configuración de nuestro sistema, es muy probable que necesitemos ejecutar este 
comando como administrador (_root_). Si ya tenemos corriendo un servidor de 
correo en ese puerto, podemos cambiarlo por otro (eg: _2525_)

### Iniciar un servidor FTP

    :::python
    python -m pyftpdlib.ftpserver


Para poder ejecutar este comando es necesario tener instalada la librería 
[pyftpdlib][1]. Debemos además ser usuario con permisos de administrador de la 
maquina para poder iniciar este servidor. Una vez ejecutado tendremos un 
servidor FTP de solo lectura en el directorio en el que lo iniciemos.

  [1]: http://code.google.com/p/pyftpdlib/

### Ejecutar un cliente FTP

    :::python
    python -m ftplib


Si ejecutamos este comando, nos devolverá la ayuda con los argumentos necesarios 
para poder conectarnos a un servidor FTP.

### Abrir una página web en el navegador

    :::python
    python -m webbrowser http://joedicastro.com


Nos abrirá la dirección web que le indiquemos en el navegador web predeterminado 
de nuestro equipo.

### Obtener el código fuente de una página web

    :::python
    python -m urllib http://example.com


Esto nos imprime en pantalla el código fuente (HTML) de una dirección web.

### Eliminar las etiquetas HTML de un fichero HTML

    :::python
    python -m htmllib test.html


Esto nos imprime el contenido del fichero `test-html` pero sin mostrarnos las 
etiquetas HTML, solo texto plano. Algo parecido a lo que hace un navegador en 
modo texto como _links_, pero de forma estática.

### Comparar dos directorios

    :::python
    python -m filecmp dir_1 dir_2


De esta manera podemos comparar dos directorios. El resultado será un resumen de 
que ficheros son iguales, cuales diferentes y lo mismo con los subdirectorios.

### Identificar la plataforma

    :::python
    python -c 'from sys import platform; print platform'


Este nos sirve para identificar la plataforma sobre la que se ejecuta el comando 
(Windows, Linux, ...) No es de mucha utilidad, pero nos sirve como curiosidad. 
Otra opción más simple y que nos devuelve un resultado más completo sería:

    :::python
    python -m platform


### Obtener el nombre de la maquina (hostname)

    :::python
    python -c 'from socket import gethostname; print gethostname()'

ó

    :::python
    python -c 'import platform; print platform.node()'


Cualquiera de estos dos one-liners nos devolverán el nombre de la maquina en que 
los ejecutemos.

### Imprimir el calendario del año en curso

    :::python
    python -m calendar


Imprime en pantalla el calendario de todo el año. Para conocer más opciones, 
como imprimir el calendario de otro año, mes, etc añadir la opción `-h` al final 
de la línea.

### Mostrar los módulos empleados en un script

    :::python
    python -m modulefinder script.py 


De esta manera podemos no solo saber que módulos son importados por el script, 
si no que además nos muestra su ruta en el sistema de archivos.

Aquí he mencionado solo algunos que empleo con cierta frecuencia o que me han 
parecido reseñables, pero existen bastantes más. Una buena pista es que la 
mayoría hace uso de los módulos de la librería estándar de Python.

## Como funciona ##

Básicamente se trata de llamar al interprete Python utilizando uno de los 
siguientes argumentos:

 * `-c`: Lo que seguiría a esta opción sería un programa Python encerrado entre 
 comillas. Por ejemplo, el primer ejemplo quedaría de este modo, 
 `python -c 'import this'`

 * `-m`: Está opción llama a un modulo de python, que puede a su vez tener 
 distintas opciones y argumentos, y lo ejecuta como script. Por ejemplo: 
 `python -m locale`


## HTTPS Server

Este no es un one-liner en Python, pero sirve como complemento a los distintos 
servidores que hemos visto que se podían iniciar con mucha facilidad gracias a 
Python. Este código inicia un servidor HTTPS en Python en el puerto _4443_ de la 
dirección local. Lo suyo sería iniciarlo en el puerto _443_, y se puede hacer 
simplemente cambiándolo, pero se necesitan entonces permisos de administrador 
para iniciarlo.

    :::python
    import BaseHTTPServer, SimpleHTTPServer
    import ssl
    
    httpd = BaseHTTPServer.HTTPServer(('localhost', 4443),
                                      SimpleHTTPServer.SimpleHTTPRequestHandler)
    httpd.socket = ssl.wrap_socket (httpd.socket, 
                                    certfile='path/to/localhost.pem', 
                                    server_side=True)
    httpd.serve_forever()


El código es original de [Martin Pitt][MP] y me ha servido en más de una ocasión 
para probar un script.

 [MP]: http://www.piware.de/2011/01/creating-an-https-server-in-python/
 
<br />

### Editar una página web con javascript

No es un one-liner escrito en Python, si no en javascript, pero lo menciono aquí 
a modo de curiosidad porque siempre me ha parecido curioso y aparentemente 
inútil, pero tiene sus aplicaciones (alguna broma ha caído gracias a él).

    :::javascript
    javascript:document.body.contentEditable='true'; document.designMode='on'; void 0


Para ejecutarlo es muy sencillo. Abrimos nuestro navegador web favorito, 
abrimos la página web que deseamos editar y luego simplemente sustituimos el 
texto de la barra de direcciones por el de este one-liner y pulsamos Enter. 
Ahora podemos editar la página web como si fuera un procesador de texto.
