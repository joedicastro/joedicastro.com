title: De Drupal a Pelican
date: 2011-06-22 02:10
tags: markdown, restructuredtext, pelican, drupal, cms, python, blog, html

Este blog no está realizado con ningún CMS, ni siquiera utiliza BDD alguna, es 
simplemente HTML + CSS y nada más. Es decir, es contenido estático, no dinámico.
Hasta hace 3 días estaba funcionando con el mejor CMS [PHP][0] que conozco, 
[Drupal][1]. Pero persiguiendo el camino hacia el minimalismo y la productividad 
(fiel al espíritu [KISS][2]) que ya inicie cuando [comencé a escribir todos mis 
artículos en Drupal con Markdown][3], el siguiente paso era evidente. La pregunta
era muy sencilla, si un blog consta de contenidos que rara vez cambian 
(exceptuando los comentarios) ¿para que necesito un gestor de contenidos 
dinámicos?

*[CMS]: Content Management System (en español, "Sistema de gestión de contenidos")
*[BDD]: Base de datos
*[KISS]: Keep It Simple, Stupid (en español, "Mantenlo simple, estúpido"). Ver enlace
 [0]: http://es.wikipedia.org/wiki/PHP
 [1]: http://drupal.org
 [2]: http://es.wikipedia.org/wiki/Principio_KISS
 [3]: http://joedicastro.com/markdown-la-mejor-opcion-para-crear-contenidos-web.html

 
La respuesta es fácil, para nada. Actualmente, gracias a servicios como los de 
[Disqus][4], [Livefyre][15], [IntenseDebate][16] ó [Echo][17] es posible 
externalizar el único contenido dinámico básico de un blog, los comentarios. 
Todo lo demás puede ser contenido puramente estático, solo HTML y CSS, sin 
renunciar a prácticamente nada de lo que nos ofrece un blog basado en un CMS 
como Wordpress o Drupal. Se pueden emplear scripts externos en javascript si se 
desea, o insertarlos dentro del HTML. Lo que nos permite implementar lo mismo 
que en un blog normal. Además se puede disponer también de feeds RSS y Atom.  
 
 [4]: http://disqus.com
 [15]: http://livefyre.com/
 [16]: http://intensedebate.com/
 [17]: http://www.aboutecho.com/commenting
 

## Elegir un generador de contenido estático

 
Evidentemente la idea no es crear las paginas HTML a mano, ni de broma, lo lógico 
era seguir empleando la misma estrategia que ya había iniciado con Drupal, 
emplear solo ficheros de texto en formato Markdown que nos generarán el HTML 
necesario de forma automática. Entonces lo que tenía que encontrar era un 
software que me permitiera hacer lo mismo que Drupal, pero sin toda la 
parafernalia que rodea a un CMS. Un generador de sitios web estáticos (a partir 
de markdown) y que a ser posible estuviera escrito en **Python**, mi lenguaje 
favorito. Como ya adelante en el [artículo sobre Markdown][3], existen varias opciones:

* [Pelican][5] de Alexis Métaireau, que emplea en su propio [blog][6]
* [Blogofile][7] de Ryan McGuire que también lo usa en su [blog][8]
* [Hyde][9] de Lakshmi Vyas. Su [blog][10] con Hyde también.
* [rstblog][11] de Armin Ronacher. Solo permite reStructuredText, con él crea su 
[blog][12], un ejemplo de elegancia y calidad.

 [5]: http://docs.notmyidea.org/alexis/pelican/
 [6]: http://blog.notmyidea.org/
 [7]: http://www.blogofile.com/
 [8]: http://www.enigmacurry.com/
 [9]: http://hyde.github.com/
 [10]: http://ringce.com/blog/
 [11]: https://github.com/mitsuhiko/rstblog
 [12]: http://lucumr.pocoo.org/
 
 
