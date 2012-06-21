title: Productividad & Linux: Turses
date: 2012-06-21 22:50
tags: productividad, linux, ncurses, python, twitter

Que medio mundo parece estar conectado a [Twitter](http://twitter.com) no es
ninguna novedad. Y que si sigues a un buen número de personas, el intentar estar
al tanto de todo lo que ocurre es una temeridad, tampoco debería sorprender a
nadie. De hecho, dado su éxito y el enorme flujo de información que circula por
él, se han desarrollado cientos de herramientas para gestionarlo.

Desde que cree mi cuenta en twitter, he probado unas cuantas, unas veinte (y
solo en Linux, en el resto uso la web). La primera, y la elección más obvia ya
que por aquel entonces usaba Ubuntu, fue __Gwibber__ . Luego cansado de sus
muchos problemas, probé un sinnúmero de aplicaciones, solo merece la pena
reseñar una: [Hotot][htt]. Es la mejor aplicación gráfica para twitter en Linux
que conozco.

  [htt]: http://hotot.org/

Pero guiado por el mismo objetivo de [mejorar la productividad][pro] en mis
herramientas habituales de trabajo, me lancé a la búsqueda de un cliente de
twitter que encajara en la misma filosofía. No hay muchas alternativas, la
mayoría, hay que reconocerlo, son demasiado "crudas" incluso para mí, que soy un
amante de la consola. Pero entonces dí con una pequeña joya, [Tyrs][tyrs],
desarrollada por [Nicolas Paris][np]. Era una herramienta sencilla, pero que
cumplía muy bien con todo lo que buscaba de ella.  Pero un buen día, Nicolas, en
su afán por mejorarla, empezó a reescribir la herramienta empleando una nueva
librería para gestionar el interfaz. Las primeras versiones tenían varios fallos
y Nicolas pronto se vio desbordado por una tarea que no le apetecía continuar y
a la que no podía dedicar más tiempo. Y [decidió abandonar el proyecto][quit],
con la esperanza de que alguien se atreviera a retomarlo. Cuando leí la entrada
de su blog no perdí la esperanza del todo, al fin y al cabo, estaba desarrollado
en Python, un lenguaje con el que me desenvuelvo. Mientras esperaba que hacer,
seguí usando la última versión estable a diario. Pero entonces, apareció el
milagro, __Turses__

  [pro]: http://joedicastro.com/tag/productividad.html
  [tyrs]: http://tyrs.nicosphere.net/
  [np]: https://github.com/Nic0
  [quit]: http://www.nicosphere.net/small-projects-life-depends-on-his-owner/

## Turses

[Alejandro Gómez][gh_ag], un usuario de __Tyrs__ [se lanzó][dialelo] a crear su
propia aplicación basándose en él. Y no solo garantizaba la continuidad del buen
trabajo empezado por Nicolas, si no que llegaba lleno de ideas frescas y muchas
ganas de hacerlo bien. El propio Nicolas [le felicitó][greetings] por el trabajo
y la iniciativa. A día de hoy, el proyecto se sigue desarrollando, y aunque aún
tiene algunas metas marcadas por delante, la aplicación es perfectamente usable
en el día a día, de hecho es mi cliente habitual.

  [gh_ag]: https://github.com/alejandrogomez/
  [dialelo]: http://dialelo.com/Python/turses/2012/03/02/turses-un-cliente-de-twitter-con-interfaz-ncurses.html
  [greetings]: http://www.nicosphere.net/turses-a-fork-from-tyrs-ncurses-twitter-client/

Como ya se habrá podido deducir, [Turses][trs] es un cliente de twitter para la
consola con interfaz [ncurses][ncs]. Está desarrollado en Python y emplea la
librería [Urwid][urw] para crear la interfaz en curses. Lo mejor de esta
aplicación es que emplea atajos de teclado inspirados en __Vim__  y es
totalmente controlable desde el teclado. Esto unido a que emplea una interfaz
basada en texto, la convierten en la aplicación más ágil de todas las que haya
probado.  __Hotot__ también tiene algunas combinaciones de teclas muy útiles,
pero ni se acercan a lo que __Turses__  te permite.

  [trs]: https://github.com/alejandrogomez/Turses
  [ncs]: https://es.wikipedia.org/wiki/Ncurses
  [urw]: http://excess.org/urwid/

Aquí se puede ver el aspecto por defecto de Turses

<p style="text-align:center;"><img src="pictures/turses.png" width="700"
height="290" alt="Turses" /></p>

Pero no se acaban ahí las bondades de Turses, tiene algunas características
geniales como la gestión dinámica de bufferes (líneas temporales) y de columnas.
Demos un repaso a lo que nos permite la aplicación:

* __Múltiples líneas temporales__  (*bufferes*). Es decir, nos permite consultar
  los tweets de la gente a la que seguimos, los nuestros, menciones, etc. Es
  decir, los bufferes habituales, incluidos conversaciones, búsquedas y
  hashtags.  Y podemos tenerlas simultáneamente abiertas y navegar entre ellas
  muy fácilmente.
* __Múltiples columnas__. En cada columna se sitúa un buffer, y podemos añadir
  o quitar columnas a voluntad de forma muy sencilla. Es decir, que podemos
  visualizar un solo buffer de forma predefinida, o podemos ver varios a la vez
  distribuidos en múltiples columnas.
* __Tweet, Reply, Retweet, Borrar__. Vamos, que permite las operaciones
  habituales con los tweets. Además se puede hacer un Retweet editando el texto,
  algo que parece obvio, pero que en algunas aplicaciones no es tan sencillo.
* __Seguir/dejar de seguir__ a un usuario. Podemos hacerlo bien a través de un
  tweet o bien introduciendo el nombre del usuario.
* __Des/Marcar como favorito__.
* __Enviar mensajes directos__.
* __Abrir URLs en un navegador__. Nos permite abrir las direcciones que aparecen
  en un tweet, así como abrir el propio tweet.
* __Visualizar conversaciones__. Podemos abrir un nuevo buffer con la
  conversación relacionada con un tweet.
* __Contador de los no leídos__ funciona para todos los bufferes y nos permite
  ponerlo a cero manualmente cuando queremos ignorar algunos no leídos.
* __Búsqueda__. Se puede buscar tanto por usuario como por termino.
* __Ver los tweets de cualquier usuario __.
* __Visualizar el perfil de un usuario__.
* __Totalmente personalizable__ y la configuración se guarda en un fichero de
  texto plano.
* __Múltiples cuentas__, eso sí, una por ejecución.
* __Ayuda en línea__ con todas las combinaciones de teclas posibles. Accesible a
  través de la tecla __`?`__


Interfaz de Turses mostrando múltiples columnas

<p style="text-align:center;"><img src="pictures/turses_2cols.png" width="700"
height="285" alt="Turses con multiples columnas" /></p>

Y entre las metas que tiene marcadas su autor, nos encontramos con el soporte
para listas, streaming, notificaciones emergentes y múltiples sesiones. Estoy
seguro de que las acabará incorporando, le sobra capacidad. Aunque he de reseñar
que actualmente he contribuido con una porción de código minúscula al proyecto y
que tengo la intención de seguir colaborando en todo lo que pueda. Si eres
programador Python y te apetece echar una mano, [anímate][trs], Alejandro es muy
receptivo y un tío muy majo que estará encantado con toda la ayuda que le
podamos dar.

## Mi configuración

Si a alguien le puede servir como inspiración mi configuración, esta disponible
en [GitHub][gh] y en [Biitbucket][bb]

  [gh]: http://github.com/joedicastro/dotfiles
  [bb]: http://bitbucket.org/joedicastro/dotfiles

Turses mostrando la información del perfil del autor de un tweet

<p style="text-align:center;"><img src="pictures/turses_uinfo.png" width="700"
height="429" alt="Turses mostrando la información de un usuario" /></p>


## Alternativas

Solo conozco dos alternativas en la misma línea que merezca la pena reseñar, las
demás que he probado no estaban a la altura:

* [TwitVim][tvim], es un plugin para Vim. Funciona fantásticamente bien, eso sí,
  solo apropiado para usuarios de Vim. La probé un tiempo y me gusto, pero
  personalmente no me gusta emplear Vim para esta tarea y Turses es bastante más
  manejable.

* [TTYtter][tty], está escrito en Perl y no tiene interfaz. Trabaja en la línea
  de comandos a modo de interprete. Funciona muy bien y también lo usé un
  tiempo, pero su propio funcionamiento le reste eficiencia comparado con
  Turses.

  [tvim]: http://www.vim.org/scripts/script.php?script_id=2204
  [tty]: http://www.floodgap.com/software/ttytter/

