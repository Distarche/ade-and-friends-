define t = Character("Tommy")

label start:


    # Aquí vamos a tener la presentación del personaje principal:
    # El personaje está en un camerino y recibe la carta de un fan.
    # Se debate si seguir cantando, el grupo y el/la manager le llaman desde la puerta
    # Y tomas la decisión de qué ruta quieres seguir.

    scene fondo

    "Intro"

    menu:

        "Actriz":
            jump ruta1

        "Idol":
            jump ruta2


    label ruta1:

            # Ruta 1

            "Texto Ruta 1"

    menu:

        "Romántica":

                jump 1_1

        "Comedia":

                jump 1_2

        "Meta":

                jump 1_3

        label 1_1

        "Esto debería ser la ruta romántica"

            jump ending


        label 1_2

        "The funny"

            jump ending


        label 1_3

        "man"

            jump ending


    label ending:

    scene bl

    "..."

    "{i}Sea cual sea la ruta que hayas escogido...{/i}"

    "{i}¡Gracias por jugar!{/i}"

    return
