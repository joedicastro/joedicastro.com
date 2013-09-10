title: Productividad & Linux: zathura
date: 2012-07-16 23:32
tags: productividad, Linux, pdf, djvu, postscript

[zathura][zth] es un programa minimalista que procura seguir el principio de
*"menos es más"*  que acuñara [Mies van der Rohe][mvdr] en la arquitectura y que
en la informática se correspondería con el principio [KISS][kiss] y la
[filosofía UNIX][unix]. Siguiendo esta filosofía, zathura es una aplicación que
hace una sola cosa, la hace bien y consume muy pocos recursos. Sus autores, la
comunidad [PWMT.org][pwmt] (*programas con nombre de película*), tienen como
propósito el crear aplicaciones de software libre que se centren en un interfaz
simple, que no malgaste espacio y que se maneje íntegramente desde el teclado.

  [zth]: http://pwmt.org/projects/zathura/
  [unix]: http://en.wikipedia.org/wiki/Unix_philosophy
  [kiss]: https://es.wikipedia.org/wiki/Principio_KISS
  [mvdr]: https://es.wikipedia.org/wiki/Ludwig_Mies_van_der_Rohe
  [pwmt]: http://pwmt.org/about

La aplicación es un visor de documentos, y es modular, por lo que puedes
instalar los plugins que quieras en función del formato de documentos que
quieras que soporte. Actualmente están disponibles los siguientes plugins:

+ *pdf-poppler*: Lectura de [PDF][pdf] a través de la famosa librería
  [Poppler][pplr], que es empleada por aplicaciones como Evince, Okular o
  Inkscape.

+ *pdf-mupdf*: Lectura de PDF mediante la librería [mupdf][mpdf] empleada por
  ejemplo por Sumatra PDF.

+ *djvu*: Para visionar documentos [DJVU][djvu]. Emplea la librería
  [djvulibre][djfree] que emplean por ejemplo Evince y Okular.

+ *ps*: Para poder ver documentos [Postscript][ps]. Usa la librería
  [libspectre][lsp] que es utilizada por Evince y Okular.

+ *cb*: Para poder abrir archivos en formato [Comic Book][cb].

  [pdf]: http://es.wikipedia.org/wiki/Pdf
  [pplr]: http://poppler.freedesktop.org/
  [mpdf]: http://mupdf.com/
  [djvu]: https://es.wikipedia.org/wiki/Djvu
  [djfree]: http://djvu.sourceforge.net/
  [ps]: https://es.wikipedia.org/wiki/Postscript
  [lsp]: http://libspectre.freedesktop.org/
  [cb]: https://es.wikipedia.org/wiki/Archivo_de_historieta


Como se puede ver emplea las mismas librerías que emplean la mayoría de
programas similares para Linux, por lo tanto nos ofrecen la misma calidad que
estos pero con un interfaz minimalista donde el protagonista es el contenido, y
proporcionándonos un control absoluto del documento desde el teclado.

<p style="text-align:center;"><img src="pictures/zathura.png" width="700"
height="957" alt="Zathura" /></p>

El interfaz es simple, una ventana de contenido y una barra de estado/línea de
comandos. El control de la misma recae en el teclado (aunque puede usarse el
ratón para funciones básicas) y sus atajos están inspirados en los de Vim.

## Características

Las características principales de Zathura son las siguientes:

+ Interfaz minimalista
+ Controlable completamente desde el teclado, inspirado en vim y muy parecido a
  pentadactyl. Permite seguir enlaces y saltos directos a páginas
+ Recarga automática de documentos si estos cambian. Útil para previsualizar la
  salida en PDF de documentos de LaTeX, por ejemplo
+ Permite establecer marcadores y marcadores rápidos dentro de un documento. Muy
  útil para labores de investigación y documentación
+ Exporta imágenes y adjuntos de un documento
+ Puede abrir documentos protegidos por contraseña (proporcionándosela, claro)
+ Imprime el documento completo o simplemente las hojas que deseemos
+ Permite buscar en el documento y desplazarse por los resultados
+ Se puede abrir y navegar por el indice del documento
+ Muestra la información disponible (metadatos) sobre el documento
+ Zoom y Rotar documentos
+ Permite cambiar el color del documento. Sirve para visualizar el documento en
  duotono con los colores invertidos
+ Se pueden personalizar los atajos de teclado y los colores empleados
+ Se personaliza a través de un fichero de texto plano

En esta imagen se puede apreciar el resultado de aplicar el comando `:info`
sobre un documento.

<p style="text-align:center;"><img src="pictures/zathura_info.png" width="700"
height="957" alt="zathura info dialog" /></p>

El poder cambiar los colores del documento, invirtiéndolos, es una
característica muy útil, por ejemplo, para leer largos documentos sin fatigar
demasiado nuestra vista. Aquí se puede ver la diferencia entre ver un documento
a pantalla completa en modo normal y con los colores invertidos.

<p style="text-align:center;"><img src="pictures/zathura.gif" width="640"
height="400" alt="zathura full screen" /></p>


## Alternativas

No hay demasiadas alternativas a Zathura que tengan un planteamiento parecido,
de hecho la única que conozco es [apvlv][apvlv]. Aunque para mi no es tan
completa como Zathura.

  [apvlv]: http://naihe2010.github.com/apvlv/

## Mi configuración

Aunque mi configuración no tiene nada de particular, está disponible en mis
*dotfiles* alojados en [GitHub][gh].

  [gh]: http://github.com/joedicastro/dotfiles




