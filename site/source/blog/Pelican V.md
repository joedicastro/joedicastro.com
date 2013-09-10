title: Pelican - Repositorio
date: 2011-07-05 23:02
tags:  pelican, python, markdown, restructuredtext, blog, mercurial, hg


Como complemento a la [serie de artículos][0] que he publicado sobre [Pelican][1], 
el software que genera este blog, añado el repositorio, [como había prometido][2], 
del contenido del mismo. El repositorio empleaba el sistema de control de
versiones [Mercurial][3] y estába alojado en [Bitbucket][4].

  [0]: http://joedicastro.com/tag/pelican.html
  [1]: http://docs.notmyidea.org/alexis/pelican/
  [2]: http://joedicastro.com/pelican-configuracion-y-personalizacion.html
  [3]: http://mercurial.selenic.com/
  [4]: https://bitbucket.org/
  
Las ventajas de disponer del contenido del blog en un repositorio son las de 
poder enmendar un error con suma facilidad y en muy poco tiempo, además de la de 
poder trabajar con distintas versiones del mismo (pruebas y producción). Además 
el repositorio en Bitbucket me proporcionaba una copia de seguridad adicional del 
sitio sin esfuerzo alguno. Y si alguien está interesado en crear su propio blog 
con Pelican y quiere saber como he realizado el mio, ahí tiene las claves. Salvo 
el propio Pelican (que no tendría mucho sentido) todo el material empleado para 
generarlo está en el. Y disponiendo del fichero **fabric**, se pueden descargar 
Pelican e instalar el entorno virtual en un minuto. 

Para automatizar todas las tareas, incluso las más comunes del repositorio, he 
añadido al fichero fabric *fabfile.py* dos tareas más:

    :::python
    def commit(message):
        """Make a commit to the local mercurial repository."""
        local("hg add")
        local("hg commit -m '{0}'".format(message))

    def push():
        """Make a push to the remote mercurial repository."""
        local("hg push ssh://hg@bitbucket.org/joedicastro/joedicastro.com")

Con estas puedo hacer un `commit` y un `push` a Bitbucket en un solo paso, por 
ejemplo:

    :::console
    fab commit:"Añadido articulo: Pelican - Repositorio" push
    
    
También he cambiado la página que generaba los archivos del blog, ya que no me 
gustaba el formato anterior: una fecha, un articulo. He pasado de esto:

    :::jinja
    {% extends "base.html" %}
    {% block content %}
    <section id="content" class="body">
    <h1>Archivos de {{ SITENAME }}</h1>

    <dl>
    {% for article in dates %}
        <dt>{{ article.locale_date }}</dt>
        <dd><a href='{{ article.url }}'>{{ article.title }}</a></dd>
    {% endfor %}
    </dl>
    </section>
    {% endblock %}

a esto:

    :::jinja
    {% extends "base.html" %}
    {% block content %}
    <section id="content" class="body">
    <h1>Archivos de {{ SITENAME }}</h1>
    {%- set years_month = {} -%}
    {%- set months = {1:'Enero', 2:'Febrero', 3:'Marzo', 4:'Abril', 5:'Mayo', 
				      6:'Junio', 7:'Julio', 8:'Agosto', 9:'Septiembre', 
				      10:'Octubre', 11:'Noviembre', 12:'Diciembre'} -%} 
    {%- for article in dates -%}
      {%- if article.date.year not in years_month -%}
        {%- do years_month.update({article.date.year:[article.date.month]}) -%}
      {%- else -%}
      	{%- if article.date.month not in years_month[article.date.year] -%}	
	      {%- do years_month[article.date.year].append(article.date.month) -%}
        {%- endif -%}
      {%- endif -%}
    {%- endfor %}

    {% for year in years_month|sort(reverse=True) -%}
      <h2 class="year">{{ year }}</h2><dl>	
      {% for month in years_month[year] -%}
        <dt class="month">{{ months[month] }}</dt>
        {% for article in dates -%}
          {% if article.date.year == year and article.date.month == month -%}
      	    <dd><span class="day">{{ article.locale_date.split()[1] }}</span>  <a href='{{ article.url }}'>{{ article.title }}</a></dd>
      	  {%- endif %}
        {%- endfor %}
      {% endfor %}</dl>
    {% endfor %}
    </section>
    {% endblock %}

Donde los artículos están archivados por año, mes y día, con un formato que 
personalmente me agrada bastante más.

El repositorio de este blog se puede encontrar en [github][gh].

  [gh]: http://github.com/joedicastro/joedicastro.com