Bueno, tenía varias posibilidades, solo tenía que elegir una que se adaptara 
mejor a mis necesidades. De entrada descarté **rstblog** porque no permitía el 
empleo de markdown, cuando los otros permitían tanto .rst como .md como formatos 
de entrada. Solo me quedaban 3 candidatos. Así que lo primero que hice antes de 
nada, fue buscar blogs creados con cada uno de ellos, para ver que posibilidades 
reales ofrecían. Encontré ejemplos de blogs de mucha calidad de todos ellos. 
Aunque enseguida me di cuenta de una cosa, en dos de ellos los mejores blogs lo 
eran porque tenían una elevada personalización detrás (artículos de sus autores 
contándolo). Y curiosamente con el tercero, casi todos preferían quedarse con la 
configuración estándar, sin tocar prácticamente nada, y la verdad es que el 
resultado era bastante decente. Luego miré que cargaba cada uno de ellos en la 
página de entrada, y volvía a repetirse la misma tendencia. En los dos primeros 
vi demasiadas hojas de estilo, imágenes y demasiados scripts javascript, en el 
tercero, nuevamente se cargaban menos elementos. Finalmente comparé 
características, modo de funcionamiento y le eché un vistazo rápido al código. 
La impresión era otra vez la misma, dos de ellos, **Hyde** y **Blogofile** aunque 
aparentemente potentes, los veía innecesariamente complejos, en cambió 
**Pelican** era bastante más sencillo. Otra forma de determinar su repercusión 
era contar el número de descargas de cada una de las aplicaciones desde PyPi. 
Los números son los siguientes (a 27 de Junio de 2011), obtenidos con 
[Vanity][vnt] o [pythonpackages.com][ppkg]:

| Paquete   | Descargas | Descargas (2 de Diciembre de 2011) |
| --------- | :-------: | :--------------------------------: |
| Blogofile |     2.419 |                              3.854 |
| Hyde      |     1.945 |                              4.518 |
| Pelican   |     3.919 |                              6.138 |

  [vnt]: https://github.com/aclark4life/vanity
  [ppkg]: http://pythonpackages.com/
  

La elección final era Pelican y no me arrepiento en absoluto, la prueba es que 
esté blog está funcionando gracias a él (Gracias Alexis!). Aunque las otras dos 
son también muy buenas opciones, y seguramente serían la primera opción para más 
de uno. Y siempre podría cambiar fácilmente, porque el contenido seguiría estando 
guardado en ficheros de texto con marcado markdown. 

**Actualización** (2-12-2011): 

La estructura de Pelican es tan sencilla y eficaz, que [Jökull Sólberg][jokull] 
ha creado a partir de una versión hospedada del mismo (y modificada) una de las 
plataformas de blogs más simples de utilizar que existen, [calepin.co][caco]. 
Publicar articulos es tán fácil como crear un archivo markdown y guardarlo en tu 
cuenta de [Dropbox][dbox]. Así de sencillo.

  [jokull]: http://www.solberg.is/
  [caco]: http://calepin.co/
  [dbox]: http://www.dropbox.com/
  

No entraré en detalles ahora de como instalar y emplear **Pelican**, eso lo dejo 
para otro próximo articulo, [Pelican][13]. Pero si voy a hacer un repaso de los 
pros y los contras de emplear Pelican frente a un CMS como Drupal para crear un 
blog.

 [13]: http://joedicastro.com/pelican-introduccion-e-instalacion.html
 

## Ventajas de Pelican vs CMS


#### Solo ficheros de texto, No BDD

Simplemente te tienes que preocupar de eso, ficheros de texto, es donde guardas 
el contenido que creas. Todo lo demás lo genera Pelican por ti. Nada de crear y 
gestiónar bases de datos, ni copias de seguridad de la misma y un montón de 
espacio y recursos desaprovechado solamente para generar dinámicamente el mismo 
contenido que te genera Pelican.

#### Mejor rendimiento, carga de página más rápida

