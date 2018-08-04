# Ren'Py automatically loads all script files ending with .rpy. To use this
# file, define a label and jump to it from another file.
label tomar:
    $ des1 = 0
    show raciocinio-:
        xalign 0.5
        yalign 0.5
    ""
    hide raciocinio-
    $ renpy.movie_cutscene("videos/Capitulo2.mpg")
    "primera carta"
    "La primer persona que debe matar es un hombre gordo pervertido"
    "el cual es un abusador que pasa la mayoría de días en un  bar de mala muerte"
    scene bar2 with fade
    show gordo1:
        xalign 0
        yalign 1.0
    "Ahí esta ese maldito…"
    menu:
        "Intentar matarlo":
            menu:
                    "Tomar el cuchillo de la barra":
                        jump capitulo3
                    "Golpearlo por la nuca con la botella":
                        scene negro
                        ""
                        show game over1:
                            xalign 0.5
                            yalign 0.5
                        ""

        "Esperar ":
                    "aun no hay contenido"
