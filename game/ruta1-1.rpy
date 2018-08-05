# Ren'Py automatically loads all script files ending with .rpy. To use this
# file, define a label and jump to it from another file.
label tomar:
    $ des1 = 0
    show raciocinio-:
        xalign 0.5
        yalign 0.5
    ""
    hide mano-dro
    hide raciocinio-
    $ renpy.movie_cutscene("videos/Capitulo2.mpg")
    stop music
    show carta2
    "primera carta"
    scene bar2 with fade
    play music "music/Strange.mp3" fadein 2.0
    show gordo1:
        xalign 0
        yalign 1.0
    "Ahí esta ese maldito…"
    menu:
        "Intentar matarlo":
            menu:
                    "Tomar el cuchillo de la barra":
                        hide gordo1
                        jump capitulo3
                    "Golpearlo por la nuca con la botella":
                        scene negro
                        show game over1:
                            xalign 0.5
                            yalign 0.5
                        ""

        "Esperar ":
                ""
