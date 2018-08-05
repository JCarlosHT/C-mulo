# Ren'Py automatically loads all script files ending with .rpy. To use this
# file, define a label and jump to it from another file.
label capitulo3:
    scene bar2 with dissolve
    scene negro with fade
    show gordo-muer:
        xalign 0.5
        yalign 0.5
    ""
    "buen trabajo"
    hide gordo-muer
    show logro:
        xalign 0.5
        yalign 0.5
    ""
    hide logro
    stop music
    $ renpy.movie_cutscene("videos/Capitulo3.mpg")
    "El siguiente en la lista es Jesse"
    "narcotraficante  y ladron, no te diré donde encontrarlo"
    "supongo que sabrás donde ya que es tu hermano"
    show sujeto2
    e"¡Qué carajos!"
    menu:
            "Aceptar el trabajo por Midori":
                hide sujeto2
                show pistola
                s "Ok aquí tienes unas pistola, te puede servir "
                hide pistola
                show text "Unas horas más tarde" with dissolve
                scene cuarto with fade
                play music "music/muerte.mp3" fadein 2.0
                show jesse2:
                    xalign 0
                    yalign 1.0
                h"¿Cómo sigues hermano?"
                show sujeto1:
                    xalign 1.0
                    yalign 1.0
                e"Mejor, eso creo"
                hide jesse2
                show jesse1:
                    xalign 0
                    yalign 1.0
                h "Me da gusto bro aunque no parece, ¿Quieres un té?"
                hide sujeto1
                show sujeto2:
                    xalign 1.0
                    yalign 1.0
                e"Si, las tazas están arriba en la alacena"
                "Este es el momento…"
                hide sujeto2
                hide jesse1
                menu:
                    "Disparar":
                        stop music
                        play sound "music/disparo.mp3"
                        "Carlos.."
                        play sound "music/plato.mp3"
                        jump capitulo4
                    "Tirarlo del banco y que se golpe con la barra":
                        show game over 3
                        ""



            "Rechazar el trabajo… es mi hermano!":
                ""
                show game over2
                ""
