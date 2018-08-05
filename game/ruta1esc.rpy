# Ren'Py automatically loads all script files ending with .rpy. To use this
# file, define a label and jump to it from another file.
define h = Character("Jesse ", who_color="#c8ffc8", what_size=34)
label ruta1esc:
    show posesion2
    e"¿Cuándo empezare?"
    s"Yo te avisare, mantente atento"
    hide posesion2
    show text "Una semana despues" with dissolve
    scene calle with fade
    show jesse1:
        xalign 0
        yalign 1.0
    h"¿Cómo has estado?, ya casi a pasado más de mes"
    h"desde la muerte de Midori y no te veo muy bien"
    show sujeto2:
        xalign 1.0
        yalign 1.0
    e"De la chingada pero lo arreglaré"
    h"Sé como te sientes pero no creo que pue… "
    e"NO, NO SABES COMO ME SIENTO"
    show sujeto3:
        xalign 1.0
        yalign 1.0
    hide sujeto2
    h"Lo sé, lo sé, cálmate…"
    h"Es más mira lo que te conseguí"
    scene calle with dissolve
    scene negro with fade
    show mano-dro:
        xalign 0.5
        yalign 0.5
    menu:
        " Tomarlas":
                    jump tomar
        "No, ya aprendí":
                    jump notomar
