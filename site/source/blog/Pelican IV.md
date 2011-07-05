title: Pelican - Configuración y personalización
date: 2011-06-30 01:21
tags: Pelican, python, markdown, reStructuredText, blog, HMTL, CSS, jinja2

Con este articulo cierro la serie que le he dedicado a [Pelican][0] como 
herramienta idónea para crear blogs estáticos con mantenimiento cero. Aquí voy a 
tratar de la parte más compleja de Pelican, la que nos permite personalizarlo y 
adaptarlo a nuestros gustos y necesidades. El primer nivel de personalización se 
obtiene a través del fichero de configuración (aunque no es necesario, es 
recomendable emplearlo). El segundo nivel vendría mediante la personalización del 
tema empleado, bien creando uno nuevo o bien modificando el que viene por 
defecto. El último nivel vendría de modificar el propio Pelican. Todos son 
posibles y están a nuestro alcance, gracias a que es Software Libre. 

  [0]: /tag/Pelican.html
  
Si bien yo he personalizado mi sitio con respecto al sitio por defecto, y aún 
quedan ciertas cosas que aún quiero cambiar, no he necesitado de momento más que 
modificar el fichero de configuración y el tema que viene por defecto. En 
Pelican no he tocado nada exceptuando el activar por defecto **Markdown Extra**, 
algo que Alexis tuvo como gentileza [aceptar como modificación][1] a Pelican. Es 
posible que en el futuro algunas de las cosas que tengo en mente me lleven a 
modificarlo, y espero poder así contribuir en alguna medida a su desarrollo. 

  [1]: https://github.com/ametaireau/pelican/pull/138

### Configuración

La configuración se hace a través de un fichero python, que en el ejemplo por 
defecto se llama `pelican.conf.py` y en nuestro ejemplo estaría en 
*myblog.com/site/pelican.conf.py*. Para llamar al fichero de configuración se 
utiliza la opción `-s` y en nuestro ejemplo sería:

    ::console
    $ pelican -s ./site/pelican.conf.py
    
  [2]: http://docs.notmyidea.org/alexis/pelican/settings.html

Este es un tema que está muy bien resuelto en la [documentación][2]. De todos 
modos voy a hablar de unos cuantos campos interesantes y alguno no incluido 
dentro de la documentación. Entre paréntesis indico los valores por defecto.
  
* **OUTPUT_PATH** (`'output/'`) y **PATH** (`None`)

    Empleando estos dos valores, conseguimos que solo tengamos que especificar el 
    fichero de configuración en la linea de comandos empleada para llamar a Pelican.
    El primero define el directorio de salida donde queremos que se genere nuestro 
    sitio y el segundo el directorio origen de nuestro contenido. 

* **SITESUBTITLE** (`u''`)

    Un subtitulo que se puede poner al blog, e.g. un lema. No aparece documentado.

* **JINJA_EXTENSIONS** (`[]`)

    Puede ser necesario habilitar ciertas extensiones de Jinja2 para personalizar 
    el tema que vamos a emplear. Por ejemplo, para mostrar la nube de etiquetas 
    con las etiquetas ordenadas alfabéticamente, he habilitado una extensión que 
    necesitaba para el proceso de esta manera:
    
        ::python
        JINJA_EXTENSIONS = ['jinja2.ext.do']

* **STATIC_PATHS** (`['images',]`)

    Te permite especificar los contenidos estáticos que quieres añadir a tu blog 
    y que acabaran colgando de la carpeta *static*. Yo por ejemplo lo empleo 
    para alojar las imágenes en *static/pictures* y el mapa flash que utilizo en 
    el articulo [Combatir el spam en Drupal][4] en *static/ammap* así:
    
        ::python
        STATIC_PATHS = ["pictures", "ammap", ]

  [4]: /combatir-el-spam-en-drupal.html

* **TAG_FEED** (`None`) y **TAG_FEED_RSS** (`None`)

    Te permiten establecer fuentes Atom y RSS por etiqueta, que es una opción 
    muy interesante para quienes solo les interesa un tema de los que trates o 
    para formar parte de un [Planet][3] sin mezclar temas. Eso si, lo lógico es 
    modificar luego el tema para que aparezcan disponibles. 

  [3]: http://es.wikipedia.org/wiki/Planeta_%28agregador%29

* **DIRECT_TEMPLATES** (`('index', 'tags', 'categories', 'archives')`)

    Estas son las plantillas del tema que generan una página por si mismas. No 
    viene documentada, pero yo he cambiado los valores por defecto para añadir 
    una página personalizada a la que redirijo los errores 404 (Página no 
    encontrada) de esta manera:
    
        ::python
        DIRECT_TEMPLATES = ('index', 'tags', 'categories', 'archives', 'notfound')
      
