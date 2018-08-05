# Ren'Py automatically loads all script files ending with .rpy. To use this
# file, define a label and jump to it from another file.
label notomar:
    $ des1 = 1
    show raciocinio:
        xalign 0.5
        yalign 0.5
    ""

    hide mano-dro
    hide raciocinio
    $ renpy.movie_cutscene("videos/Capitulo2.mpg")
    play music "music/Strange.mp3" fadein 2.0
    scene bar2 with fade
    show gordo1:
        xalign 0
        yalign 1.0
    "Ahí esta ese maldito…"
    "El bartender salio y solo  estamos los dos debería…"
    menu:
        "Intentar matarlo":
            menu:
                    " Distraerlo y envenenar la bebida":
                        hide gordo1
                        stop music
                        jump capitulo3
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
