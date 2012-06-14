title: Productividad & Linux: Aplicaciones
date: 2012-06-07 22:40
tags: linux, productividad, usabilidad

En la anterior serie de artículos sobre [Productividad en el escritorio
Linux][pro], hacia referencia a los lanzadores de aplicaciones y a los gestores
de ventanas de mosaico como elementos diferenciadores a la hora de ser más
productivos. Aunque la productividad en el escritorio es fundamental para
trabajar de forma más eficiente, son las aplicaciones que empleamos, las que en
último lugar, determinaran la realidad de nuestro día a día frente a la
pantalla.

Gran parte de las aplicaciones para Linux (las más conocidas y extendidas) son
realmente una adaptación de los conceptos de los sistemas operativos más
difundidos: Windows & Mac OS. Esto es, aplicaciones muy pesadas, repletas de
opciones y funciones de las que se aprovechan en realidad muy pocas.  Además
están por lo general fuertemente orientadas al empleo del ratón y muchas veces
con un interfaz gráfico muy agradable visualmente pero con un concepto de
usabilidad, en mi opinión, no siempre bien enfocado.

  [pro]: http://joedicastro.com/productividad-en-el-escritorio-linux-introduccion.html

## La usabilidad mal entendida, como enemiga de la productividad

La [usabilidad][fordummies], ese concepto tan de moda últimamente, está desde mi
punto de vista, frecuentemente muy mal enfocado. Dejando a un lado lo que
teóricamente se pretende, en el 80% de las ocasiones esto se traduce en la
práctica en dos palabras en ingles: *For dummies*  ("pá tontos", en castizo). Es
decir, que cualquiera pueda manejar la aplicación sin grandes dificultades y en
el menor tiempo posible. Reducir las barreras de entrada está muy bien, pero
desgraciadamente muchas veces esto es una estrategia a corto plazo que no
debería emplearse __NUNCA de este modo__ en aplicaciones profesionales.
Entiendo, y además apoyo, está estrategia en aplicaciones web y aplicaciones de
consumo, pero lo veo nocivo a la hora de aplicaciones destinadas a producir
datos y contenidos de forma masiva e intensiva. Y a mi modo de ver es un
problema serio en un gran número de escenarios.

  [fordummies]: https://es.wikipedia.org/wiki/Usabilidad


### Un caso real de usabilidad engañosa

No proporcionare datos reales por respeto a las partes implicadas, pero quiero
aportar aquí un ejemplo real que he podido vivir de cerca durante varios años,
de lo que la pretendida usabilidad, ni lo es, ni ayuda a sacar más partido de
las herramientas:

__Escenario fallido__ : un negocio que se dedica el 90% del tiempo a editar
grandes cantidades de texto. Se informatizan a mediados de los 80 y adoptan como
procesador de textos WordPerfect para consola. Después de varios años, están en
la versión de WordPerfect 5.1 para MSDOS con un 90% de los empleados (unos
diez), con un dominio asombroso de la aplicación, basando todo su trabajo en
atajos de teclado y una pantalla donde únicamente se visualiza el texto sobre el
que están trabajando. Productividad: realmente elevada.  Principios del siglo
XXI, un consultor informático embaucador (*aka* comercial) los convence de que
el futuro es [WYSIWYG][cool] y que eso del terminal de texto es cosa del pasado.
Tras una primera migración a WordPerfect para Windows, la productividad baja de
forma significativa. La solución propuesta: Word, la productividad cae de forma
dramática. La excusa del "asesor": necesidad de adaptación al nuevo concepto.
Dos años después, la productividad sigue sin incrementarse, el trabajo se
acumula y se contratan a dos personas más para refuerzo. El personal ya se ha
adaptado y están tan hipnotizados por el ratón, los iconos y los "regalitos" que
su software les proporciona en cada nueva versión, que se oponen radicalmente a
volver al "pasado". En realidad, nadie desde dentro se cuestionaba que el
problema real era que habían dejado de centrarse en el contenido, para centrarse
en el continente. Lo más irónico: lo que realmente hacían era crear e imprimir
documentos, impresos en impresoras matriciales que seguían imprimiendo con la
misma calidad y la misma fuente Courier 11 sobre el mismo tipo de documentos
oficiales.

  [cool]: https://es.wikipedia.org/wiki/Wysiwyg

