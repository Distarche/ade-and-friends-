define c = Character("[name]")
define m = Character("Manager")
define ade = Character("ADE GÓMEZNASAI")
define g = Character("Yumi")
define g0 = Character("Grupo")
define f = Character("Fan")
define idk = Character("???")
define j = Character("IDOL JUDA")
define jj = Character("Judah")
define i = Character("Hermanita")
define ii = Character("Alien camuflado como Idol")
define pp = Character("Becario al que no le pagan lo suficiente")
define e = Character("Eminem")
define n = Character("Novio")
define d = Character("Dragón con un severo caso de déficit de atención")
define z = Character("Director")
define ph = Character("Pato Héroe")
define b = Character("Er público")
 

label start:

    # Aquí vamos a tener la presentación del personaje principal:
    # El personaje está en un camerino y recibe la carta de un fan.
    # Se debate si seguir cantando, el grupo y el/la manager le llaman desde la puerta
    # Y tomas la decisión de qué ruta quieres seguir

    scene bg camerino

    with Dissolve(.5)

    play music alegre

    "En un camerino, se encontraba una chica preparándose para dar un concierto."

    "A lo lejos, se escuchaba una multitud gritando su nombre."


    python:
        name = renpy.input(_("Se escuchaba el nombre de..."))

        name = name.strip() or __("Ai")

    c "[name]"

    "Mientras ponía en orden sus pensamientos, alguien llamó a la puerta..."

    with hpunch

    m "¡VENGA, TE TOCA SALIR!"

    with hpunch

    g0 "¡VAMOS, NO PODEMOS HACER EL ESPECTÁCULO SIN TI!"


    c "..."

    c "No paro de darle vueltas sobre que quiero ser."

    c "..."

    c "Está bien, ya va siendo hora de tomar una decisión..."

    menu:
        "He nacido para esto":
            jump rama1
        "Esto no es lo mío":
            jump rama2