Generar contenido dinámico es más caro en recursos y es más lento (consultas a 
la BDD). Sobre todo a medida que llenas tu CMS de personalizaciones y plugins. 
¿Que hacen prácticamente todos los sistemas de caché?, generar contenido 
estático para luego servirlo más rápidamente. ¿No es un poco estúpido crear 
contenido que apenas cambia en el tiempo, en un sistema dinámico que genera ese 
contenido cada vez y que para mejorar su rendimiento lo convierte en estático? 
Y ya no hablemos de las múltiples hojas CSS, scripts javascript y enlaces a 
contenido externo que cargan la mayoría de los CMS por defecto. Cada plugin que 
añadimos pone su granito de arena y optimizar todo esto requiere dedicación y 
esfuerzo (o seguir sumando aún más plugins en el mejor de los casos). Con 
Pelican ya tienes directamente el contenido estático y menos recursos que 
descargar. En este blog, sin contar con los ficheros javascript de Disqus y 
Piwik, lo único que se descarga es un fichero HTML, una hoja CSS y las imágenes 
que se incluyen en los artículos (cuando las hay). Es decir sirves el mismo 
contenido pero generando menos tráfico desde tu servidor. 

#### Soporta mejor el tráfico

Cuando un sitio web soporta mucho tráfico, emplear un CMS requiere de mucha 
optimización y generalmente de mucha maquina o complejas instalaciones. Y la 
base principal siempre es un sistema de caché que sirva contenido lo más 
estático posible. Se cachea todo lo que se puede, y si es en memoria mejor. Las 
BDD son un problema aparte, desde soluciones NoSQL a clusters o BDD distribuidas. 
Con contenido estático no te tienes que preocupar de optimizar los accesos a la 
BDD, solo de tener un buen servidor web y si quieres, cachear en memoria o 
ampliar máquina. Pero poco más.


#### Seguridad

Olvídate de problemas de seguridad, los únicos agujeros de seguridad de un sitio 
con contenido estático están del lado del servidor web, de todo lo demás, te 
olvidas. Establece bien los permisos en el sistema de ficheros y punto. El único 
contenido dinámico del sitio (javascript) ni siquiera es algo que deba 
preocuparte, es algo externo que le concierne a **Disqus** o al sistema de 
analíticas web que elijas (Google Analytics o Piwik).

#### Olvidarse de gestionar un CMS. Mantenimiento mucho más sencillo (nulo)

Instalar el CMS, crear la BDD, encontrar, instalar y probar los plugins que 
necesitas, actualizaciones, actualizaciones de seguridad, personalizaciones, 
temas... Todo lo que rodea a cualquier CMS. Y ya no digamos si hablamos de un 
CMS potente y complejo como Drupal, con cientos de posibilidades. Y sin olvidar 
toda la basura que se va acumulando en las BDD tras varias actualizaciones y 
múltiples pruebas de plugins, con Pelican siempre tienes un sistema limpio. 
Todo eso lo olvidas con Pelican, lo instalas, personalizas y automatizas una 
sola vez, luego te olvidas de todo lo que no sea escribir (si quieres, nada te 
impide seguir cambiándolo y mejorándolo). Emplea tú tiempo en crear contenido.

#### Backups más sencillos

Con un CMS deberías hacer Backups del servidor web tanto del sistema de ficheros 
como de la BDD. Y sería aconsejable tener un servidor web local montado para 
probar los cambios que vayas a hacer en el CMS sin miedo a romper nada. Con 
Pelican ni siquiera necesitas hacer Backups del servidor ni del contenido web. 
Todo lo que necesitas para generarlo ya está en tu ordenador en esos ficheros de 
texto. Incluso si empleas un tema propio, también está en tu equipo. Así que las 
copias de seguridad de tu sitio web no son distintas a las que 
regularmente ya haces de tu ordenador personal.


*[deberías hacer Backups]: No hacerlas es una decisión nefasta
*[regularmente ya haces]: No me digas que aún no las haces, ¿estas de broma?

#### Hosting en cualquier sitio

Solo tienes que alojar contenido estático, no necesitas BDD ni soporte para 
ningún lenguaje o librería en particular. Puedes hasta utilizar recursos 
gratuitos como las páginas de [GitHub][githb] o [BitBucket][bbckt] o un sistema 
de ficheros en la nube económico como [Amazon S3][AS3] (o 
[Amazon CloudFront][ACF]). Solo necesitas eso, servir ficheros, nada más. Hasta 
el hosting más económico te sirve. 

  [githb]: https://github.com/
  [bbckt]: http://bitbucket.org/
  [AS3]: http://aws.amazon.com/es/s3/
  [ACF]: http://aws.amazon.com/es/cloudfront/

