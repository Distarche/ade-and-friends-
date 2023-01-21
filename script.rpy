
define t = Character("Tommy")
define y = Character("Yumi")
define k = Character("er bicho")
define pt = Character("Pato Tecno")

label start:

    scene lib

    # Aquí vamos a tener la presentación del personaje principal.
    # El personaje está estudiando y de repente nota un temblor/terremoto.
    # Toda la clase se refugia en un refugio de clase donde casualmente, está una chica que le gusta.
    # Y tomas la decisión de qué ruta quieres seguir.

    "Tommy era un joven estudiante universitario que se encontraba en la biblioteca cuando comenzó el caos."

    scene bg room

    "Era un día normal en la ciudad de Tokio cuando de repente, una sirena de emergencia comenzó a sonar."

    "Todo el mundo corría a refugiarse mientras la noticia se extendía rápidamente: Godzilla había vuelto."

    show bicho

    #Si es posible hacer que la imagen de Godzilla vibre ligeramente

    k "GWAAAAAG"

    hide bicho

    "Tommy trató de calmarse y pensar en qué hacer, pero se sentía tan confuso debido a la situación tan surrealista que estaba viviendo..."

    "De repente, recordó a su amiga de la infancia, Yumi la cual conocía desde hace años. Tommy siempre había sentido una atracción especial hacia ella, aunque nunca se hubiera atrevido a confesarlo."

    #Y si hacemos lo de que ya le gustara de antes más ambiguo porque entonces se puede sentir desconectado de las otras dos rutas"

    "Tommy decidió buscar a Yumi y juntos trataron de escapar de la ciudad. Los edificios se derrumbaban a su alrededor y el suelo temblaba con cada paso de Godzilla."

    scene refugio1

    "Sin embargo, Tommy y Yumi no se rindieron y finalmente encontraron un refugio seguro."

    scene refugio2

    "A partir de aquí el destino de Tommy y Yumi era uno que solo una fuerza superior podía saber. Así que..."

    show piba

    y "Entonces, ¿Qué es lo que vamos a hacer a partir de ahora?"

    menu:

        "Ruta 1":
            jump ruta1

        "Ruta 2":
            jump ruta2

        "Ruta 3":
            jump ruta3

    label ruta1:

            # Ruta Romántica

            t "modo sexo activado"

    menu:

        "Ruta 1: Final A":
            jump ruta1_final_true

        "Ruta 1: Final B":
            jump ruta1_final_false


            label ruta1_final_true:
            "Ruta 1: Final A"

            jump ending

            label ruta1_final_false:
            "Ruta 1: Final B"

            jump ending


    label ruta2:

            # Ruta Comedia

            t "modo payaso activado"

    menu:

        "Ruta 2: Final A":
            jump ruta2_final_true

        "Ruta 2: Final B":
            jump ruta2_final_false

            label ruta2_final_true:
            "Ruta 2: Final A"
            jump ending

            label ruta2_final_false:
            "Ruta 2: Final B"
            jump ending



    label ruta3:

            # Ruta Meta

            t "Berserk - Theme of Guts (Cut & Looped for One Hour)"

    menu:

            "Ruta 3: Final A":
                jump ruta3_final_true

            "Ruta 3: Final B":
                jump ruta3_final_false

                label ruta3_final_true:
                    "Ruta 3: Final A"
                    jump ending

                label ruta3_final_false:
                    "Ruta 3: Final B"
                    jump ending

    label ending:

    "¡Gracias por jugar!"

    return
