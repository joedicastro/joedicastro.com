title: Cambio de diseño
date: 2011/12/16
tags: blog, diseño, css

Después de los ligeros cambios de diseño que introduje en el sitio la semana 
pasada he decidido ir un poco más allá y dar un giro completo al mismo, 
conservando la estructura (casi no he tocado el HTML), pero con un diseño 
más limpio y minimalista.

La idea principal es la de favorecer aún más la lectura del mismo y darle el protagonismo absoluto al contenido (en el diseño anterior ya tenia un gran peso), 
eliminando todos aquellos elementos superfluos que pueden entorpecer o distraer 
de la lectura del mismo. Por eso he realizado cambios en la tipografía, el fondo, 
la división gráfica de las secciones, los cuadros con fragmentos de código y he 
eliminado los enlaces e iconos de la parte inferior. Además he transformado la 
página de *about me* en la de entrada al sitio. 

## Motivos del cambio

Realmente los motivos que me han llevado a realizar el cambio son mi propia 
tendencia, y cada vez la de más gente, a leer los contenidos web de otra forma.
Normalmente leo los articulos a través de un lector de feeds, como 
**Google Reader** o [RSSOwl](http://www.rssowl.org/), donde el contenido está 
compuesto únicamente por el texto y las imágenes originales del mismo, 
sobre un diseño sencillo que nos elimina cualquier trazo del diseño original. 
Esto facilita la lectura y unifica el diseño de sitios muy dispares. Lo que nos 
libra además de tener que lidiar con diseños recargados de imágenes, iconos, 
enlaces y publicidad[^1], centrándonos únicamente en lo que realmente importa: 
**el contenido**

Esta tendencia se ha acentuado últimamente con el éxito de servicios como los de 
[Read It Later][ril] e [Instapaper][insta] que nos permiten postergar para un 
momento más idóneo la lectura de aquello que nos interesa leer con calma. Además 
nos permite leer el contenido en formato *"solo texto"* y offline, sin tener que 
acceder al sitio original. Tal ha sido el éxito de estos servicios y tan clara la 
tendencia a emplear el modo texto de los mismos, que han surgido algunos nuevos 
servicios destinados precisamente a facilitar la lectura de cualquier contenido 
web. Los más destacados son [Readability][rdblty] y [Evernote Clearly][Eclearly]. 
Personalmente, cuando visito una pagina que tiene un diseño algo cargado y me 
interesa leer su contenido, no me lo pienso dos veces; tecleo ** `:rea ↹ ↵` ** en 
[Pentadactyl][penta] y en par de segundos tengo el texto en **Readability** para 
leerlo tranquilamente sin distracciones.

Aunque realmente no me acaba de convencer el diseño último de ninguno de estos 
sitios, por eso es mi idea el proporcionar la mejor experiencia de lectura 
posible de mi sitio, sin tener que recurrir a servicios externos. Porque desde mi 
punto de vista "lo simple es bello" y "menos es más", eliminar lo superfluo, 
contribuye a mejorar la calidad del diseño.

## Inspiración

Para el nuevo diseño, me he inspirado principalmente en los diseños de blogs en 
esta línea que más me gustan, como son los de [Steve Losh][slosh], 
[Armin Ronacher][armin], el tema [Manifest][manifest] para Wordpress o algunos 
de los temas minimalistas más empleados en **Tumblr**. 

Quizá lo más importante haya sido el cambio a una tipografía [Serif](http://es.wikipedia.org/wiki/Serif), por ser más cómoda la lectura empleando la misma. 
Y también el haberme decidido a emplear una [Web Font](http://es.wikipedia.org/wiki/Web_Open_Font_Format) después de haberlas descartado inicialmente para el sitio, 
para las cabeceras. Al haber eliminado los iconos inferiores y depender de una 
hoja de estilo alojada externamente en los servidores de Google, apenas se ve 
afectada la velocidad de carga y el peso de la página.


## CSS 3 para los bloques de código

Quizá lo más espectacular del cambio de diseño sea el nuevo aspecto que tienen 
ahora los bloques en los que se presentan los fragmentos de código, como el que 
sigue. Para poder verlos debidamente es necesario emplear una versión reciente 
del navegador web que permita HTML 5 y CSS 3. 

Estas son las reglas CSS 3 que empleo para implementarlo:

    :::css
    .codehilite:before, .codehilite:after {
        content: "";
        position: absolute;
        z-index: -1;
        -ms-transform: skew(-3deg,-2deg);
        -webkit-transform: skew(-3deg,-2deg);
        -o-transform: skew(-3deg,-2deg);
        -moz-transform: skew(-3deg,-2deg);
        bottom: 14px;
        box-shadow: 0 15px 5px rgba(0, 0, 0, 0.3);
        height: 50px;
        left: 1px;
        max-width: 50%;
        width: 50%;
    }
    
    .codehilite:after {
        -ms-transform: skew(3deg,2deg);
        -webkit-transform: skew(3deg,2deg);
        -o-transform: skew(3deg,2deg);
        -moz-transform: skew(3deg,2deg);
        left: auto;
        right: 1px;
    }
    
    .codehilite {
        position: relative;
        padding: 1px;
        background: #FAFAFA;
        box-shadow: 0px 0px 1px 1px rgba(0,0,0,0.2);
        -o-box-shadow: 0px 0px 1px 1px  rgba(0,0,0,0.2);
        -moz-box-shadow: 0px 0px 1px 1px  rgba(0,0,0,0.2);
        margin: 25px;
    }
    


### Diseño antiguo

Por supuesto *nunca llueve a gusto de todos* y habrá quien prefiera el aspecto 
anterior de la página, pero sinceramente creo que esto nuevo diseño contribuye en 
gran manera a ayudar a "digerir" los "pequeños" artículos con los que suelo 
prodigarme. Para que quede como testigo del cambio, está imagen corresponde 
con el diseño que tenia anteriormente el blog:

<p style="text-align:center;"><img src="pictures/diseño_2011.png" 
alt="diseño anterior del blog" title="diseño anterior del blog" width=700 
height=813 /></p>

[^1]: Bueno, nos libra de "casi" toda la publicidad, algunos deberían aprender que incluir publicidad en los feeds es de bastante mal gusto.


  [armin]: http://lucumr.pocoo.org/about/
  [slosh]: http://stevelosh.com/about/
  [manifest]: http://jimbarraud.com/manifest/
  [ril]: http://readitlaterlist.com/
  [rdblty]: http://www.readability.com/
  [insta]: http://www.instapaper.com/
  [Eclearly]: http://www.evernote.com/about/download/clearly.php
  [penta]: http://dactyl.sourceforge.net/pentadactyl/
  
  
  
  