#### Emplear un CVS para gestionarlo

Poder emplear Git o Mercurial o cualquier otro CVS para gestionar los cambios 
del blog no tiene precio. Ningún sistema de revisiones de CMS es tan potente. 
Además tienes la posibilidad de crear un *hook* para que al enviar un commit 
después de crear un articulo (o realizar un cambio) se suba el contenido 
automáticamente al servidor. Con esto realizar cualquier cambio o revertir un 
error es algo trivial. Además te permite subir una copia a un sitio como GitHub 
o BitBucket y tenerlo siempre disponible en cualquier sitio con conexión a la 
red. Como maravillosa opción, esto permite que el contenido de un blog, incluso 
de un mismo articulo, sea editado por más de una persona de manera bastante más 
sencilla, potente y menos propensa a errores que con un CMS. 
 

*[CVS]: Control Version System (en español, "Sistema de Control de Versiones")


#### Crear los articulos off-line

Eso te permite ir creando los artículos al ritmo que te de la gana, cuando 
quieras y en cualquier sitio con un portátil. No necesitas estar conectado a la 
red. Esto también puede hacerse con un CMS, pero suele ser más complejo 
(exceptuando emplear cortar y pegar) e inseguro (si se habilita el envío remoto 
de artículos). Yo lo había logrado en Drupal empleando markdown, pero seguía 
necesitando un segundo paso on-line para personalizar las etiquetas. 

#### Edición de artículos más cómoda

Puede parecer que un CMS con su editor WYSIWYG es más cómodo, pero todo lo 
contrario. Ya lo comentaba en el [artículo sobre markdown][3]. Pero es que 
además me proporciona una mejor experiencia de edición y más potente. Explico 
como redacto yo los artículos para que se entienda mejor. Divido la pantalla en 
dos mitades, a la izquierda el editor de textos y a la derecha el navegador. 
Como editor de textos empleo Gedit, que tiene resaltado de texto para markdown y 
un corrector ortográfico (por esto no uso vim para esto) bastante mejor que el 
de Firefox (que solo examina el texto hasta cierto número de casos dudosos). 
Además Pelican tiene una maravillosa opción, `autoreload` que lo hace correr en 
segundo plano y cuando detecta un cambio en uno de los ficheros, vuelve a generar 
el contenido. Entonces en gedit le digo que autoguarde el contenido cada 3 
minutos (o a voluntad, manualmente) y cuando Pelican lo detecta, automáticamente 
regenera los ficheros HTML. Como navegador empleo Firefox y tengo, abierto en 
una pestaña, el fichero `index.html` que genera Pelican y empleando la extensión 
[Auto Reload][14] el contenido de la página (en local) se actualiza 
automáticamente al detectar un cambio en el fichero. Es decir, como en la 
primera página se puede ver el contenido completo del último articulo, lo que 
estoy viendo es una previsualización automática del contenido en la página cada 
3 minutos. Y todo esto en off-line, sin estar conectado a internet. Esto si es 
un verdadero editor WYSIWYG, y no los otros. Además, que demonios, los 
navegadores no se diseñaron para crear texto, cualquier editor de texto es más 
potente.

 [14]: https://addons.mozilla.org/es-ES/firefox/addon/auto-reload/?src=api

#### Control del Spam

