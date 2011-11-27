title: Productividad en el escritorio Linux: Xmonad
date: 2011-11-26
tags: linux, ubuntu, unity, tiling, twm, productividad, xmonad, gnome


[xmonad][xmonad] es un [Gestor de ventanas de mosaico][twm], uno de los más 
empleados y de los más potentes. Después de haber probado varios (dwm, bluetile, 
wmii y el plugin Compiz Grid) llevo ya unos cuantos meses trabajando con él y 
posiblemente siga conmigo mucho, mucho tiempo. Una vez que trabajas con un 
**tiling window manager** es muy difícil que echarse atrás, volver a un gestor de
ventanas flotantes tradicional es casi impensable. Probaré uno más, 
[awesome][awesome], que promete mucho y solo si este logra convencerme del cambio, 
abandonaré Xmonad. 

  [xmonad]: http://xmonad.org
  [twm]: http://joedicastro.com/productividad-en-el-escritorio-linux-tiling.html
  [awesome]: http://awesome.naquadah.org
  

¿Pero que tiene de especial un **twm** como **Xmonad** para haber decidido 
abandonar la gestión de ventanas por defecto de Compiz, Gnome Shell, Unity, Kwin, 
etc y apostar por él? Cuando uno está cansado de perder el tiempo con maniobras y 
decisiones triviales -ajustar las ventanas en la pantalla, que si el navegador por 
aquí, que si este terminal por allá, etc y cambiando continuamente la mano del 
teclado al ratón y viceversa- pues entonces decides que hay que darle una 
oportunidad a un twm, que sea el gestor de ventanas quien haga el trabajo sucio 
por ti.

¿Y hasta que punto resuelve bien este problema un twm como Xmonad? En este vídeo 
de xmonad trabajando con mi configuración, uno se puede hacer una idea de lo que 
es capaz.

<div style="text-align:center">
<iframe src="http://player.vimeo.com/video/32747627?title=0&amp;byline=0&amp;portrait=0&amp;color=59a5d1" width="667" height="417" frameborder="0" webkitAllowFullScreen mozallowfullscreen allowFullScreen></iframe><p>Esbozo de las posibilidades de un Tiling Window Manager como Xmonad trabajando conjuntamente con Gnome 3 y Unity 2D sobre un Ubuntu 11.10</p>
</div>


**Xmonad** no necesita de un entorno de escritorio para trabajar, se puede iniciar 
una sesión directamente en él, al igual que la mayoría de gestores de ventanas 
de mosaico y otros gestores de ventanas como [OpenBox][ob]. En el vídeo se puede 
apreciar que lo estoy empleando conjuntamente con Unity, en concreto **Unity 2D**. 
Esto es así porque emplear Xmonad (u otro twm) de forma autónoma te obliga a 
montar una serie de servicios que vienen montados por defecto normalmente en un 
escritorio, como salvapantallas, fondo de pantalla, bandeja de sistema, gestor 
de red, notificaciones, control de volumen, soporte impresoras, etc. Como estoy 
contento con el funcionamiento en general de Gnome, lo mejor es no reinventar la 
rueda y aprovechar lo mejor de los dos mundos empleando ambos a la vez. 
Anteriormente con Gnome 2, lo tenia funcionando sin Unity, pero con Gnome 3 me 
encuentro con la desagradable situación de que Gnome classic (el fallback mode) 
tiene un panel que es un autentico desastre y que además no es redimensionable 
en altura (tiene 30px y yo lo quiero con 21px). Actualmente hay una 
[forma de arreglar esto][fix], pero de momento lo tengo montado todo con Unity 
2D y no hecho nada en falta. Eso si, de Unity solo empleo el panel, el Global Menu 
y la base de Gnome 3, lo demás lo descarto. Resumiendo, que básicamente sustituyo 
`metacity` por `xmonad`.

  [ob]: http://es.wikipedia.org/wiki/Openbox
  [fix]: http://askubuntu.com/questions/69576/how-to-customize-the-gnome-classic-panel/76884#76884


## Xmonad con Unity 2D

Aquí contaré como tengo configurado actualmente __Xmonad__ con __Ubuntu 11.10__
(Oneiric Ocelot) y con __Gnome 3__ y el panel de __Unity 2D__ (`unity-2p-panel`). 
Si alguien continua con Gnome 2D o alguna versión anterior de Ubuntu puede revisar 
[este enlace][lucid], la base es muy parecida, y luego solo habría que aplicar mi 
configuración (u otra).

  [lucid]: http://markhansen.co.nz/xmonad-ubuntu-lucid/
  
