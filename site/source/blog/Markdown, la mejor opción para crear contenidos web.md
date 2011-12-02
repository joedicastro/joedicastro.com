title: Markdown, la mejor opción para crear contenidos web
date: 2011-04-02 20:29
tags: markdown, wysiwyg, textile, editores, marcado, html, xhtml

Normalmente cuando se crea contenido en un blog o CMS, como Wordpress, Blogger, 
Drupal, Joomla, Plone, Typo, etc, se hace a través de un editor visual (WYSIWYG). 
Algunos editores de este tipo son [TinyMCE][0], [CKeditor][1], [NicEdit][2], 
[WYMEditor][3], [markItUP!][4], [openWYSIWYG][5], etc. 

  [0]: http://tinymce.moxiecode.com/
  [1]: http://ckeditor.com/
  [2]: http://nicedit.com/
  [3]: http://www.wymeditor.org/
  [4]: http://markitup.jaysalvat.com/home/
  [5]: http://www.openwebware.com/

*[WYSIWYG]: What You See Is What You Get (en inglés, "lo que ves es lo que obtienes")

Yo mismo he empleado varios de ellos durante años, en varias plataformas como 
Blogger, Wordpress, Joomla, Drupal, etc. Y si, hay que reconocerlo, te hacen la 
vida muy fácil, sobre todo para aquellos que no quieran preocuparse más que de 
añadir contenido en su página. E incluso usuarios más avanzados como 
administradores o diseñadores web, lo suelen emplear por comodidad frente a un 
área de texto plano. Y si, es cómodo, muy cómodo, a corto plazo. A largo plazo... 
a largo plazo es cuando empiezas a verle los peros y los problemas, que los 
tienen, y bastantes. Veamos cuales son esos problemas y la alternativa, que para 
mi personalmente, es la solución. 

### Los problemas de los editores WYSIWYG

