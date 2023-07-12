define t = Character("Tommy")
define c = Character("[name]")

label start:


    # Aquí vamos a tener la presentación del personaje principal.
    # El personaje está estudiando y de repente nota un temblor/terremoto.
    # Toda la clase se refugia en un refugio de clase donde casualmente, está la chica que le gusta.
    # Y tomas la decisión de qué ruta quieres seguir.

    scene fondo

    with Dissolve(.5)


    play music alegre

    play sound kachau

    "Intro"

    #Input nombre (aunque se puede usar para otras cosas como responder preguntas. Para que se represente hay que escribir "[name]"

    python:
        name = renpy.input(_("Se escuchaba el nombre de..."))

        name = name.strip() or __("Ai")

    "Otra frase"

    with hpunch
    with vpunch

    show objeto at left:
        zoom 0.35
        yalign 0.5


    with Dissolve(.5)

    menu:

        "Opción 1":
            jump ruta1

        "Opción 2":
            jump ruta2

        "Opción 3":
            jump ruta3

    label ruta1:

            # Ruta 1

            "Texto Ruta 1"

    menu:

        "Final A":
            jump ruta1_final_true

        "Final B":
            jump ruta1_final_false


            label ruta1_final_true:

            "Texto Final A"

            jump ending

            label ruta1_final_false:

            "Texto Final B"

            jump ending


    label ruta2:

            # Ruta 2

            "Texto Ruta 2"


    menu:

        "Final A":
            jump ruta2_final_true

        "Final B":
            jump ruta2_final_false

            label ruta2_final_true:

            "Texto Final A"


            jump ending

            label ruta2_final_false:

            "Texto Final B"

            jump ending



    label ruta3:

            # Ruta 3

            "Texto Ruta 3"


    menu:

            "Final A":
                jump ruta3_final_true

            "Final B":
                jump ruta3_final_false

                label ruta3_final_true:
                    "Texto Final A"

                    jump ending

                label ruta3_final_false:

                    "Texto Final B"


                    jump ending

    label ending:

---------------------------------------
    #alpha es para definir como de transparente quieres que sea una imagen.

    show yumii at center:

                    alpha 0.80

                with Dissolve(.5)

    #with move es para que la imagen se mueva a la hora de hacer la transición.

    show ade at right:
                    xalign 0.75
                    yalign 1.0

                with move

---------------------------------------
#vspace sirve para que la frase ra esté encima de p1.
c "ra
   {vspace=1}
   p1"

#what_size permite cambiar el tamaño de una palabra o frase

c "Chiquito" (what_size=12)

    scene bl

    "..."

    "{i}Sea cual sea la ruta que hayas escogido...{/i}"

    "{i}¡Gracias por jugar!{/i}"

    return