Lo primero que se necesita es instalar xmonad, que en Ubuntu viene siendo así:

    ::bash
    $ sudo apt-get install xmonad
    
A continuación crearíamos un fichero `~/.xmonad/xmonad.hs` de configuración 
básica 

    ::bash
    $ mkdir ~/.xmonad           # El carácter ~ se obtiene pulsando Alt Gr + 4
    $ vi ~/.xmonad/xmonad.hs    # Puedes emplear gedit en vez de vi si lo prefieres

e incluiríamos lo siguiente dentro de él:

    ::haskell
    import XMonad
    import XMonad.Config.Gnome

    myManageHook = composeAll (
        [ manageHook gnomeConfig
        , className =? "Unity-2d-panel" --> doIgnore
        , className =? "Unity-2d-launcher" --> doFloat
        ])

    main = xmonad gnomeConfig { manageHook = myManageHook }

Ahora tendríamos que recompilar Xmonad, es algo necesario cada vez que realizamos 
algún cambio en la configuración, pero es un proceso que no suele llevar más de 
5 segundos (y Xmonad se puede reiniciar sin tener que cerrar la sesión):

    ::bash
    $ xmonad --recompile
    
Lo siguiente es crear los ficheros necesarios para crear una nueva sesión de 
Gnome. Creamos primero el fichero que define nuestra nueva sesión:

    ::bash
    $ sudo vi /usr/share/gnome-session/sessions/xmonad.session
    
y dentro añadimos esto:

    [GNOME Session]
    Name=Xmonad Unity 2D
    RequiredComponents=gnome-settings-daemon;
    RequiredProviders=windowmanager;panel;
    DefaultProvider-windowmanager=xmonad
    DefaultProvider-panel=unity-2d-panel

a continuación creamos el fichero que inicia esta sesión:

    ::bash
    $ sudo vi /usr/share/xsessions/xmonad-unity-session.desktop

con este contenido:

    [Desktop Entry]
    Name=XMonad Unity 2D
    Comment=Tiling window manager
    TryExec=/usr/bin/gnome-session
    Exec=gnome-session --session=xmonad
    Type=XSession


Con esto estaría ya montada una sesión con la configuración por defecto de 
Xmonad funcionado sobre Gnome y empleando el panel de Unity 2D. Ahora solo 
tendrías que cerrar la sesión e iniciar la sesión con *Xmonad Unity 2D*. 

 >**Advertencia:** Por defecto verás que se ha creado automáticamente una sesión 
 llamada Xmonad al instalar este. Bien, si vas iniciar esa sesión, será mejor 
 que sepas que para salir tienes que pulsar **Win + Mayús + Q**, porque será una 
 sesión donde solo tendrás Xmonad, y es la única forma de cerrar la sesión.

Si queréis hacer alguna prueba con esta configuración básica por defecto, es 
mejor tener a mano una referencia con las combinaciones de teclas disponibles, 
aquí hay un [mapa del teclado][keys] de referencia que será muy útil.

  [keys]: http://haskell.org/wikiupload/b/b8/Xmbindings.png

## Mi configuración

Para poder emplear la configuración que se puede ver en el vídeo simplemente 
habría que editar el fichero `~/.xmonad/xmonad.hs` y sustituir su contenido por 
el de mi fichero de configuración. El contenido del fichero lo incluyo al final 
del articulo para no entorpecer la lectura del mismo.

### Atajos de teclado

Al comienzo del fichero enumero las combinaciones de teclas empleadas en mi 
configuración, que difieren de las combinaciones por defecto y se asemejan de 
algún modo a las que estaba habituado en Gnome y son más intuitivas para los que 
estamos acostumbrados a él. Aunque las que se emplean por defecto también me son 
muy familiares al estar basadas en parte en Vim. Voy a detallar algunas de estas 
combinaciones.

