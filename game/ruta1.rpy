define a = Character("Midori", who_color="#c8ffc8", what_size=34)
define s = Character("Sombra", who_color="#c8ffc8", what_size=34)
label ruta1:
    stop music
    scene barcito with dissolve
    scene lluvia with fade
    play music "music/Lluvia.mp3" fadein 2.0
    show midori1:
        xalign 0
        yalign 1.0
    show sujeto2:
        xalign 1.0
        yalign 0.9
    e"Ey, ¿Por qué no estas en la fiesta?"
    hide midori1
    show midori2:
        xalign 0
        yalign 1.0
    "No me gustan las fiestas"
    hide midori2
    show midori3:
        xalign 0
        yalign 1.0
    "nunca se que hacer con las manos prefiero ver la lluvia "
    scene lluvia with dissolve
    scene negro with fade
    show mano
    e"Te entiendo…¿Cómo te llamas?"
    "Puedes llamarme [a]"
    e"Mucho gusto [a]"
    e"yo soy [e]. \n¿Que dices si vamos a ver la lluvia en otro lugar?"
    a"Claro… why not?"
    stop music
    $ renpy.movie_cutscene("videos/cigarro.mpg")
    scene negro with dissolve
    scene ladrillos with fade
    show sujeto2
    e"¿Quieres probar lo que me dio Hugo?"
    scene ladrillos with dissolve
    scene negro with fade
    show drogas
    a"Why not? Para eso se lo compramos"
    hide drogas
    scene negro with dissolve
    $ renpy.movie_cutscene("videos/viaje.mpg")
    "Buenos días amor…¿Amor?"
    play sound "music/plato.mp3"
    show midori-muerta
    "¿[a]?"
    "...Despierta"
    scene negro with dissolve
    $ renpy.movie_cutscene("videos/reloj1.mpg")
    play music "music/Twisted Eyes.mp3" fadein 2.0
    scene negro2 fade
    show posesion1
    s "[e], ¿Ya escucharas mi propuesta?"
    menu:
        "Escucharlo":
                        "¿Qué debo de hacer?"
                        hide posesion1
                        jump ruta1esc
        "Cállate carajo":
                        hide posesion1
                        s"Ok,ok le diré a [a] que no quieres…"
                        show sujeto2
                        e"¿Qué dices?"
                        s"Toma…"
                        hide sujeto2
                        "mostramos una carta "

                        jump ruta1esc
