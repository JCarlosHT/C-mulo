define a = Character("alicia", who_color="#c8ffc8", what_size=34)
label ruta1:
    stop music
    scene barcito with dissolve
    scene lluvia with fade
    play music "music/Lluvia.mp3" fadein 2.0
    e"Ey, ¿Por qué no estas en la fiesta?"
    a"No me gustan las fiestas"
    a"nunca se que hacer con las manos prefiero ver la lluvia "
    scene lluvia with dissolve
    scene negro with fade
    e"Te entiendo…¿Cómo te llamas?"
    a"Alicia, puedes llamarme Alice"
    e"Mucho gusto, Sergio. ¿Quieres ir a otro lado a ver la lluvia?"
    a"Claro… why not?"
    stop music
    $ renpy.movie_cutscene("videos/cigarro.mpg")
    scene negro with dissolve
    scene ladrillos with fade
    show sujeto2
    e"¿Quieres probar lo que me dio Hugo?"
    a"Why not? Para eso se lo compramos"
    scene ladrillos with dissolve
    scene negro with fade
    $ renpy.movie_cutscene("videos/viaje.mpg")