__Escenario exitoso__ : Paralelamente, en un área de negocio distinta, pero
estrechamente relacionada con la anterior, una empresa que ha trabajado siempre
en entorno de terminal contra un [AS/400,][a4k] presentaba una mentalidad y un
resultado totalmente opuestos. Nunca se han dejado seducir por los cantos de
sirena del marketing y se han opuesto radicalmente a cualquier cambio de
sistema, simplemente han evolucionado el que ya tenían y conservando su
plantilla prácticamente intacta durante el mismo periodo. El resultado: la
productividad se ha mantenido constante a lo largo de los años y han podido
asumir importantes picos de carga de trabajo sin demasiadas dificultades. Y un
efecto secundario de esta toma de decisiones: el haberse mantenido dentro de un
sistema maduro y estable les ha librado de un mantenimiento casi nulo en el área
de software, limitándose el mismo al área de hardware (lo habitual). Como podéis
imaginar, en un sistema basado en plataforma Windows y actualizaciones sucesivas
de SO y aplicaciones, el mantenimiento del área de software les ha supuesto una
importante carga económica al otro negocio.

Que cada uno extraiga sus propias conclusiones. La mía: que la carrera hacia
adelante de fabricantes de sistemas operativos y aplicaciones (cuyo único
recurso para seguir vendiendo ha sido con frecuencia un simple
lavado de cara) ha supuesto, en muchos aspectos, un paso atrás en varias áreas de
la informática.

  [a4k]: https://es.wikipedia.org/wiki/As/400


## La usabilidad bien entendida

No quiero decir con lo anterior, que las aplicaciones gráficas sean el problema
ni mucho menos. De hecho, hay aplicaciones gráficas que son una maravilla de la
usabilidad. Por ejemplo, Autocad, que te permite un control casi absoluto como
usuario avanzado (con los comandos y [AutoLISP][alsp]) y que al mismo tiempo te
permite realizar gran parte del trabajo de manera muy intuitiva (siempre
teniendo en cuenta el contexto del usuario al que va dirigido) empleando la
interfaz gráfica. Lo que permite que sea muy usable sin detrimento de la
productividad. Lo que quiero decir, es que es necesario añadir el sentido común
como un criterio más, si no el primero, a la hora de implementar la usabilidad.

  [alsp]: https://es.wikipedia.org/wiki/Autolisp

Si consultamos la Wikipedia, encontramos dos definiciones de la ISO para el
concepto de [usabilidad][fordummies] :

> La usabilidad se refiere a la capacidad de un software de ser comprendido,
aprendido, usado y ser atractivo para el usuario, en condiciones específicas de
uso

> Usabilidad es la eficacia, eficiencia y satisfacción con la que un producto
permite alcanzar objetivos específicos a usuarios específicos en un contexto de
uso específico

Como decía anteriormente, la realidad dista mucho de la teoría. En la
práctica se ha adoptado con bastante fidelidad la primera definición, eso sí,
ignorando con bastante frecuencia la parte de "condiciones específicas" y la
segunda definición parece haber sido ampliamente ignorada.

Si bien es cierto que la mayoría de las aplicaciones actuales pueden ser muy
potentes, lo que yo veo mirando al pasado, es que la gran mayoría de los
empleados que utilizaban una aplicación a diario eran usuarios avanzados y
cuando no expertos. Hoy en día, y ciñéndonos al ámbito profesional, a algunos
les cambias el icono de la misma, y no saben iniciarla. Y no es culpa de ellos,
las aplicaciones se diseñan para que las puedan usar hasta los más reacios a la
tecnología (siempre en su contexto), pero una vez que necesitas realizar algo
complejo, existe un salto conceptual que la mayoría de los usuarios, ni se
atreven a dar, ni quieren darlo.