#### Lanzar aplicaciones

    ::haskell
    -- Win  +  Enter                   Terminal
    -- Win  +  F1                      Nautilus
    -- Win  +  F2                      Firefox                  (single instance)
    -- Win  +  F3                      Thunderbird              (single instance)
    -- Win  +  F4                      RSSOwl                   (single instance)
    -- Win  +  F5                      Hotot                    (single instance)
    -- Win  +  F6                      ncmpcpp  - MPD player
    -- Win  +  F7                      taskwarrior               
    -- Win  +  F8                      PAC                      (single instance)
    -- Win  +  F9                      Aptana                   (single instance)
    -- Win  +  F10                     Xmind                    (single instance)
    -- Win  +  F11                     Dbeaver                  (single instance)
    -- Win  +  F12                     VirtualBox               (single instance)

Lo primero que se puede ver es una serie de atajos para lanzar aplicaciones 
empleando la tecla **Win** más las teclas de función. La tecla **Win** (también 
llamada **Super**) es la tecla maestra por defecto de Xmonad (`mod4Mask`) y es la 
que se emplea en combinación con otras para realizar todo tipo de acciones. Estas 
combinaciones me permiten lanzar las aplicaciones que uso con más frecuencia con 
un par de teclas. 

Algunas aparecen con la frase *single instance* entre paréntesis, esto quiere 
decir que de estas aplicaciones solamente se abrirá una ventana. De hecho, lo que 
ocurre si volvemos a pulsar la combinación de teclas que abre la aplicación (una 
vez que esta ya está abierta) es que en lugar de abrir una nueva, nos movemos a 
la ventana ya abierta, esté en el escritorio que esté. Lo que es muy útil para 
localizar la ventana de una de estas aplicaciones de forma inmediata.

Adicionalmente la combinación **Alt + Enter** nos permite abrir una ventana del 
terminal. En este caso lo tengo predeterminado para que abra una venta de 
`terminator`

#### Consola emergente

    ::haskell
    -- Win  +  Space                   Run or Raise Shell Prompt
    -- Win  +  Shift   +  Space        Run Shell Prompt
    -- Win  +  Control +  Space        Window Prompt


A continuación podemos ver las teclas dedicadas a la consola emergente inferior 
(al estilo de Guake, Yakuake o Tilda) y que según la combinación pulsada 
realizara una acción u otra. La consola cuenta con auto-completado de texto, con 
lo cual escribiendo las primeras letras se nos muestran todas las coincidencias 
disponibles, a través de las que podemos desplazarnos con el tabulador.

*  **Win + Espacio** nos despliega una consola que nos permite lanzar una 
aplicación de igual modo que los lanzadores gráficos. Si la aplicación ya se 
encuentra abierta, nos dirige a la ventana de la misma.

* **Win + Mayús + Espacio** ejecuta el comando que escribamos. Similar a la 
ventana de ejecutar comando de Gnome (*Alt + F2* en Gnome)

* **Win + Control + Espacio** nos muestra las ventanas que están abiertas en ese 
momento. Seleccionando una nos envía directamente a ella. Gracias a esto, 
localizar una ventana abierta entre los múltiples escritorios es cuestión de 
segundos. Si conocemos el nombre de la ventana podemos filtrarla escribiendo las 
primeras letras con el teclado. Imagina una sesión en la que tenemos abiertas más 
de 10 aplicaciones en varios escritorios distintos, esto nos permite localizar 
una ventana en segundos, es muy útil.

#### Reiniciar Xmonad

Con la combinación **Win + q** lo que hacemos es reiniciar Xmonad sin necesidad 
de reiniciar la sesión. Esto es muy útil cuando introducimos cambios en la 
configuración, después de guardar el fichero y ejecutar `xmonad --recompile` en 
un terminal, pulsamos esta combinación y los cambios se reflejaran de forma 
inmediata.


## Transparencias

Una de las carencias de Xmonad es que no incorpora un [gestor de composición][cm] 
por lo que si queremos manejar transparencias en nuestros terminales, 
notificaciones, ventanas, etc, debemos emplear uno externo. Para esto empleo 
`xcompmgr` que funciona perfectamente y es muy ligero. Como aún conservo las 
otras sesiones de Ubuntu (Unity, Unity 2 D, Gnome Shell, etc) lo que hago para 
que solo se ejecute en la sesión de *Xmonad Unity 2D* es emplear este script bash:

    ::bash
    #!/bin/bash

    if [ $DESKTOP_SESSION = "xmonad-unity-session" ]; then
        xcompmgr -I1 -O1 -Ff;    
    fi

Luego añado el script a las aplicaciones que se ejecutan al inicio de la sesión 
y listo.

  [cm]:  http://es.wikipedia.org/wiki/Gestor_de_composici%C3%B3n_de_ventanas