El Spam, esa lacra que azota toda la web. En Pelican, ese problema, lo tiene que 
gestionar Disqus, no tú. Tú solo tienes que gestionar el poco que se le escape. 
Pero el buscar un plugin, configurarlo y que funcione bien, es algo de lo que no 
tienes que preocuparte. En Drupal tenía este asunto solucionado, pero fue cosa 
de probar varios plugins, hasta que al final [di con uno que me lo solucionaba de
verdad](http://joedicastro.com/combatir-el-spam-en-drupal.html). 

#### Recursos de CPU y RAM

El contenido dinámico consume mucha más memoria RAM y CPU en el servidor que 
servir contenido estático. Al fin y al cabo, en el caso del contenido estático, 
es poco más complejo que servir ficheros. Si tienes que compartir el servidor 
con más proyectos, agradecerás no tener que emplear un CMS para servir el blog.

#### Resaltado de Sintaxis incorporada con Pygments

Mientras en la mayoría de CMS necesitas un plugin para habilitar el resaltado de 
sintaxis para código fuente, en Pelican esto viene por defecto empleando el 
excelente [Pygments](http://pygments.org/)

#### Cumplimiento de Estándares Web

Con Pelican es relativamente sencillo configurar el tema para que cumpla los 
estándares web y genere contenido valido. Y una vez que lo haces, es para 
siempre, a no ser que modifiques algo en el tema, todo el contenido que generes 
cumplirá con los estándares (a no ser que incluyas HTML dentro que no lo sea). 
De este modo, este sitio valida HTML5, CSS3 y genera feeds RSS y Atom validos. 
Conseguir esto con un CMS y empleando editores WYSIWYG es bastante más complejo
y doloroso. Aunque yo lo había conseguido con Drupal y markdown, tuve que 
modificar un tema casi por completo, casi como crearlo desde cero. 



## Inconvenientes de Pelican vs CMS

#### Comentarios sin resaltado de sintaxis

Algo que me permitía Drupal y no me permite Disqus (por ahora) era emplear 
markdown en los comentarios y resaltado de sintaxis para el código fuente. Es el 
mayor inconveniente que he encontrado hasta ahora. Pero bueno, tampoco es algo 
imprescindible y esperemos que Disqus lo soporte en un futuro.

#### Sitemap

Tampoco Pelican genera sitemaps en xml para los buscadores. Aunque tampoco es 
algo imprescindible y Drupal tampoco lo soporta por defecto, si no a través de 
un módulo. El autor lo tiene como tarea pendiente, y si tarda mucho, a lo mejor 
me animo y lo creo yo mismo.

#### Personalización más sencilla para non geeks

Esta es la parte que menos me afecta, pero es el gran inconveniente para la gran 
mayoría sin conocimientos avanzados. Aunque Pelican no es difícil de instalar y 
configurar, si queremos personalizarlo bastante, la cosa cambia. Los CMS son 
mucho más sencillos en ese sentido, pero el coste a pagar por otro lado no me 
compensa. 

#### No tiene búsqueda incorporada

Es otro pequeño inconveniente que puede suplirse empleando la de Google AdSense 
en el sitio, por ejemplo. Personalmente no me importa demasiado, teniendo 
disponibles en el sitio recursos como el archivo de todos los artículos 
publicados o la nube de etiquetas.


#### No puedes personalizar el contenido dinámicamente

Con un CMS puedes hacer cosas como mostrar un contenido o un tema distinto según 
el perfil del usuario, o según la carga del servidor, etc. Con contenido 
estático lógicamente no puedes hacer esto. A mi me da igual, no lo necesito, es 
solo un blog.

<br />

Llevo varios años empleando Drupal en varios sitios y me sigue pareciendo un CMS 
excelente y una buenísima opción para generar contenido dinámico para no 
desarrollladores (de otro modo prefiero un framework como Django). Pero 
actualmente, para crear blogs, si se tienen conocimientos suficientes, emplear 
un CMS me parece una decisión poco acertada, es matar moscas a cañonazos. Hoy en 
día hay soluciones como Pelican y las mencionadas arriba (y otras alternativas 
en otros lenguajes) que te permiten crear blogs con facilidad, centrándote 
únicamente en crear los artículos y automatizar todo lo demás. ¿Acaso esa no es 
la razón principal del grandisimo éxito de [twitter][twtr] o [tumblr][tmblr]? 
La inmediatez de los resultados y la delegación de la gestión a terceros, tú 
solo escribes. Pelican te permite lo mismo, solo requiere la personalización 
inicial y listo, con la ventaja añadida de que puedes personalizarlo a tu gusto 
y hasta donde te dé la gana o seas capaz.

 [twtr]: http://twitter.com/
 [tmblr]: http://www.tumblr.com/












