# Ren'Py automatically loads all script files ending with .rpy. To use this
# file, define a label and jump to it from another file.
label capitulo3:
    scene barcito with dissolve
    scene negro with fade
    "poner imagen del gordo muerto"
    "El siguiente en la lista es Jesse"
    "narcotraficante  y ladron, no te diré donde encontrarlo"
    "supongo que sabrás donde ya que es tu hermano"
    e"¡Qué carajos!"
    menu:
            "Aceptar el trabajo por Midori":
                S "Ok aquí tienes unas pistola, te puede servir "

            "Rechazar el trabajo… es mi hermano!":
                show game over2
