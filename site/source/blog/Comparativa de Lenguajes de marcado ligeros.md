title: Comparativa de Lenguajes de marcado ligero
date: 2011-04-02 20:29
tags: markdown, Textile, BBCode, reStructuredText, Texy!, txt2tags, Creole, MediaWiki, marcado, HTML, XHTML


Esta es una comparativa de los lenguajes de marcado ligero más empleados de los 
disponibles actualmente. Dicha comparativa surge a partir de este articulo, 
[Markdown, la mejor opción para crear contenidos web][mrkdwn], donde defiendo la 
idoneidad de markdown para crear contenidos web.

  [mrkdwn]: http://joedicastro.com/markdown-la-mejor-opcion-para-crear-contenidos-web.html

En esta comparativa se verá como emplear cada uno de los lenguajes de marcado 
disponibles para crear un contenido web similar. Tomo como referencia a markdown, 
aunque no todos los lenguajes soportan todas o las mismas características que 
este.

## Documento de ejemplo realizado con Markdown

<div>
<table>
 <thead>
  <tr>
   <th style="width: 50%;">Markdown</th><th>Resultado</th>
  </tr>
 <tbody>
  <tr>
   <td>
    <pre class="no_mrkdwn">
Documento de ejemplo
====================
 
Lorem ipsum [dolor sit amet](#mark), consectetur adipiscing elit. Curabitur eget ante nunc. Pellentesque a tortor ipsum, id rhoncus orci. Quisque leo sapien, rutrum id convallis id, rutrum in ligula. Vestibulum **semper adipiscing leo** et blandit.
 
Sed nibh quam, hendrerit _sit amet aliquam_ vel, pulvinar molestie augue.
 
> Integer cursus, nunc eu ultrices pellentesque, eros leo malesuada turpis, vel convallis neque dolor a nunc. Sed lacus risus, condimentum vitae posuere quis, ultrices pharetra nunc.
 
Lenguajes de marcado ligero 

 * **Markdown**
 * Textile
 * reStructuredText
 * Texy!
 * Txt2tags
 * Marcado Wiki
   1. Creole
   2. MediaWiki

![avatar](pictures/no_wysiwyg.png)
 
### Cabecera H3 ###
 
- - -
 
Morbi erat augue, feugiat eu pellentesque eget, hendrerit quis lectus. Fusce dignissim pretium nibh sed dignissim. Pellentesque lobortis ante eu dui fermentum vitae blandit risus aliquet.
 
|   | solo texto | HTML Limpio  |
| -------------- | -- | ------- |
| Markdown       | Si | Si      |
| Editor WYSISWG | X  | A veces |

_Ejemplo de código_

&nbsp;&nbsp;&nbsp;&nbsp;import lifetime
&nbsp;&nbsp;&nbsp;&nbsp; 
&nbsp;&nbsp;&nbsp;&nbsp;for each_day in lifetime.days():
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;carpe_diem()
 
 
Suspendisse posuere velit et velit vehicula at scelerisque orci suscipit. Nulla facilisis lorem eu sem viverra varius nec ut felis.
 
Esto es un texto con nota al pie [^ejemplo] y esta es otra nota [^segunda]
 
*[vehicula]: automobila
[^ejemplo]: Esto es una nota al pie.
[^segunda]: Esto es la segunda nota.
    </pre>
   </td>
   <td>
<h1>Documento de ejemplo</h1> 
 
<p>Lorem ipsum <a href="#mark">dolor sit amet</a>, consectetur adipiscing elit. Curabitur eget ante nunc. Pellentesque a tortor ipsum, id rhoncus orci. Quisque leo sapien, rutrum id convallis id, rutrum in ligula. Vestibulum <strong>semper adipiscing leo</strong> et blandit.</p> 
 
<p>Sed nibh quam, hendrerit <em>sit amet aliquam</em> vel, pulvinar molestie augue.</p> 
 
<blockquote> 
  <p>Integer cursus, nunc eu ultrices pellentesque, eros leo malesuada turpis, vel convallis neque dolor a nunc. Sed lacus risus, condimentum vitae posuere quis, ultrices pharetra nunc.</p> 
</blockquote> 
 
<p>Lenguajes de marcado ligero</p> 
 
<ul> 
<li><strong>Markdown</strong></li> 
<li>Textile</li> 
<li>reStructuredText</li> 
<li>Texy!</li> 
<li>Txt2tags</li> 
<li>Marcado Wiki
 
<ol> 
<li>Creole</li> 
<li>MediaWiki</li> 
</ol></li> 
</ul> 
 
<p><img src="pictures/no_wysiwyg.png" alt="avatar" /></p> 
 
<h3>Cabecera H3</h3> 
 
<hr /> 
 
<p>Morbi erat augue, feugiat eu pellentesque eget, hendrerit quis lectus. Fusce dignissim pretium nibh sed dignissim. Pellentesque lobortis ante eu dui fermentum vitae blandit risus aliquet.</p> 
 
<table> 
<thead> 
<tr> 
  <th></th> 
  <th>solo texto</th> 
  <th>HTML Limpio</th> 
</tr> 
</thead> 
<tbody> 
<tr> 
  <td>Markdown</td> 
  <td>Si</td> 
  <td>Si</td> 
</tr> 
<tr> 
  <td>Editor WYSISWG</td> 
  <td>X</td> 
  <td>A veces</td> 
</tr> 
</tbody> 
</table> 
 
<p><em>Ejemplo de código</em></p> 
 
<pre class="txt" style="font-family:monospace;">import lifetime
&nbsp;
for each_day in lifetime.days():
    carpe_diem()</pre> 
 
<p>Suspendisse posuere velit et velit <abbr title="automobila">vehicula</abbr> at scelerisque orci suscipit. Nulla facilisis lorem eu sem viverra varius nec ut felis.</p> 
 
<p>Esto es un texto con nota al pie <sup id="fnref:ejemplo"><a href="#fn:ejemplo" rel="footnote">1</a></sup> y esta es otra nota <sup id="fnref:segunda"><a href="#fn:segunda" rel="footnote">2</a></sup></p> 
 
<div class="footnotes"> 
<hr /> 
<ol> 
 
<li id="fn:ejemplo"> 
<p>Esto es una nota al pie.&#160;<a href="#fnref:ejemplo" rev="footnote">&#8617;</a></p> 
</li> 
 
<li id="fn:segunda"> 
<p>Esto es la segunda nota.&#160;<a href="#fnref:segunda" rev="footnote">&#8617;</a></p> 
</li> 
 
</ol> 
</div> 
   </td>
  </tr>
 </tbody>
</table>
</div>

----

## Textile

Es una buena alternativa a Markdown y bastante extendido, aunque quizás menos 
que Markdown. Tiene algunas posibilidades que no tiene Markdown como emplear 
colores, poder alinear el texto o emplear superindice y subindice. También tiene 
carencias como el no poder dibujar líneas horizontales o el poder emplear 
acronimos solo con mayusculas y tener que declararlos en cada una de las partes 
del texto que aparezcan. Pero quiźas para mi la mayor desventaja es la menor 
legibilidad del texto, es menos evidente a un vistazo que markdown.

<table>
 <thead>
  <tr>
   <th style="width: 50%;">Textile</th><th>Resultado</th>
  </tr>
 <tbody>
  <tr>
   <td>
    <pre class="no_mrkdwn">
h1. Documento de ejemplo
 
Lorem ipsum "dolor sit amet":#mark, consectetur adipiscing elit. Curabitur eget ante nunc. Pellentesque a tortor ipsum, id rhoncus orci. Quisque leo sapien, rutrum id convallis id, rutrum in ligula. Vestibulum **semper adipiscing leo** et blandit.
 
Sed nibh quam, hendrerit _sit amet aliquam_ vel, pulvinar molestie augue.
 
bq. Integer cursus, nunc eu ultrices pellentesque, eros leo malesuada turpis, vel convallis neque dolor a nunc. Sed lacus risus, condimentum vitae posuere quis, ultrices pharetra nunc.
 
Lenguajes de marcado ligero 

* **Markdown**
* Textile
* reStructuredText
* Texy!
* Txt2tags
* Marcado Wiki
## Creole
## MediaWiki

!pictures/no_wysiwyg.png (avatar)!
 
h3. Cabecera H3

Morbi erat augue, feugiat eu pellentesque eget, hendrerit quis lectus. Fusce dignissim pretium nibh sed dignissim. Pellentesque lobortis ante eu dui fermentum vitae blandit risus aliquet.
 
|_. @@|_. solo texto|_. HTML Limpio|
|Markdown|Si|Si|
|Editor WYSISWG|X|A veces|

_Ejemplo de código_

bc.. import lifetime

for each_day in lifetime.days():
    carpe_diem()
 
 
p. Suspendisse posuere velit et velit VEHICULA(automobila) at scelerisque orci suscipit. Nulla facilisis lorem eu sem viverra varius nec ut felis.
 
Esto es un texto con nota al pie[1] y esta es otra nota[2]
 
fn1. Esto es una nota al pie.

fn2. Esto es la segunda nota.
    </pre>
   </td>
   <td>
<h1>Documento de ejemplo</h1>

<p>Lorem ipsum <a href="#mark">dolor sit amet</a>, consectetur adipiscing elit. Curabitur eget ante nunc. Pellentesque a tortor ipsum, id rhoncus orci. Quisque leo sapien, rutrum id convallis id, rutrum in ligula. Vestibulum <b>semper adipiscing leo</b> et blandit.</p>

<p>Sed nibh quam, hendrerit <em>sit amet aliquam</em> vel, pulvinar molestie augue.</p>

<blockquote>
	<p>Integer cursus, nunc eu ultrices pellentesque, eros leo malesuada turpis, vel convallis neque dolor a nunc. Sed lacus risus, condimentum vitae posuere quis, ultrices pharetra nunc.</p>
</blockquote>

<p>Lenguajes de marcado ligero </p>

<ul>
	<li><b>Markdown</b></li>
	<li>Textile</li>
	<li>reStructuredText</li>
	<li>Texy!</li>
	<li>Txt2tags</li>
	<li>Marcado Wiki
<ol>
	<li>Creole</li>
	<li>MediaWiki</li>
</ol></li>
</ul>

<p><img src="pictures/no_wysiwyg.png" title="avatar" alt="avatar" /></p>

<h3>Cabecera H3</h3>

<p>Morbi erat augue, feugiat eu pellentesque eget, hendrerit quis lectus. Fusce dignissim pretium nibh sed dignissim. Pellentesque lobortis ante eu dui fermentum vitae blandit risus aliquet.</p>

<table>
	<tr>
        <th></th>
		<th>solo texto</th>
		<th><span class="caps"><span class="caps">HTML</span></span> Limpio</th>
	</tr>
	<tr>
		<td>Markdown</td>
		<td>Si</td>
		<td>Si</td>
	</tr>
	<tr>
		<td>Editor <span class="caps"><span class="caps">WYSISWG</span></span></td>
		<td>X</td>
		<td>A veces</td>
	</tr>
</table>

<p><em>Ejemplo de código</em></p>

<pre>
import lifetime

for each_day in lifetime.days():
    carpe_diem()
</pre>

<p>Suspendisse posuere velit et velit <acronym title="automobila"><span class="caps">VEHICULA</span></acronym> at scelerisque orci suscipit. Nulla facilisis lorem eu sem viverra varius nec ut felis.</p>

<p>Esto es un texto con nota al pie<sup class="footnote"><a href="#fn8701048694d94660b0d4d4">1</a></sup> y esta es otra nota<sup class="footnote"><a href="#fn13831162204d94660b122f5">2</a></sup></p>

<p id="fn8701048694d94660b0d4d4" class="footnote"><sup>1</sup> Esto es una nota al pie.</p>

<p id="fn13831162204d94660b122f5" class="footnote"><sup>2</sup> Esto es la segunda nota.</p>
   </td>
  </tr>
 </tbody>
</table>

----

## BBCode

Es uno de los más extendido porque es ampliamente usado en foros por toda la red. 
Nació para ser empleado en foros y es prácticamente el único ámbito en el que se 
emplea. Es también muy limitado porque no soporta muchas de las características 
de los otros lenguajes y además hay múltiples variantes que no ayudan a crear un 
estándar. Por ejemplo las listas y las tablas no son contempladas en algunas de 
esas variantes.

<table>
 <thead>
  <tr>
   <th style="width: 50%;">BBCode</th><th>Resultado</th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td>
    <pre class="no_mrkdwn">
Documento de ejemplo
 
Lorem ipsum [url=http://joedicastro.com]dolor sit amet[/url], consectetur adipiscing elit. Curabitur eget ante nunc. Pellentesque a tortor ipsum, id rhoncus orci. Quisque leo sapien, rutrum id convallis id, rutrum in ligula. Vestibulum [b]semper adipiscing leo[/b] et blandit.
 
Sed nibh quam, hendrerit [i]sit amet aliquam[/i] vel, pulvinar molestie augue.
 
[quote]Integer cursus, nunc eu ultrices pellentesque, eros leo malesuada turpis, vel convallis neque dolor a nunc. Sed lacus risus, condimentum vitae posuere quis, ultrices pharetra nunc.[/quote]
 
[img]http://joedicastro/files/
imagenes/no_wysiwyg.png[/img]
 
Cabecera H3
 
Morbi erat augue, feugiat eu pellentesque eget, hendrerit quis lectus. Fusce dignissim pretium nibh sed dignissim. Pellentesque lobortis ante eu dui fermentum vitae blandit risus aliquet.

[i]Ejemplo de codigo[/i]

[code]
import lifetime
 
for each_day in lifetime.days():
    carpe_diem()
[/code]
    </pre>
   </td>
   <td><div>
<p>
Documento de ejemplo<br />
</p>
<p>
Lorem ipsum <a href="http://joedicastro.com" target="_new">dolor sit amet</a>, consectetur adipiscing elit. Curabitur eget ante nunc. Pellentesque a tortor ipsum, id rhoncus orci. Quisque leo sapien, rutrum id convallis id, rutrum in ligula. Vestibulum <strong>semper adipiscing leo</strong> et blandit.
</p>
<p>
Sed nibh quam, hendrerit <em>sit amet aliquam</em> vel, pulvinar molestie augue.
</p>
<blockquote>
<p>
Integer cursus, nunc eu ultrices pellentesque, eros leo malesuada turpis, vel convallis neque dolor a nunc. Sed lacus risus, condimentum vitae posuere quis, ultrices pharetra nunc.
</p>
</blockquote>
<p><img src="pictures/no_wysiwyg.png" alt="" /></p>
<p>Cabecera H3</p>
<p>Morbi erat augue, feugiat eu pellentesque eget, hendrerit quis lectus. Fusce dignissim pretium nibh sed dignissim. Pellentesque lobortis ante eu dui fermentum vitae blandit risus aliquet.</p>
<em>Ejemplo de codigo</em>
<pre class="code">
import lifetime

for each_day in lifetime.days():
carpe_diem()
</pre></div>
   </td>
  </tr>
 </tbody>
</table>

-----


## reStructuredText

Fue creado para crear documentación, en concreto documentación para lenguajes de 
programación como Python. Tiene algunas carencias al no estar orientado a HTML, 
pero también tiene posibilidades de las que carece Markdown. Es muy potente, 
bastante legible, pero un poco incomodo para según que cosas, a mi modo de ver. 

<table>
 <thead>
  <tr>
   <th style="width: 53%;">reStructuredText</th><th>Resultado</th>
  </tr>
 <tbody>
  <tr>
   <td>
    <pre class="no_mrkdwn">
Documento de ejemplo
====================

Lorem ipsum `dolor sit amet <#mark>`_, consectetur adipiscing elit. Curabitur eget ante nunc. Pellentesque a tortor ipsum, id rhoncus orci. Quisque leo sapien, rutrum id convallis id, rutrum in ligula. Vestibulum **semper adipiscing leo** et blandit.
 
Sed nibh quam, hendrerit *sit amet aliquam* vel, pulvinar molestie augue.
 
 Integer cursus, nunc eu ultrices pellentesque, eros leo malesuada turpis, vel convallis neque dolor a nunc. Sed lacus risus, condimentum vitae posuere quis, ultrices pharetra nunc.
 
Lenguajes de marcado ligero 

&nbsp;* **Markdown**
&nbsp;* Textile
&nbsp;* reStructuredText
&nbsp;* Texy!
&nbsp;* Txt2tags
&nbsp;* Marcado Wiki

&nbsp;&nbsp;&nbsp;1. Creole
&nbsp;&nbsp;&nbsp;2. MediaWiki

.. image:: pictures/no_wysiwyg.png
   :alt: avatar

---------------

Cabecera H3
^^^^^^^^^^^ 

Morbi erat augue, feugiat eu pellentesque eget, hendrerit quis lectus. Fusce dignissim pretium nibh sed dignissim. Pellentesque lobortis ante eu dui fermentum vitae blandit risus aliquet.

============== ========== ===========
\              solo texto HTML Limpio
============== ========== ===========
Markdown           Si         Si      
Editor WYSISWG     X        A veces 
============== ========== ===========

*Ejemplo de código*::

&nbsp;&nbsp;&nbsp;&nbsp;import lifetime
 
&nbsp;&nbsp;&nbsp;&nbsp;for each_day in lifetime.days():
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;carpe_diem()
 
 
Suspendisse posuere velit et velit vehicula at scelerisque orci suscipit. Nulla facilisis lorem eu sem viverra varius nec ut felis.
 
Esto es un texto con nota al pie [1]_ y esta es otra nota [2]_
 
.. [1] Esto es una nota al pie.
.. [2] Esto es la segunda nota.
    </pre>
   </td>
   <td>
<h1 id="documento-de-ejemplo">Documento de ejemplo</h1>
<p>Lorem ipsum <a href="#mark">dolor sit amet</a>, consectetur adipiscing elit. Curabitur eget ante nunc. Pellentesque a tortor ipsum, id rhoncus orci. Quisque leo sapien, rutrum id convallis id, rutrum in ligula. Vestibulum <strong>semper adipiscing leo</strong> et blandit.</p>
<p>Sed nibh quam, hendrerit <em>sit amet aliquam</em> vel, pulvinar molestie augue.</p>
<blockquote>
<p>Integer cursus, nunc eu ultrices pellentesque, eros leo malesuada turpis, vel convallis neque dolor a nunc. Sed lacus risus, condimentum vitae posuere quis, ultrices pharetra nunc.</p>
</blockquote>
<p>Lenguajes de marcado ligero</p>
<ul>
<li><strong>Markdown</strong></li>
<li>Textile</li>
<li>reStructuredText</li>
<li>Texy!</li>
<li>Txt2tags</li>
<li>Marcado Wiki
<ol style="list-style-type: decimal">
<li>Creole</li>
<li>MediaWiki</li>
</ol></li>
</ul><p />
<img src="pictures/no_wysiwyg.png" alt="avatar" />
<hr />
<h2 id="cabecera-h3">Cabecera H3</h2>
<p>Morbi erat augue, feugiat eu pellentesque eget, hendrerit quis lectus. Fusce dignissim pretium nibh sed dignissim. Pellentesque lobortis ante eu dui fermentum vitae blandit risus aliquet.</p>
<table>
<thead>
<tr class="header">
<th align="left"> </th>
<th align="left">solo texto</th>
<th align="left">HTML Limpio</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left">Markdown</td>
<td align="left">Si</td>
<td align="left">Si</td>
</tr>
<tr class="even">
<td align="left">Editor WYSISWG</td>
<td align="left">X</td>
<td align="left">A veces</td>
</tr>
</tbody>
</table>
<p><em>Ejemplo de código</em>:</p>
<pre>import lifetime

for each_day in lifetime.days():
    carpe_diem()
</pre>
<p>Suspendisse posuere velit et velit vehicula at scelerisque orci suscipit. Nulla facilisis lorem eu sem viverra varius nec ut felis.</p>
<p>Esto es un texto con nota al pie <sup><a href="#fn1" class="footnoteRef" id="fnref1">1</a></sup> y esta es otra nota <sup><a href="#fn2" class="footnoteRef" id="fnref2">2</a></sup></p>
<div class="footnotes">
<hr />
<ol>
<li id="fn1"><p>Esto es una nota al pie. <a href="#fnref1" class="footnoteBackLink" title="Jump back to footnote 1">↩</a></p></li>
<li id="fn2"><p>Esto es la segunda nota. <a href="#fnref2" class="footnoteBackLink" title="Jump back to footnote 2">↩</a></p></li>
</ol>
</div>
   </td>
  </tr>
 </tbody>
</table>

----


## Texy!

Fue específicamente diseñado para crear documentos XHTML, por ello es bastante 
completo, pero no está muy extendido. Es legible, pero también tiene carece de 
soporte para ciertos tags de HTML.

<table>
 <thead>
  <tr>
   <th style="width: 53%;">Texy!</th><th>Resultado</th>
  </tr>
 <tbody>
  <tr>
   <td>
    <pre class="no_mrkdwn">
Documento de ejemplo
====================
 
Lorem ipsum [dolor sit amet | http://joedicastro.com], consectetur adipiscing elit. Curabitur eget ante nunc. Pellentesque a tortor ipsum, id rhoncus orci. Quisque leo sapien, rutrum id convallis id, rutrum in ligula. Vestibulum **semper adipiscing leo** et blandit.
 
Sed nibh quam, hendrerit *sit amet aliquam* vel, pulvinar molestie augue.
 
> Integer cursus, nunc eu ultrices pellentesque, eros leo malesuada turpis, vel convallis neque dolor a nunc. Sed lacus risus, condimentum vitae posuere quis, ultrices pharetra nunc.
 
Lenguajes de marcado ligero 

- **Markdown**
- Textile
- reStructuredText
- Texy!
- Txt2tags
- Marcado Wiki
 1) Creole
 2) MediaWiki

[* pictures/no_wysiwyg.png .(alt text)[avatar] *]
 
### Cabecera H3 ###
 
-----
 
Morbi erat augue, feugiat eu pellentesque eget, hendrerit quis lectus. Fusce dignissim pretium nibh sed dignissim. Pellentesque lobortis ante eu dui fermentum vitae blandit risus aliquet.

|------------------------------
|   | solo texto | HTML Limpio  
|------------------------------
| Markdown       | Si | Si      
| Editor WYSISWG | X  | A veces 

*Ejemplo de código*

/---code
&nbsp;&nbsp;import lifetime
 
&nbsp;&nbsp;for each_day in lifetime.days():
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;carpe_diem()
\---
 
Suspendisse posuere velit et velit "vehicula"((automobila)) at scelerisque orci suscipit. Nulla facilisis lorem eu sem viverra varius nec ut felis.
    </pre>
   </td>
   <td>

<h1 id="toc-documento-de-ejemplo">Documento de ejemplo</h1>

<p>Lorem ipsum <a href="http://joedicastro.com">dolor sit amet</a>, consectetur
adipiscing elit. Curabitur eget ante nunc. Pellentesque a tortor ipsum, id
rhoncus orci. Quisque leo sapien, rutrum id convallis id, rutrum in ligula.
Vestibulum <strong>semper adipiscing leo</strong> et blandit.</p>

<p>Sed nibh quam, hendrerit <em>sit amet aliquam</em> vel, pulvinar
molestie&nbsp;augue.</p>

<blockquote>
    <p>Integer cursus, nunc eu ultrices pellentesque, eros leo malesuada turpis, vel
    convallis neque dolor a nunc. Sed lacus risus, condimentum vitae posuere quis,
    ultrices pharetra&nbsp;nunc.</p>
</blockquote>

<p>Lenguajes de marcado ligero</p>

<ul>
    <li><strong>Markdown</strong></li>

    <li>Textile</li>

    <li>reStructuredText</li>

    <li>Texy!</li>

    <li>Txt2tags</li>

    <li>Marcado Wiki
        <ol>
            <li>Creole</li>

            <li>MediaWiki</li>
        </ol>
    </li>
</ul>

<div><img src="pictures/no_wysiwyg.png" class="avatar"
alt="alt text"></div>

<h1 id="toc-cabecera-h3">Cabecera H3</h1>

<hr>

<p>Morbi erat augue, feugiat eu pellentesque eget, hendrerit quis lectus. Fusce
dignissim pretium nibh sed dignissim. Pellentesque lobortis ante eu dui
fermentum vitae blandit risus aliquet.</p>

<table>
    <thead>
        <tr>
            <th>&nbsp;</th>

            <th>solo texto</th>

            <th>HTML Limpio</th>
        </tr>
    </thead>

    <tbody>
        <tr>
            <td>Markdown</td>

            <td>Si</td>

            <td>Si</td>
        </tr>

        <tr>
            <td>Editor WYSISWG</td>

            <td>X</td>

            <td>A&nbsp;veces</td>
        </tr>
    </tbody>
</table>

<p><em>Ejemplo de código</em></p>

<pre>import lifetime

for each_day in lifetime.days():
    carpe_diem()</pre>

<p>Suspendisse posuere velit et velit <acronym
title="automobila">vehicula</acronym> at scelerisque orci suscipit. Nulla
facilisis lorem eu sem viverra varius nec ut&nbsp;felis.</p>
   </td>
  </tr>
 </tbody>
</table>


-----

## txt2tags
 
Está escrito en Python y es muy potente, al igual que RestructuredText, 
permitiendo macros. Permite la salida en muchos formatos, incluido el XHTML. 
Es muy legible y muy fácil de emplear, es una pena que no esté más extendido y 
soportado. Aunque aún tiene algunas carencias como las notas al pie o las 
abreviaturas, que pueden ser soportadas con macros, también tiene un desarrollo 
muy activo. En la futura versión 3.0 serán soportados directamente las notas al 
pie. Es una alternativa con muy buen futuro.

<table>
 <thead>
  <tr>
   <th style="width: 53%;">txt2tags</th><th>Resultado</th>
  </tr>
 <tbody>
  <tr>
   <td>
    <pre class="no_mrkdwn">
=Documento de ejemplo=
 
Lorem ipsum [dolor sit amet #mark], consectetur adipiscing elit. Curabitur eget ante nunc. Pellentesque a tortor ipsum, id rhoncus orci. Quisque leo sapien, rutrum id convallis id, rutrum in ligula. Vestibulum **semper adipiscing leo** et blandit.
 
Sed nibh quam, hendrerit //sit amet aliquam// vel, pulvinar molestie augue.
 
<tab>Integer cursus, nunc eu ultrices pellentesque, eros leo malesuada turpis, vel convallis neque dolor a nunc. Sed lacus risus, condimentum vitae posuere quis, ultrices pharetra nunc.
 
Lenguajes de marcado ligero 

 - **Markdown**
 - Textile
 - reStructuredText
 - Texy!
 - Txt2tags
 - Marcado Wiki
  + Creole
  + MediaWiki


[pictures/no_wysiwyg.png]
 
===Cabecera H3===
 
--------------------
 
Morbi erat augue, feugiat eu pellentesque eget, hendrerit quis lectus. Fusce dignissim pretium nibh sed dignissim. Pellentesque lobortis ante eu dui fermentum vitae blandit risus aliquet.
 
||   | solo texto | HTML Limpio
| Markdown       |  Si  |  Si  |
| Editor WYSISWG |  X  |  A veces  |

//Ejemplo de codigo//

```
import lifetime

for each_day in lifetime.days():
    carpe_diem()
```
    </pre>
   </td>
   <td>
<h1>Documento de ejemplo</h1>

<p>
Lorem ipsum <a href="#mark">dolor sit amet</a>, consectetur adipiscing elit. Curabitur eget ante nunc. Pellentesque a tortor ipsum, id rhoncus orci. Quisque leo sapien, rutrum id convallis id, rutrum in ligula. Vestibulum <b>semper adipiscing leo</b> et blandit.
</p>
<p>
Sed nibh quam, hendrerit <i>sit amet aliquam</i> vel, pulvinar molestie augue.
</p>
<blockquote><p>
Integer cursus, nunc eu ultrices pellentesque, eros leo malesuada turpis, vel convallis neque dolor a nunc. Sed lacus risus, condimentum vitae posuere quis, ultrices pharetra nunc.</p>
</blockquote>
<p>
Lenguajes de marcado ligero 
</p>

 <ul>
 <li><b>Markdown</b>
 <li>Textile
 <li>reStructuredText
 <li>Texy!
 <li>Txt2tags
 <li>Marcado Wiki
  <ol>
  <li>Creole
  <li>MediaWiki
  </ol>
 </ul>

<p>
<img src="pictures/no_wysiwyg.png" alt="">
</p>

<h3>Cabecera H3</h3>

<hr />

<p>
Morbi erat augue, feugiat eu pellentesque eget, hendrerit quis lectus. Fusce dignissim pretium nibh sed dignissim. Pellentesque lobortis ante eu dui fermentum vitae blandit risus aliquet.
</p>

<table cellapadding="4">
  <tr>
    <th></th>
    <th>solo texto</th>
    <th>HTML Limpio</th>
  </tr>
  <tr>
    <td>Markdown</td>
    <td align="center">Si</td>
    <td align="center">Si</td>
  </tr>
  <tr>
    <td>Editor WYSISWG</td>
    <td align="center">X</td>
    <td align="center">A veces</td>
  </tr>
</table>

<p>
 <i>Ejemplo de codigo</i>
</p>

<pre>
import lifetime

for each_day in lifetime.days():
    carpe_diem()
</pre>
   </td>
  </tr>
 </tbody>
</table>

----


## Creole ##

Creado a partir de los lenguajes más empleados en los Wikis y usado 
fundamentalmente en Wikis, por lo que también tiene ciertas carencias.

<table>
 <thead>
  <tr>
   <th style="width: 50%;">Creole</th><th>Resultado</th>
  </tr>
 <tbody>
  <tr>
   <td>
    <pre class="no_mrkdwn">
== Documento de ejemplo ==

Lorem ipsum [[#mark|dolor sit amet]], consectetur adipiscing elit. Curabitur eget ante nunc. Pellentesque a tortor ipsum, id rhoncus orci. Quisque leo sapien, rutrum id convallis id, rutrum in ligula. Vestibulum **semper adipiscing leo** et blandit.
 
Sed nibh quam, hendrerit //sit amet aliquam// vel, pulvinar molestie augue.
 
> Integer cursus, nunc eu ultrices pellentesque, eros leo malesuada turpis, vel convallis neque dolor a nunc. Sed lacus risus, condimentum vitae posuere quis, ultrices pharetra nunc.
 
Lenguajes de marcado ligero 

 * **Markdown**
 * Textile
 * reStructuredText
 * Texy!
 * Txt2tags
 * Marcado Wiki
 ## Creole
 ## MediaWiki

{{pictures/no_wysiwyg.png|avatar}}
 
==== Cabecera H3 ====
 
-----
 
Morbi erat augue, feugiat eu pellentesque eget, hendrerit quis lectus. Fusce dignissim pretium nibh sed dignissim. Pellentesque lobortis ante eu dui fermentum vitae blandit risus aliquet.
 
|= |= solo texto |= HTML Limpio |
| Markdown       | Si | Si      |
| Editor WYSISWG | X  | A veces |

//Ejemplo de código//
{{{
import lifetime
 
for each_day in lifetime.days():
    carpe_diem()
}}}
    </pre>
   </td>
   <td>
<h1>Documento de ejemplo</h1>

<p>Lorem ipsum <a href="#mark">dolor sit amet</a>, consectetur adipiscing elit. Curabitur eget ante nunc. Pellentesque a tortor ipsum, id rhoncus orci. Quisque leo sapien, rutrum id convallis id, rutrum in ligula. Vestibulum <strong>semper adipiscing leo</strong> et blandit.</p>
<p>Sed nibh quam, hendrerit <em>sit amet aliquam</em> vel, pulvinar molestie augue.</p>
<blockquote><p>Integer cursus, nunc eu ultrices pellentesque, eros leo malesuada turpis, vel convallis neque dolor a nunc. Sed lacus risus, condimentum vitae posuere quis, ultrices pharetra nunc.</p>
</blockquote>
<p>Lenguajes de marcado ligero </p>

<ul><li><strong>Markdown</strong>
</li><li>Textile
</li><li>reStructuredText
</li><li>Texy!
</li><li>Txt2tags
</li><li>Marcado Wiki
<ol><li>Creole
</li><li>MediaWiki
</li></ol></li></ul>
<p><img src="pictures/no_wysiwyg.png" alt="avatar" title="avatar" /></p>
<h3>Cabecera H3</h3>
<p>-----</p>
<p>Morbi erat augue, feugiat eu pellentesque eget, hendrerit quis lectus. Fusce dignissim pretium nibh sed dignissim. Pellentesque lobortis ante eu dui fermentum vitae blandit risus aliquet.</p>

<table><tr><th></th><th>solo texto</th><th>HTML Limpio</th></tr>
<tr><td>Markdown</td><td>Si</td><td>Si</td></tr>
<tr><td>Editor WYSISWG</td><td>X</td><td>A veces</td></tr>
</table>
<p><em>Ejemplo de código</em></p>
<pre>
import lifetime
 
for each_day in lifetime.days():
    carpe_diem()
</pre>

   </td>
  </tr>
 </tbody>
</table>

----


## MediaWiki

Quizás el más extendido, no en vano MediaWiki es el Wiki empleado por la 
Wikipedia. Igual que Creole, tiene ciertas limitaciones que suple con plugins y 
etiquetas HTML. No me acaba de gustar. La manera que tiene de crear tablas - 
por ejemplo - aunque potente, no me parece nada legible en texto plano.  

<table>
 <thead>
  <tr>
   <th style="width: 53%;">MediaWiki</th><th>Resultado</th>
  </tr>
 <tbody>
  <tr>
   <td>
    <pre class="no_mrkdwn">
==Documento de ejemplo==
 
Lorem ipsum [http://joedicastro.com dolor sit amet], consectetur adipiscing elit. Curabitur eget ante nunc. Pellentesque a tortor ipsum, id rhoncus orci. Quisque leo sapien, rutrum id convallis id, rutrum in ligula. Vestibulum '''semper adipiscing leo''' et blandit.
 
Sed nibh quam, hendrerit ''sit amet aliquam'' vel, pulvinar molestie augue.
 
<blockquote>Integer cursus, nunc eu ultrices pellentesque, eros leo malesuada turpis, vel convallis neque dolor a nunc. Sed lacus risus, condimentum vitae posuere quis, ultrices pharetra nunc.</blockquote>
 
Lenguajes de marcado ligero 

* '''Markdown'''
* Textile
* reStructuredText
* Texy!
* Txt2tags
* Marcado Wiki
*# Creole
*# MediaWiki

[[File:pictures/no_wysiwyg.png|caption]]
 
=== Cabecera H3 ===
 
----
 
Morbi erat augue, feugiat eu pellentesque eget, hendrerit quis lectus. Fusce dignissim pretium nibh sed dignissim. Pellentesque lobortis ante eu dui fermentum vitae blandit risus aliquet.

{| 
! 
! solo texto
! HTML Limpio
|-
|Markdown
|Si
|Si
|-
|Editor WYSISWG
|X
|A veces
|}

''Ejemplo de código''

&nbsp;&nbsp;import lifetime
&nbsp;&nbsp; 
&nbsp;&nbsp;for each_day in lifetime.days():
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;carpe_diem()
 
 
Suspendisse posuere velit et velit <span title="automobila">vehicula</span> at scelerisque orci suscipit. Nulla facilisis lorem eu sem viverra varius nec ut felis.
 
Esto es un texto con nota al pie <ref name="ejemplo">Esto es una nota al pie.</ref> y esta es otra nota <ref name="segunda"> Esto es la segunda nota.</ref>
 
{{reflist}}
    </pre>
   </td>
   <td>
<h2><span class="mw-headline" id="Documento_de_ejemplo">Documento de ejemplo</span></h2>
<p>Lorem ipsum <a href="http://joedicastro.com" class="external text" rel="nofollow">dolor sit amet</a>, consectetur adipiscing elit. Curabitur eget ante nunc. Pellentesque a tortor ipsum, id rhoncus orci. Quisque leo sapien, rutrum id convallis id, rutrum in ligula. Vestibulum <b>semper adipiscing leo</b> et blandit.</p>

<p>Sed nibh quam, hendrerit <i>sit amet aliquam</i> vel, pulvinar molestie augue.</p>
<blockquote>
<p>Integer cursus, nunc eu ultrices pellentesque, eros leo malesuada turpis, vel convallis neque dolor a nunc. Sed lacus risus, condimentum vitae posuere quis, ultrices pharetra nunc.</p>
</blockquote>
<p>Lenguajes de marcado ligero</p>
<ul>
<li><b>Markdown</b></li>
<li>Textile</li>
<li>reStructuredText</li>

<li>Texy!</li>
<li>Txt2tags</li>
<li>Marcado Wiki
<ol>
<li>Creole</li>
<li>MediaWiki</li>
</ol>
</li>
</ul>
<p><img src="pictures/no_wysiwyg.png" alt="" /></p>
<h3><span class="mw-headline" id="Cabecera_H3">Cabecera H3</span></h3>

<hr />
<p>Morbi erat augue, feugiat eu pellentesque eget, hendrerit quis lectus. Fusce dignissim pretium nibh sed dignissim. Pellentesque lobortis ante eu dui fermentum vitae blandit risus aliquet.</p>
<table>
<tr>
<th></th>
<th>solo texto</th>
<th>HTML Limpio</th>
</tr>
<tr>
<td>Markdown</td>
<td>Si</td>
<td>Si</td>

</tr>
<tr>
<td>Editor WYSISWG</td>
<td>X</td>
<td>A veces</td>
</tr>
</table>
<p><i>Ejemplo de código</i></p>
<pre>
import lifetime

for each_day in lifetime.days():
    carpe_diem()

</pre>
<p>Suspendisse posuere velit et velit <span title="automobila">vehicula</span> at scelerisque orci suscipit. Nulla facilisis lorem eu sem viverra varius nec ut felis.</p>

<p>Esto es un texto con nota al pie <sup id="cite_ref-ejemplo_0-0" class="reference"><a href="#cite_note-ejemplo-0"><span>[</span>1<span>]</span></a></sup> y esta es otra nota <sup id="cite_ref-segunda_1-0" class="reference"><a href="#cite_note-segunda-1"><span>[</span>2<span>]</span></a></sup></p>
<div class="reflist" style="list-style-type: decimal;">
<ol class="references">
<li id="cite_note-ejemplo-0"><b><a href="#cite_ref-ejemplo_0-0">^</a></b> Esto es una nota al pie.</li>
<li id="cite_note-segunda-1"><b><a href="#cite_ref-segunda_1-0">^</a></b> Esto es la segunda nota.</li>

</ol>
   </td>
  </tr>
 </tbody>
</table>

