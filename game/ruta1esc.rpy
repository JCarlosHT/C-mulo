# Ren'Py automatically loads all script files ending with .rpy. To use this
# file, define a label and jump to it from another file.
define h = Character("Jesse ", who_color="#c8ffc8", what_size=34)
label ruta1esc:
    show sujeto3
    e"¿Cuándo empezare?"
    s"Yo te avisare, mantente atento"
    hide sujeto3
    h"¿Cómo has estado?, ya casi paso un mes y no te veo muy bien"
    show sujeto2:
        xalign 1.0
        yalign 1.2
    e"De la chingada pero lo arreglaré"
    h"Sé como te sientes pero no creo que pue… "
    e"NO, NO SABES COMO ME SIENTO"
    hide sujeto2
    h"Lo sé, lo sé, cálmate…"
    h"es más mira lo que te conseguí"

    menu:
        " Tomarlas":
                    jump tomar
        "No, ya aprendí":
                    jump notomar
