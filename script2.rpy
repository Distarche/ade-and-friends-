define c = Character("Chica")
define m = Character("Manager")
define g = Character("Grupo")
define f = Character("Fan")

label start:

    # Aquí vamos a tener la presentación del personaje principal:
    # El personaje está en un camerino y recibe la carta de un fan.
    # Se debate si seguir cantando, el grupo y el/la manager le llaman desde la puerta
    # Y tomas la decisión de qué ruta quieres seguir

    scene fondo

    "Intro"

    menu:
        "Actriz":
            jump rama1
        "Idol":
            jump rama2
# los labels a la izquierda, con : al final y su contenido indentado
label rama1:
    # Rama 1
    "Texto Rama 1"
    menu:

        "Ruta Sentimental":

            jump rama1_ruta1

        "Ruta Cachondeo":

            jump rama1_ruta2

        "Ruta Meta":

            jump rama1_ruta3

            # Ruta Sentimental

            label rama1_ruta1:

                "Ruta Sentimental"

                menu:

                    "Sen1":

                        jump rama1_ruta1_end1

                    "Sen2":

                        jump rama1_ruta1_end2

                label rama1_ruta1_end1:

                    "Final A Ruta 1"

                    jump ending

                label rama1_ruta1_end2:

                    "Final B Ruta 1"

                    jump ending

            # Ruta Cachondeo

            label rama1_ruta2:

                "Ruta Cachondeo"

                menu:

                    "Cacho1":

                        jump rama1_ruta2_end1

                    "Cacho2":

                        jump rama1_ruta2_end2

                label rama1_ruta2_end1:

                    "Final A Ruta 2"

                    jump ending

                label rama1_ruta2_end2:

                    "Final B Ruta 2"

                    jump ending

            # Ruta Meta

            label rama1_ruta3:

                "Ruta Meta"

                menu:

                    "Meta1":

                        jump rama1_ruta3_end1

                    "Meta2":

                        jump rama1_ruta3_end2

                label rama1_ruta3_end1:

                    "Final A Ruta 3"

                    jump ending

                label rama1_ruta3_end2:

                    "Final B Ruta 3"

                    jump ending

label rama2:
    # Rama 2
    "Texto Rama 2"
    menu:

        "Ruta Sentimental":

            jump rama2_ruta1

        "Ruta Cachondeo":

            jump rama2_ruta2

        "Ruta Meta":

            jump rama2_ruta3

            # Ruta Sentimental

            label rama2_ruta1:

                "Ruta Sentimental"

                menu:

                    "Sen1":

                        jump rama2_ruta1_end1

                    "Sen2":

                        jump rama2_ruta1_end2

                label rama2s_ruta1_end1:

                    "Final A Ruta 1"

                    jump ending

                label rama2_ruta1_end2:

                    "Final B Ruta 1"

                    jump ending

            # Ruta Cachondeo

            label rama2_ruta2:

                "Ruta Cachondeo"

                menu:

                    "Cacho1":

                        jump rama2_ruta2_end1

                    "Cacho2":

                        jump rama2_ruta2_end2

                label rama2_ruta2_end1:

                    "Final A Ruta 2"

                    jump ending

                label rama2_ruta2_end2:

                    "Final B Ruta 2"

                    jump ending

            # Ruta Meta

            label rama2_ruta3:

                "Ruta Meta"

                menu:

                    "Meta1":

                        jump rama2_ruta3_end1

                    "Meta2":

                        jump rama2_ruta3_end2

                label rama2_ruta3_end1:

                    "Final A Ruta 3"

                    jump ending

                label rama2_ruta3_end2:

                    "Final B Ruta 3"

                    jump ending


    label ending:

    scene bl

    "..."

    "{i}Sea cual sea la ruta que hayas escogido...{/i}"

    "{i}¡Gracias por jugar!{/i}"

    return