## Bandeja del sistema

Una de las carencias de Unity en la versión 11.10 es que no han incorporado una 
bandeja del sistema donde alojar los iconos de aplicaciones que aún no tienen 
soporte para los *indicadores*. Se supone que debería añadirlos de forma 
automática al panel, incluso hay una configuración a través de `dconf` para 
habilitar esto, pero no funciona para todas las aplicaciones. Para añadir un 
*systray* empleo un script parecido al anterior para lanzar la aplicación 
`trayer` en esta sesión.

    ::bash
    #!/bin/bash

    MYARGS="--edge top --widthtype request --transparent true --alpha 0 --distancefrom right --distance 1100 --height 24 --tint 0x4c4a44 --align right"

    if [ $DESKTOP_SESSION = "xmonad-unity-session" ]; then
        sleep 24 && trayer $MYARGS;
    fi

</br>

## Como personalizar Xmonad: Haskell

El mayor inconveniente de Xmonad (y a la vez una de sus ventajas) es que la 
configuración es necesario hacerla a través del mismo lenguaje de programación 
en el que está creado: [Haskell][hskll]. Esto es una importante barrera de 
entrada para los que no conocen el lenguaje, yo incluido, pero a base de ir 
probando algunas de las configuraciones aportadas y el prueba y error, puedes 
salir del paso muy satisfactoriamente. Con un poco de práctica y estudiando un 
poco el lenguaje (que de entrada no es de los más fáciles de leer) y gracias a 
la documentación disponible, puedes conseguir exactamente lo que quieres. Y esa es 
precisamente también su mayor ventaja, que puedes llegar a un gran nivel de 
personalización si conoces Haskell. Además Haskell le proporciona una gran 
estabilidad y extensibilidad. 
  
  [hskll]: http://haskell.org/haskellwiki/Haskell
  
Afortunadamente hay varios recursos disponibles que nos hacen el trabajo más 
fácil, porque Xmonad está aceptablemente bien documentado (en Inglés).