Los editores visuales están pensados para que de una forma muy fácil, se pueda 
editar el contenido de forma visualmente atractiva, sin tenerse que andar 
preocupando del HTML que se genera a partir de él, esto es, no es necesario 
conocer nada de HTML para usar un editor WYSIWYG. Puedes añadir negritas, 
cursivas, alinear el texto, cambiar el tamaño, el color, crear tablas, etc, sin 
conocimiento alguno de HTML o CSS. Se supone que el editor genera HTML valido 
correctamente por ti. Y aquí es donde empiezan los problemas:

 * Los editores visuales generalmente crean el formato con **CSS embebido dentro 
 del HTMl**, es decir mezclando el contenido y el estilo de la página. Algunos 
 incluso te permiten incluir tus propias hojas de estilo para que el contenido 
 se ajuste al estilo actual de tu web. 

    ¿Pero que ocurre cuando al cabo de un tiempo, con decenas o más de artículos 
    generados quieres cambiar el estilo de tú página? Pues dependiendo de como 
    haya realizado el trabajo tu editor WYSIWYG, te puedes encontrar con el 
    desagradable problema de que todo queda desencajado o no se ajusta al estilo 
    actual. Yo me he tenido que enfrentar con este problema en el pasado al 
    actualizar una versión de Drupal y cambiar completamente el tema, y no fue 
    nada cómodo de solucionar, o al importar contenido de un CMS a otro. 

 * Los editores visuales **se crearon inicialmente para impresión en papel**, no 
 para HTML. Y HTML se emplea en multitud de dispositivos (desde móviles hasta 
 ereaders) y bien empleado proporciona una flexibilidad que se rompe al mezclar 
 la estructura del documento (HTML) con el estilo del mismo (CSS) en el mismo 
 archivo. Así que a la hora de crear versiones para dispositivos móviles, con 
 todas esas etiquetas CSS embebidas, puede ser un verdadero quebradero de cabeza. 

 * Se supone que **tienen que generar HTML válido**, pero durante mucho tiempo 
   **esto no ha sido siempre así**, sobre todo si el editor no está bien 
   configurado o tiene algún plug-in que no respeta este tema. Además, generan 
   HTML valido ahora, ¿que pasa en el futuro? Es decir, si quieres pasar 
   contenido antiguo para por ejemplo pasar de HTML 2.0 a HTML 4.0 o incluso 5 
   y eliminar etiquetas obsoletas y generar HTML que cumpla con el estándar, 
   prepárate, porque te espera una ardua tarea. Por no decir que muchos de estos 
   editores tienen errores en su propio código javascript, lo que lleva a 
   frecuentes actualizaciones de los mismos.

 * Pueden **generar cantidades absurdas de HTML**, sobre todo si no están 
 correctamente configurados. Algunos editores (a veces con la configuración por 
 defecto hacen esto, y tienes que ser tú quien lo ajuste para que no ocurra) 
 crean toneladas de `<div>`,`<p>` y `<span>` sin sentido y totalmente superfluos. 
 Cuando no emplean tablas para formatear algunas presentaciones complejas. Y ni 
 que decir tiene de aquellos editores visuales que te dejan pegar contenido 
 desde un procesador de textos como Word, el HTML generado en estos casos, 
 bueno, hay que verlo para creerlo, un absoluto despropósito. 

 * Es incluso factible que un usuario inexperto pueda **romper el diseño de una 
 página a través de un editor WYSIWYG**, creando párrafos o `<div>` de forma 
 inadecuada. Incluso al reescribir un texto es posible que se mezclen  estilos 
 CSS embebidos antiguos con nuevos, generando unos embrollos inmensos a nivel de 
 HTML. Y ya no digo nada de los que rompen el estilo visual de un tema abusando 
 de colores en las fuentes, tamaños, etc

 * El **contenido** que se guarda **en la base de datos** esta **mezclado con** 
 las etiquetas **HTML y CSS**, todo junto, vamos que no se parece en nada a lo 
 que has introducido en tu editor. Todo esto en principio carece de importancia, 
 pero puede suponer hasta el 20% del tamaño de las páginas de tu sitio, espacio 
 absurdamente desperdiciado en tu BDD. De hecho el contenido XHTML se genera por 
 lo normal cada vez que se visualiza la página de forma dinámica. Si te preocupa 
 el rendimiento, tranquilo, los sistemas de cache están ahí para echarte una 
 mano y que te dejes de preocupar por eso. 

 * **Distraen la atención**, el problema de absolutamente todos los editores 
 visuales, incluidos procesadores de texto, el centrarse en el formato y no en 
 el contenido. Una gran mayoría de usuarios desperdicia un tiempo notable 
 preocupándose por más el aspecto visual del documento, que por el contenido del 
 mismo. Que si esto en negrita, que si mejor con esta fuente, que si mejor con 
 la otra... Se desvía la atención de lo importante, el contenido. Mal amigo de 
 la productividad, se tarda bastante más en general, por esta razón, en generar 
 el mismo contenido en un editor WYSIWYG.

 * **Son bastante poco flexibles**, si quieres introducir tu propio HTMl en el 
 contenido (e.g. para tener un control más fino sobre las tablas, yo lo hago en 
 este articulo) puede que te encuentres que lo genera como lo tiene 
 preestablecido, eliminado la estructura que tu quieras darle. Y embeber 
 contenido multimedia o scripts también es frecuentemente un problema, siendo 
 hasta habitual que existan plugins para estos editores para insertar contenidos 
 de sitios como YouTube.

 * Todos los editores WYSIWYG **aumentan el peso por página y disminuyen la 
 velocidad de carga**, al necesitar pesado código javascipt que necesita tanto 
 ser descargado como ejecutado por tu navegador. Ya de por si los CMS suelen 
 emplear bastante código javascript, como para encima añadirle un editor visual. 
 Además realizan bastantes llamadas HTTP, ralentizando aún más la velocidad de 
 carga. Ejemplo: tienes un articulo de 80 lineas de texto cuyo contenido XHTML 
 puede pesar tranquilamente de 10 á 20 veces menos que el javascript del editor, 
 ¿no es un poco ridículo?. Aunque muy pocos editores web se preocupan de esto, 
 la verdad, es que hay que pensar que no todo el mundo disfruta de buenas 
 conexiones a la red. 

 * Por último y no menos importante, **no cuidan la accesibilidad**. El HTML 
 valido que cumpla con los estándares, es esencial para crear páginas con una 
 buena accesibilidad, pensando en aquellos que no lo tienen tan fácil para 
 navegar por nuestros sitios web. Deberían tenerse al menos en cuenta un mínimo 
 de puntos sobre este tema al crear contenidos en la web.

En conclusión, que los editores WYSIWYG pueden no dar problemas hasta que tus 
necesidades cambian, entonces pueden darte más de un quebradero de cabeza. 

<br />

### Texto plano y Markdown {#mark}