* **PIWIK_URL** y **PIWIK_SITE_ID**

    Te permiten configurar tu sitio para emplear el magnifico sistema de 
    analíticas web [Piwik][5]. Yo hace unos dos años que lo empleo en mis sitios, 
    porque tiene la ventaja de que no dependes de un script de un dominio externo. 
    Esto te ahorra consultas DNS y que la página se quede esperando a cargar 
    completamente cuando estos fallan. De esta manera tienes el control total 
    sobre las estadísticas de tu web sin tener que renunciar a la calidad de 
    otros servicios externos.
 
  [5]: http://piwik.org/
  
* **FILES_TO_COPY** (`()`)

    Básica si queremos emplear ficheros como *.htaccess* o *robots.txt*. No está 
    documentada tampoco. El uso de la misma consiste en una tupla de tuplas con 
    los valores de las rutas del fichero origen y su destino. En este sitio por 
    ejemplo:
    
        ::python
        FILES_TO_COPY = (('extra/robots.txt', 'robots.txt'),
                         ('extra/favicon.ico', 'favicon.ico'),
                         ('extra/.htaccess', '.htaccess'),)
  
### Personalización


Pero si realmente queremos personalizar el sitio, tanto en funcionalidad básica 
como en su aspecto, nos toca modificar el tema por defecto. Aquí podemos optar por 
tres vías: Crear el nuestro propio, empezar un tema casi desde cero, 
eligiendo el tema por defecto `simple` (solo texto) o partir de la base del tema 
por defecto `notmyidea`. Este último es el que hemos estado empleado en nuestro 
ejemplo y el que yo modifiqué hasta llegar donde lo tengo ahora. 

Para comprender de que consta un tema y como podemos personalizarlo, lo mejor es 
analizar el tema `notmyidea`.

    ::console
    notmyidea/
    ├── static
    │   ├── css
    │   │   ├── main.css
    │   │   ├── pygment.css
    │   │   ├── reset.css
    │   │   └── wide.css
    │   └── images
    │       └── icons
    │           ├── delicious.png
    │           ├── lastfm.png
    │           ├── linkedin.png
    │           ├── rss.png
    │           └── twitter.png
    └── templates
        ├── analytics.html
        ├── archives.html
        ├── article.html
        ├── article_infos.html
        ├── base.html
        ├── categories.html
        ├── category.html
        ├── comments.html
        ├── disqus_script.html
        ├── github.html
        ├── index.html
        ├── page.html
        ├── pagination.html
        ├── piwik.html
        ├── skribit_tab_script.html
        ├── skribit_widget_script.html
        ├── tag.html
        ├── taglist.html
        ├── tags.html
        ├── translations.html
        └── twitter.html


* ***static/css***

    Aquí es donde se guardan las [Hojas de estilo en cascada (CSS)][6] que emplea el 
    tema. Aunque la el fichero *wide.css* no es empleado por el tema, solo para la 
    versión wide del mismo. Yo la eliminé como primera medida. Luego tenemos 
    *main.css* que es la hoja de estilo principal, *pygment.css* que es la que emplea 
    Pygments para el resaltado de sintaxis y *reset.css* para resetear los navegadores 
    a unos valores comunes por defecto. 

  [6]: http://es.wikipedia.org/wiki/CSS
 
    Si lo que queremos es tener un sitio con un buen rendimiento, deberíamos dar 
    como mínimo dos pasos, consolidar todas la hojas de estilo en una sola y 
    minimizar el tamaño de esta. Consolidarla en este caso es realmente sencillo, 
    simplemente debemos insertar el contenido de *reset.css* al principio del 
    fichero *main.css* y *pygment.css* al final del mismo. Depués hay que 
    eliminar los imports de estas hojas en *main.css**. Luego para minimizar 
    su tamaño eliminar comentarios y lineas en blanco y poner una regla por línea. 
    
    Otro paso que dí para mejorar el rendimiento es no usar las web fonts 
    externas (ni internas), que aunque le dan un aspecto inmejorable, hay que 
    reconocerlo, requieren cargar otro recurso externo, desde mi punto de vista 
    innecesario.
    
    Lo mejor en estos casos es seguir siempre las recomendaciones de estas dos 
    magnificas herramientas: [YSlow][7] de **Yahoo** y [Page Speed][8] de 
    **Google**. Afortunadamente hay sitios web como [GTmetrix][9] o 
    [WebPagetest][10] que nos permiten ver los resultados de ambas herramientas 
    en nuestro sitio web sin necesidad de instalarlas (aunque para el desarrollo 
    es más que recomendable). Si por ejemplo emplearamos **GTmetrix** los valores 
    que arroja un sitio con el tema por defecto son:
    
    | Page Speed (tema por defecto) | YSlow (tema por defecto) |
    | --------- | ----------- |
    | **B (80%)** | **B (85%)** |
     
    Valores bastante mejorables. Los valores actuales para este sitio, una vez 
    personalizado el tema y configurado correctamente el *.htaccess* son:
    
    | Page Speed (tema personalizado) | YSlow (tema personalizado) |
    | --------- | ----------- |
    | **A (91%)** | **A (95%)** |
       
    Y si nos fijamos en [los resultados][11], las penalizaciones de rendimiento 
    vienen de los scrips externos de Piwik y Disqus, principalmente de este 
    último. Sin emplear estos scripts los valores suben a:
    
    | Page Speed (sin scripts) | YSlow (sin scripts) |
    | --------- | ----------- |
    | **A (100%)** | **A (98%)** |
    
    En resumen, una optimización más que correcta, solo hay que ver los valores 
    de las páginas del Top 1000 que ofrecen en GTmetrix. Obtener una optimización 
    como esta con un CMS no es imposible (había conseguido unos valores solo un 
    poquito peores con Drupal) pero si bastante más complicado. La experiencia 
    del usuario depende mucho de estos valores, hay que contar con que no todo 
    el mundo dispone de buenos accesos a Internet.
    
  [7]: http://developer.yahoo.com/yslow/
  [8]: http://code.google.com/speed/page-speed/
  [9]: http://gtmetrix.com/
  [10]: http://www.webpagetest.org/
  [11]: http://gtmetrix.com/reports/joedicastro.com/BeFSzvAa
  
  
    Evidentemente, después cada uno retocara el fichero CSS resultante a su 
    gusto para personalizar el aspecto del sitio. En este caso estoy empleando
    CSS 3 y valida correctamente. 

