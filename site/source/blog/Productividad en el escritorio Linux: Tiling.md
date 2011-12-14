title: Productividad en el escritorio Linux: Tiling
date: 2011-11-25
tags: linux, ubuntu, unity, tiling, twm, productividad, xmonad

Los **Gestores de Ventanas de Mosaico** ([Tiling Windows Manager][twm]) son el 
gran desconocido entre la mayoría de usuarios de Linux. Y sin embargo, a mi 
juicio, suponen el salto más importante en productividad en el escritorio linux 
que se haya producido en mucho tiempo. Permiten manejar todo el escritorio sin 
apenas despegar las manos del teclado y sin verse relegado a emplear únicamente 
la consola. Las ventanas se distribuyen ellas solas de forma automática por la 
pantalla y no es necesario emplear el ratón para moverlas y redimensionarlas 
(aunque puede seguir empleándose, naturalmente).

  [twm]: http://en.wikipedia.org/wiki/Tiling_window_manager
  
A diferencia de un gestor de ventanas tradicional, a los que estamos normalmente 
acostumbrados, las ventanas no se apilan y flotan unas encima de otras, si no 
que se redistribuyen por toda la pantalla de acorde a un esquema previo (variable) 
sin solaparse entre ellas, quedando todas a la vista de forma simultanea. De ahí 
el símil del mosaico, donde el mismo seria el escritorio y donde las ventanas 
serian las teselas que lo componen. Puede no ser fácil visualizar de entrada en 
que consiste exactamente esto y como funciona, luego los vídeos nos ayudarán a 
entender mejor de lo que estoy hablando. Aunque uno no aprecia realmente las 
ventajas que aportan hasta que prueba uno. 

## ¿Que ventajas tienen?

Primero mencionar que esto no es una idea nueva, ni mucho menos, esto ya lo 
inventó en 1981 **Xerox** (el inventor a su vez de los entornos de ventanas) e 
incluso MS Windows 1.0 lo empleaba. La razón de que algo desarrollado desde hace
dos décadas aún no haya llamado demasiado la atención hasta ahora, es bien 
sencilla, el triunfo de un dispositivo de entrada más amigable e intuitivo que 
el teclado: el ratón. La metáfora de el entorno de ventanas con el escritorio 
junto con la del ratón como la extensión de nuestro brazo, propiciaba que fuera 
lo más natural emplearlo para mover las ventanas y redimensionarlas. Pero que 
sea más fácil o intuitivo no quiere decir que sea más eficiente, nadie en su sano 
juicio escribiría un documento empleando el ratón sobre un teclado virtual ni 
realizaría retoque fotográfico empleando únicamente el teclado. ¿Pero cuantos 
dirían que el teclado es el medio más eficiente para manejar las ventanas?