Es realmente complejo, muy complejo, conseguir una interfaz de usuario que sea
realmente amigable e intuitiva y que al mismo tiempo consiga satisfacer las
necesidades reales tanto del usuario profesional, como del usuario ocasional. El
problema de base está en intentar crear herramientas todoterreno. Ni maldita
falta que le hace un Word actual a un usuario domestico y que demonios hace un
escritor profesional empleándolo en vez de algo como Latex + editor de texto.
Ni un usuario domestico necesita de herramientas para correspondencia, programar
macros, etc, ni un escritor necesita preocuparse del formato del texto. Y sin
embargo es empleado hasta por editores que deberían estar empleando
herramientas de autoedición.

Por ejemplo, una aplicación que es un claro ejemplo de buena usabilidad y que
está teniendo una buena acogida últimamente, es [Sublime Text][st]. Es bonita,
es potente, es amigable y es francamente muy, muy usable. Realmente lo que han
hecho ha sido recoger el testigo que dejo [TextMate][tm], que fueron los
primeros en darse cuenta de algo muy sencillo. Esto es, los editores de texto y
los IDEs para programadores son una de las aplicaciones en las que nunca llueve
a gusto de todos, surgen continuamente nuevas alternativas, pero no se acaba por
imponer ninguna. Por que en realidad, si nos fijamos en los programadores más
experimentados, dos de los editores más utilizados y defendidos a muerte, son
[Vim][vim] y [Emacs][emacs], ambos basados en conceptos de hace casi cuatro
décadas. Es que la usabilidad ya estaba inventada hace mucho tiempo, y no tiene
nada que ver ni con gráficos bonitos, ni con tratar a los usuarios como
imbéciles. La usabilidad, señores, está en la adaptación del interfaz del
ordenador de la manera más optima posible al interfaz que la naturaleza nos dio,
nuestras manos. Y desde luego, jamás un ratón, con los botones que quieras
ponerle, sera más eficaz que un teclado (usado con los diez deditos), al igual
que no lo es más que un bolígrafo o una tableta gráfica con lápiz. Que para eso
tenemos los dedos y no muñones. Si vamos a comprar un libro en Internet, el
ratón es nuestro gran aliado para hacerlo de forma intuitiva sin conocimientos
previos, pero si me vas a obligar a introducir entradas de almacén 40 horas a la
semana con la misma aplicación, por favor, no me condenes a usar el ratón cada
dos pasos. Sentido común!

  [st]: http://www.sublimetext.com/
  [tm]: http://macromates.com/
  [vim]: https://es.wikipedia.org/wiki/Vim
  [emacs]: https://es.wikipedia.org/wiki/Emacs


## Las aplicaciones amigas de la productividad

Este entrada pretende ser la introducción y el indice de una nueva serie de
artículos dedicada a esas aplicaciones para Linux que para mi marcan la
diferencia entre *hacer el trabajo* y *marear la perdiz*. Estas aplicaciones
comparten en general tres puntos en común:

* Son muy eficientes y ayudan a incrementar nuestra productividad.
* Realizan a una sola tarea y lo hacen bien o muy bien.
* No están muy extendidas.

Iré actualizando la entrada a medida que vaya creando los artículos para cada
aplicación.

### Aplicaciones

Estas son algunas de las aplicaciones que yo empleo a menudo y que al igual que
a mí, pueden servirte para incrementar de forma notable tu productividad.

+ [Pentadactyl][penta], complemento para Firefox para controlar el navegador
  completamente desde el teclado, permite navegar entre las páginas a velocidad
  de vértigo. Además es muy potente y posee muchísimas opciones y posibilidades.

  [penta]: http://joedicastro.com/productividad-linux-pentadactyl.html

