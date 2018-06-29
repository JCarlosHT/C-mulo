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
define e = Character("sergio", who_color="#c8ffc8", what_size=34)


# The game starts here.

label start:
    stop music
    play music "music/Take Me Somewhere Nice.mp3" fadein 2.0
    scene barcito
    show sujeto1
    e"Bienvenido jugador, mi nombre es Sergio"
    e"es un placer darle la bienvenida a cumulo"
    hide sujeto1
    show sujeto2
    e "esta es una historia desalentadora."

    e "llena de dolor y muerte...."
    hide sujeto2

    show sujeto3
    e"Espero la puedas disfrutar"
    e "te deseo lo mejor."
    e"¿listo para comensar?"
    hide sujeto3
    menu:
        "si":
            stop music
            $ renpy.movie_cutscene("videos/CumuloCapitulo1.mpg")
            jump ruta1
        "no":
            e"entonces no tendremos opciones"

    return
