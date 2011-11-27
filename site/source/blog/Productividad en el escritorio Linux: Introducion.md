title: Productividad en el escritorio Linux: Introducción
date: 2011-11-24
tags: linux, unity, gnome, kde, productividad, desktop

En el último lustro se ha producido una renovación en el [escritorio Linux]
[el] buscando innovar, mejorar su funcionamiento, equiparlo a las evoluciones de 
otros SOs (Mac OS X) y porque no, intentar acercar a más usuarios al mundo linux. 

Quizá la primera innovación importante fue el gestor de ventanas [Compiz][compiz] 
en el 2006 que tuvo una elevada repercusión en su momento por lo novedoso y lo 
espectacular de sus efectos 3D empleando OpenGL. También ese mismo año hacia su 
aparición [LXDE][lxde], un entorno de escritorio ligero y rápido que supone un 
paso adelante dentro de las opciones poco ávidas de recursos. Luego dos años más 
tarde, [KDE][kde] decide renovarse por completo con un nuevo diseño y nueva 
tecnología, convirtiéndose en el escritorio más avanzado del momento. Y este año 
[Gnome][gnome] ha presentado también un gran cambio, no tan radical a nivel 
tecnologico como el de KDE, pero si presentando un cambio de paradigma con su 
[Gnome Shell][gshell], aún algo inmaduro. [Ubuntu][ubuntu] se ha desmarcado de 
gnome creando su propia alternativa empleando su propio Shell, [Unity][unity], 
con un enfoque parecido.

  [el]: http://es.wikipedia.org/wiki/Escritorio_Linux
  [compiz]: http://es.wikipedia.org/wiki/Compiz
  [lxde]: http://es.wikipedia.org/wiki/LXDE
  [kde]: http://es.wikipedia.org/wiki/KDE
  [gnome]: http://es.wikipedia.org/wiki/GNOME
  [gshell]: http://es.wikipedia.org/wiki/GNOME_Shell
  [ubuntu]: http://es.wikipedia.org/wiki/Ubuntu
  [unity]: http://es.wikipedia.org/wiki/Unity_%28entorno_de_escritorio%29
  
Todos estos cambios han traído avances tanto en el diseño como en la 
espectacularidad del escritorio linux, no teniendo nada que envidiarle en diseño 
ni usabilidad a la referencia tradicional en este campo, Mac OS X. Bien, ahora 
tenemos unos entornos de escritorio elegantes, completos y amigables, y cada vez 
más orientados al usuario final. De hecho, se ha evolucionado tanto en este 
sentido, que hemos pasado del tópico de que Linux era solo para expertos frente 
a una linea de comandos, a la situación actual en la que probablemente sea el 
escritorio más amigable y con menor curva de aprendizaje (para aquel que se 
inicia y nunca haya tenido contacto previo con un ordenador). 

## ¿Se ha mejorado la productividad?

¿Pero que ocurre con los profesionales? ¿En que ha mejorado para ellos? Y cuando 
hablo de profesionales me refiero a todos aquellos que pasan la mayor parte de 
su jornada delante de la pantalla de un ordenador. ¿Que han aportado todos estos 
cambios a la productividad de estos usuarios, a su trabajo diario? Personalmente 
opino que estos cambios no han aportado absolutamente nada, puede que incluso 
hayan supuesto un paso atrás en algunos casos. Personalmente, **Unity** me 
parece una broma de mal gusto, está bien que se piense en los usuarios domésticos 
(aquellos que principalmente hacen uso de internet y multimedia), pero por favor, 
el resto no merecemos ser tratados como idiotas. Y Gnome Shell, bueno, dentro de 
lo malo, tiene la excusa de ser aún un desarrollo muy temprano, y aparenta ser 
más prometedor.

Desde mi punto de vista, los dos grandes avances en productividad en el 
escritorio linux que se han producido en los últimos años, provienen de dos 
ideas que han tenido un éxito muy dispar, pero que tienen en común estar 
basados en proyectos muy pequeños lejos de la repercusión de los grandes 
entornos de escritorio. Estas dos ideas son los **Lanzadores de aplicaciones** y
 los **Gestores de ventanas de mosaico**

## Lanzadores de aplicaciones.

Es una idea genial, *lanzar aplicaciones a partir de su nombre*, simple y 
rápido. Antes de nada, dejar claro que el ratón es enemigo de la productividad, 
cualquiera con la suficiente experiencia sabe que realizar acciones a través del 
teclado es más efectivo que realizar las mismas a través del ratón. Alguien que 
conozca los atajos de teclado de una aplicación realizara el mismo trabajo en 
menos tiempo que otro que deba emplear el ratón para todo. Y el uso del ratón es 
además el principal causante del [Sindrome del túnel carpiano][STC] entre los 
informáticos, y los que lo hemos sufrido -en mayor o menor medida- sabemos que 
no es ninguna broma. De hecho aunque los [docks][docks] son visualmente más 
atractivos y repletos de llamativos iconos, no son tan eficientes como los 
lanzadores cuando manejamos un buen número de distintas aplicaciones.

  [STC]: http://es.wikipedia.org/wiki/S%C3%ADndrome_del_t%C3%BAnel_carpiano
  [docks]: http://es.wikipedia.org/wiki/Dock

La idea del lanzador de aplicaciones proviene de la aplicación [Quicksilver][QS] 
desarrollada en 2006 para el SO de Apple. Dos años después aparecería la primera 
aplicación similar para linux, **Gnome Do**. Estas aplicaciones han tenido un 
gran éxito y son de sobra conocidas, por lo que no voy a profundizar más en
ellas, simplemente apuntar que gracias a los plugins realizan bastantes más 
tareas que lanzar aplicaciones. Actualmente para linux hay disponibles los 
siguientes lanzadores de aplicaciones:

* [Gnome Do][Do], programado en Mono, es probablemente el mejor lanzador 
disponible hoy día. Es muy rápido y con gran cantidad de plugins. 
* [Synapse][Synapse], programado en Vala. Es una buena alternativa a Do, 
rapidísimo y muy ligero.
* [Launchy][Launchy], es multiplataforma y está escrito en C++. Más popular en 
sistemas Windows que en Linux.
* [Katapult][Katapult], es un lanzador pensado para KDE. Escrito en C++
* [Gnome Pie][Pie], a medio camino entre un lanzador y un dock. Más espectacular 
que eficaz, escrito en Vala.
* [Kupfer][Kupfer], la última incorporación notable. Escrito en Python. Es el 
que empleo actualmente. Completo, rápido, ligero y no requiere de un 
[composition manager][cm] para funcionar correctamente.


  [QS]: http://es.wikipedia.org/wiki/Quicksilver_%28software%29
  [Do]: http://do.davebsd.com/
  [Synapse]: https://launchpad.net/synapse-project
  [Launchy]: http://www.launchy.net/
  [Katapult]: http://katapult.kde.org/
  [Pie]: http://www.simonschneegans.de/?page_id=12
  [Kupfer]: http://kaizer.se/wiki/kupfer/
  [cm]: http://es.wikipedia.org/wiki/Gestor_de_composici%C3%B3n_de_ventanas
  
  
  
Tal es el éxito que han tenido estas aplicaciones que tanto Gnome 3 como Unity 
lo incluyen como pilar básico en sus Shells (combinado con un dock) y KDE 4 
integra una aplicación similar denominada **KRunner**.


### Gestores de ventanas de mosaico.

Merecen un [articulo aparte][twm] para hablar de ellos.

  [twm]: http://joedicastro.com/productividad-en-el-escritorio-linux-twm.html
    