# los labels a la izquierda, con : al final y su contenido indentado
label rama1:
    # Rama 1

    with vpunch

    c "¡DECIDIDO!"

    stop music

    "Al levantarse de sopetón, la montaña de cartas que había delante suya se desplomó, desperdigándose sobre el suelo."

    "Alguna de esas cartas le llamaba particularmente la atención..."

    show carta1 at left:
        zoom 0.35
        yalign 0.5


    with Dissolve(.5)


    "Una de ellas tenía un corazón sellándola, lo cual le pareció un gesto tierno."

    show carta2 at center:
        zoom 0.35
        xalign 0.5
        yalign 0.5

    with Dissolve(.5)

    "Otra de ellas, un verde lima, le causó cierta gracia."

    show carta3 at right:
        zoom 0.35
        yalign 0.5

    with Dissolve(.5)

    "Y otra carta, completamente negra, hizo que le recorriera un escalofrío por la espalda."


    menu:

        "Qué carta más cuqui...":

            jump rama1_ruta1

        "Qué carta más simpática...":

            jump rama1_ruta2

        "Qué carta más tétrica...":

            jump rama1_ruta3

            # Ruta Sentimental

            label rama1_ruta1:

                hide carta1

                hide carta2

                hide carta3

                c "Ya recuerdo el porqué sigo siendo idol…"
                "Estaba claro desde el principio, pero no creo que nadie lo acepte…"
                "Especialmente en este mundillo…"

                scene bg negro

                with Dissolve(.5)

                c "Yo…"
                c "¡YO!"

                with vpunch

                c "¡YO AMO A YUMI MAKEBA!"

                with vpunch

                scene bg camerino with Dissolve(.4)

                "En ese momento la puerta se abrió de golpe."

                show yumii

                with Dissolve(.5)

                g "[name], ¿a qué esperas?"
                "Era Yumi Makeba, la chica de la que estaba enamorada."
                "¿Me habrá escuchado decir eso?"
                g "¿Te encuentras bien, [name]? Pareces afectada por algo."
                "Ante esa expresión de preocupación yo solo sentía alegría, el sentir que Yumi se preocupaba por mí me aceleraba el corazón más que ningún concierto."
                "Estaba claro, no podía dejar este mundillo, Yumi estaba en él."
                "Y yo jamás la abandonaría."
                c "Tranquila, ahora sé que estoy lista."
                "Ella me respondió con una sonrisa."
                "Yumi, a tu lado siento que todo es posible."

                scene bg escenario

                with Dissolve(.5)

                "Sin un atisbo de duda en mi interior, salí al escenario."

                scene bg backstage

                with Dissolve(.5)

                "Después del concierto, Yumi me detuvo en el backstage para hablar conmigo."

                show yumii

                with Dissolve(.5)

                g "Has estado increíble [name], pero ¿seguro que te encuentras bien?"
                c "Po-por supuesto, tú también has estado increíble Yumi, se nota que tienes madera de idol."

                show yumii at center:

                    alpha 0.80

                with Dissolve(.5)

                play music sentimental


                "Sí, eres una gran idol."
                "Mejor que yo incluso, que soy la líder."
                "Tus bailes."
                "Tu voz."
                "Tu belleza."
                "Tú y solo tú."

                show yumii at center:

                    alpha 1

                with Dissolve(.5)

                c "Eres perfecta."
                g "¿Eh?, ¿decías algo?"

                "…"

                stop music

                with hpunch

                "¿HABÍA DICHO ESO EN VOZ ALTA?"
                c "Q-que eres…"
                c "Perfectamente capaz de tomar mi puesto como líder."
                g "…"
                g "Por favor, no digas eso."
                g "Eres la chica más increíble que he visto jamás."
                g "Tus bailes."
                g "Tu voz."
                g "Tu belleza."
                g "Tú y solo tú podrías ser nuestra líder."
                g "Así que, por favor, no digas eso."
                "Me…"

                with hpunch

                "¿ME ESTÁ TIRANDO LOS TEJOS?"
                "No no no no, no te sonrojes."
                "Relájate, relajadita."
                "Solo te está halagando, nada más."
                "Aun así…"
                "Es… "
                "¿Es esto lo que la gente llama felicidad?"
                c "B-bueno, a ver, sí que es cierto que soy b-bastante buena, jejeje."
                g "Por cierto, [name]."
                g "Mañana tenemos el día libre, ¿querrías salir conmigo?"
                g "Conozco una cafetería muy buena que acaba de abrir."
                "…"
                "Esto… Este momento exacto, se llama felicidad."
                c "C-c-claro."
                c "Si no te importa salir conmigo, adelante…"

                with vpunch

                "QUÉ ESTOY DICIENDO."

                with hpunch

                "DEJA DE METER LA PATA."
                "Espera…"
                "Seguro que también ha invitado a Futaba, al fin y al cabo, somo un grupo de tres."
                c "Por cierto, ¿Futaba ya se ha ido?"
                g "Sí, tenía que hacer las maletas pronto ya que mañana va a visitar a su familia."
                "Es…"
                "ESPERA UN MOMENTO."

                with vpunch

                "¿ESO SIGNIFICA QUE ESTAREMOS SOLAS YUMI Y YO?"
                "Cálmate… perfectamente podría ser para hablar de negocios o algo referente al grupo."
                "Ni siquiera sabes si le gustan las chicas."
                c "Bueno, ¿Y a qué se debe el ofrecimiento?"

                with vpunch

                "¿CÓMO QUE “{i}¿A QUE SE DEBE EL OFRECIMIENTO?{/i}” ¿TÚ ERES TONTA?"
                g "Es que me he dado cuenta de que sé muy poco sobre ti, [name]."
                g "Así que me gustaría hablar contigo para conocerte mejor."
                "…"
                "Este sentimiento es…"

                with hpunch

                "FELICIDAD ABSOLUTA."

                scene bg negro

                with Dissolve(.5)

                "Esa misma noche casi no pude dormir pensando en ella."
                "¿Sobre qué podría hablarle?"
                "¿Qué puedo decirle?"
                "…"
                "¿Cómo le digo que me gusta?"

                scene bg dormitorio

                with Dissolve(.3)

                "A la mañana siguiente me debatí mucho entre que ropa ponerme."
                "¿Casual o formal? ¿Sugerente o tapada?"
                "…"
                "Al final me decidí por mi vestido favorito."
                "Hoy es un día especial."

                scene bg cafe

                with Dissolve(.7)

                #Cafe sfx

                "Al llegar a la cafetería no pude evitar fijarme en la estética europea del local."
                "Estaba muy bien cuidada y el olor del café recién hecho era diferente al habitual de todas las mañanas."
                "Antes de que pudiese continuar apreciando ese bello local, oí a alguien llamarme con una voz dulce."

                show yumi

                with Dissolve(.5)

                g "[name], aquí aquí."
                "Era Yumi, llevaba puesto un vestido similar al mío…"
                "Pero a ella le quedaba claramente mejor."
                "No pude evitar pensar en lo mucho que me gustaría quitárselo."

                #Bro, that shit escalated pretty quickly

                "..."
                "NO NO NO NO, NO TE SONROJES, NO PIENSES ESO."
                c "G-gracias por invitarme, la verdad es que no sabía que te gustaban este tipo de locales."
                g "Entonces creo que sabemos muy poco de la otra."
                "…"
                "Ella me dijo eso con una sonrisa, pero yo no podía evitar pensar que, en realidad, salvo por lo profesional, sabía muy poco de ella."
                "Entonces, ¿Estos sentimientos son puramente…?"
                g "Sabes, [name]"
                g "A mí, me hubiese gustado tener una cafetería así, me parece un lugar muy acogedor…"
                c "…"
                c "Ah, entiendo, quieres decir que te gustaría ser bartender o camarera o…"
                c "Espera…"
                c "¿Por qué hablas en pasa…?"
                g "En realidad, yo odio ser idol."
                "…"
                "¿Qué?"
                c "A-a ver, entiendo que este mundillo puede ser apabullante a veces y que no es que sea muy agradable el cómo esos hombres nos miran con ojos lujuriosos, sin contar lo que dicen de nosotras en internet y…"
                c "…"
                c "Pero si lo ves desde un punto de vis…"
                g "Si eso es lo que piensas, ¿Por qué sigues siendo idol?"
                "…"
                "¿Por qué?"
                "…"
                "Por ti Yumi, tú y solo tú me mantienes a flote en esta industria tan cosificada."
                c "Sé que solo somos muñecas para ellos."
                c "Objetos de deseo para sus mentes calenturientas."


                c "Máquinas de merchandising para sus paredes llenas de posters."
                g "Entonces pensamos lo mismo."
                "¿Eh…?"
                "¿Estaba diciendo eso en voz alta?"
                g "¿Sabes, [name]?"
                g "Yo solo busco una vida tranquila…"
                g "Vivir a las afueras, quizás en la costa, y tener mi propia cafetería donde pueda recibir clientes con una sonrisa."
                g "Y quiero…"
                c "..."
                g "Quiero hacerlo a tu lado."
                "Qué…"
                "Se me había declarado, pero más que felicidad lo que sentía era tristeza, porque ya sabía lo que vendría ahora."
                c "Yumi, tú también me gustas."
                g "…"
                g "Entonces escapa conmigo."
                c "Pero Yumi, nuestras carreras de idols enton…"
                g "El manager está buscando una sustituta para ocupar mi lugar en el grupo…"
                c "Espera… ¿Qué?"
                g "A ti nunca te echaría porque eres la cabecilla, pero yo…"
                g "Yo solo sigo en este mundillo porque tú estás en él…"
                g "De no ser así, ya me habría ido hace tiempo."
                g "Sé que no estoy a tu nivel, pero si lo que dijiste en el camerino es verdad..."
                g "Por favor, huyamos juntas."
                "Pero…"

                scene bg negro

                with Dissolve(.2)

                "Pero yo ya tenía mi vida hecha."
                "Iba a ser idol hasta los 25, cuando empezasen a bajar los números me convertiría en manager e iniciaría un nuevo grupo con el dinero que hubiese ahorrado hasta ese momento…"
                "Después, si todo sale bien me jubilaría a los 45, dándole mi puesto a la chica mejor preparada y me centraría en disfrutar del dinero que haya obtenido hasta ese momento, quizás ayudando como experta de marketing a nuevos grupos."
                "Esa es la vida que mis padres planearon para mí cuando me metieron en este mundillo, y esa es la ruta que iba a seguir…"

                scene bg cafe

                show yumi

                with Dissolve(.5)

                "Hasta que te conocí, Yumi."
                c "Yumi, te quiero, y quiero salir contigo…"
                c "Pero ahora mismo llevo una carrera muy prolífica que no puedo aban…"
                g "Por favor [name]…"
                g "Ya no puedo seguir en este mundillo donde todo es falso y nada más que el dinero importa."
                g "Por favor, si de verdad tu amor es real, huye conmigo."
                g "Ahora que Futaba está fuera es nuestra oportunidad, es ahora o nunca."


                menu:

                    "Te seguiré hasta el fin del mundo, Yumi":

                        c "Hagámoslo."
                        "Por primera vez en toda la conversación, Yumi esbozó una sonrisa sincera."
                        "Sentí como si rompiese los grilletes de mi autoimpuesta vida de “ensueño” y me sentí libre."
                        g "Gracias, gracias… gracias [name]."
                        "Con la decisión ya tomada, pagamos la cuenta sin siquiera tomarnos el café que minutos antes tan apetecible se me hacía y nos dirigimos hacia nuestras habitaciones del hotel."

                        scene bg hotel

                        with Dissolve(.5)

                        "Hice las maletas tan rápido como pude, pero no paraban de surgirme las dudas. "
                        c "¿Habré tomado una buena decisión?"
                        c "Estaría tirando todo lo que he construido…"
                        c "…"

                        with vpunch

                        c "NO."

                        with vpunch

                        c "SI ES CON YUMI, SÉ QUE PODRÉ HACERLO."

                        pause(1)

                        scene bg estacion

                        with Dissolve(.5)

                        "A la mañana siguiente hice que el taxi me llevase a la estación acordada, una estación a las afueras, cerca de la costa."
                        "He de admitir que tenía miedo de que me hubiese dejado plantada."

                        show yumi

                        with Dissolve(.5)

                        "Pero el miedo se disipó cuando la vi allí sentada, todavía soñolienta por habernos levantado temprano."
                        c "Hola Yumi, pareces cansada."
                        g "Eh, oh…"
                        g "Hola [name], he estado pensando..."
                        "Uy… ¿Qué ha estado pensando?"

                        play music sentimental

                        g "…en lo mucho que te quiero."
                        g "Quiero conocerte más, quiero vivir a tu vera, quiero llevar una cafetería contigo, quiero…"
                        g "Quiero quererte."
                        c "…"
                        c "Serás tonta..."
                        c "Yo también te quiero, así que no te preocupes, ya sea una cafetería o siendo idol…"
                        c "Yo siempre te querré."

                        show yumi:

                            alpha 0.80

                        with Dissolve(.5)

                        "En ese momento mi teléfono empezó a sonar, era el manager."
                        "Antes de que pudiese cogerle la llamada, Yumi me detuvo."

                        show yumi:

                            alpha 1

                        with Dissolve(.5)

                        g "¿Recuerdas lo que dijiste en el camerino, [name]?"
                        g "No contestes…"
                        g "Tú ya no eres [name] la idol, eres [name], mi novia."

                        hide yumi

                        with Dissolve(.5)

                        "Y así, mientras el teléfono seguía sonando…"
                        "Yumi besó mis labios…"
                        "Y supe que todo estaría bien."

                        jump ending

                    "No puedo abandonarlo todo así sin más":

                        c "Lo siento Yumi, pero yo ya tengo mi vida construida desde los cimientos para este trabajo."
                        g "No… no… por favor."
                        c "Lo siento Yumi…"
                        c "Pero en otro momento, quizás en otro mundo, me hubiese encantado llevar una cafetería contigo."
                        g "Tu también odias este mundo, entonces…"
                        g "¿Por qué?"
                        g "¿Por qué me hiciste creer que tendría alguna posibilidad?"
                        "Mientras oía esas palabras decidí levantar mi derrotada cara…"
                        "Solo para recibir de golpe una imagen que nunca me hubiese gustado ver."
                        "Había hecho llorar a Yumi."
                        c "L-lo siento Yumi, quizás más tarde…"
                        g "No va a haber un ‘más tarde’. "

                        hide yumi

                        with Dissolve(.5)

                        "Diciendo esto, Yumi se levantó y se fue sin siquiera tornarse, dejándome con la cuenta, un café frio y este dolor en el pecho que siento que jamás olvidaré…"

                        scene bg negro

                        with Dissolve(.5)

                        "O eso pensaba…"

                        pause (1)

                        scene bg estacion

                        with Dissolve(.5)

                        "20 años más tarde, en una estación a las afueras me encontré con Yumi de nuevo…"
                        "Ella todavía no me había visto, y yo no sabía con certeza si era ella."
                        "Pero aun así decidí preguntárselo."
                        c "Disculpa, ¿es usted Yumi Makeba?"

                        show yumiv

                        with Dissolve(.5)

                        g "…"
                        "Ella me miró con cara de sorpresa."
                        g "No…"
                        g "No lo…"
                        "Antes de que pudiese terminar esa frase, su cara empezó a tornarse diferente y lágrimas empezaron a caer por su bello rro."

                        g "No, por favor…"
                        g "No puede ser…"
                        c "Eres tú, ¿me equivoco?"

                        hide yumiv

                        with Dissolve(.5)

                        "Antes de que pudiese continuar, ella me abrazó."
                        "Sabía que era ella, pero no sabía nada de ella, por lo que había pasado, lo que había hecho todos estos años…"
                        "{i}Lo que sí sabía…{/i}"
                        c "Todavía te quiero."
                        g "Por favor, huyamos juntas."
                        "{i}…es que nuestro amor sería eterno.{/i}"

                        jump ending


            # Ruta Cachondeo

            label rama1_ruta2:

                hide carta1

                hide carta2

                hide carta3

                "[name] tiene intención de leer la carta en este momento porque la curiosidad de que la firme un tal Willyx le hace mucha gracia."

                "¿Qué persona es capaz de llamarse como el pato de un anuncio de cerveza?"

                #puerta sfx

                "Sin embargo, llaman a la puerta."

                idk "[name], soy yo. ¿Estás ocupada?, ¿puedo pasar?"

                idk "Todavía tenemos un poco de tiempo antes del concierto, así que voy a aprovechar para comentarte un asunto. Siéntate, por favor."

                show adeb at center:

                    alpha 1

                with Dissolve(.5)

                pause (1)

                hide adeb

                show ade at center:

                    alpha 1

                with Dissolve(.5)

                play music ade

                ade "Mira, tengo que serte franca."

                ade "Tú sabes que nuestro grupo de idols, {i}Andaluz Melody{/i}, ha tenido sus momentos de gloria gracias a que '{i}Hay que venir al sur{/i}' llegó al número uno en las listas hace no mucho, y que desde ahí hemos ido subiendo como la espuma…"

                show ade at right:
                    xalign 0.75
                    yalign 1.0

                with move

                "La manager desvía la mirada y termina por llevarse las manos a la cara."

                show ade at center:

                with move

                ade "No te lo voy a esconder más."

                ade "Tenemos una demanda por derechos de autor."

                ade "Yo no lo sabía, pero resulta que tanto nuestro hit como {i}'Sarandonga', 'Que la detengan', 'Salta la rana'{/i} y, bueno, prácticamente todas las canciones que hemos sacado ya estaban registradas…"

                ade "He tenido incluso que despedir a nuestro coach Anfe por no informarme de estas cosas y estar jugando en horas de trabajo al Valorant con Rafa, el profesor de danza urbana."

                ade "Es que siempre tienen que estar enviándose mensajitos a las 6 de la mañana para quedar, y claro, así no me rinden luego entrenando a las idols, y muchas veces ni están."
                ade "Si es que Dios los cría y ellos se juntan."
                ade "A ver, tampoco los puedo juzgar mucho, que lo que ganan no les da ni para una skin del Mercado Nocturno…"
                "Por la cara de desconcierto de [name], la manager entiende que hace mucho que se ha desviado del tema."
                ade "Además, apenas les da tiempo de vida a las idols como para que pueda saber que existen juegos y vicios como el Valorant."

                ade "El tema es que económicamente la agencia de idols está en un aprieto, en números rojos, y eso por no hablar del último escándalo en el que nos metió tu compañera Pauwula."
                ade "Es que otra igual, y yo que no tenía ya bastante con que Ermianime se marchase al grupo rival y me dijese que estaba perdiendo perspectiva profesional, que el grupo nunca iba a triunfar si poníamos a las idols a hacer videorreacciones en YouTube…"

                ade "Perdona, voy ya al grano..."
                ade "Paris ha estado buscando algunas propuestas comerciales que nos ayuden a salir del bache y ha encontrado varias muy interesantes."
                ade "Sinceramente, a mí me llamaba más la atención la del anuncio de San Roque de molletes, pero cree que encajaría mejor con el grupo hacer un acuerdo que tenga que ver con la música."
                ade "Por ello, hoy vas a cantar en el concierto esta canción."

                "La manager le da a [name] la letra en papel de una canción que, en el fondo, parece más un chiste cutre. Entonces, [name] se acuerda de la carta que vio antes y, de hecho, le empieza a sonar demasiado ese chiste…"

                ade "¿Quieres que el grupo haga en formato canción el chiste del pato tecno de Mixta?"

                "La manager asiente con una gravedad bastante cómica."

                ade "Ellos nos lo han ofrecido porque se han dado cuenta de que plagiar se nos da de maravilla. Es una oportunidad de volver al redil del espectáculo sin quedar en ridícu…"
                ade "Bueno, de ganarnos un buen dinerillo."
                ade "Ya está preparada la base tecno y solo tienes que seguir el ritmillo mientras cantas la letra."

                show traje:
                    xalign 0.85
                with Dissolve(.3)

                ade "También he traído conmigo tu outfit inspirado en un pato, por si no te habías dado cuenta."
                ade "Deivi ha hecho un traje impecable, porque parece ser el único que sabe hacer su trabajo."


                hide traje

                with Dissolve(.3)

                ade "Va a ser tu momento solista para brillar. Ninguna compañera, solo tú. Coser y cantar."
                ade "Hemos cosido nosotros."
                ade "Y a ti te toca cantar."
                ade "Tú verás si quieres seguir teniendo el sueldo y los horarios de un camarero español, o peor, que tu manager tenga que hacerse una ruta sentimental."
                ade "Evidentemente, a nadie le interesa, con el sponsor ricachón que me saca 25 años."
                ade "Yo veo la decisión bastante clara."

                hide ade

                with Dissolve(.5)

                stop music


                "La manager sale de la habitación."
                "[name] está contrariada: por un lado, no se siente confiada en poder llevar a cabo una actuación que no ha preparado previamente."
                "Por otro, venderse de esa manera a una empresa le parece ir contra su ideal, su sueño de ser una idol y triunfar únicamente por su talento, uno del que ya no está segura si tiene."
                "[name] se pone el traje y, lo mejor que puede, memoriza las líneas del chiste."
                "En un último suspiro, mira por último la carta que le dejó Willyx y se marcha al escenario."

                scene bg escenario

                with Dissolve(.5)

                "Las luces de los focos la iluminan de manera cegadora y el ruido de un público clamoroso, aunque más callado que en otras ocasiones, dándole el empujón necesario para decidir si cantará ahora."

                menu:

                    "Cantar la canción del Pato Tecno":

                        "[name] está en el escenario preparada. Toma aire y agarra el micrófono. La base tecno comienza a sonar: le taladra los oídos."
                        c "¡Chicooos, espero que lo estén pasando bien!"

                        play music pato

                        c "Para empezar os voy a contar un chiste que he visto por internet…"
                        c "PERO TECNO"
                        "El público está estupefacto."
                        "Quizá piensan que se han equivocado y en lugar de sacar entradas para ver a Andaluz Melody, las han sacado para asistir al Club de la comedia. Y tener esto en la mente ha dejado paralizada a [name]."
                        c "¡Ahora viene! Una, dos y… ¡es-escuchad mi chiste!"
                        "La pose que había visto en los animes de Macross no es la más indicada para este momento, aunque a ella le había funcionado para otros conciertos."
                        "[name] no arranca a cantar el chiste y el único movimiento que hizo hasta entonces no pegaba para nada con el tecno."
                        "El plan no está funcionando."
                        idk "Deja trabajar a las profesionales."

                        show juda at center:

                            alpha 1

                        with Dissolve(.5)

                        stop music
                        "El susurro de su compañera le provoca un respingo que la devuelve a la realidad del escenario. La aparta a un lado y toma el micro en su lugar. No puede ser otra que ella, la única capaz de cantar esto…"

                        play music judah

                        j "¡Chicooos, manos arriba, caderas en movimiento!"
                        j "¡Es el momento de que cantemos el pato tecno!"

                        show juda at center:

                            alpha 0.75

                        with Dissolve(.5)

                        "Con el mismo outfit, pero como si en ella fuese una segunda piel, Judahol comienza a contonear su cuerpo al ritmo repetitivo y glitcheado de la base tecno."
                        "De su melodiosa voz sale el chiste más hermoso que alguna vez [name] escuchó."
                        c "¿Cómo es capaz de convertirlo en música?"
                        with hpunch
                        c "SI SOLO ES UN CHISTE"

                        show juda at center:

                            alpha 1

                        with Dissolve(.5)
                        j "¡Esto es un pato, que va a un bar de pinchos!"
                        "Todos corean con ella el final de cada oración."
                        j "¿¡Y qué le pasa, chicooos?!"
                        with vpunch
                        j "PUES QUE SE PINCHA"
                        j "¡¿Y qué diceeee?!"

                        "El público responde a todo pulmón..."

                        show juda:
                            xalign 0.75

                        with move
                        with hpunch

                        "UY"

                        show juda:
                            xalign 0.25

                        with move
                        with vpunch

                        "AY"
                        show juda:
                            xalign 0.75

                        with move
                        with hpunch

                        "UY"

                        show juda:
                            xalign 0.5

                        with move

                        with vpunch

                        "QUE ME PINCHO"

                        "Ya no queda más letra, pero la idol Judahol continúa su canto improvisando una canción que solo un talento como el de ella podía lograr..."

                        "Una que anima a la liberación de un pato cautivo, presa de las garras de los medios del entretenimiento."

                        "Sin esperarlo, está cantando una crítica feroz a la situación en la que el grupo se encuentra."

                        "¿Podría haberlo conseguido aquella hazaña [name] si no hubiese dudado?"

                        "¿Quizá habiendo hecho cualquier otra cosa hubiera llamado también la atención?"

                        "Ya poco tiene que hacer mientras la seguridad la saca del escenario. Encima de él, solo puede haber una estrella."

                        stop music

                        #Final 1 Ruta Idol

                        jump ending

                    "Improvisar":

                        with hpunch
                        c "NO"
                        with vpunch
                        c "ME MANTENDRÉ FIEL A MIS IDEALES."
                        c "EL QUE TENGA MIEDO A FRACASAR, QUE NO NAZCA."
                        "Con una determinación digna de una idol andaluza, agarró un disco que tenía en uno de los cajones de su camerino y salió directa hacia el chiquillo de la mesa de mezclas que portaba un semi-afro parecido a una coliflor."
                        c "Oye tu, pelo-polla, ya me estás quitando el rollo ese del pato y metiendo este cd."
                        pp "pe-pe-pelo-po..."

                        with vpunch

                        c "¿NO ME ESCUCHAS, SHIQUILLO? PONME EL CD Y RÁPIDITO."
                        "Un aura de superioridad la había obnubilado y su ego estaba disparadísimo…"
                        "La idol dentro de ella había muerto… Y había activado su “forma calle”."
                        "Había recordado porqué entró a este mundillo, no por las idols, sino por las batallas de gallos."
                        "Y este era su momento."
                        c "Ya estoy cansada de ser la muñequita, ahora soy peor."

                        play music eminem

                        "Cuando '{i}Lose Yourself de Eminem'{/i} empezó a sonar de fondo la idol comenzó a dejarse llevar por el flow."

                        c " Escucha bien, que te cuento una historia
                        {vspace=1}
                        De una idol andaluza, que es toda una gloria
                        {vspace=1}
                        Es fan del rap God, y su flow es potente
                        {vspace=1}
                        Hoy va a rapear, sobre su vida exigente."

                        c " La gente piensa, que ser idol es fácil
                        {vspace=1}
                        Pero es todo lo contrario, es un trabajo volátil
                        {vspace=1}
                        Hay que bailar, cantar, sufrir y sonreír
                        {vspace=1}
                        Pero detrás de cámaras, todos se quieren morir."

                        c " Los ensayos son largos, y el estrés es constante
                        {vspace=1}
                        La dieta es estricta, y el sueño es un talante
                        {vspace=1}
                        Los fans son maravillosos, pero también son exigentes
                        {vspace=1}
                        Hay que estar siempre en forma, y sin resfriados pendientes."

                        c " Pero que sepáis todos que lo llevo con pasión
                        {vspace=1}
                        Soy una artista completa, y lo hago con emoción
                        {vspace=1}
                        Hoy voy a rapear, y lo haré con estilo
                        {vspace=1}
                        Porque la vida de una idol, no es un camino sencillo."

                        c "Así que mueve tus caderas, y levanta las manos
                        {vspace=1}
                        Disfruta de la música, y de los buenos momentos
                        {vspace=1}
                        Pero no olvides, que detrás de todo esto
                        {vspace=1}
                        Hay un trabajo arduo, y un esfuerzo constante, eso es cierto."

                        c "Por eso, hoy estoy rapeando, con una sonrisa en el rostro
                        {vspace=1}
                        Para demostrarte, que ser idol no es sólo un gusto
                        {vspace=1}
                        Hay que trabajar duro, y tener una gran pasión
                        {vspace=1}
                        Para brillar en el escenario, hay que tener corazón."

                        "El público se quedó atónito ante tal despliegue."

                        #aplausos

                        "De repente, alguien empezó a aplaudir, y ese aplauso se expandió entre el resto del público."
                        "Y esa persona que comenzó el aplauso..."

                        show eminem at center

                        "Era Eminem himself, the OG Slim Shady."

                        play sound good


                        e "Hey, you're pretty good."


                        c "E-Eminen."
                        e "Your palms might be sweaty, but you are DAMN ready to drop bombs, girl."
                        c "N…"
                        c "No entiendo ni jota, pero me gustan mucho tus instrumentales."
                        e "You go big girl."
                        c "Ay… es que es tan moooono."
                        "Sin duda alguna en sus ojos, se lanzó hacia el público para alcanzarle cuando…"

                        stop music

                        scene bg techo

                        with Dissolve(.5)

                        with vpunch

                        "THOMP"
                        c "¿Dónde estoy?"
                        "Ah bueno, que todo resultó ser un sueño, y se acababa de caer de la cama."
                        c "AAAAAAAAAAAAAARGH…"
                        c "..."
                        c "Yo quería seguir en el sueñito."
                        "…Pero no podía, era maestra de lengua y resulta que la clase había empezado…"

                        with hpunch

                        c "HACE CINCO MINUTOOOOOOS"

                        jump ending


            # Ruta Meta

            label rama1_ruta3:

                hide carta1

                hide carta2

                hide carta3


                "El día que recibí una carta negra, ese día, unas palabras cambiaron mi vida. "

                scene bg negro

                with Dissolve(.3)

                show carta3:
                    zoom 0.75
                    xalign 0.5
                    yalign 0.5

                with Dissolve(.5)

                play music tension

                "Era una carta muy hermosa, enserio, parecía como las famosas cartas que se les daban al ducado francés o inglés cuando alguno de la realeza se casaba."
                "Cartas llenas de ornamentación que parecían de oro, perfumadas, con pequeños pétalos de flores dentro y atada con una hermosa cinta."
                "Era la carta más bella que alguna haya visto. "

                "Lo único que no me gustaba es que era algo difícil de leer, tanto la letra como el papel de color negro. "
                "Solo resultaba legible cuando acercabas lo suficiente la mirada al papel para ver las marcas de impresión. "
                "Pese a su belleza, nunca se la mostré a nadie, ni a mi Manager ni a mi grupo. Era mi más preciado tesoro. "

                scene bg camerino

                with Dissolve(.3)

                "El día que la leí supe que mi voz era lo más importante que le podía compartir a otros en este mundo. "
                "Y hoy, a fecha del aniversario del día que decidí que todos me miraran al ser una idol y que es casualmente la misma fecha en el que hice mi primer concierto. "
                "El día de este nuevo concierto, el más grande que hemos tenido. "
                "Por eso hoy quiero contarles a todos mis fans aquellas palabras de esta carta negra, que me motivaron a estar con ellos este día. "
                "Este será el concierto más emotivo que he dado. "
                "Y así, dio comienzo el concierto. "

                stop music

                scene bg escenario with Dissolve(.4)

                "Entré con mi grupo como siempre lo he hecho, hace tiempo que dejé de ser la más popular de las cuatro, no me molesta. "
                "He de admitir que hasta a veces siento que me menosprecian. "
                "Aun así cada vez que practicamos siento su esfuerzo, sus ganas, y su pasión me alcanza y me motiva a mantenerme con ellas. "
                "No suelen decir mucho mi nombre, pero cuando lo hacen siento que lo dicen con la mayor de las admiraciones, como si todas me debieran su fama gracias a mi talento. "
                "Sé que es mentira, soy la peor de las cuatro, además que mi popularidad va en descenso, ya ni si quiera recibo tantas cartas. "
                "Generalmente solo sigo las órdenes, no propongo nada porque ellas parecen cegadas por el éxito y qué puedo decir, funciona, solo miren este concierto. "
                "Los gritos de los fans vitoreando nuestros nombres, los nombres de las cuatro. "
                "Todas sonreían al escucharlos. "

                g0 "Tenemos un gran anuncio por este gran concierto y por tan especial ocasión."
                "Ese es el pie a la lectura de mi carta, lo comentamos antes de empezar. "
                "Todas asintieron, les parecía una gran idea y luego hicimos lo que siempre hacíamos antes de todos los conciertos. "
                "Juntar las manos y decirnos “Esforcémonos.” Por alguna razón siempre sentía que las manos de ellas temblaban cuando yo ponía la mía encima. "
                "Serán los nervios. "

                "Después del gran grito del público por la emoción del anuncio, cogí mi micrófono, pasé al frente de la tarima y hubo un silencio expectante por unos segundos. "
                "Mientras abría la carta todo el mundo lucía emocionado, mis compañeras lucían algo nerviosas. "
                "Y yo lucía como la persona más decidida del planeta. "

                "Recuerdo haber leído la carta unas 100 veces el día que la abrí, era corta y hasta la memoricé de lo mucho que me afectó. Por eso desde ese día no la había abierto, porqué quería que el momento que la volviera a leer fuese especial. "
                "Les mencioné a todos que les iba a leer una carta de un fan que me motivó a ser la cantante que soy hoy, y que quería que sus palabras también los motivaran a todos… "
                "Grité alto y claro. "
                "¡AQUÍ VOY! "
                g0 "PARA REEMPLAZAR A [name], QUEREMOS ANUNCIAR A LA NUEVA MIEMBRO DE NUESTRO GRUPO MUSICAL HOY AQUÍ EN ESTE CONCIERTO. "
                "El público gritó de juvilo."

                c "¡¿QUÉ?! "

                "Me desplomé."


                g0 "Sé que es una decisión algo inesperada pero las 3 sabemos que ya era el momento."
                "{sc}¿Acaso fue por querer leer mi carta?{/sc}"

                show juda

                with Dissolve(.4)

                g0 "Reciban con un fuerte grito a la nueva integrante."
                "{sc}¿Era acaso mucho pedir ser la protagonista por un momento?{/sc}"


                j "Sé que será muy difícil superar el legado de [name] pero daré mi mejor esfuerzo. "
                "{sc}Yo solo quería leer mi carta.{/sc}"

                g0 "Sé que lo harás, juntas lo haremos y contamos con el apoyo de todos ustedes ¿No? "
                "{sc}¿Por qué me hacen esto?{/sc}"

                g0 "Esperamos que la apoyen tanto como apoyaron a [name]."

                scene bg negro

                "Cállense, CÁLLENSE."

                with vpunch

                "¡CÁLLENSE TODAS!"

                "La carta, la carta… tengo que leerla, VOY A LEERLA, YA NO ME IMPORTA EL CONCIERTO, MI TRABAJO O MIS AMIGAS."


                with hpunch

                "YO"

                "SOLO"

                "QUIERO"

                "LEER"

                "MI"

                with hpunch

                "CARTA."

                scene bg escenario

                with Dissolve(.2)

                show carta3:
                    zoom 0.75
                    xalign 0.5
                    yalign 0.5

                with Dissolve(.3)

                "Sin más demora, comencé a leer la carta."
                "”Mírate.” "
                "“Oh, por favor, mírate.” "
                "“Quiero que sus ojos solo te miren a ti.” "
                "“¿Te has vuelto más hermosa?” "
                "“¿Seguro te debes sentir muy linda con tu uniforme?” "
                "“¿Gustarías de cantar otra canción?” "
                "“Espero que sí, porque amo tu voz, [name]. ” "
                "“Y haré cuanto haga falta para que todos te amen.” "
                "“Sé qué eres la mejor y sé que brillarás más que cualquier otra.” "
                "“Así que por favor, sigue esforzándote.” "
                "“Creo en ti más que en nadie, gana su atención.” "

                show carta3:
                    alpha 0.95

                with Dissolve(.3)
                "“Gana su atención.” "

                show carta3:
                    alpha 0.75

                with Dissolve(.3)

                "“Gana su atención.” "

                show carta3:
                    alpha 0.55

                with Dissolve(.3)

                "“Gana su atención.” "

                show carta3:
                    alpha 0.35

                with Dissolve(.3)

                "“Gana su atención.” "

                show carta3:
                    alpha 0.15

                with Dissolve(.3)

                "“Gana su atención.” "

                show carta3:
                    alpha 0.1

                with Dissolve(.3)

                scene bg negro

                with Dissolve(.1)

                with hpunch

                "GANA SU ATENCIÓN. GANA SU ATENCIÓN. GANA SU ATENCIÓN. GANA SU ATENCIÓN. GANA SU ATENCIÓN. GANA SU ATENCIÓN. GANA SU ATENCIÓN. GANA SU ATENCIÓN. GANA SU ATENCIÓN. GANA SU ATENCIÓN. GANA SU ATENCIÓN. GANA SU ATENCIÓN. GANA SU ATENCIÓN. GANA SU ATENCIÓN. GANA SU ATENCIÓN. GANA SU ATENCIÓN."


                "Por favor, que esto gane la atención de alguien..."

                "..."

                "En realidad, después de leer la carta ella había decidido que no podía cumplir las expectativas de sus fans, que su talento le parecía insuficiente para tales palabras, que no las merecía. "
                "Pero una idol siempre tiene que cumplir las expectativas de sus fans. "


                "Así decidió quitarse la vida, sabiendo que tal hecho traería fama nacional a su grupo por lo trágico del suceso. "
                "Después de ello la comunidad nacional quiso apoyar a las chicas y le brindaron toda su atención, hasta volverlas uno de los grupos más grandes del mundo. Hoy es el concierto del aniversario de su compañera. "
                "Ojalá ella estuviera aquí para vernos y verse a sí misma, contemplar lo mucho que hemos logrado gracias a ella. "

                scene bg escenario with Dissolve(.5)

                g0 "Hoy es el aniversario de nuestra querida [name]. "
                g0 "Descubrimos una carta negra que creemos que la motivó a tomar la decisión, nunca la pudimos leer porque la sangre la dejó ilegible. "
                g0 "Pero ella nos dejó unas palabras escritas antes de despedirse, “Ganen su atención”. "
                g0 "Por favor sigan dándonos su atención, así nosotras podemos seguir honrándola. "
                g0 "No la defraudaremos, donde sea que esté. "
                g0 "Así que, ¡Gracias a todos por asistir al concierto del aniversario de la muerte de [name]!"

                jump ending

