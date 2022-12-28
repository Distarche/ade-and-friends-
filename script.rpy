# The script of the game goes in this file.

# manteca de la abuela

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define t = Character("Tommy")
define y = Character("Yumi")
define k = Character("er bicho")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene lib

    # Aquí vamos a tener la presentación del personaje principal.
    # El personaje está estudiando y de repente nota un temblor/terremoto.
    # Toda la clase se refugia en un refugio de clase donde casualmente, está una chica que le gusta.
    # Y tomas la decisión de qué ruta quieres seguir.

    "Empieza"

    show pibe

    "¿Qué ruta quieres seguir"

        menu:

        "Ruta 1":
            jump ruta1

        "Ruta 2":
            jump ruta2

        "Ruta 3":
            jump ruta3

    label ruta1:

        $ ruta1_final = True

        e "While creating a multi-path visual novel can be a bit more work, it can yield a unique experience."

        jump choice1_done

    label ruta2:

        $ menu_flag = False

        e "Games without menus are called kinetic novels, and there are dozens of them available to play."

    label ruta2:

        $ menu_flag = False

        e "Games without menus are called kinetic novels, and there are dozens of them available to play."

        jump choice1_done

    label choice1_done:

        # ... the game continues here.


        "Y aquí termina"

    # This ends the game.

    return
