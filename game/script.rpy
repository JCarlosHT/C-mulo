# The script of the game goes in this file.
label splashscreen:
    scene black
    with Pause(1)

    show text "Un proyecto creado por..." with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)

    $ renpy.movie_cutscene("videos/Cumulo.mpg")

    return

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define e = Character("Charly", who_color="#c8ffc8", what_size=34)


# The game starts here.

label start:
    stop music
    play music "music/Take Me Somewhere Nice.mp3" fadein 2.0
    scene barcito
    show sujeto1
    "Bienvenido jugador, mi nombre es [e]"
    e"Es un placer darle la bienvenida a Cúmulo"
    hide sujeto1
    show sujeto2
    e "Esta es una historia desalentadora."

    e "Llena de dolor y muerte...."
    hide sujeto2

    show sujeto3
    e"Espero la puedas disfrutar"
    e "Te deseo lo mejor."
    e"¿Listo para comenzar?"
    hide sujeto3
    menu:
        "Sí":
            stop music
            $ renpy.movie_cutscene("videos/CumuloCapitulo1.mpg")
            jump ruta1
        "No":
            e"Entonces no tendremos opciones"

    return