* [Pantallazos](http://haskell.org/haskellwiki/Xmonad/Screenshots)
* [Ficheros de configuración](http://haskell.org/haskellwiki/Xmonad/Config_archive)
* [Wiki](http://haskell.org/haskellwiki/Xmonad)
* [API Docs](http://xmonad.org/xmonad-docs/xmonad/index.html)
* [API Extensiones Docs](http://xmonad.org/xmonad-docs/xmonad-contrib/index.html)
  

## Xmonad.hs


Este es mi mi fichero de configuración de Xmonad:

    ::haskell
    -- joe di castro's xmonad.hs
    -- Based on rupa's xmonad.hs, https://github.com/rupa/xmonad

    -- ===============================================================  KEY BINDINGS

    ------------------------------------------------- Launch (or Raise) Applications
    -- Win  +  Enter                   Terminal
    -- Win  +  F1                      Nautilus
    -- Win  +  F2                      Firefox                  (single instance)
    -- Win  +  F3                      Thunderbird              (single instance)
    -- Win  +  F4                      RSSOwl                   (single instance)
    -- Win  +  F5                      Hotot                    (single instance)
    -- Win  +  F6                      ncmpcpp  - MPD player
    -- Win  +  F7                      taskwarrior               
    -- Win  +  F8                      PAC                      (single instance)
    -- Win  +  F9                      Aptana                   (single instance)
    -- Win  +  F10                     Xmind                    (single instance)
    -- Win  +  F11                     Dbeaver                  (single instance)
    -- Win  +  F12                     VirtualBox               (single instance)                                                             
    ----------------------------------------------------------- Shell/Window prompts
    -- Win  +  Space                   Run or Raise Shell Prompt
    -- Win  +  Shift   +  Space        Run Shell Prompt
    -- Win  +  Control +  Space        Window Prompt
    --------------------------------------------------------------------- Navigation
    -- Win  +  [1..9]                  Switch to workspace N
    -- Win  +  Shift   +  [1..9]       Move client to workspace N
    -- Ctrl +  Alt     +  Left/Right   Previous/Next workspace
    -- Alt  +  Tab                     Focus next window
    -- Alt  +  Shift   +  Tab          Focus previous window
    -------------------------------------------------------------- Window management
    -- Win  +  Shift   +  Left         Move window to previous workspace
    -- Win  +  Shift   +  Right        Move window to next workspace
    -- Win  +  Control +  Left         Move window to previous empty workspace
    -- Win  +  Control +  Right        Move window to next empty workspace
    -- Ctrl +  Up/Down                 Move focused window up/down
    -- Win  +  m                       Toggle focused window Full Screen
    -- Win  +  n                       Refresh
    -- Win  +  -                       Move focused windows to master area
    -- Win  +  w  (or Alt + F4)        Close focused window
    -- Win  +  t                       Back to tiling (unfloat floating window)
    -- Win  +  Shift   +  t            Back All to tiling (unfloat ALL windows)
    -------------------------------------------------------------  Layout management
    -- Win  +  Tab                     Rotate layouts
    -- Win  +  Left/Right              Shrink/Expand the master area
    -- Win  +  Up/Down                 Mirror Shrink/expand
    -- Win  +  ,/.                     Increment/Deincrement 1 window in master area
    -- Win  +  f                       Hide/Unhide the gnome-panel/status bar
    -- Win  +  Shift   +  n            Reset current workspace to main layout
    ------------------------------------------------------------------ Mosaic Layout
    -- Win  +  a/z                     Taller/Wider
    -- Win  +  Control +  n            Reset
    ------------------------------------------------------------------------- Others
    -- Print Screen                    Capture screen
    -- Win  +  q                       Restart XMonad
    -- Win  +  Shift   +  q            Close gnome session dialog


    -- ============================================================== MOUSE BINDINGS

    -- Win  +  Button 1                Float Window and Move by dragging
    -- Win  +  Button 2                Raise Window to the top
    -- Win  +  Button 3                Float Window and Resize by dragging


     
    import XMonad
    import qualified XMonad.StackSet as W
    import qualified Data.Map        as M
    import Data.Monoid
     
    import XMonad.Actions.CycleWS
    import XMonad.Actions.FlexibleResize as Flex
    import XMonad.Actions.SinkAll
    import XMonad.Actions.UpdatePointer
    import XMonad.Actions.WindowGo
     
    import XMonad.Hooks.DynamicLog
    import XMonad.Hooks.EwmhDesktops
    import XMonad.Hooks.ManageDocks
    import XMonad.Hooks.ManageHelpers
     
    import XMonad.Layout.LayoutHints
    import XMonad.Layout.NoBorders
    import XMonad.Layout.ResizableTile
    import XMonad.Layout.Tabbed
    import XMonad.Layout.ToggleLayouts
    import XMonad.Layout.WindowArranger
    import XMonad.Layout.Mosaic
     
    import XMonad.Prompt
    import XMonad.Prompt.Input
    import XMonad.Prompt.RunOrRaise
    import XMonad.Prompt.Shell
    import XMonad.Prompt.Window
     
    import XMonad.Util.Run
    import XMonad.Util.Scratchpad
    import XMonad.Util.WorkspaceCompare
    import XMonad.Util.XSelection

    import XMonad.Config.Gnome

    -- Mod4 is the Super / Windows key
    winMask = mod4Mask
    altMask = mod1Mask

    -- key bindings
    myKeys conf@(XConfig {XMonad.modMask = modMask}) = M.fromList $
        [ ((winMask,                    xK_Return   ), spawn $ XMonad.terminal conf)
        , ((winMask,                    xK_F1       ), spawn "nautilus ~")
        , ((winMask,                    xK_F2       ), runOrRaise "firefox" (className =? "Firefox"))
        , ((winMask,                    xK_F3       ), runOrRaise "thunderbird" (className =? "Thunderbird"))
        , ((winMask,                    xK_F4       ), runOrRaise "./rssowl/RSSOwl" (className =? "RSSOwl"))
        , ((winMask,                    xK_F5       ), runOrRaise "hotot" (className =? "Hotot"))
        , ((winMask,                    xK_F6       ), spawn "terminator -e ncmpcpp")
        , ((winMask,                    xK_F7       ), spawn "terminator -e 'task shell' -p task")    
        , ((winMask,                    xK_F8       ), runOrRaise "pac" (className =? "Pac"))        
        , ((winMask,                    xK_F9       ), runOrRaise "./Aptana Studio 3/AptanaStudio3" (className =? "Aptana Studio 3"))            
        , ((winMask,                    xK_F10      ), runOrRaise "/usr/local/xmind/xmind" (className =? "XMind"))            
        , ((winMask,                    xK_F11      ), runOrRaise "./dbeaver/dbeaver" (className =? "DBeaver"))        
        , ((winMask,                    xK_F12      ), runOrRaise "VirtualBox" (className =? "VirtualBox"))    
        , ((winMask,                    xK_space    ), runOrRaisePrompt mySP)
        , ((winMask .|. shiftMask,      xK_space    ), shellPrompt mySP)
        , ((winMask .|. controlMask,    xK_space    ), windowPromptGoto mySP)
        , ((0,                          xK_Print    ), unsafeSpawn "gnome-screenshot")
        , ((altMask .|. controlMask,    xK_Right    ), moveTo Next (WSIs (return $ not . (=="NSP") . W.tag)))  
        , ((altMask .|. controlMask,    xK_Left     ), moveTo Prev (WSIs (return $ not . (=="NSP") . W.tag)))
        , ((winMask .|. shiftMask,      xK_Right    ), shiftTo Next (WSIs (return $ not . (=="NSP") . W.tag)))
        , ((winMask .|. shiftMask,      xK_Left     ), shiftTo Prev (WSIs (return $ not . (=="NSP") . W.tag)))
        , ((winMask .|. controlMask,    xK_Right    ), shiftTo Next EmptyWS)
        , ((winMask .|. controlMask,    xK_Left     ), shiftTo Prev EmptyWS)
        , ((winMask,                    xK_Tab      ), sendMessage NextLayout >> (dynamicLogString myPP >>= \d->safeSpawn "gnome-osd-client" [d]))
        , ((altMask,                    xK_Tab      ), windows W.focusDown)
        , ((altMask .|. shiftMask,      xK_Tab      ), windows W.focusUp)
        , ((controlMask,                xK_Down     ), windows W.swapDown)
        , ((controlMask,                xK_Up       ), windows W.swapUp)
        , ((winMask,                    xK_Left     ), sendMessage Shrink)
        , ((winMask,                    xK_Right    ), sendMessage Expand)
        , ((winMask,                    xK_Down     ), sendMessage MirrorShrink)
        , ((winMask,                    xK_Up       ), sendMessage MirrorExpand)
        , ((winMask,                    xK_minus    ), windows W.shiftMaster)
        , ((winMask,                    xK_comma    ), sendMessage (IncMasterN 1))
        , ((winMask,                    xK_period   ), sendMessage (IncMasterN (-1)))
        , ((winMask,                    xK_n        ), refresh)
        , ((winMask .|. shiftMask,      xK_n        ), setLayout $ XMonad.layoutHook conf)
        , ((winMask ,                   xK_a        ), sendMessage Taller)
        , ((winMask ,                   xK_z        ), sendMessage Wider)
        , ((winMask .|. controlMask,    xK_n        ), sendMessage Reset)
        , ((winMask,                    xK_m        ), sendMessage (Toggle "Full") >> (dynamicLogString myPP >>= \d->safeSpawn "gnome-osd-client" [d]))
        , ((winMask,                    xK_t        ), withFocused $ windows . W.sink)
        , ((winMask .|. shiftMask,      xK_t        ), sinkAll)    
        , ((winMask,                    xK_f        ), sendMessage ToggleStruts)
        , ((winMask,                    xK_w        ), kill)
        , ((altMask,                    xK_F4       ), kill)
        , ((winMask,                    xK_q        ), broadcastMessage ReleaseResources >> restart "xmonad" True)
        , ((winMask .|. shiftMask,      xK_q        ), spawn "gnome-session-quit")   
        ]
     
        ++
        -- mod-[1..9], Switch to workspace N
        -- mod-shift-[1..9], Move client to workspace N
        [ ((m .|. winMask, k), windows $ f i)
            | (i, k) <- zip (XMonad.workspaces conf) [xK_1 .. xK_9]
            , (f, m) <- [(W.greedyView, 0), (W.shift, shiftMask)] ]
            
    -- mouse bindings 
    myMouseBindings (XConfig {XMonad.modMask = modMask}) = M.fromList $
        [ ((winMask, button1), (\w -> focus w >> mouseMoveWindow w))
        , ((winMask, button2), (\w -> focus w >> windows W.shiftMaster))
        , ((winMask, button3), (\w -> focus w >> Flex.mouseResizeWindow w)) ]
     
    -- decoration theme
    myDeco = defaultTheme
        { activeColor           = "orange"
        , inactiveColor         = "#222222"
        , urgentColor           = "yellow"
        , activeBorderColor     = "orange"
        , inactiveBorderColor   = "#222222"
        , urgentBorderColor     = "yellow"
        , activeTextColor       = "orange"
        , inactiveTextColor     = "#222222"
        , urgentTextColor       = "yellow"
        , decoHeight            = 10 }
     
    -- tab theme
    myTab = defaultTheme
        { activeColor           = "black"
        , inactiveColor         = "black"
        , urgentColor           = "yellow"
        , activeBorderColor     = "orange"
        , inactiveBorderColor   = "#222222"
        , urgentBorderColor     = "black"
        , activeTextColor       = "orange"
        , inactiveTextColor     = "#222222"
        , urgentTextColor       = "yellow" }
     
    -- shell prompt theme
    mySP = defaultXPConfig
        { bgColor               = "black"
        , fgColor               = "white"
        , bgHLight              = "gray"
        , fgHLight              = "black"
        , borderColor           = "orange"
        , promptBorderWidth     = 2
        , position              = Bottom
        , height                = 40
        --, autoComplete        = Just 1000
        , historySize           = 1000 }
     
    -- dynamicLog theme (suppress everything but layout)
    myPP = defaultPP
        { ppLayout  = (\ x -> case x of
          "Hinted ResizableTall"        -> "[|]"
          "Mirror Hinted ResizableTall" -> "[-]"
          "Hinted Tabbed Simplest"      -> "[T]"
          "Mosaic"                      -> "[M]"
          "Full"                 -> "[ ]"
          _                      -> x )
        , ppCurrent             = const ""
        , ppVisible             = const ""
        , ppHidden              = const ""
        , ppHiddenNoWindows     = const ""
        , ppUrgent              = const ""
        , ppTitle               = const ""
        , ppWsSep               = ""
        , ppSep                 = "" }
     

    -- layouts
    myLayout = avoidStruts $ toggleLayouts (noBorders Full)
        (smartBorders (tiled ||| mosaic 2 [3,2] ||| Mirror tiled ||| layoutHints (tabbed shrinkText myTab)))
        where
            tiled   = layoutHints $ ResizableTall nmaster delta ratio []
            nmaster = 1
            delta   = 2/100
            ratio   = 1/2
     
    -- special windows
    myManageHook = composeAll
        [ className =? "MPlayer"                --> doFloat
        , className =? "Gimp-2.6"               --> doFloat
        , className =? "Gnome-panel"            --> doIgnore
        , className =? "XVkbd"                  --> doIgnore
        , className =? "Cellwriter"             --> doIgnore
        , className =? "Gtkdialog"              --> doFloat
        , resource  =? "desktop_window"         --> doIgnore
        , className  =? "Xmessage"              --> doCenterFloat
        , className =? "Unity-2d-panel" 	    --> doIgnore
        , isFullscreen                          --> doFullFloat
        , isDialog                              --> doCenterFloat
        , title =? "RSSOwl"                     --> doIgnore
        , title =? "Dbeaver"                    --> doIgnore
        , title =? "Xmind-bin"                  --> doIgnore
        , title =? "AptanaStudio3"              --> doIgnore
        , resource =? "sun-awt-X11-XDialogPeer" --> doCenterFloat
        , title =? "screenkey"                  --> doIgnore
        , className =? "Gloobus-preview"        --> doCenterFloat
        --                                      x y w h
        , scratchpadManageHook $ W.RationalRect 0 0 1 0.42
        , manageDocks ] <+> manageHook defaultConfig
     
    -- let Gnome know about Xmonad actions
    myLogHook = ewmhDesktopsLogHookCustom scratchpadFilterOutWorkspace >> updatePointer (Relative 0.5 0.5)

           
    myConfig = ewmh defaultConfig
        { terminal           = "terminator"
        , borderWidth        = 2
        , normalBorderColor  = "black"
        , focusedBorderColor = "orange"
        , focusFollowsMouse  = True
        , modMask            = mod4Mask
        , keys               = myKeys
        , mouseBindings      = myMouseBindings
        , layoutHook         = myLayout
        , manageHook         = myManageHook
        , startupHook        = gnomeRegister
        }


    -- need to override ewmh's logHook cause I'm using Scratchpad
    main = xmonad $ myConfig
        { logHook            = myLogHook }