<p style="text-align:center;">
    <a href="http://jigsaw.w3.org/css-validator/validator?uri=http%3A%2F%2Fjoedicastro.com%2F&amp;profile=css3&amp;usermedium=all&amp;warning=1&amp;vextwarning=&amp;lang=es">
        <img style="border:0;width:88px;height:31px"
            src="pictures/valid-css3.png"
            alt="¡CSS 3 Válido!" title="¡CSS 3 Válido!" />
    </a>
</p>

* **static/images/icons**

    Son los iconos empleados por la hoja de estilo para los enlaces sociales de 
    la parte inferior de la página. Yo no los empleo. ¿Entonces como se ven? 
    Bueno lo primero que hice fue crear un [sprite][12] para cargar una sola 
    imagen en lugar de 6, es decir menos solicitudes al servidor. Después 
    incorporé esta imagen [dentro del propio fichero CSS con un Data URL][13], y 
    gracias a haberla optimizado hasta ocupar solamente ~3k, me compensaba 
    hacerlo. Una consulta menos al servidor. Lo mismo hice después con el 
    logotipo (1K) y al final no se carga ninguna imagen por defecto en el blog, 
    0 consultas. Los navegadores modernos soportan esto sin problemas, los que 
    no lo hacen, no muestran la imagen, solo el enlace, que tampoco es un ningún 
    problema.
    
  [12]: http://www.w3schools.com/css/css_image_sprites.asp
  [13]: http://www.websiteoptimization.com/speed/tweak/inline-images/

    Así es como queda en *main.css* la imagen que da vida a los iconos de los 
    enlaces a la redes sociales:
    
        ::css
        #extras div[class='social'] a{background-repeat:no-repeat;background-image:url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAACSCAMAAAB7VbqAAAAAwFBMVEWQBQCWFxU5VpedVy+tUE5LZaBPZZZDabDdYSpke75vfZBkfbJZgc+heztshKvldjBgld91j9+Uj4p5ksZ/lLzthzLqhz+MmrAcvuaDofihpYRzq/D4mDeUp9KetkSirsnQpKWpvV/qqHvHsJjnqY/3qWK1ubbIun2jwLHEu7xm1O+6xoOtv++7wte0yNzxwH563e/3xJjK06ya5vXY3p7U2+3e3tbm6IT63cLn7czr7fbZ9Prz7+r8+O/3+fb9//z6WVfkAAADNElEQVRIx9WV4XqiPBCFoyu4aVjQBrW2ImBX3aJYdQERIbn/u9qTRKzd7/n+b88jxHlnMswEY4hIGYUcLZYKklLbtixqNBymhNl2yG/2lBFqu1LKKjD2dEioxfIKKOfaVgA+HkoptsoGoDxPA8orKZTtEIdyNWE4zXEbUgVokAq4p1JuqQHIX8G9lYK2EdOpkNuhlJxec+TTrcxpJVENAOK3iK9oLkOLEmbqGQZ4dMAtRlJj617QZErQvqpHiVLVvvhL/y6oFx40HhktaqJt9X2mtSDwHg7L1p6NAJZY9eZwB8aHsgF61zaAnr8spXxX9piMR8umxAQQZBp5ZDTSOZYgzXjkKTCbvTeKNPLgKaCTK/dCNldQlu9wL0aNHH9XADnK2UGWXil/GoDJyFx6P69gNlPPWy698cIDWOj68DzvO+Qt0D7MsXcV2v86by55+qSEPP3+pKf/ARfxF5Dy8gH2+/0N7Pc3oCUMSJIWyESBRANxgX4nyQ1cEiMDEkR8BheT4jYl2bdJW5DsdczlA9z09N/2v86bw1Vs4vl8c6xbcI7ncQxkCBFFPM8a0QAfDTjOM70453lc630bx2ezXJt5oUARx40BmQF3EfFroXJs5gaU30inF+G3vombBnuu7JFer9OJ1JQMZcQ/SK8WEekRVRYqjb+RSMq60yHF8VzXRVHAWUsV0TZVIEekctzafEPKTnS/o+qog7z361FHkfhK/5ZV0MrnPAgqEvBWYZoGPCSt6aujLGScuC5j+LAdNkAVALCrUuVndwARvhoJs3C3WSXUFB8HjtW1LFxCvz3WtQC03Bw5fOsDdEPl794BPMW9Ap3DAMuyCc5nJQ2sO2AB+BgYCU1dCkwwhjjnfNUO8ycTl/lf6pxTtzzfQXl1BduXAQ5/7jiDl50CgcMnq6Ku69WEOQHAgD8+Pq5WbysMLle78tdq8jDR4oMc4HzKsuPuBRoMLKHB6+spG2hgrwCydQZpQH0NTmsgB/4BTVe1AphyNCBXoMk2p9MvB7bT1xEitB+eFXCch3WhSl/Z/T6dcMddr581KAD6fdd9fnyoTbdvrN93+v2uXbTt17sQyvV6/AE7UZJYs2UOngAAAABJRU5ErkJggg==");padding-left:25px;}
        .social a[href*='atom.xml']{background-position:3px 6px;}
        .social a[href*='rss.xml']{background-position:3px -20px;}
        .social a[href*='twitter.com']{background-position:3px -46px;}
        .social a[href*='identi.ca']{background-position:3px -72px;}
        .social a[href*='facebook.com']{background-position:3px -98px;}
        .social a[href*='bitbucket.org']{background-position:3px -124px;}