label rama2:
    # Rama 2

    with vpunch

    c "¡DECIDIDO!"

    stop music

    "Al levantarse de sopetón, la montaña de cartas que había delante suya se desplomó, desperdigándose sobre el suelo."

    show carta1 at left:
        zoom 0.35
        yalign 0.5


    with Dissolve(.5)


    "Una de ellas tenía un corazón sellándola, lo cual le pareció un gesto tierno."

    show carta2 at center:
        zoom 0.35
        xalign 0.5
        yalign 0.5

    with Dissolve(.5)

    "Otra de ellas, un verde lima, le causó cierta gracia."

    show carta3 at right:
        zoom 0.35
        yalign 0.5

    with Dissolve(.5)

    "Y otra carta, completamente negra, hizo que le recorriera un escalofrío por la espalda."

    menu:

        "Qué carta más cuqui...":

            jump rama2_ruta1

        "Qué carta más simpática...":

            jump rama2_ruta2

        "Qué carta más tétrica...":

            jump rama2_ruta3

            # Ruta Sentimental

            label rama2_ruta1:

                hide carta1

                hide carta2

                hide carta3

                play music signal

                "Tenía la sensación de que debía leer esa carta, incluso aunque mis responsabilidades me llamasen física y mentalmente."

                "La carta, como muchas otras venía de un fan. Una persona cualquiera cuyos días se habían hecho más amenos gracias a escuchar nuestra música y ver nuestros bailes."

                "Nada nuevo."

                "Pero lo que más me llamó la atención fueron un par de líneas en particular:"

                "{i} Hace unos años tenía muy claro que [name] era mi integrante favorita. Pero lo pienso hoy... Y no lo tengo tan claro.{/i}"

                "{i}Me sigue gustando el grupo, pero es verdad que las nuevas canciones no me gustan tanto. No siento la misma pasión que con las de hace 3 años.{/i}"

                scene bg negro

                with Dissolve(.5)

                c "Jijiji..." (what_size=12)

                "Me estaba riendo en voz baja porque finalmente lo había entendido. No era algo que solo sentía yo."

                "El grupo estaba cayendo, y yo lideraba este salto al vacío."

                "Ya lo había decidido antes, pero ahora lo sentía con más fuerza que nunca."

                "Tengo que largarme de aquí. Empezar de nuevo en otra parte. Ser actriz era un trabajo similar y siempre me había hecho ilusión salir en alguna película o serie."

                stop music

                scene bg camerino

                with Dissolve(.5)

                "Todavía no me había puesto el traje de Idol y la mayoría de aparatos que nos hacían falta eran propiedad del edificio. Así que solo tenía que levantarme, coger 4 cosas y salir por la puerta."

                show manager

                with Dissolve(.5)

                m "Oye [name], de verdad que te tienes que dar prisa, solo quedan 5 minut..."

                "Mierda."

                m "¿Pero a dónde vas? El espectáculo va a comenzar."

                c "A mi casa."

                m "¿Qué? ¿Te has dejado algo muy importante o qué?"

                c "No, nada. Simplemente dejo esto de ser Idol."

                "Hubo una lapso de 5 segundos donde ninguno dijimos nada. El manager estaría pensando qué decir."

                m "Mira, lo que sea que tengas que discutir que por lo menos sea después de este concierto."

                c "No. Que le den."

                m "¿Pero qué te pasa de repente? Antes estabas como siempre."

                play music tension

                c "Lo que pasa es que ESTOY CANSADA."

                show manager:
                    alpha 0.80
                with Dissolve(.3)

                "No quería alzar la voz demasiado pero como el manager dijera alguna estupidez más, iba a explotar."

                c "Ya no siento lo mismo que cuando empecé. Por un golpe de suerte el grupo tuvo un pico de éxito con el segundo álbum y desde entonces solo hemos intentado recuperar esa gloria."

                c "Pero las cosas pueden tener un final. La gente se ha ido a escuchar otros grupos. Está bien."

                c "Ni el dinero ni la fama me van a quitar esa sensación de desasosiego cuando me muera y vea que he desperdiciado parte de mi vida interpretando a un cádaver viviente."

                c "Eso es todo."

                hide manager with Dissolve(.3)

                "Al final pasó lo que me veía venir y justo cuando iba a abrir el pomo de la puerta a la salida trasera, escuché a mis compañeras venir por detrás."

                show yumii:
                    xalign 0.27
                    yalign 0.5
                with Dissolve(.4)

                show idol2:
                    xalign 0.73
                    yalign 0.5
                with Dissolve(.4)

                g "Hola..."

                "Pude notar por su tono de voz que Yumi estaba preocupada."

                j "Escuchamos cosas y quisimos venir a ver qué ocurría."

                "..."

                menu:

                    "Despedirse":

                        "Decidí darme la vuelta un poco."

                        c "Yumi, Juda... Gracias por vuestra compañía."

                        c "Sois el motivo de que no vaya a recordar estos últimos años con amargura."

                        "Me estaban entrando ganas de llorar pero antes tenía que decir una última cosa..."

                        c "Me hicisteis feliz."

                        stop music

                        jump ending

                    "Marcharse sin decir nada":

                        stop music

                        scene bg salida

                        with Dissolve(.3)

                        "Abrí la puerta y salí corriendo."

                        "Admito que no fue la acción de adulta responsable más apta para esta situación."

                        "Pero creo que lo mejor tanto para mí como para ellas es que nos olvidemos de esto cuanto antes posible."

                        "Sería gracioso que me reemplazasen por otra chica que consiga traer un viento de aire fresco al grupo."

                        "Me alegraría bastante."

                        "Sin embargo, eso ya no es asunto mío. Ahora solo queda mirar al horizonte y ver qué me depara el futuro."

                        jump ending


            # Ruta Cachondeo Actriz

            label rama2_ruta2:

                hide carta1

                hide carta2

                hide carta3

                c "Decidí abrir esa carta que me llamaba tanto la atención y comencé a leerla."

                play music cachondeo

                "” Mira killo, una cosita to viadesí...”"
                "” Que resulta resultón tener que pedirte peticiones a una idol idealizada...”"
                "” A ver, párate que te me quieres parar que se me esta liando la liandera...”"
                "” Lo que quiero decir eh...”"
                "” TENGO UNA OBRA DE TEATRO AHÍ PUTAMADRE CON SUS COSAS Y DEMÁS...”"
                "” Pero me falta la estrella...”"
                "” Y eres bella...”"
                "” ¿Me sigue la rola?”"



                c "Está muy mal escrita."
                "Pero aun así algo dentro de mí, algo que llevaba mucho tiempo dormido..."
                "¡DESPERTÓ!"
                c "Espera un momento..."
                c "¿Qué coño hago siendo idol?"
                c "Si yo quería interpretar a Shakespeare..."
                c "Ganarme a Broadway."
                c "Cómo me decía mamá:"
                "Si se te quema el caramelo, nunca tendrás tu puchero en orden."
                c "¡CLARO!"
                c "Ahora entiendo las palabras de mamá."
                c "¡ACEPTARÉ ESE PAPEL!"
                m "[name], sal a la de ya, el concierto va a empezar y..."

                with vpunch

                "Abrí la puerta con la fuerza de mil soles."

                scene bg backstage

                with Dissolve(.3)

                show  test

                m "[name], te necesitamos..."

                with vpunch

                c "Ahora no, tengo un papelón que cristalizar."
                m "Espera, ¿Has vuelto a tomar drogas?"
                i "Menos mal [name], el concierto va a... "

                with vpunch

                c "Ahora no, tengo un pantalón que criminalizar."

                with hpunch
                ii "¿Te has cagado encima?"

                hide test

                show juda
                j "Oh, [name], ahora..."

                with vpunch
                c "Ahora no, tengo un petrolero que contra-señalizar."

                with hpunch
                j "¿Quieres estrellar un petrolero?"

                with vpunch

                scene bg escenario
                b "Oh, esa es [name], vitoreadla todos para... "

                with hpunch
                c "AHORA NO, TENGO UN PERMATRAGO QUE CROTOLAMIZAR."
                b "..."
                b "Espera... ¿Pero que es...?"

                scene bg negro with Dissolve(.5)

                "Y así, pasaron 579 trillones de años..."
                "El universo se reinició y una versión alternativa de mí misma estaba lista para llevar a cabo la obra de teatro... "

                stop music

                scene bg calle

                with Dissolve(.5)

                "Lo que no esperaba era que..."
                c "Ay ay ay ay..."
                c "LLEGARÉ TARDE A LA OBRA..."
                "Hallándome yo misma para mí de mi persona corriendo calle abajo camino al teatro con un cacho de pan bimbo en la boca..."

                with hpunch

                "PLAF"
                c "Oh oh uy..."
                c "Lo siento, yo solo..."

                show hol with Dissolve(.5)

                play music pato

                ph "Uy ay uy..."
                ph "m’epinchao."
                "Había chocado con un pato bastante chunda chunda."
                "Pero... por alguna razón... ese pato... era..."
                "TAAAAAAAAN..."
                "PERO QUE TAAAAAAN..."
                "..."
                "¿Sexy?"
                "Su ritmillo sabrosón me estaba nublando el juicio."
                "Espera..."

                with vpunch

                "SERÁ ESTO..."

                with hpunch

                "HUMOR"

                with vpunch

                "No..."

                with hpunch

                "PUDOR"
                "..."
                "Nah..."
                "..."

                with vpunch

                "¡LA OBRA!"
                "..."
                "Creo que tampoco..."
                "Espera..."

                with hpunch
                "¡QUE LLEGO TARDE! "
                c "Lo siento Pato extrañamente sensual, pero llego tarde a mi obra."
                ph "¿Tu obra...?"
                ph "..."

                with vpunch

                ph "¿ACASO ERES DIOS?"
                c "No no no, una obra de tea..."
                ph "Dios no sé, pero sin duda eres un ángel."
                "..."
                "El pato buscaba lio..."
                "Y siendo honestos..."
                "Yo también... "

                with hpunch

                c "PERO NO ES MOMENTO PARA ESTO."
                c "Necesito llegar al teatro..."

                with vpunch

                c "SEA COMO SEA."
                ph "¿Tú también vas al teatro?"

                with vpunch

                c "SÍIIIII"
                ph "Yo tengo que hacer de héroe en una obra de teatro infantil hoy..."
                ph "Pero es que en las obras infantiles no me dejan poner trrrrrremendo chunda chunda."
                ph "Y me ha entrado una pereza brutal."
                c "Te comprendo, noble pato discotequero entretenedor de infantes..."
                "Espera... "
                c "¿Tú eres el sustituto del héroe?"
                ph "Sí..."
                ph "No..."
                ph "Quizás..."
                ph "No lo sé."
                ph "Puedes repetir la pre..."

                with hpunch

                c "VÁMONOS A LA OBRA AHORA MISMO. "

                with vpunch

                c "NO PIENSO DEJAR QUE OTRO HOMBRE ME DEJE PLANTADA..."
                ph "Me gusta tu decisión, noble creadora de todo lo conocido y por conocer..."
                "Y así, mientras arrastraba a mi obra a aquel estúpido y sensual pato tecno..."
                "...no pude evitar pensar en la bronca que me echaría la directora."

                stop music

                scene bg backstage with Dissolve(.5)


                "Pero, sin embargo, al llegar al backstage..."
                z "Moza..."
                z "Oye, moza."
                "Me llamaba con una voz amable..."
                "Me esperaba lo peor."
                c "¿S-sí, directora?"
                z "Sabes que te quiero como a una hija ¿verdad?"
                c "S... ¿Sí?"
                z "Y le prometí a tu madre que te cuidaría como si fueses mía."
                c "..."
                c "Sí, me acuerdo de aquella conversación entre mi madre y usted."
                z "Sí..."
                z "Una pena que muriese al caer al puchero de caramelos..."
                c "Ya..."
                z "Pero bueno, la vida sigue..."
                z "Ahora moza..."

                with vpunch

                play music cachondeo

                z "¡SAL AHÍ Y CÓMETE EL MUNDO!"
                with hpunch

                show hol

                ph "¿C-COMERSE EL MUNDO?"
                ph "¿PERO NO ERAS UNA CREADORA?"

                show hol:
                    alpha 0.90

                with Dissolve(.1)

                z "Maravilloso, ha llegado el suplente."
                c "Espere, ¿y el actor original?"
                z "Muerto."

                with vpunch

                c "¿Q-QUÉ?"
                z "O si no está muerto, más le vale estarlo."
                c "Ah bueno, pues que se cuide."
                z "Pato, sales en la próxima escena..."
                z "..."
                c "..."
                z "¿Pato?"


                show hol:
                    alpha 1.0

                show cono at right


                with vpunch
                ph "MIRAD QUE CAPIROTE MÁS GUAPO ME HE ENCONTRADO."
                with vpunch
                ph "ES QUE ME PATO FLIPA."
                z "Deja ese capirote y ponte la ropa anda..."
                "Sin más dilación, salí al escenario."

                scene teatro

                show kaiju3:
                    zoom 0.75
                    xalign 0.5
                    yalign 0.5

                with Dissolve(.5)


                d "¿Ayer cené bocadillo o pasta?"
                "El dragón que había iniciado la obra parecía un poco perdido así que decidí improvisar un poco para darle pie a que dijese sus líneas."
                c "Oh, terrorífico dragón."
                c "No me devores."
                c "Pues soy demasiado deliciosa."
                c "Y te extasiaría."
                "Tras decir esa, si se me permiten el atrevimiento, maravillosa frasecilla sacada de la manga..."
                "El dragón ni me miró..."
                "Se quedo ahí como un pasmarote..."
                d "Uy, esa chica tiene los cordones desatados..."
                d "Oye, tú, que tie..."

                with vpunch

                "HABÍA CAPTADO SU ATENCIÓN." #shake
                c "Oh, malvado dragón."
                c "Que será de mí sin un héroe para vencerte."

                show pato medieval at right with Dissolve(.3)

                "En ese momento entró el pato vestido de héroe de fantasía..."
                "Ese traje tan apretado hacía que se le notasen sus tecno-pectorales aún más de lo normal."
                ph "Cuan promiscua ha sido mi aventura, de cazar a un goblin a un dragón de gran envergadura."
                ph "Más al ver la figura de la damisela de lado, no cabe duda... me he enamorado."
                ph "Ahora la bella dama ha de decidir."
                ph "O el dragón con déficit de atención o el héroe al que le queda mucho por vivir."
                "Eh..."

                with hpunch

                "ESPERA..." #shake

                with vpunch

                "ESTO NO ESTABA EN EL GUIÓN." #shake
                c "Si he de decidir, no me gustaría morir."
                "Uy, sin haberlo planeado..."

                with hpunch

                "AHORA NO ES MOMENTO PARA ESO." #shake
                "Tengo que pensar. "
                "¿Hago que el pato mate al dragón y sigo el guion o elijo quedarme con el dragón que no ha hecho nada malo...?"


                menu:

                    "El dragón es bastante mono en su estupidez.":
                        c "Oh gran dragón, creo comprender su pasión. "
                        c "Usted no busca dolor o gloria. "
                        c "Sino persistir narrando su historia. "
                        d "..."
                        d "¿Qué...?"
                        c "Oh gran dragón, si me caso con usted... "
                        c "¿Me daría su tesoro?"
                        d "Ah, la caja esa..."
                        d "Sep... por qué no..."
                        d "Eso que me ahorro..."

                        show pato medieval at right

                        ph "WOWOWOWOWOW, quieto parao."
                        ph "¿Y el guion...?"
                        c "Esta no es su misión. "
                        c "Oh noble pato."
                        ph "Mira, yo me voy yendo, ya si tal vosotros..."

                        hide  pato medieval with Dissolve (.3)
                        c "Oh noble pato, gracias por aceptar nuestro amor."
                        d "Oye... "
                        d "¿No querías el cofre?"
                        c "Oh gracias gran dragón."
                        "Sin más dilación, me dispuse a abrir el cofre en el que se encontraban las riquezas del dragón."

                        stop music

                        hide kaiju3

                        show cofre

                        with Dissolve(.4)

                        "..."
                        "¿Un capirote?"

                        jump ending

                    "PATO PATO PATO PATO":

                        stop music

                        "De repente, todos los actores se detuvieron en seco cual robots..."
                        "...Y mostraron unos carteles que decían:"


                        scene nolosie with Dissolve(.5)

                        pause 10


                        jump ending


            # Ruta Meta Actriz

            label rama2_ruta3:

                hide carta1

                hide carta2

                hide carta3

                "Decidí leer esa tétrica carta negra y..."

                play music creepy

                " ”Hola querida, iré al grano, quiero comprarte.”"
                c "..."

                with hpunch

                c "¿QUÉ?"

                "”No me importa el precio, te quiero toda para mí.”"
                "”¿20 millones?”"
                "”Los tengo.”"
                "”¿30 millones?”"
                "”No me importa el precio, solo me importas tú.”"
                "”Tú y solo tú.”"
                "”Necesito tenerte, te necesito ahora.”"
                "”Llevo siendo fan tuya desde tu debut, eres lo único que amo en este mundo."
                "”El dinero no es problema, lo único que quiero es...”"

                scene bg negro

                with Dissolve(.5)

                "”{sc}Arrancarte esa ropita de furcia y hacerte toda mía.{/sc}”" #sfx mieo

                scene bg camerino

                with Dissolve(.5)
                "Estaba a punto de vomitar."
                "¿De verdad estos eran nuestros fans?"
                "¿De verdad esta fama era lo que buscaba cuando era una niña?"

                with vpunch

                "NO NO NO NO NO NO NO NO NO."


                "Aún con ganas de vomitar tras lo que había leído, salí corriendo de allí dejando a mis compañeras atrás."
                "..."

                stop music

                scene bg negro

                with Dissolve(.5)
                "Y así pasaron 2 meses..."
                "En ese tiempo decidí que quería ser actriz, al fin y al cabo, las actrices son más respetadas que las idols..."
                "O eso pensaba..."
                "Una cosa tenía por segura, jamás volvería a casa, volver mi pueblo natal sería como tirar por tierra todo lo que había construido."
                "Aún así el huir de un concierto no es que te dé mucho caché, así que prácticamente tuve que empezar de cero."

                scene bg piso

                with Dissolve(.5)

                "Por suerte una de mis amigas de la infancia, Judah, había empezado su carrera de actuación hace poco, y su otra compañera de piso, Yumi, parecía bastante maja."
                "Yumi era una actriz veterana cuyos momentos de gloria ya habían pasado y solo la aceptaban en telenovelas."
                "Aun así, ella conseguía mantener el piso donde residíamos así que le estábamos muy agradecidas... Aunque a mí me tocase dormir en el sofá."
                "Hasta que un día..."

                show yumiv:
                    xalign 0.27
                    yalign 0.5
                with Dissolve(.4)

                show idol2:
                    xalign 0.73
                    yalign 0.5
                with Dissolve(.4)

                play music alegre

                g "Chicas, me han dado un nuevo papel en “{i}Lo que pasó tras el café{/i}”"
                g "Necesitan a un extra para la escena de la cafetería de mañana."

                with hpunch

                c "¡No puede ser!"
                c "¿Qué les has dicho?"

                jj "Yo no voy a poder tomarlo, mi novio me ha invitado a conocer a sus padres."
                c "Espera…"
                c "¿Desde cuando tienes novio?"
                jj "Desde hace 6 meses, más o menos, estaba fuera por trabajo."
                c "¿Y por qué nunca me lo dijiste?"
                jj "Pues porque no sabía si iba en serio, me ha invitado a casa de sus padres así que estoy nerviosi..."
                g "Chicas chicas... "
                g "El trabajo..."
                jj "Creo que le vendrá mejor a [name], al fin y al cabo, yo no podré."
                jj "Además, ya llevas un tiempo sin tener un papel en una serie."
                c "Judah..."

                with vpunch

                c "GRACIAS GRACIAS GRACIAS."


                scene bg cafe

                with Dissolve(.5)

                "Al día siguiente me preparé para mi papel cuando me fijé en que, no solo yo era un extra, sino que también Yumi lo era..."
                "En ese momento pensé..."
                c "¿De dónde sacará el dinero para el piso?"
                "No tenía nada que perder así que decidí preguntárselo tras el rodaje."

                show yumiv with Dissolve(.4)

                g "Oh, verás, es que los trabajos que más me pagan y los más importantes son por la noche."
                g "Ya sabes, escenas a la luz de la luna o esperando al tren de medianoche."
                g "Ahí es cuando de verdad me luzco."
                c "Ajá, es decir que luces mejor cuanta menos luz hay..."

                with vpunch

                g "Oye chiquilla, ¿te recuerdo que vives en mi piso?"


                c "..."
                "En ese momento me recorrió un escalofrío por la espalda."
                g "Pfffff..."

                with vpunch

                g "JAJAJA"
                g "Me parto contigo."
                c "Sí, jeje..."
                g "Bueno, tú vuelve ya a casa que yo ahora me voy al trabajo de por la noche."
                c "Claro, buena suerte con eso."
                g "Yo no necesito suerte, soy toda una profesional."

                stop music

                scene bg negro

                "Volví al piso sin saber lo que de verdad significaban esas palabras."

                scene bg tf

                with Dissolve(.4)

                with vpunch

                "..." #sfx telefono
                "Por la noche, el teléfono del salón me despertó."
                idk "Hola, ¿Eres [name]?"
                c "¿Quién pregunta?"
                n "Soy yo, el novio de Judah."
                n "¿La has visto hoy?"
                c "¿Eh?"
                c "¿No iba a ir contigo a casa de tus padres?"
                n "Es que lleva todo el día sin coger el teléfono, así que... "
                n "Espera..."

                with hpunch

                n "¿TÚ TAMPOCO LA HAS VISTO?"
                c "N-no, creí que ya se había ido contigo y..."
                n "Oh joder, no puede ser..."
                n "Espera, ¿y la otra vieja bruja que vive con ustedes?"
                n"¿Ella sabe algo?"
                n"¿Vi-vieja bruja...?"
                "¿Se refiere a Yumi?"
                c "Ahora está trabajando, llegará más tarde."

                with hpunch

                n "NO PUEDO ESPERAR."

                with hpunch

                n "LO DENUNCIARÉ A LA POLICÍA."
                c "Espera, ella ya está crecidita, no creo que la hayan secuestrado o..."
                n "Oh Dios no, esto no puede estar pasando..."
                c "A ver, lo primero tranquilízate, yo soy la primera que está preocupada por Judah."
                c "Te llamaré si vuelve hoy a casa o algo."
                n "No..."
                n "No puedo esperar..."
                "En ese momento colgó el teléfono..."
                "Espera, entonces..."
                "¿Qué había pasado con Judah?"
                "Nada más colgar el teléfono, este volvió a sonar..."

                show test:
                    alpha 0.5
                    xalign 0.35
                with Dissolve(.4)

                m "Buenas noches, Yumi, no me cogías al teléfono así que te lo digo por aquí..."
                "No dije una palabra, me limité a escuchar."
                m "Mira, iré al grano, hoy vienen unos invitados muy importantes desde Hollywood, California y me preguntaba si..."
                m "Bueno, ya sabes, ¿Podrías mandarme a una de tus chicas para un “trabajo muy especial”?"
                m "Cómo siempre el dinero irá directito a tu bolsi..."
                m "Espera... "
                m "¿Yumi?"
                "Tenía muchas preguntas sobre lo que acababa de decir, a lo cual yo, sin pensarlo mucho, simplemente respondí..."
                c "Yumi no está en casa ahora mismo."
                c "¿Necesita hablar con Yumi?"
                m "..."
                m "..."

                with vpunch

                m "POR SUPUESTO, ASÍ ES, NECESITO HABLAR CON ELLA..."


                m "Ahora, si me disculpas, he de volver al trabajo."

                hide test

                with Dissolve(.5)
                "Y colgó..."


                "“Trabajo muy especial”, no, no..."
                "NO NO NO NO NO NO NO NO..."
                "NO PIENSES ESO NO PIENSES ESO NO PIENSES ESO."
                "No puede ser que Judah..."
                "NO NO NO NO NO."
                "Me quedé despierta toda la noche hasta que, llegadas las 4 de la madrugada, la puerta se abrió."

                scene bg piso oscuro

                show yumiv:
                    alpha 0.95

                with Dissolve(.5)

                "Era Yumi..."
                g "Lo siento, hoy estoy cansadísima, cariño."
                g "Mañana hablamos sobre lo que te…"
                c "Ha llamado nuestro manager…"
                g "…"
                g "¿Y qué te ha dicho?"


                menu:

                    "Algo sobre un “trabajo muy especial":

                        play music creepy

                        "..."
                        "Lo solté así, sin más…"
                        "Y mientras esas palabras salían de mi boca, la cara de Yumi empezó a tornarse triste."
                        g "…"
                        g "Lo he intentado, de verdad…"
                        g "Pero este mundillo acaba por consumirnos a todas."
                        "No me lo creía…"
                        "O, mejor dicho, no quería creerlo."
                        c "Yumi…"
                        c "…"
                        c "Yumi, ¿qué has hecho?"
                        g "..."
                        g "No tenía otra opción."
                        g "Era esto o abandonar todo lo que había conseguido hasta ahora…"
                        g "Para acabar volviendo a mi pueblucho natal."
                        c "Yumi..."
                        c "..."
                        c "Yumi, ¿dónde está Judah?"
                        "Su cara al mencionar a Judah pasó de tristeza al shock."
                        g "..."
                        g "Jejeje..."
                        g "No lo sé…"
                        g "En Tailandia, ¿quizás?"
                        g "Puede que Taiwán."
                        g " O quien sabe, a lo mejor ha llegado a Hollywood."
                        c "¿C-como actriz?"
                        "Ante mi pregunta, ella se giró para mirarme y..."
                        "...me dirigió la sonrisa más tétrica que jamás haya visto."
                        c "No…"
                        c "No no no no"

                        with vpunch

                        c "¡SUFICIENTE!"
                        c "Voy a avisar a la policía..."
                        "Me di la vuelta y dirigí hacia la puerta cuando..."
                        "De pronto…"

                        stop music

                        scene bg negro

                        with Dissolve (.2)

                        with hpunch


                        "*THOMP*"

                        "Sentí un fuerte golpe…"
                        "Todo mi cuerpo dejó de responderme."
                        g "Niñata…"
                        g " ¿Quién te crees que me ha ayudado con Judah?"
                        g "Tranquila, pronto estarás con ella..."
                        g "Hay mucha gente que pagaría MUUUCHO por tener su propia idol."
                        "Eso fue lo último que alcancé a escuchar antes de desmayarme."
                        pause 5

                        scene bg trailer

                        with Dissolve(.5)

                        "Al despertarme, lo primero que sentí fue el frío suelo de metal."
                        "El ruido de un vehículo y el traqueteo de este me devolvieron a la realidad..."

                        play music creepy

                        c "¿D-dónde estoy...?"
                        "Mientras intentaba levantarme, sentí como la cabeza me daba vueltas."
                        "Al incorporarme, noté un chichón donde había sentido el golpe..."
                        c "¿Eh?"
                        c "¿Cuánto tiempo ha pasado?"
                        "Había otras chicas en esa aparente caja metálica..."
                        "Pero poco o nada me importaban..."
                        c "¿Que sería de mí ahora?"
                        "..."
                        "Mientras pensaba en los peores escenarios posibles..."
                        "..."
                        "Me di cuenta que ni en lo más oscuro de mi imaginación hubiera estado preparada para el infierno que sería el resto de mi vida."

                        stop music

                        jump ending

                    "(Mentir) Quería hablar contigo mañana":

                        "..."
                        g "..."
                        g "¿Eso era todo?"
                        c "Sí... creo que sí."
                        "Tenía que salir de allí."
                        "Tenía que escapar."
                        "Lo que sea que estuviese tramando, no quería saber nada."
                        c "Por cierto, mi madre se ha puesto enferma así que tendré que ir a cuidarla un tiempo."
                        g "..."
                        g "¿Eh?"
                        g "Si por aquí tienes un prometedor futuro por delante..."
                        c "Lo sé, pero…"
                        c "Desde la muerte de mi padre, en casa solo están mi hermanita y mi madre."
                        c "Así que necesito ir a cuidarla."
                        "Algo bueno había sacado de este mundillo…"
                        "Ahora se me daba bien mentir..."
                        g "Es una pena, te había conseguido un papel muy bueno."
                        g "¿Seguro que tienes que volver a tu casa? "
                        "No he estado más segura de algo en mi vida."
                        c "Sí, lo siento Yumi."

                        scene bg negro with Dissolve(.5)

                        "Esa misma noche, dejé la maleta hecha…"
                        "Para, temprano por la mañana, partir hacia la estación. "
                        "Yumi todavía dormía."

                        scene bg vagon

                        with Dissolve(.5)

                        play music tension

                        "En el viaje de tren todavía seguía pensando sobre lo que le pasó a Judah."
                        c "¿Dónde estará Judah ahora?"
                        "..."
                        "Conseguí dejar de pensar en ello cuando el tren llegó a mi estación."

                        scene bg habitacion with Dissolve(.5)

                        "Lo único en lo que podía pensar mientras subía las escaleras de casa era en lo estúpida que había sido..."
                        c "Nunca volveré a ese mundo..."
                        c "Jamás."
                        "Al llegar a casa vi una nota sobre la mesa que iba para mi hermanita, mi madre se había ido de compras. "
                        "Me alegré al saber que mi mentira no se había convertido en realidad."
                        "El verdadero susto me lo llevé cuando vi la habitación de mi madre abierta..."
                        "Y vi a mi hermanita, que se había maquillado con los cosméticos de nuestra madre..."

                        with hpunch

                        i "¡HOLA HERMANITA!"

                        with vpunch

                        i "¡MIRA COMO ME QUEDA!"

                        with hpunch

                        i "¿A QUE ESTOY GUAPA?"

                        with vpunch

                        i "Pronto seré una gran estrella, justo como mi hermanita."
                        c "..."

                        stop music

                        jump ending



    label ending:

    scene bg negro

    with Dissolve(.5)

    "..."

    "{i}Sea cual sea el camino o decisión que hayas tomado...{/i}"

    "{i}¡Gracias por jugar!{/i}"

    return