En una pantalla de grandes dimensiones y elevada resolución (e.g. un 
monitor de 24" y 1920x1200) es muy frecuente andar redimensionando continuamente 
las ventanas para acomodarlas y redistribuirlas dentro del escritorio. Nos sobra 
espacio por todos los lados y la mayoría de las aplicaciones que en monitores y 
resoluciones menores empleábamos maximizadas, ahora son incomodas de usar a 
pantalla completa (e.g. navegador web). ¿No sería útil que las ventanas se 
recolocaran y redimensionaran automáticamente por si solas? Más o menos esto es 
lo que viene a hacer un gestor de ventanas de mosaico. 

Pero cuales son las ventajas reales de este sistema:

* **Las ventanas se organizan solas**, muchas veces no necesitas mover o 
redimensionar una ventana, simplemente aparece en un lugar adecuado y con las 
dimensiones adecuadas. Una vez le que coges el truco te organizas de manera que 
esto ocurre con cierta naturalidad.

* **Se aprovecha todo el espacio de la pantalla**. Las ventanas se ajustan a todo 
el espacio libre disponible del escritorio. Aún así pueden emplearse paneles, 
docks, ...

* Las ventanas normalmente apenas tienen marco y carecen de barra de titulo y 
decoraciones, por lo tanto se ahorra espacio. Combinado con un menú integrado 
como el *Global Menu* de Unity, **se ahorra mucho espacio**.

* **No es un método excluyente**, aún se pueden emplear con toda normalidad las 
ventanas flotantes como habitualmente. Incluso pueden convivir entre ellas sin 
problema alguno.

* **En un sistema de múltiples monitores se facilita mucho el manejo de las 
múltiples ventanas** y el tener simultáneamente abiertas un número elevado de 
ellas es algo realmente sencillo. 

* **Es posible automatizar el tamaño, posición y escritorio virtual en donde se 
situara la ventana(s) de una aplicación al iniciarse**, lo que abre un mundo de 
posibilidades. 

* **Es posible tener múltiples escritorios virtuales (usualmente 9 por monitor) 
con características distintas en cada uno**. Puede ser un esquema distinto 
(desde una simple rejilla a un escritorio normal) o un escritorio para cada tarea 
(e.g. 1 - navegar, 2 - correo y redes sociales, 3 - trabajo, 4 - terminales, ...)

* **Mover las ventanas, redimensionarlas, lanzar aplicaciones, cerrarlas, ... y 
manejar los escritorios virtuales desde el teclado** es mucho más eficiente que 
emplear el ratón para lo mismo.

* **Te olvidas de buscar una ventana entre la pila de ventanas flotantes** sobre 
el escritorio, es sencillo incluso encontrar una ventana dentro de otro 
escritorio virtual (con unos gestores más que otros). Los escritorios modernos 
permiten mostrar un mosaico con todas las aplicaciones abiertas (Exposé, Scale, 
...), ¿pero que ocurre cuando tienes abiertas cerca de 30? con un twm la localizas enseguida si lo configuras adecuadamente, en mi caso menos de 2 segundos.

* **Te permite organizar las ventanas en función de múltiples patrones distintos:** 
rejillas, columnas, filas, espirales, por pestañas, etc... de forma automática, 
acomodándose a múltiples situaciones distintas.

* **Se pueden emplear de forma autónoma, sin un escritorio detrás** (gnome, kde, 
...) lo que permite tener un sistema muy ligero ideal para equipos poco potentes. 

* **Puede ser una manera de mejorar la accesibilidad del escritorio** para 
aquellos que encuentren dificultades para manejar un ratón pero puedan defenderse 
con un teclado.


## Inconvenientes

No son para todo el mundo. Soy plenamente consciente de ello, una buena mayoría 
de los usuarios son reticentes a aprenderse los atajos de teclado de una 
aplicación (hay quien no sabe cortar y pegar desde él), así que entiendo 
perfectamente que siquiera lleguen a plantearse el emplearlos. De hecho los 
tímidos avances que están realizando los escritorios en este sentido implican el 
uso del ratón para implantar un sucedáneo de este sistema. También es una 
cuestión de gustos, habrá a quien simplemente la desagradará el como funciona 
este sistema.

Por otro lado los profesionales multimedia que requieren un uso elevado del ratón 
probablemente prefieran seguir empleando un gestor de ventanas tradicional, 
aunque los gestores de mosaico pueden moverse con soltura en este entorno. 

También es cierto que la mayoría de ellos requieren un esfuerzo por nuestra 
parte para configurarlos a nuestro gusto. Aunque es precisamente esto lo que nos 
permite configurarlos exactamente a nuestro gusto, con muchas posibilidades de 
configuración. Pero es una barrera de entrada importante para los gestores más 
potentes y completos. Alguno hasta requiere conocimientos en algún lenguaje de 
programación (C, Lua, Haskell)

Aunque por un lado pueden suponer una ventaja en la accesibilidad a determinados 
discapacitados, pueden suponer un escollo para otros, pues no están tan adaptados 
como puedan estarlo los escritorios tradicionales para determinadas 
discapacidades.


## Tipos de gestores

Básicamente existen dos tipos de gestores de ventanas de mosaico, en función de 
el modo de organización de las ventanas. 

* ***Manuales***, requieren que el usuario sea quien decida la posición (a veces 
el tamaño) de las ventanas, con el inconveniente de la perdida de tiempo a costa 
de lograr un control más preciso.

* ***Automáticos***, ajustan automáticamente la posición y el tamaño de las 
ventanas en función del esquema por defecto. Posteriormente podemos variar tanto 
el esquema como la posición y tamaño de las ventanas individuales.

## Adaptación de la idea en los escritorios más comunes

Tal y como ocurre con los lanzadores de aplicaciones, los escritorios más 
tradiciones de linux comienzan a incorporar esta idea a sus desarrollos, en 
mayor o menor medida. Unity, Compiz, Gnome y KDE se han atrevido a dar un paso 
en esta dirección en sus últimas versiones:

* **Compiz Grid**, es un plugin de Compiz que permite realizar un tiling 
primitivo, empleando el ratón o el teclado. Divide la pantalla en una rejilla de 
3 x 3 y permite que las ventanas se ajusten al tamaño de una cuadricula o varias. 
Manejarlo desde el teclado es muy sencillo, simplemente pulsamos Ctrl + Alt + una 
tecla del teclado numérico del 1 al 9 según la cuadricula a la que la queramos 
ajustar la ventana. Para cambiar el tamaño de la ventana mantenemos pulsadas las 
teclas Ctrl + Alt y volvemos a pulsar la tecla numérica las veces que sea 
necesario hasta tener el tamaño que deseemos. Es decir, si pulsamos Ctrl+Alt+7 
nos sitúa la ventana en la parte superior izquierda de la pantalla ocupando 1/9 
de la misma. 

* **Unity**, emplea el plugin Grid de compiz anterior, pero modificado desde la 
versión 11.10 para que se comporte como ellos desean. En este vídeo se puede ver 
como se comporta este plugin manejándolo desde el teclado. Personalmente opino 
que mejor lo hubieran dejado como estaba.

<div style="text-align:center">
<iframe src="http://player.vimeo.com/video/32746967?title=0&amp;byline=0&amp;portrait=0&amp;color=59a5d1" width="667" height="417" frameborder="0" webkitAllowFullScreen mozallowfullscreen allowFullScreen></iframe><p>Demostración del tiling básico del plugin de Compiz, Grid, en Ubuntu 11.10 con Unity</p>
</div>

* **Gnome Shell**, tiene un tiling muy básico parecido al que emplea Unity. Te 
permite maximizar una ventana o ajustarla a la mitad derecha/izquierda de la 
pantalla simplemente arrastrándola al borde correspondiente.

* **KDE** a partir de la versión 4.4 tiene un tiling bastante conseguido, aunque 
no tan avanzado como los gestores dedicados. Desde luego es el escritorio que ha 
apostado más fuerte por este sistema y el que mejores resultados obtiene. Aunque 
no viene activarlo por defecto, es necesario activarlo a mano. De momento solo 
permite elegir entre dos esquemas predeterminados: columnas y espiral (fibonacci).

### Aplicaciones que funcionan como un gestor

Para aquellos que no quieran instalar un gestor o no empleen uno de los entornos 
de escritorio anteriores, siempre existe la posibilidad de emplear alguna de 
estas aplicaciones que emulan el comportamiento básico de un gestor de ventanas
de mosaico. Ambos son del tipo manual.

* [QuickTile][qtl], es un script en python que ofrece las mismas funcionalidades 
que el plugin Grid de Compiz. 

* [x tile][xtl], es una aplicación instalable (viene en los repositorios de 
algunas distros) que ofrece más opciones que la anterior. 

  [qtl]: http://ssokolow.github.com/quicktile/
  [xtl]: http://www.giuspen.com/x-tile/
  
  

## Gestores más populares

Hay muchos y para todos los gustos. Incluso los hay disponibles para otros SOs 
como Mac OS X o Windows (es muy famoso el WinSplit-Revolution para Windows, en 
el que se basa el plugin Grid, aunque los primeros gestores para linux son del 
2000 y WinSplit aparece en el 2007). Me centrare aquí solo en los más populares.


### [awesome][aw]

Automático. Escrito en *C* y *Lua*, es configurable y extensible en *Lua*. Basado 
en **dwm**
 
Uno de los dos grandes, junto con **Xmonad**. Es quizá el que más opciones 
presenta hoy en día. Está basado en XCB en vez de Xlib, lo que le proporciona 
mayor agilidad. Aporta su propia barra de información, bandeja del sistema 
(systray) y lanzador de aplicaciones integrado. Tiene un soporte de ratón 
superior a la competencia. Pero su desarrollo no es aún solido, varía demasiado a 
lo largo de las distintas versiones y te obliga a reconfigurarlo cada vez que 
sale una nueva.

</br>

### [bluetile][bt]


Automático. Escrito en *Haskell*. Basado en **Xmonad**

Es uno de los más sencillos de utilizar y de los más sencillos de probar. Es el 
más adecuado para probar por primera vez para los que se inician en esto. Está 
pensado para emplear conjuntamente con Gnome y pensando para que los están 
acostumbrados al ratón lo usen indistintamente con el teclado. En el siguiente 
vídeo realizado por su autor, Jan Vornberger, se puede ver como funciona:

<div style="text-align:center">
<iframe src="http://player.vimeo.com/video/6661713?title=0&amp;byline=0&amp;portrait=0" width="667" height="500" frameborder="0" webkitAllowFullScreen allowFullScreen></iframe>
</div>

</br>

### [dwm][dwm]

Automático. Escrito, configurable y extensible en *C*. 

Uno de los más ligeros, rápidos y simples. Su configuración se hace modificando 
su código fuente en *C* y luego hay que recompilarlo y reiniciarlo. Esto lo 
limita a usuarios avanzados con conocimientos de programación. Su diseño 
minimalista sido la inspiración para los dos más grandes: Awesome y Xmonad. 

Para lanzar las aplicaciones se desarrolló **dmenu** un lanzador basado en texto, 
que es muy empleado en otros gestores. Funciona al igual que los lanzadores 
gráficos como Gnome Do. 

</br>

### [i3][i3]

Manual. Escrito en *C* y configurable con ficheros de texto. Basado en **wmii**

Muy sencillo y que presume de estar bien documentado. Fácil de usar y configurar. 
Es manual, lo que le permite crear esquemas muy flexibles y personalizados, pero 
que por otro lado le resta comodidad. 

</br>

### [wmii][wmii]

Manual. Escrito en *C* y configurable en *bash*, *rc*, *ruby* o *python*

Escrito por el mismo desarrollador que **dwm**. Digamos que es el gestor 
equivalente a **dwm** pero manual. 

</br>

### [xmonad][xmnd]

Automático. Escrito, extensible y configurable en *Haskell*. Inspirado en **dwm**

Muy potente, estable y con muchas opciones. Es altamente personalizable, con 
muchas extensiones disponibles. Se integra muy bien con Gnome y KDE. Tiene un 
desarrollo muy activo y una gran comunidad de usuarios detrás. Es el que empleo 
desde hace meses y le he dedicado un [articulo completo][proxm].

</br>

Todos estos gestores están incluidos en los repositorios de Ubuntu, Debian, 
Gentoo y Arch Linux, y la mayoría están disponibles también en otras 
distribuciones. 

Como curiosidad, mencionar otros dos, que aunque no son muy populares, están desarrollados en Python: [tritium](http://sourceforge.net/projects/tritium/) y [qtile](http://qtile.org/)

  [aw]: http://awesome.naquadah.org/
  [bt]: http://bluetile.org/
  [dwm]: http://dwm.suckless.org/
  [i3]: http://i3wm.org/
  [wmii]: http://wmii.suckless.org/
  [xmnd]: http://xmonad.org/
  [proxm]: http://joedicastro.com/productividad-en-el-escritorio-linux-xmonad.html
  
  