* **static/templates**

    Estas son las plantillas que dan vida al tema y emplean Jinja2. Los nombres 
    son bastante descriptivos de la función que realiza cada una de ellas. En mi 
    caso hay una serie de ellas que no empleo, como son: *analytics.html*, 
    *article_infos.html*, *github.html*, *skribit_tab_script.html*, 
    *skribit_widget_script.html*, *translations.html* y *twitter.html*. He 
    realizado bastantes modificaciones en las plantillas y me extendería demasiado 
    explicándolo, además sigo realizando cambios. Aún no lo tengo todo como yo 
    lo quiero, y aún voy a personalizar y optimizar más cosas. Cuando lo tenga 
    todo listo, pienso publicar un repositorio con el contenido que genera este 
    blog, tanto a efectos de copia de seguridad, como de que le pueda servir a 
    alguien como guía para montar el suyo propio. 
    
    De todos modos si puedo decir que he añadido una que no existía, 
    *notfound.html* para los errores 404 y pienso crear una nueva para los 
    errores 403. Además he creado los enlaces para los feeds RSS y Atom de las 
    etiquetas y eliminado el bloque de información que aparecía en cada articulo.
    Además en la plantilla *tags.html* que por defecto viene vacía, he creado lo 
    necesario para generar la nube de etiquetas. *tags.html* queda entonces así:
    
        ::jinja2
        {% extends "base.html" %}
        {% block content %}
        <section id="content" class="body">
        <h1>etiquetas</h1>
          <ul id="cloud">
	        {%- set all_tags = {} -%}
	        {% for ctag in tag_cloud -%}
              {% do all_tags.update({ctag.0:ctag.1}) %}
            {%- endfor %}
            {% for tag in all_tags|sort %}
              <li class="tag-{{ all_tags[tag] }}"><a href="tag/{{ tag|replace(" ", "%20") }}.html">{{ tag }}</a></li>
            {% endfor %}
          </ul>
        </section>
        {% endblock %}

    También he realizado las modificaciones pertinentes para que el contenido 
    validara perfectamente en HTML 5. 
    
<p style="text-align:center;">
    <a href="http://validator.w3.org/check?uri=http%3A%2F%2Fjoedicastro.com%2F">
        <img style="border:0;width:88px;height:31px"
            src="pictures/valid-html5.png"
            alt="¡HTML 5 Válido!" title="¡HTML 5 Válido!" />
    </a>
</p>

Pero como ya he dicho es un proceso que aún no he finalizado. Cuando lo 
termine y publique el repositorio, actualizaré también este articulo.
