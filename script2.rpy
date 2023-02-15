define t = Character("Tommy")
define y = Character("Yumi")
define k = Character("Kaiju")
define pt = Character("Pato Tecno")
define pm = Character("Pepsiman")

label start:


    # Aquí vamos a tener la presentación del personaje principal.
    # El personaje está estudiando y de repente nota un temblor/terremoto.
    # Toda la clase se refugia en un refugio de clase donde casualmente, está la chica que le gusta.
    # Y tomas la decisión de qué ruta quieres seguir.

    scene fondo

    "Intro"

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

    scene bl

    "..."

    "{i}Sea cual sea la ruta que hayas escogido...{/i}"

    "{i}¡Gracias por jugar!{/i}"

    return