¿Cual sería entonces la solución para esquivar estos problemas? Texto plano, 
nada más, que se transforme automáticamente en HTML valido respetando el formato 
que nosotros queramos darle. Esto existe, y es posible gracias a los lenguajes 
de marcado ligero, entre los que se encuentra [Markdown][mkdwn]. Nada mejor que 
empezar demostrándolo con un ejemplo:

   [mkdwn]: http://daringfireball.net/projects/markdown/

<br />

<div>
<table>
  <thead><tr><th style="width: 50%;">Markdown</th><th>Resultado</th></tr></thead>
<tbody><tr>
    <td><pre class="no_mrkdwn">
<p>Documento de ejemplo
====================</p><p>Lorem ipsum [dolor sit amet](#mark), consectetur adipiscing elit. Curabitur eget ante nunc. Pellentesque a tortor ipsum, id rhoncus orci. Quisque leo sapien, rutrum id convallis id, rutrum in ligula. Vestibulum **semper adipiscing leo** et blandit.</p><p>Sed nibh quam, hendrerit _sit amet aliquam_ vel, pulvinar molestie augue.</p><p>&gt; Integer cursus, nunc eu ultrices pellentesque, eros leo malesuada turpis, vel convallis neque dolor a nunc. Sed lacus risus, condimentum vitae posuere quis, ultrices pharetra nunc.</p><p>Lista numerada (ordenada)</p><p>1. Este es el primer elemento
2. Este es el segundo elemento
   * Una lista de puntos anidada
   * Se llama también desordenada
     * Tercer nivel de anidamiento
3. Este es el tercer elemento</p><p>![avatar](pictures/avatar.png)</p><p>### Cabecera ###</p><p>- - -</p><p>Morbi erat augue, feugiat eu pellentesque eget, hendrerit quis lectus. Fusce dignissim pretium nibh sed dignissim. Pellentesque lobortis ante eu dui fermentum vitae blandit risus aliquet.</p><p>
|   | solo texto | HTML Limpio  |
| -------------- | -- | ------- |
| Markdown       | Si | Si      |
| Editor WYSISWG | X  | A veces |</p><p>
&nbsp;&nbsp;&nbsp;&nbsp;:::python
&nbsp;&nbsp;&nbsp;&nbsp;import lifetime
&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;for each_day in lifetime.days():
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;carpe_diem()</p><p>Suspendisse posuere velit et velit vehicula at scelerisque orci suscipit. Nulla facilisis lorem eu sem viverra varius nec ut felis.</p><p>Esto es un texto con nota al pie [^prima] y esta es otra nota [^secunda]</p><p>
 *[vehicula]: automobila
[^prima]: Esto es una nota al pie.
[^secunda]: Esto es la segunda nota.</p></pre>
     </td>
     <td>
<h1>Documento de ejemplo</h1>

<p>Lorem ipsum <a href="#mark">dolor sit amet</a>, consectetur adipiscing elit. Curabitur eget ante nunc. Pellentesque a tortor ipsum, id rhoncus orci. Quisque leo sapien, rutrum id convallis id, rutrum in ligula. Vestibulum <strong>semper adipiscing leo</strong> et blandit.</p>

<p>Sed nibh quam, hendrerit <em>sit amet aliquam</em> vel, pulvinar molestie augue.</p>

<blockquote>
  <p>Integer cursus, nunc eu ultrices pellentesque, eros leo malesuada turpis, vel convallis neque dolor a nunc. Sed lacus risus, condimentum vitae posuere quis, ultrices pharetra nunc.</p>
</blockquote>

<p>Lista numerada (ordenada)</p>

<ol><li>Este es el primer elemento</li>
<li>Este es el segundo elemento

<ul><li>Una lista de puntos anidada</li>

<li>Se llama también desordenada

<ul><li>Tercer nivel de anidamiento</li>
</ul></li>
</ul></li>
<li>Este es el tercer elemento</li>
</ol><p><img src="pictures/avatar.png" alt="avatar" /></p>

<h3>Cabecera</h3>

<hr /><p>Morbi erat augue, feugiat eu pellentesque eget, hendrerit quis lectus. Fusce dignissim pretium nibh sed dignissim. Pellentesque lobortis ante eu dui fermentum vitae blandit risus aliquet.</p>

<table><thead><tr><th></th>
  <th>solo texto</th>

  <th>HTML Limpio</th>
</tr></thead><tbody><tr><td>Markdown</td>
  <td>Si</td>
  <td>Si</td>
</tr><tr><td>Editor WYSISWG</td>
  <td>X</td>
  <td>A veces</td>

</tr></tbody></table>

<div class="codehilite"><pre><span class="kn">import</span> <span class="nn">lifetime</span>

<span class="k">for</span> <span class="n">each_day</span> <span class="ow">in</span> <span class="n">lifetime</span><span class="o">.</span><span class="n">days</span><span class="p">():</span>
<span class="n">    carpe_diem</span><span class="p">()</span></pre></div>
<p>Suspendisse posuere velit et velit <abbr title="automobila">vehicula</abbr> at scelerisque orci suscipit. Nulla facilisis lorem eu sem viverra varius nec ut felis.</p>

<p>Esto es un texto con nota al pie <sup id="fnref:prima"><a href="#fn:prima" rel="footnote">1</a></sup> y esta es otra nota <sup id="fnref:secunda"><a href="#fn:secunda" rel="footnote">2</a></sup></p>

<div class="footnotes">
<hr /><ol><li id="fn:prima">
<p>Esto es una nota al pie. <a href="#fnref:prima" rev="footnote">↩</a></p>
</li>

<li id="fn:secunda">
<p>Esto es la segunda nota. <a href="#fnref:secunda" rev="footnote">↩</a></p>
</li>
</ol>
    </td>
  </tr>
</tbody></table>
</div>

Es así de sencillo, el texto plano que se escribe en la columna de la izquierda 
genera el HTML que se puede ver representado en la derecha. Es además HTML 
valido, sin CSS embebido (exceptuando el código con resaltado de sintaxis, pero 
esto es necesario y tampoco es generado por **Markdown** si no por 
[GeSHi][geshi] anteriormente y ahora por [Pygments][pygments]) y empleando el 
mínimo necesario, siendo lo más limpio posible. 
Pero el contenido que se guarda en la base de datos y el que tú editas es el de 
la izquierda. Este contenido generará HTML valido hoy y mañana, es totalmente 
independiente del estilo que emplees en tu página y puedes migrarlo de un CMS a 
otro sin problema alguno. Todo son ventajas, el único inconveniente es que tienes 
que aprender a usar **Markdown**, algo que es sumamente sencillo, a la par que 
incrementa la legibilidad del texto plano. 

La legibilidad del texto es uno de los pilares fundamentales de **Markdown**, 
tal y como el mismo autor, [John Gruber][jgrub], lo cuenta[^1]:

> El objetivo fundamental de diseño para la sintaxis de Markdown es hacerlo tan 
legible como sea posible. La idea es que un documento formateado con Markdown 
debería poder ser publicado tal y como está, como texto plano, sin que parezca 
que ha sido marcado con etiquetas o instrucciones de formateado. Mientras que la 
sintaxis de Markdown ha sido influenciada por muchos filtros texto-a-HTML 
existentes, la principal fuente de inspiración es el formato de los correos 
electronicos en texto plano. 


  [jgrub]: http://en.wikipedia.org/wiki/John_Gruber
  [^1]: The overriding design goal for Markdown’s formatting syntax is to make 
    it as readable as possible. The idea is that a Markdown-formatted document 
    should be publishable as-is, as plain text, without looking like it’s been 
    marked up with tags or formatting instructions. While Markdown’s syntax has 
    been influenced by several existing text-to-HTML filters, the single biggest 
    source of inspiration for Markdown’s syntax is the format of plain text 
    email. [fuente](http://daringfireball.net/projects/markdown/)

No voy ahora, en este articulo, a enseñarte a emplear **Markdown**, pero tienes 
una guía de prácticamente todas las posibilidades que te brinda en 
[Markdown & Pygments Lexers Cheat Sheet](/pages/markdown.html). 
Además, si somos así de vagos, podemos emplear también algunos editores visuales 
que generan y emplean markdown, como [markItUP!][4] o el conocido [WMD][wmd] que 
empleamos en [python majibu](http://python.majibu.org). Aunque ambos editores 
solo soportan Markdown estándar, cuando en este sitio también soporto las 
capacidades adicionales de [Markdown Extra][xtra].

   [geshi]: http://qbnz.com/highlighter/
   [wmd]: http://code.google.com/p/wmd/
   [xtra]: http://michelf.com/projects/php-markdown/extra/
   [pygments]: http://pygments.org/

Todo el contenido de este sitio (exceptuando el automático, como las búsquedas, 
etiquetas, acerca de, ...) está generado empleando **Markdown** y todo está en 
HTML 5 valido. Un ejemplo del HTML que genera Markdown sería el siguiente:

<table>
 <thead>
  <tr>
   <th style="width: 50%;">Markdown</th><th>HTML</th>
  </tr>
 <tbody>
  <tr>
   <td>
    <pre class="no_mrkdwn">
Documento de ejemplo
====================
 
Lorem ipsum [dolor sit amet](#mark), consectetur adipiscing elit. Curabitur eget ante nunc. Pellentesque a tortor ipsum, id rhoncus orci. Quisque leo sapien, rutrum id convallis id, rutrum in ligula. Vestibulum **semper adipiscing leo** et blandit.
 
Sed nibh quam, hendrerit _sit amet aliquam_ vel, pulvinar molestie augue.
    </pre>
   </td>
   <td>
    <pre class="no_mrkdwn">
&lt;h1&gt;Documento de ejemplo&lt;/h1&gt;
 
&lt;p&gt;Lorem ipsum &lt;a href="#mark"&gt;dolor sit amet&lt;/a&gt;, consectetur adipiscing elit. Curabitur eget ante nunc. Pellentesque a tortor ipsum, id rhoncus orci. Quisque leo sapien, rutrum id convallis id, rutrum in ligula. Vestibulum &lt;strong&gt;semper adipiscing leo&lt;/strong&gt; et blandit.&lt;/p&gt; 
 
&lt;p&gt;Sed nibh quam, hendrerit &lt;em&gt;sit amet aliquam&lt;/em&gt; vel, pulvinar molestie augue.&lt;/p&gt; 
     </pre>
   </td>
  </tr>
 </tbody>
</table>


Como se puede ver es el HTMl justo, limpio y cumpliendo estándares, ni más ni 
menos. Este es un ejemplo muy sencillo, y posiblemente cualquier editor WYSIWYG 
sea capaz de dar el mismo resultado, el problema aparece con documentos más 
complejos, con sucesivas re-ediciones del texto y con editores mal configurados. 
Eso si, lo que se almacena en la BDD con **Markdown** es texto plano, con los 
otros editores, el texto, las etiquetas HTML y CSS embebido. 

### ¿Porque Markdown y no otros?

Evidentemente **Markdown** no es el único [lenguaje de marcado ligero][lml], 
existen otros también conocidos y extendidos como [Textile][6], [BBCode][7], 
[reStructuredText][8], [Texy!][9], [Txt2tags][10] o los empleados en los Wikis 
como [Creole][11] o el de [MediaWiki][12].

En primer lugar **Markdown** es uno de los que más características soporta, uno 
de los que más salidas puede generar (no solo HTML, también LaTeX, RTF, PDF, 
EPUB, ...) y además es probablemente el más extendido y soportado de todos 
(exceptuando BBCode y los de los Wikis, empleados en sus nichos particulares). 
Pero también es uno de los más fáciles de emplear (saliendo del formato básico 
como negritas, etc) y que produce un texto plano más vistoso y legible. 

   [lml]: http://es.wikipedia.org/wiki/Lenguajes_de_marcas_ligeros
   [6]: http://textile.thresholdstate.com/
   [7]: http://www.bbcode.org/
   [8]: http://docutils.sourceforge.net/rst.html
   [9]: http://texy.info/en/
   [10]: http://txt2tags.org/
   [11]: http://www.wikicreole.org/
   [12]: http://www.mediawiki.org/wiki/Help:Formatting

### Comparativa

Como no, lo mejor, es ver una comparativa co un ejemplo de el mismo documento y 
el texto empleado por cada uno de los lenguajes para generarlo. Para ello he 
creado un articulo aparte para mostrarla.

[Comparativa](/comparativa-de-lenguajes-de-marcado-ligero.html)


### ¿Quién emplea Markdown?

Una de las razones para emplear **Markdown** es porque es uno de los más 
extendidos, sobre todo en el mundo de la programación. Por ejemplo, 
[Stack Overflow][13] y todos los sitios de [Stack Exchange][14] emplean una 
variante de Markdown para la entrada de texto. Repositorios de código como 
[GitHub][15] y [Bitbucket][16] también lo emplean para ciertas funciones. 
También lo emplea el sistema de seguimiento de incidencias [LightHouse][17]. 

  [13]: http://stackoverflow.com/
  [14]: http://stackexchange.com/
  [15]: https://github.com/
  [16]: https://bitbucket.org/
  [17]: http://lighthouseapp.com/

Fuera del ámbito de la programación, sitios tan conocidos como [Reddit][18] lo 
emplean. Plataformas para la educación online como [Moodle][19] o 
[Podmedics][20] también hacen uso de él. Un Wiki como [Instiki][21] permite 
emplear Markdown. Plataformas de blogs y contenidos como [Posterous][22], 
[Tumblr][23] y [Squarespace][24] lo ofrecen como opción. Y seguro que me estoy 
dejando en el tintero muchos más lugares donde es empleado habitualmente. 

  [18]: http://www.reddit.com/
  [19]: http://moodle.org/
  [20]: http://podmedics.heroku.com/
  [21]: http://www.instiki.org/
  [22]: https://posterous.com/
  [23]: http://www.tumblr.com/
  [24]: http://www.squarespace.com/

Hay que tener en cuenta de que aquí no he hablado de software CMS que lo soporta, 
eso lo contemplo en el próximo punto, si no más bien de organizaciones/compañías.

### Excusas para no emplearlo

La primera que dice todo el mundo, es un incordio usarlo y aprenderlo, la 
pregunta es: ¿Has intentado emplearlo? Créeme se aprende en nada, sobre la 
marcha, y una vez que te acostumbras a él, lo elegirás frente a los editores 
WYSIWYG, casi con toda seguridad. Una vez aprendido no tienes qune separar los 
dedos de tu teclado, no necesitas para nada el ratón para crear tu contenido. 
Ganarás mucho tiempo para ti mismo y lo agredeceras, créeme.

La segunda, no puedo usarlo en mi CMS o blog. ¿Seguro? A continuación te detallo 
las opciones que conozco para publicar contenidos empleando **Markdown**.

#### CMS y Blogs:

* Por defecto, como opción o nativamente:
    * [Nesta](http://nestacms.com/)
    * [Kohanut](http://kohanut.com/)
    * [MovableType](http://www.movabletype.org/)
    * [Typo](http://fdv.github.com/typo/)
* Con añadidos:
    * [Drupal](http://drupal.org/) A través de un modulo, [Markdown Filter](http://drupal.org/project/markdown)
    * [Wordpress](http://wordpress.org/) Hay varios plugins disponibles para emplearlo.
    * [Django](http://djangoproject.com/) Hay varias formas de soportarlo.
    * [Plone](http://plone.org) Se puede habilitar a través de un modulo.
    * [Blogger](http://blogger.com) A través de algunos proyectos externos, [Blogger-markdown-editor](http://code.google.com/p/blogger-markdown-editor/)
    * [ExpressionEngine](http://expressionengine.com/) A través de un plugin.
    * [Joomla](http://www.joomla.org/) A través de una extensión, [jMarkdown](http://extensions.joomla.org/extensions/edition/code-display/8391)

### Generadores de sitios con contenido estático (HTML):

* [Pelican](https://github.com/ametaireau/pelican/)
* [hyde](http://ringce.com/hyde)
* [Blogofile](http://www.blogofile.com/)
* [Poole](https://bitbucket.org/obensonne/poole/src)
* [Growl](https://github.com/xfire/growl/tree)
* [Markdoc](http://markdoc.org/)
* [Webgen](http://webgen.rubyforge.org/)
* [nanoc](http://nanoc.stoneship.org/)
* [jekyll](http://jekyllrb.com/)
* [Hakyll](http://jaspervdj.be/hakyll/)
* [Webby](http://webby.rubyforge.org/)
* [toto](http://cloudhead.io/toto)
* [Rote](http://rote.rubyforge.org/)

### Plataforma de Blogs con contenido estático (HTML):

* [Calepin.co](http://calepin.co/) es un **Pelican** hospedado, que lee ficheros 
markdown desde **DropBox**
  
### Wiki:

* Por defecto, como opción o nativamente:
    * [Instiki](http://instiki.org)
    * [ikiwiki](http://ikiwiki.info/)
    * [sputnik](http://sputnik.freewisdom.org/)
    * [nanoki](http://alt.textdrive.com/nanoki/)
    * [gitit](https://github.com/jgm/gitit)
* Con añadidos: 
    * [MoinMoin](http://moinmo.in/) con una [extensión](http://moinmo.in/ParserMarket/Markdown)
    * [MediaWiki](http://www.mediawiki.org) con una [extensión](http://www.mediawiki.org/wiki/Extension:MarkdownSyntax)
    * [DokuWiki](http://www.dokuwiki.org/)
    * [Oddmuse](http://oddmuse.org/)
    * [PmWiki](http://www.pmwiki.org/)
     
### Foros:

* [phpBB](http://www.phpbb.com/) A través de un 
[MOD](http://www.phpbb.com/community/viewtopic.php?f=70&t=2093183)

### Conversor Markdown desde/a otros formatos:

* [Pandoc](http://johnmacfarlane.net/pandoc/try)

### Editores de Texto que lo soportan (marcado de sintaxis):

* [Vim](http://www.vim.org/) con [Vim-Markdown](https://github.com/plasticboy/vim-markdown)
* [Emacs](http://www.gnu.org/software/emacs/) con [markdown-mode](http://jblevins.org/projects/markdown-mode/)
* [Gedit](http://projects.gnome.org/gedit/) con [gedit-markdown](http://live.gnome.org/Gedit/MarkdownSupport)
* [Eclipse](http://www.eclipse.org/) con el experimental [markdown editor](http://www.winterwell.com/software/markdown-editor.php)
* [TextMate](http://macromates.com/)
* [SubEthaEdit](http://www.codingmonkeys.de/subethaedit/)
* [Ecto](http://ecto.kung-foo.tv/)
* [MarsEdit](http://www.red-sweater.com/marsedit/)
 
### Editor Markdown:

* [ReText](http://sourceforge.net/p/retext/home/)
* [Markdown Pad](http://markdownpad.com/)
* [Byword](http://bywordapp.com/)

### Editor Offline para blogs:

* [QTM](http://qtm.blogistan.co.uk/)

### Editores Online para probar Markdown:

* [Dingus](http://daringfireball.net/projects/markdown/dingus) por [John Gruber](http://daringfireball.net/)
* [Dingus PHP](http://michelf.com/projects/php-markdown/dingus/) por Michel Fortin
* [Markdown Extra + GeShi](http://anthonybush.com/markdown_extra_geshi/) por Anthony Bush
* [Dilinger](http://dillinger.io/) es una aplicación en HTML 5 por Joe McCann
* [Babelmark](http://babelmark.bobtfish.net/?markdown=*This+**is+a+test*.&normalize=on) para comparar las distintas implementaciones de Markdown
* [Markdown Editor](http://joncom.be/experiments/markdown-editor/edit/) por John Combe
* [Showdown](http://softwaremaniacs.org/playground/showdown-highlight/)
* [Markdownr](http://markdownr.com/)

Y si eres desarrollador, tienes disponibles distintas implementaciones de Markdown:

| Lenguaje | Implementaciones |
| :- | :-- |
| Python | [Python-markdown](http://www.freewisdom.org/projects/python-markdown/) |
| PHP | [PHP Markdown y PHP Markdown Extra](http://michelf.com/projects/php-markdown/) |
| Perl | [Original](http://daringfireball.net/projects/markdown/) y [MultiMarkdown](https://github.com/fletcher/MultiMarkdown) |
| Ruby | [BlueCloth](http://deveiate.org/projects/BlueCloth), [Maruku](https://github.com/nex3/maruku) y [Kramdown](http://kramdown.rubyforge.org/) |
| C# | [Markdown.NET](http://aspnetresources.com/blog/markdown_announced) |
| C | [Discount](http://www.pell.portland.or.us/~orc/Code/markdown/) y [Peg-Markdown](https://github.com/jgm/peg-markdown) |
| C++ | [Cpp-markdown](http://cpp-markdown.sourceforge.net/) |
| Java | [MarkdownJ](http://sourceforge.net/projects/markdownj/) |
| Javascript | [Showdown](https://github.com/coreyti/showdown) |
| Lua | [markdown.lua](http://www.frykholm.se/files/markdown.lua) |
| Haskell | [Pandoc](http://johnmacfarlane.net/pandoc/) |
| Common Lisp | [CL-Markdown](http://common-lisp.net/project/cl-markdown/) |
| Scala | [Knockoff](http://tristanhunt.com/projects/knockoff/) y [Actuarius](http://henkelmann.eu/projects/actuarius/) |

Entonces, habiendo tantas opciones, ¿por qué no lo pruebas?

Y si hay más excusas, pues la verdad, no las conozco, dímelas tú.
