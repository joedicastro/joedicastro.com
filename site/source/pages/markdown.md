title: markdown
date: 2011-03-20 13:03

Markdown & Pygments Lexers Cheat Sheet
======================================

Esta es una guía que me sirve para recordar todas las posibilidades que ofrecen 
markdown y Pygments para editar y formatear texto y que empleo para crear los 
artículos de este blog. Está redactada de forma que no solo me sirva de guía a 
mí, si no a cualquiera que se acerque por primera vez a markdown o Pygments.

----

Lo que sigue a continuación es una lista detallada de todas las características 
que se pueden emplear en Markdown y Markdown Extra (empleando _Python Markdown_) 
y los lexers más comunes de Pygments para resaltar el código fuente.

* [Markdown](#header1)
    * [¿Que es Markdown?](#mark0)
* [Sintaxis Markdown](#mark1)
    * [Cabeceras](#mark2)
    * [Enlaces](#mark3)
    * [Parrafos](#mark4)
    * [Formato](#mark5)
    * [Citas](#mark6)
    * [Listas](#mark7)
    * [Listas de definiciones](#mark8)
    * [Imágenes](#mark9)
    * [Tablas](#mark10)
    * [Código](#mark11)
    * [Lineas Horizontales](#mark12)
    * [Escapar caracteres](#mark13)
    * [Notas a pie de página](#mark14)
    * [Abreviaturas](#mark15)
    * [Indentificadores de cabecera](#mark16)
* [Pygments](#header2)
    * [Lexers de Pygments más comunes para resaltado de sintaxis](#syntax0)

<br />

## Markdown  {#header1}

Este es el lenguaje de marcado empleado para crear este sitio, que permite 
formatear el texto fácilmente sin la necesidad de emplear el más engorroso HTML 
o emplear un editor visual.

### ¿Que es Markdown? {#mark0}

[Markdown][3] es un lenguaje de marcado ligero parecido al que se emplea en 
muchas wikis y basado originalmente en convenciones existentes en el marcado de 
los los correos electronicos. Emplea texto plano, procurando que sea legible 
pero consiguiendo que se convierta en XHTML correctamente formateado. Los
artículos de este sitio están elaborados empleando markdown, sin utilizar ningún
tipo de editor visual WYSIWYG, lo que facilita el crear documentos XHTML 
limpios y fácilmente editables en el futuro. Son un buen ejemplo de las 
capacidades de Markdown. Aunque no es muy conocido, empieza a ser muy popular y 
utilizado entre los programadores.

 [3]: http://es.wikipedia.org/wiki/Markdown
*[WYSIWYG]: What You See Is What You Get (en inglés, "lo que ves es lo que obtienes")
*[XHTML]: Páginas Web

Para conocer más sobre markdown, se pueden leer los artículos en los que explico 
porque es el más adecuado para crear un blog y porque lo he elegido para este 
sitio, [artículos markdown](../tag/markdown.html)

----

## Sintaxis Markdown {#mark1}

### Cabeceras {#mark2}

Los encabezamientos HTML se producen colocando un número determinado de 
almohadillas **#** antes del texto correspondiente al nivel de encabezamiento 
deseado (HTML ofrece hasta seis niveles). Los encabezamientos posibles se pueden 
ver en la siguiente tabla:

<table>
 <thead><tr><th style="width: 50%;">Tecleas</th><th>Obtienes</th></tr></thead>
<tbody><tr>
    <td><pre class="no_mrkdwn">
# Esto es un H1</pre></td>
     <td><h1>Esto es un H1</h1></td>
  </tr>
  <tr>
    <td><pre class="no_mrkdwn">
## Esto es un H2</pre></td>
     <td><h2>Esto es un H2</h2></td>
  </tr>
  <tr>
    <td><pre class="no_mrkdwn">
### Esto es un H3</pre></td>
     <td><h3>Esto es un H3</h3></td>
  </tr>
  <tr>
    <td><pre class="no_mrkdwn">
#### Esto es un H4</pre></td>
     <td><h4>Esto es un H4</h4></td>
  </tr>
  <tr>
    <td><pre class="no_mrkdwn">
##### Esto es un H5</pre></td>
     <td><h5>Esto es un H5</h5></td>
  </tr>
  <tr>
    <td><pre class="no_mrkdwn">
###### Esto es un H6</pre></td>
     <td><h6>Esto es un H6</h6></td>
  </tr>
</tbody></table>

Se puede encerrar cada encabezado entre almohadillas, por motivos puramente 
estéticos, porque no es necesario en absoluto, es decir, se puede hacer esto:

<table>
  <thead><tr><th style="width: 50%;">Tecleas</th><th>Obtienes</th></tr></thead>
  <tbody><tr>
    <td><pre class="no_mrkdwn">
### Esto es un H3 ###</pre></td>
     <td><h3>Esto es un H3</h3></td>
  </tr>
</tbody></table>

Para los encabezamientos de los dos primeros niveles existe también otra manera 
de hacer lo mismo, que sería la siguiente:

<table>
  <thead><tr><th style="width: 50%;">Tecleas</th><th>Obtienes</th></tr></thead>
  <tbody><tr>
    <td><pre class="no_mrkdwn">
Esto es un H1
=============</pre></td>
     <td><h1>Esto es un H1</h1></td>
  </tr>
  <tr>
    <td><pre class="no_mrkdwn">
Esto es un H2
-------------</pre></td>
     <td><h2>Esto es un H2</h2></td>
  </tr>
</tbody></table>

Es decir para los encabezamientos principales se subraya el texto con el signo 
igual. Para los encabezamientos de segundo nivel se utilizan guiones para subrayar. 
Es indiferente el número de signos iguales o guiones que se empleen, con uno es 
suficiente.


----

### Enlaces {#mark3}

Existen también dos maneras de crear enlaces, se pueden ver en la siguiente tabla:

<table>
  <thead><tr><th style="width: 65%;">Tecleas</th><th>Obtienes</th></tr></thead>
  <tbody>
<tr>
    <td><pre class="no_mrkdwn">
[Con titulo](http://joedicastro.com "titulo")</pre></td>
     <td><a href="#mark3" title="titulo">Con titulo</a></td>
  </tr>
  <tr>
    <td><pre class="no_mrkdwn">
[Sin titulo](http://joedicastro.com)</pre></td>
     <td><a href="#mark3">Sin titulo</a></td>
  </tr><tr>
    <td><pre class="no_mrkdwn">
[Enlace 1][1], [Enlace 2][2], [Enlace 3][3]

&nbsp;[1]: http://joedicastro.com/consejos
&nbsp;[2]: http://joedicastro.com/consejos "Consejos"
&nbsp;[3]: http://joedicastro.com/</pre></td>
     <td><a href="http://joedicastro.com/consejos">Enlace 1</a>, <a href="http://joedicastro.com/consejos" title="Consejos">Enlace 2</a>, <a href="http://joedicastro.com">Enlace 3</a></td>
  </tr>
</tbody></table>

Existe una manera adicional de crear enlaces automáticos para direcciones URL, 
simplemente encerrarla entre los caracteres menor **<** que y mayor que **>**:

<table>
  <thead><tr><th style="width: 65%;">Tecleas</th><th>Obtienes</th></tr></thead>
  <tbody>
   <tr>
    <td>
    <pre class="no_mrkdwn">
&lt;http://joedicastro.com&gt;</pre>
    </td>
    <td><a href="#mark3">http://joedicastro.com</a></td>
   </tr>
  </tbody>
</table>

----

### Párrafos {#mark4}

Para crear párrafos se deja una línea en blanco. De este modo.

<table>
  <thead><tr><th style="width: 50%;">Tecleas</th><th>Obtienes</th></tr></thead>
  <tbody><tr>
    <td><pre class="no_mrkdwn">
Este es el primer párrafo.

Este es el segundo párrafo.</pre></td>
     <td><p>Este es el primer párrafo.</p><p>Este es el segundo párrafo</p></td>
  </tr>
</table>

Para crear un salto de línea dentro de un párrafo, simplemente se dejan dos 
espacios al final de la última palabra de esa línea, de este modo:

<table>
  <thead><tr><th style="width: 50%;">Tecleas</th><th>Obtienes</th></tr></thead>
  <tbody><tr>
    <td><pre class="no_mrkdwn">
Esta es la primera línea  
y este es el salto de línea.</pre></td>
     <td>Esta es la primera línea<br>y este es el salto de línea.</td>
  </tr>
</table>

----

### Formato {#mark5}

El formato básico del texto, es decir negritas y cursiva, se pueden realizar de 
varias maneras:

<table>
  <thead><tr><th style="width: 50%;">Tecleas</th><th>Obtienes</th></tr></thead>
  <tbody><tr>
    <td><pre class="no_mrkdwn">
**Esto es negrita**</pre></td>
     <td><strong>Esto es negrita</strong></td>
  </tr>
  <tr>
    <td><pre class="no_mrkdwn">
__Esto también es negrita__</pre></td>
     <td><strong>Esto también es negrita</strong></td>
  </tr>
  <tr>
    <td><pre class="no_mrkdwn">
*Esto es cursiva*</pre></td>
     <td><em>Esto es cursiva</em></td>
  </tr>
  <tr>
    <td><pre class="no_mrkdwn">
_Esto también es cursiva_</pre></td>
     <td><em>Esto también es cursiva</em></td>
  </tr>
  <tr>
    <td><pre class="no_mrkdwn">
***Esto es negrita y cursiva***</pre></td>
     <td><strong><em>Esto es negrita y cursiva</em></strong></td>
  </tr>  
  <tr>
    <td><pre class="no_mrkdwn">
___Esto también es negrita y cursiva___</pre></td>
     <td><strong><em>Esto también es negrita y cursiva</em></strong></td>
  </tr>  
</table>

Se pueden emplear indistintamente tanto el asterisco **\*** como el guión bajo 
**\_** siempre y cuando no se mezclen y lo que determina el formato es el número 
de ellos antes y después del bloque de texto a formatear. Uno es cursiva, dos es 
negrita, y tres ambas a la vez, así de sencillo.

----

### Citas {#mark6}

Para crear bloques de cita, se emplea el carácter mayor que `>` antes del bloque 
de texto. En la siguiente tabla se pueden ver las opciones para crearlos.

<table>
  <thead><tr><th style="width: 54%;">Tecleas</th><th>Obtienes</th></tr></thead>
  <tbody><tr>
    <td><pre class="no_mrkdwn">
Esto es una línea normal

> Esto es parte de un bloque de cita.
> Esto es parte del mismo bloque de cita.</pre></td>
     <td>
<p>Esto es una línea normal</p>

<blockquote>
  <p>Esto es parte de un bloque de cita.
  Esto es parte del mismo bloque de cita.</p>
</blockquote>
     </td>
  </tr>
  <tr>
    <td><pre class="no_mrkdwn">
> Esto es parte de un bloque de cita.
Esto continúa el bloque incluso aunque no hay símbolo 'mayor que'.

La línea en blanco finaliza el bloque.</pre></td>
     <td>
<blockquote>
  <p>Esto es parte de un bloque de cita.
  Esto continúa el bloque incluso aunque no hay símbolo 'mayor que'.</p>
</blockquote>

<p>La línea en blanco finaliza el bloque.</p>
     </td>
  </tr>
  <tr>
    <td><pre class="no_mrkdwn">
Esto es una línea normal

> Esto es parte de un bloque de cita.
> Esto es parte del mismo bloque de cita.
>
> > Esto es otro bloque de cita anidado.
> > Esto es parte del bloque anidado.
>
> Esto es parte del bloque de cita de primer nivel.</pre></td>
     <td>
<p>Esto es una línea normal</p>

<blockquote>
  <p>Esto es parte de un bloque de cita.
  Esto es parte del mismo bloque de cita.</p>

  <blockquote>
    <p>Esto es otro bloque de cita anidado.
    Esto es parte del bloque anidado.</p>
  </blockquote>

  <p>Esto es parte del bloque de cita de primer nivel.</p>
</blockquote>
     </td>
  </tr>
</table>

----

### Listas {#mark7}

Markdown permite crear dos tipos de listas, ordenadas y desordenadas, es decir 
numeradas o listas de puntos. Para distinguir los tipos y como se crean, nada 
mejor que verlo con ejemplos:

<table>
  <thead><tr><th style="width: 50%;">Tecleas</th><th>Obtienes</th></tr></thead>
  <tbody><tr>
    <td><pre class="no_mrkdwn">
Lista numerada (ordenada)

1. Este es el primer elemento
2. Este es el segundo elemento
3. Este es el tercer elemento
</pre></td>
     <td>
<p>Lista numerada (ordenada)</p>

<ol><li>Este es el primer elemento</li>
<li>Este es el segundo elemento</li>
<li>Este es el tercer elemento</li>
</ol>
</td>
  </tr>
  <tr>
    <td><pre class="no_mrkdwn">
Lista de puntos (desordenada)

* Un elemento de la lista
* Otro elemento de la lista
* El tercer elemento de la lista
</pre></td>
     <td>
<p>Lista de puntos (desordenada)</p>

<ul><li>Un elemento de la lista</li>
<li>Otro elemento de la lista</li>
<li>El tercer elemento de la lista</li>
</ul>
</td>
  </tr>
  <tr>
    <td><pre class="no_mrkdwn">
Se pueden emplear también + y - en vez de *

* Un elemento de la lista
+ Otro elemento de la lista
- El tercer elemento de la lista
</pre></td>
     <td>
<p>Se pueden emplear también <code>+</code> y <code>-</code> en vez de <code>*</code></p>

<ul><li>Un elemento de la lista</li>
<li>Otro elemento de la lista</li>
<li>El tercer elemento de la lista</li>
</ul>
</td>
  </tr>
  <tr>
    <td><pre class="no_mrkdwn">
Se pueden mezclar distintos tipos de listas y anidar unas dentro de otras.

1. Esto es una lista ordenada
2. Segundo elemento de la lista ordenada
    1. Esta es una lista ordenada anidada dentro de otra
        * Lista desordenada anidada a tercer nivel
        * Segundo elemento de esta lista
    2. Este es el segundo elemento de la lista ordenada anidada
</pre></td>
     <td>
<p>Se pueden mezclar distintos tipos de listas y anidar unas dentro de otras.</p>

<ol>
<li>Esto es una lista ordenada</li>
<li>Segundo elemento de la lista ordenada<ol>

<li>Esta es una lista ordenada anidada dentro de otra<ul>
<li>Lista desordenada anidada a tercer nivel</li>
<li>Segundo elemento de esta lista</li>
</ul>
</li>
<li>Este es el segundo elemento de la lista ordenada anidada</li>
</ol>
</li>
</ol>
</td>
  </tr>
</table>

----

### Listas de definiciones {#mark8}

Se pueden crear lista de definiciones, que están compuestas de términos y las 
definiciones de los mismos, como si fuera un diccionario. Su creación es muy 
sencilla:

<table>
  <thead><tr><th style="width: 50%;">Tecleas</th><th>Obtienes</th></tr></thead>
  <tbody><tr>
    <td><pre class="no_mrkdwn">
Primer termino
 : Primera definición

Segundo termino
 : Segunda definición</pre></td>
     <td>
<dl>
  <dt>Primer término</dt>
    <dd>Primera definición</dd>
  <dt>Segundo término</dt>
    <dd>Segunda definición</dd>
</dl>
</td>
  </tr>
  <tr>
    <td><pre class="no_mrkdwn">
Se pueden aplicar más de una definición a un termino

Primer termino
 : Primera definición
 : Segunda definición

Segundo termino
 : Segunda definición</pre></td>
     <td>
<p>Se pueden aplicar más de una definición a un termino</p>
<dl>
  <dt>Primer término</dt>
    <dd>Primera definición</dd>
    <dd>Segunda definición</dd>
  <dt>Segundo término</dt>
    <dd>Segunda definición</dd>
</dl>
</td>
  </tr>
  <tr>
    <td><pre class="no_mrkdwn">
Se pueden aplicar más de un termino a una definición

Primer termino
Segundo termino
 : Primera definición

Tercer termino
 : Segunda definición</pre></td>
     <td>
<p>Se pueden aplicar más de una definición a un termino</p>
<dl>
  <dt>Primer término</dt>
  <dt>Segundo término</dt>
    <dd>Primera definición</dd>
  <dt>Tercer término</dt>
    <dd>Segunda definición</dd>
</dl>
</td>
  </tr>
 <tr>
    <td><pre class="no_mrkdwn">
Si dejamos una línea en blanco entre el termino y la definición, se creara un párrafo para la definición.

Primer termino

 : Primera definición

Segundo termino
 : Segunda definición</pre></td>
     <td>
<p>Si dejamos una línea en blanco entre el termino y la definición, se creara un párrafo para la definición.</p>

<dl><dt>Primer termino</dt>

<dd>
<p>Primera definición</p>
</dd>

<dt>Segundo termino</dt>
<dd>Segunda definición</dd>
</dl>
</td>
  </tr>
<tr>
    <td><pre class="no_mrkdwn">
Una definición puede constar de varios párrafos.

Primer termino
 : Primera definición

 Segundo párrafo de la primera definición

Segundo termino
 : Segunda definición</pre></td>
     <td>
<p>Una definición puede constar de varios párrafos.<p>
<dl>
  <dt>Primer término</dt>
    <dd><p>Primera definición</p>
<p>Segundo párrafo de la primera definición</p></dd>
  <dt>Segundo término</dt>
    <dd>Segunda definición</dd>
</dl>
</td>
  </tr>
</table>


----

### Imágenes {#mark9}

La manera de enlazar imágenes es básicamente la misma de crear enlaces, con un 
única diferencia, se añade el carácter exclamación **!** al principio de la 
pareja de corchetes que definen el nombre del enlace. Ejemplos:

<table>
 <thead>
   <tr><th style="width: 55%;">Tecleas</th><th>Obtienes</th></tr>
 </thead>
 <tbody>
  <tr>
  <td>
   <pre class="no_mrkdwn">
![Con titulo](pictures/avatar.png "titulo")</pre>
  </td>
  <td>
    <img src="/pictures/avatar.png" title="avatar" alt="avatar" />
  </td>
  </tr>
   <tr>
   <td>
    <pre class="no_mrkdwn">
![Sin titulo](pictures/avatar.png)</pre>
   </td>
   <td>
    <img src="/pictures/avatar.png" alt=""/>
   </td>
   </tr>
   <tr>
   <td>
    <pre class="no_mrkdwn">
![Imagen 1][1]  ![Imagen 2][2]

&nbsp;[1]: pictures/avatar.png
&nbsp;[2]: pictures/scaphandre.png "scaphandre"</pre>
   </td>
   <td>
    <img src="/pictures/avatar.png" alt=""/>  <img src="/pictures/scaphandre.png" title="scaphandre" alt=""/>
   </td>
   </tr>
</tbody>
</table>

----

### Tablas {#mark10}

Crear tablas es sumamente sencillo, simplemente debemos indicar cuales son los 
elementos de la cabecera y separar los campos con el símbolo **|**

<table>
    <thead>
        <tr>
            <th>Tecleas</th>
            <th>Obtienes</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>
                <pre class="no_mrkdwn">
Cabecera A | Cabecera B
-- | --
Campo A0 | Campo B0
Campo A1 | Campo B1</pre>
            </td>
            <td>
                <table>
                    <thead>
                        <tr>
                            <th>Cabecera A</th>
                            <th>Cabecera B</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>Campo A0</td>
                            <td>Campo B0</td>
                        </tr>
                        <tr>
                            <td>Campo A1</td>
                            <td>Campo B1</td>
                        </tr>
                    </tbody>
                </table>
            </td>
        </tr>
    </tbody>
</table>

Si se desea, por estética, se pueden alinear las columnas e incluso comenzar y 
finalizar las filas con el símbolo **|**, pero no es en absoluto necesario.

<table>
  <thead><tr><th style="width: 50%;">Tecleas</th><th>Obtienes</th></tr></thead>
  <tbody><tr>
    <td><pre class="no_mrkdwn">
| Cabecera A | Cabecera B |
| ---------- | ---------- |
| Campo A0   | Campo B0   |
| Campo A1   | Campo B1   |
</pre></td>
     <td>
<table>
  <thead><tr><th>Cabecera A</th><th>Cabecera B</th></tr></thead>
  <tbody>
    <tr><td>Campo A0</td><td>Campo B0</td></tr>
    <tr><td>Campo A1</td><td>Campo B1</td></tr>
  </tbody>
</table>
</td>
  </tr>
</tbody></table>

Se puede especificar la alineación de cada columna mediante la adición de dos 
puntos a las líneas de separación. Dos puntos a la izquierda de la línea de 
separación hará que la columna esté alineada a la izquierda, dos puntos a la 
derecha de la línea hará que la columna esté alineada a la derecha, dos puntos 
en ambos lados significa que la columna se alinea al centro.

<table>
  <thead><tr><th style="width: 50%;">Tecleas</th><th>Obtienes</th></tr></thead>
  <tbody><tr>
    <td><pre class="no_mrkdwn">
| Elemento | Cantidad | Precio |
| :------- | :------: | -----: |
| Item 1   | 15       | 150€   |
| Item 2   | 3250     | 23,65€ |
</pre></td>
     <td>
<table>
<thead>
<tr>
  <th style="text-align:left;">Elemento</th>
  <th style="text-align:center;">Cantidad</th>
  <th style="text-align:right;">Precio</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="text-align:left;">Item 1</td>
  <td style="text-align:center;">15</td>
  <td style="text-align:right;">150€</td>
</tr>
<tr>
  <td style="text-align:left;">Item 2</td>
  <td style="text-align:center;">3250</td>
  <td style="text-align:right;">23,65€</td>
</tr>
</tbody></table>
     </td>
  </tr>
</tbody></table>

----

### Código {#mark11}

Se pueden crear bloques de código para albergar extractos de código fuente de un 
lenguaje de programación o para reproducir literalmente cualquier tipo de texto 
sin que sea interpretado por markdown. Lo único necesario es que cada línea de 
este bloque empiece por al menos 4 espacios o 1 tabulado.

**De todos modos, es mucho más recomendable para estas tareas emplear el 
resaltado de código que se especifica en [esta sección](#header2).**

<table>
  <thead><tr><th style="width: 50%;">Tecleas</th><th>Obtienes</th></tr></thead>
  <tbody><tr>
   <td>
<pre class="no_mrkdwn">
Esto es un párrafo normal.  
</pre><pre class="no_mrkdwn">
    Esto es un párrafo de código.
</pre> 
   </td>
   <td><p>Esto es un párrafo normal.</p><div class="codehilite"><pre><code>Esto es un párrafo de código.</code></pre></div>
</td>
  </tr>
</table>

Existe otro modo de crear un bloque de código, encerrándolo entre dos líneas formadas por tres o más caracteres tilde **~**

<table>
  <thead><tr><th style="width: 50%;">Tecleas</th><th>Obtienes</th></tr></thead>
  <tbody><tr>
    <td><pre class="no_mrkdwn">
Esto es un párrafo normal

~~~
Esto es un párrafo de código.
~~~</pre></td>
     <td><p>Esto es un párrafo normal.</p><div class="codehilite"><pre><code>Esto es un párrafo de código.</code></pre></div>
</td>
  </tr>
</table>

Por último existe una opción para resaltar pequeños trozos de código dentro de 
párrafos de texto normal. Para lograr esto debemos encerrar el código entre dos 
acentos graves **`**

<table>
  <thead><tr><th style="width: 50%;">Tecleas</th><th>Obtienes</th></tr></thead>
  <tbody><tr>
    <td><pre class="no_mrkdwn">
Esto es un párrafo normal, con un trozo de código, `import this` insertado en el medio del mismo.
</pre></td>
     <td><p>Esto es un párrafo normal, con un trozo de código, <code>import this</code> insertado en el medio del mismo.</p>
</td>
  </tr>
</table>

----

### Líneas Horizontales {#mark12}

Para crear líneas horizontales se debe crear una línea rodeada de líneas en 
blanco y compuesta por 3 o más símbolos, que pueden ser guiones, asteriscos o 
guiones bajos. Pueden crearse espacios entre estos caracteres si así se desea 
por estética.

<table>
  <thead><tr><th style="width: 50%;">Tecleas</th><th>Obtienes</th></tr></thead>
  <tbody><tr>
    <td><pre class="no_mrkdwn">

***

</pre></td>
     <td><hr /></td>
  </tr>
  <tr>
    <td><pre class="no_mrkdwn">

- - -

</pre></td>
     <td><hr /></td>
  </tr>
  <tr>
    <td><pre class="no_mrkdwn">

___

</pre></td>
     <td><hr /></td>
  </tr>
</table>

----

### Escapar carácteres {#mark13}

¿Que ocurre cuando queremos mostrar un carácter que markdown emplea para el 
marcado? Es posible que dependiendo de donde y como se emplee este símbolo, sea 
interpretado por markdown y nos estropee el formato del texto. En este caso lo 
que se necesita es *escapar* el carácter con el símbolo backslash **\\**
En esta tabla se muestran los símbolos que pueden ser escapados por markdown.

<table>
  <thead><tr><th style="width: 60%;">Tecleas</th><th>Obtienes</th></tr></thead>
  <tbody><tr>
    <td><pre class="no_mrkdwn">\\ \` \* \_  \{\} \[\] \(\) \# \+ \- \. \! \: \|</pre></td>
     <td><h3>\ ` * _  {} [] () # + - . ! : |</h3></td>
  </tr>
</table>

-----

### Notas a pie de página {#mark14}

Las notas de página se crean de una manera muy sencilla en Markdown. Cada nota 
de pie de página se compone de dos elementos: un marcador al lado del texto que 
se convierte en un superíndice y de una definición que se puede colocar en una 
lista de notas al pie al final de documento. Ejemplo:

<table>
  <thead><tr><th style="width: 51%;">Tecleas</th><th>Obtienes</th></tr></thead>
  <tbody><tr>
    <td><pre class="no_mrkdwn">
Esto es un texto con nota al pie [^1]

[^1]: Esto es una nota al pie de página.
</pre></td>
     <td>
<p>Esto es un texto con nota al pie <sup id="fnref:1"><a href="#fn:1" rel="footnote">1</a></sup></p>
<div class="footnotes">
<hr /><ol><li id="fn:1">
<p>Esto es una nota al pie de página. <a href="#fnref:1" rev="footnote">↩</a></p>
</li>
</ol>
</div>
</td>
  </tr>
</table>

Las definiciones de la nota al pie se pueden encontrar en cualquier parte del 
documento, pero las notas siempre se mostrarán en el orden en que están 
vinculados en el texto. Hay que tener en cuenta que no puede hacer dos enlaces a 
la misma nota al pie: si se intenta, la referencia de la nota segunda quedará 
como texto sin formato.

Cada marcador de nota debe tener un nombre distinto. Ese nombre se utiliza para 
vincular la nota a la que hace referencia a las definiciones de la nota, pero no 
tiene ningún efecto sobre la numeración de las notas al pie. Los nombres pueden 
contener cualquier carácter válido que sirva para la una Identificación de un 
atributo HTML (es decir, que cumpla con la expresión regular 
`[A-Za-z][-A-Za-z0-9_:.]*`), no tienen porque ser necesariamente números. 
Ejemplo:

<table>
  <thead><tr><th style="width: 55%;">Tecleas</th><th>Obtienes</th></tr></thead>
  <tbody><tr>
    <td><pre class="no_mrkdwn">
Esto es un texto con nota al pie [^nota1] y esta es otra nota [^nota2]

[^nota1]: Esto es una nota al pie de página.
[^nota2]: Esto es la segunda nota al pie.
</pre></td>
     <td>
<p>Esto es un texto con nota al pie <sup id="fnref:nota1"><a href="#fn:nota1" rel="footnote">1</a></sup> y esta es otra nota <sup id="fnref:nota2"><a href="#fn:nota2" rel="footnote">2</a></sup></p>

<div class="footnotes">
<hr /><ol><li id="fn:nota1">
<p>Esto es una nota al pie de página. <a href="#fnref:nota1" rev="footnote">↩</a></p>
</li>

<li id="fn:nota2">
<p>Esto es la segunda nota al pie. <a href="#fnref:nota2" rev="footnote">↩</a></p>
</li>
</ol>
</div>
</td>
  </tr>
</table>

----

### Abreviaturas {#mark15}

Para crear abreviaturas HTML lo único necesario es crear una lista de ellas 
(normalmente al final del texto) y en cualquier lugar del texto que aparezca la 
abreviatura se aplicará automáticamente. Las listas de abreviaturas se crean 
como las listas de enlaces, pero precedidas por un asterisco.

<table>
  <thead><tr><th style="width: 60%;">Tecleas</th><th>Obtienes</th></tr></thead>
  <tbody><tr>
    <td><pre class="no_mrkdwn">
La especificación HTML es mantenida por el W3C.

 *[HTML]: Hyper Text Markup Language
 *[W3C]:  World Wide Web Consortium
</pre></td>
     <td>
<p>La especificación <abbr title="Hyper Text Markup Language">HTML</abbr> es mantenida por el <abbr title="World Wide Web Consortium">W3C</abbr>.</p>
</td>
  </tr>
</table>

Las abreviaturas son sensibles a mayúsculas, por lo que hay que tenerlo en 
cuenta. Se pueden crear abreviaturas de más de una palabra.

----


### Identificadores de Cabecera {#mark16}

Los identificadores de cabecera nos permiten establecer un Identificador a las 
cabeceras para luego poder enlazarlas en cualquier otro lugar del texto. Es lo 
que empleo para crear el índice de esta página. Funcionaría como un *anchor* HTML
(ancla) pero que solo se puede aplicar en las cabeceras.

<table>
  <thead><tr><th style="width: 60%;">Tecleas</th><th>Obtienes</th></tr></thead>
  <tbody><tr>
    <td><pre class="no_mrkdwn">
### Esto es una cabecera con un Id {#cabecera1}

[Enlace a esa cabecera]{#cabecera1}
</pre></td>
     <td>

<h3 id="cabecera1">Esto es una cabecera con un Id</h3>
<p><a href="#cabecera1">Enlace a esa cabecera</a></p>
</td>
  </tr>
</table>

En Markdown Python todas las cabeceras llevan por defecto asociado un Id que 
depende del texto de la misma, aunque siempre prevalece la que nosotros 
establezcamos.

----

<br />



## Pygments: Resaltado de Sintaxis para Código Fuente  {#header2}

Para introducir ejemplos de código fuente en el sitio, habilitar el 
resaltado (o coloreado) de sintaxis mejora la presentación y legibilidad de los 
mismos. Existen diversos motores que nos permiten realizar esta función y 
Pygments es uno de los mejores. Está realizado en Python, por lo que se integra 
perfectamente con el software que genera este sitio y con python markdown. 

Resaltar código con markdown y Pygments es realmente sencillo, solamente hay que 
hacer los mismo que haríamos com markdown, pero añadiendo un **lexer** de 
Pygments en la primera línea. Un [lexer][lxr] es un identificador del lenguaje 
que queremos resaltar para que el coloreado se haga correctamente. Los lexer se 
construyen empleando 2 caracteres `:` seguidos del nombre del lexer, por ejemplo, 
`:::python` sería el lexer empleado para identificar un fragmento de código en 
lenguaje Python.

  [lxr]:http://pygments.org/docs/lexers

Lo podemos ver mejor con un ejemplo:

<table>
  <thead><tr><th style="width: 50%;">Tecleas</th><th>Obtienes</th></tr></thead>
  <tbody><tr>
   <td>
    <pre class="no_mrkdwn">
&nbsp;&nbsp;&nbsp;&nbsp;:::python
&nbsp;&nbsp;&nbsp;&nbsp;import lifetime
&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;for each_day in lifetime.days():
&nbsp;&nbsp;&nbsp;&nbsp;    carpe_diem()</pre>
  </td>
  <td>
<div class="codehilite"><pre><span class="kn">import</span> <span class="nn">lifetime</span>

<span class="k">for</span> <span class="n">each_day</span> <span class="ow">in</span> <span class="n">lifetime</span><span class="o">.</span><span class="n">days</span><span class="p">():</span>
    <span class="n">carpe_diem</span><span class="p">()</span>
</pre></div>
  </td>
  </tr>
</tbody></table>


## Lexers de Pygments más comunes para resaltado de sintaxis {#syntax0}

A continuación muestro una relación de los lexers más comunes empleados para el 
resaltado de código fuente.


* #### `apache` - configuración Apache

        :::apache
        <VirtualHost *:80>
        DocumentRoot /www/example1
        ServerName www.example1.com

        # Other directives here

        </VirtualHost>


* #### `bash` y  `console` - Bash y Shell

        :::bash
         #!/bin/bash
         echo "Hola mundo"

* #### `bat` - Fichero Batch DOS/Windows

        :::bat
        @echo ¡Hola, Mundo!
    
* #### `boo` - Boo

        :::boo
        print "Hello, world!"
    

* #### `c` - C

        :::c
        #include <stdio.h>

        int main()
        {
            printf("¡Hola, mundo!\n");
            return 0;
        }


* #### `cpp` - C++

        :::cpp
        #include <iostream.h>
        using namespace std;

        int main() {
          cout << "¡Hola, mundo!" << endl;
          return 0;
        }


* #### `csharp` - C#

        :::csharp
        using System;

        class MainClass
        {
            public static void Main()
            {
                System.Console.WriteLine("¡Hola, mundo!");
            }
        }


* #### `css` - Cascade Style Sheet (CSS)

        :::css
        </pre>
           </td>
           <td class="get">
        <css>
        body {
            font: 75% georgia, sans-serif;
            color: #555753;
            background: #fff;
            margin: 0;
            padding: 5px;
        }


* #### `diff` ó  `udiff` - Diff

        :::diff
        --- /path/to/original ''timestamp''
        +++ /path/to/new      ''timestamp''
        @@ -1,3 +1,9 @@
        +This is an important
        +notice! It should
        +therefore be located at
        +the beginning of this
        +document!
        +
         This part of the
         document has stayed the
         same from version to

* #### `erlang` - Erlang

        :::erlang
        -module (hola).
        -export([hola_mundo/0]).

        hola_mundo() -> io:fwrite("Hola mundo!\n").


* #### `go` - Go

        :::go
        package main
         
        import "fmt"
         
        func main() {
           fmt.Println("Hello World!")
        }    

* #### `haskell` - Haskell

        :::haskell
        holaMundo :: IO ()
        holaMundo = putStrLn "Hola mundo!"


* ####  `html` - HTML

        :::html
        <html>
          <head>
            <title>Hola Mundo</title>
          </head>
          <body>

        ¡Hola Mundo!
           </body>
        </html>


* #### `java` - Java

        :::java
        public class HolaMundo {
               public static void main(String[] args) {
                  System.out.println("¡Hola, mundo!");
               }
        }


* #### `js` - javascript

        :::js
        <script type="text/javascript">
          document.write("¡Hola, mundo!");
        </script>


* #### `latex` - LaTeX

        :::latex
        \documentclass[12pt]{article}
        \usepackage{lingmacros}
        \usepackage{tree-dvips}
        \begin{document}

        \section*{Notes for My Paper}


* #### `lisp` - Lisp

        :::lisp
        (format t "¡Hola, mundo!")


* #### `lua` - Lua

        :::lua
        print("¡Hola, Mundo!\n")


* #### `mysql` - MySQL

        :::mysql
        SELECT 'HOLA MUNDO';


* #### `pascal` y  `delphi` - Pascal y Delphi

        :::pascal
        Program HolaMundo;
        Begin
            Write('¡Hola, Mundo!');
        End.


* #### `perl` - Perl

        :::perl
        print "Hola, mundo\n"


* #### `php` - PHP

        :::php
        <?php print "Hola Mundo!"; ?>


* #### `python` ó  `py` ó  `pycon` ó  `pytb` ó  `python3` ó  `cython` - Python

        :::python
        print "¡Hola Mundo!"


* #### `ruby` - Ruby

        :::ruby
        puts "Hola Mundo"

* #### `scala` - Scala

        :::scala
        object HelloWorld extends Application {
          println("Hello world!")
        }

* #### `scheme` -  Scheme

        :::scheme
        (display "Hello World")

* #### `smalltalk` - Smalltalk

        :::smalltalk
        Transcript show: '¡Hola, mundo!'


* #### `sql` - SQL

        :::sql
        SELECT 'HOLA MUNDO'
        FROM DUAL;

* #### `sqlite3` - sqlite3

        :::sqlite3
        sqlite> CREATE TABLE tbl2 (
           ...>   f1 varchar(30) primary key,
           ...>   f2 text,
           ...>   f3 real
           ...> );
        sqlite>

* #### `text` - Texto simple monoespaciado

        :::text
        Hola Mundo

* #### `vala` - Vala

        :::vala
        class Demo.HelloWorld : GLib.Object {
            public static int main(string[] args) {
                stdout.printf("Hello, World\n");
                return 0;
            }
        }

* #### `vbnet` - Visual Basic .NET

        :::vbnet
        Private Sub Form_Load()
           Msgbox "Hola Mundo"
         End Sub


* #### `vim` - Vim Script

        :::vim
        function! ToggleSyntax()
           if exists("g:syntax_on")
              syntax off
           else
              syntax enable
           endif
        endfunction

        nmap <silent>  ;s  :call ToggleSyntax()<CR>


* #### `xml` - XML

        :::xml
        <?xml version="1.0" encoding="ISO-8859-1"?>
         - <note>
               <to>Tove</to>
               <from>Jani</from>
               <heading>Reminder</heading>
               <body>Don't forget me this weekend!</body>
           </note>


