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

    "Era un día como cualquier otro en la ciudad de Tokio."

    "Tommy era un joven estudiante universitario que se encontraba en la biblioteca cuando comenzó el caos."

    "De repente, una sirena de emergencia comenzó a sonar."

    play music euro

    "Todo el mundo corría a refugiarse mientras la noticia se extendía rápidamente: Godzilla había vuelto."

    # No mostrar al principio para sorpresa en las rutas, usarlo (show kaiju)

    # Si es posible hacer que la imagen de Godzilla vibre ligeramente

    "'GWAAAAAG'"

    "Tommy trató de calmarse y pensar en qué hacer, se sentía tan confuso con lo que estaba pasando..."

    "De repente, recordó a Yumi, su amiga de la infancia."

    "Se conocían desde hace años. Tommy siempre había sentido una atracción especial hacia ella, aunque nunca se hubiera atrevido a confesarlo."

    "Tommy decidió buscar a Yumi y juntos trataron de escapar. Los edificios se derrumbaban a su alrededor y el suelo temblaba con cada paso de Godzilla."

    "Sin embargo, Tommy y Yumi no se rindieron y finalmente encontraron un refugio seguro."

    stop music

    scene bunker

    "A partir de aquí, el destino de Tommy y Yumi era uno que solo una fuerza superior podía saber."

    "Así que..."

    show yumi

    y "Entonces, ¿qué es lo que vamos a hacer a partir de ahora?"

    menu:

        "Me quedaré contigo":
            jump ruta1

        "Vamos a explorar":
            jump ruta2

        "Caminaremos hasta el final del túnel":
            jump ruta3

    label ruta1:

            # Ruta Romántica

            hide yumi

            "Me senté en una lona roja una vez llegado al refugio."

            "Sentía como si el pecho fuese a explotarme mientras que en mi cabeza solo cabía ideas desordenadas."

            "Voy a hacerlo, si no me declaro ahora, me arrepentiré toda la vida."

            "El año que viene nuestros caminos se separarán, yo volveré a mi país natal y ella desaparecerá de mi vida."

            "Eso si ese monstruo no nos aplasta antes…"

            "¿De verdad iba a dejar que todo lo que hemos vivido estos 2 años se esfume?"

            "¿De verdad iba a dejar que el tiempo diluyese su rostro en mis recuerdos?"

            "¡NO, NO QUIERO ESO!"

            "Mientras lo pensaba mis pies ya me habían llevado a su vera. Sin vacilar le dirigí una mirada cobarde y…"

            show yumi

            y "Oh, hola Tommy, ¿necesitas algo?"

            "Ante mis ojos se encontraba Yumi, la chica de la que estaba enamorado. El solo verla hacía que mis latidos se acelerasen y me entrasen sudores fríos."

            t "H-hola Yumi, ¿podrías acompañarme un momento?"

            y "La verdad es que ahora poco podemos hacer, ¿A dónde quieres ir?"

            t "A… ¿Al pasillo? S-sé que parece raro, pero es que tengo algo que decirte."

            y "..."

            y "Tommy, estás un poco raro..."

            y "¿Te pasa algo?"

            t "N-no, estoy bien, es solo… bueno, los nervios por estar en esta situación, supongo…"

            t "¿Podrías acompañarme solo un rato?"

            "Mientras estas palabras salían de mi boca, dejé de mirarme los zapatos un momento y vi como su hermoso rostro blanquecino ahora se asemejaba más a un tomate."

            "Espera… esto significa que yo le… No."

            "Primero he de confesarme, una vez lo haga todo estará bien."

            "En esos 30 segundos que nos quedamos mirándonos cómo pasmarotes, lo único que se escuchaba eran el susurro del resto de habitantes del refugio."

            "Creí escuchar a alguien comentar las noticias, pero todo me entraba por un oído y me salía por otro."

            "Era como si, en ese preciso instante, solo estuviésemos ella y yo, perdiéndonos en esa simple mirada en la que sobraban las palabras."

            "Como si los problemas, las personas y el universo a nuestro alrededor se hubiese esfumado durante ese lapso de tiempo. Mi objetivo era claro."

            y "¿Vamos?"

            t "S-sí... Claro..."

            "Mientras caminábamos, lo único que podía pensar era en esa forma tan elegante que tenía ella de caminar. El aroma de su fragancia nublaba mi juicio y me impedía liberar esas palabras atoradas en mi garganta."

            "Llegamos hasta los baños del refugio y yo dejé de caminar."

            t "Yumi..."

            y "S-s.."

            # Otro pequeño script donde el sprite de Yumi se agita.

            y "¡¿SÍ?!"

            t "Ll-llevo mucho tiempo queriendo decirte esto..."

            "¡NO TARTAMUDEES!"

            "¡NO TE ATASQUES!"

            "¡NO VACILES!"

            scene bl

            "Todos esos momentos que has pasado con ella."

            "Todas esas tardes estudiando juntos."

            "Todos esos paseos al volver de clase."

            "Ya ni recuerdo de qué hablábamos en esos paseos."

            "Lo único que recuerdo era esa felicidad que inundaba mi ser solo por estar a su lado."

            "¡NO SABES LO QUE PASARÁ HOY! ¡NO SABES LO QUE PASARÁ MAÑANA!"

            "¡NI TAMPOCO LO QUE PASARÁ EN EL FUTURO! ¡ES AHORA O NUNCA!"

            "¡TOMMY, MANTÉN ESA DETERMINACIÓN Y HAZLO!"

            "¡SOLO HAZLO! ¡HAZLO!"

            "¡HAZLO! ¡HAZLO! ¡HAZLO! ¡HAZLO! ¡HAZLO!"

            # Destello blanco

            scene bunker

            show yumi

            t "¡Yumi...!"

            t "¡Tú me...!"

            "En ese preciso instante oímos un estruendo proveniente de la sala principal del búnker."

            "Era ese monstruo. Estaba arrasando con todo."

            "Los gritos de puro terror provenientes de la sala nos dejaron paralizados. En ese momento no pensé en mi familia ni en mi propio bienestar."

            "El único pensamiento que cabía en mi cabeza era:"

            "¡TENGO QUE SACAR A YUMI DE AQUÍ!"

            "¡TENGO QUE SALVARLA!"

            "En un ademán de valentía intenté cogerle de la mano y empezar a correr."

            t "¡VAMOS, YUMI!"

            scene bl

            "Pero al momento me inundó el terror y los únicos pensamientos que cabían en mi cabeza eran todos negativos."

            "¿Voy a morir? ¿Cómo moriré? ¿Sufriré?"

            "¿Pasará mi vida ante mis ojos o no tendré tiempo ni para eso?..."

            "..."

            "¡¡¡YUMI!!!"

            "ESTO TENGO QUE HACERLO, NO POR MÍ, SINO POR ELLA..."

            "Tengo que salvarla."

            "¡¡¡SEA COMO SEA!!!"

            y "Tommy..."

            y "¡Tommy!"

            scene bunkerfb

            "Su llamada me devolvió a la realidad."

            "Antes de que pudiese situarme…"

            y "¡AAAAAAAAH!"

            "Antes de que mis sentidos pudieran reaccionar, lo primero que noté es un dolor muy fuerte proveniente de mi tobillo derecho."

            "No puede ser…"

            y "Tommy…"

            y "No, no…"

            y "Esto no puede estar pasando."

            "Los lamentos de Yumi hicieron que mi vista se desviase de su rostro en el que solo cabía preocupación y tristeza."

            "Veía mi tobillo…"

            "No veía mis zapatillas…"

            "Había sido aplastado por un trozo del techo del refugio."

            "Conseguí volver en mí solo para soltar un grito ahogado."

            t "¡AAAAAAAAAGH!"

            "Tenía que pensar rápido."

            "En esa situación y sin vistas de que pudiese siquiera levantarme, solo tenía dos opciones..."

    menu:

        "Déjame, por favor huye ":
            jump ruta1_final_true

        "Ayúdame Yumi":
            jump ruta1_final_false


            label ruta1_final_true:
            t "Huye, corre y no mires atrás..."

            y "¡¿Q-QUÉ?!"

            y "No puedo hacer eso."

            y "Tommy, tú…"

            y "¡¡¡ME GUSTAS!!!"

            t "…"

            "Lo había oído bien."

            "No cabía lugar a dudas."

            "Yumi se me había declarado."

            "Aún con una piedra donde antes estaba mi pie…"

            "Me sentía el hombre más afortunado del mundo."

            "En esa situación, ordené mis ideas entre el insufrible dolor y…"

            "Simplemente lo dije."

            t "Tú también me gustas."

            t "Siempre me has gustado."

            t "Desde el primer día que te ví, he querido que llegase este momento."

            t "Tú también me gustas, y siempre me gustarás…"

            t "Pero…"

            "Antes de perder la consciencia, grité con todas mis fuerzas."

            scene mano

            t "¡AHORA TIENES QUE CORRER!"

            t "¡ESCAPA!"

            t "¡DÉJAME AQUÍ Y CORRE!"

            t "…"

            t "Por favor…"

            "Entre gritos y súplicas me digné a dirigirle la mirada solo para ver como en su rostro solo cabía tristeza."

            "El shock había desaparecido y ya solo quedaban los llantos y balbuceos."

            y "C-como esperas que me vaya después de decirme eso…"

            y "Por favor, Tommy…"

            y "¿Tommy?"

            "Sentía como mis sentidos empezaban a fallarme y mi cabeza comenzaba a apagarse."

            scene black

            play music blich

            "Mientras, lo único que escuchaba era el sonido ahogado de su dulce voz…"

            "Gritando por mí…"

            "…"

            "Volví en mí una última vez solo para decirle mi último deseo."

            "Un deseo egoísta y cruel."

            t "Por favor…"

            t "Sálvate tú."

            "Lo último que conseguí percibir antes de que mi mirada se nublase era la figura de Yumi alejándose."

            "Por favor, si aún queda un poco de justicia en este mundo, ella habrá llegado fuera y…"

            "No podía continuar, no me pegaba ser el héroe."

            "Mi último pensamiento no fue uno altivo, un pensamiento cobarde…"

            t "Ojalá haber podido verte un poco más…"

            t "Vivir a tú vera…"

            t "Despertarnos cada mañana juntos."

            t "…"

            t "¡¿DE VERDAD PEDÍA TANTO?!"

            "Los pasos del monstruo se escuchaban cada vez más cerca."

            "El techo empezó a fracturarse y…"

            "Antes de que pudiese darme cue…"

            stop music

            jump ending

            label ruta1_final_false:
            t "Por favor…"

            play music blich

            "¿De verdad le había pedido tal cosa?"

            "No sé siquiera sí puedo caminar."

            "¡¿CÓMO DEMONIOS IBA A CARGAR CONMIGO?!"

            "…"

            "Doy asco…"

            y "Tommy…"

            y "…"

            y "Te sacaré de aquí."

            "Yumi actuó con rapidez y me quitó la piedra intentando hacerla rodar."

            "En el momento en el que la sangre llegó a esa parte de mi cuerpo retenida por la piedra…"

            t "¡AAAAAAAAGH!"

            "Sin poder aguantarme, solté un grito de los que te hielan la sangre."

            "El dolor era atroz."

            "Decidí no mirar para intentar despejar mi mente."

            "Ese dolor era lo único que se me venía a la cabeza hasta que…"

            y "Tommy…"

            "Yumi me apretó la cara con sus delicadas manos."

            y "Fíjate solo en mí."

            y "¿Vale?"

            y "No mires al monstruo."

            y "Ni a tu pierna."

            y "Solo a mí."

            y "…"

            y "¿Vale?"

            y "…"

            t "S-sí."

            "Con una fuerza inesperada viniendo de ella me ayudo a levantarme y paso mi brazo alrededor de su cuello."

            "Comenzamos a caminar."

            "Lo único que podía era en lo mucho que me gustaba Yumi."

            "Eso era lo que me distraía del insoportable dolor."

            "Los pasos de ese maldito monstruo cada vez sonaban más cerca."

            "Causando a su paso nada más que destrucción."

            "Seguíamos las señales que indicaban la salida hasta que…"

            t "¿Yumi?"

            "Había empezado a perder el sentido."

            "Me había tropezado y ahora ya no tenía fuerzas para levantarme."

            y "Tommy…"

            y "Por favor, aguanta."

            "El monstruo se acercaba."

            "Nos quedaba poco tiempo, así que decidí soltarlo sin más."

            t "Yumi…"

            "Se me empezó a nublar la vista."

            "Poco podíamos hacer ya."

            "¿Había hecho mal en decirle que se quedase?"

            t "Me gustas…"

            t "Gracias…"

            t "Gracias por todo."

            "El monstruo estaba sobre nosotros."

            "Y, sin embargo, allí estaba ella."

            "Agarrándome la mano mientras lloraba."

            "Lo último que escuché antes de que el techo se desmoronase fue un susurro."
            
            y "Idiota"

            stop music

            y "..."


            jump ending


    label ruta2:

            # Ruta Comedia - Vamos a explorar

            hide yumi

            "Tommy y Yumi caminaron por el túnel del búnker durante largo rato."

            play music tec

            "Se detuvieron al escuchar un extraño sonido..."

            "No eran pisadas ni el ajetreo de la calle en una posible salida, sonaba como una percusión bastante pegadiza"

            "¿Era música aquello?"

            show yumi at left

            show tommy at right

            y "¿Habrá alguien más aquí abajo?"

            "Como respuesta a la pregunta, Tommy sintió un roce suave en sus piernas. Agachó la cabeza."

            hide yumi

            hide tommy

            show hol

            pt "Hola, Tommy."

            scene bunker

            show yumi at left

            show tommy

            show pt at right

            "Un pato blanco, con el plumaje brillante a pesar de la oscuridad, se había dirigido hacia él."

            pt "Es tu día de suerte."

            y "¿Estás viendo lo mismo que yo o es un mal sueño?"

            pt "De mal sueño nada. Soy vuestra salvación."

            t "¿Qué hace un pato como tú en un túnel como este?"

            pt "Te estaba buscando, Tommy. Eres nuestra única esperanza. Déjame que te explique."

            "El pato agitó las alas muy animado, casi al ritmo de la música."

            pt "Vengo del futuro y te aviso que no pinta nada bien."

            pt "Este problema del bicho gigante es serio."

            pt "Yo intenté impedirlo con el poder del tecno, también con mi ataque final punzante…"

            t "¿Lo pinchaste?"

            "Tommy lo inspeccionaba incrédulo."

            pt "!NO ME INTERRUMPAS, HOMBRE!"

            pt "Ejem..."

            pt "El asunto es que me derrotó y el mundo tal y como lo conoceis colapsó en el futuro."

            pt "Aun así, sigo siendo un pato con influencia, por lo que pude viajar en el tiempo y llegar hasta vosotros."

            pt "Tommy, te conozco del futuro y sé que puedes tener el poder suficiente para vencer al bicho."

            pt "Toma esto."

            "Sin saber cómo, el pato guardaba bajo el ala un móvil más moderno, aunque tampoco mucho."

            y "¿Y quién nos dice que eres de fiar?"

            pt "Deja que hablemos los protagonistas de esta ruta, por favor."

            t "¿Qué pretendes que haga con esto? Si casi no tenemos cobertura aquí para llamar a nadie."

            pt "Este móvil está configurado con un sistema operativo llamado *Mudae*"

            pt "Te permite, en base a tu suerte, poder {i}mudarte{/i} de cuerpo."

            pt "Vamos, transformarte en un personaje conocido que te salga en el sistema."

            pt "Se le llama casamiento."

            pt "El móvil replicará al personaje y se dará lugar a una unión más que física, espiritual, que te permitirá tomar todos sus atributos."

            t "Esto no pinta a sistema de nada, parece un gacha de esos de Discord."

            pt "Tommy, está en tu mano. Sé que tendrás suerte y te saldrá un personaje lo suficientemente poderoso como para que te transformes en él y puedas vencer al bicho gigante."

            y "Por Dios, Tommy, no me digas que vas a hacer caso a un pato que habla. Pasa de él y vámonos de aquí."

            stop music


    menu:

        "Tienes razón":
            jump ruta2_final_true

        "Lo haré":
            jump ruta2_final_false

            label ruta2_final_true:
            t "Tienes razón, Yumi."

            t "¿Qué va a saber este pato?"

            t "Seguro que me quiere estafar."

            y "Por favor, es que está claro."

            y "Venga, vámonos, cariño."

            pt "UN MOMENTO"

            pt "¿¡HAS DICHO {b}CARIÑO{/b}!?"

            pt "Si en esta línea temporal acababas dándole calabazas a Tommy..."

            pt "Espera..."

            pt "TÚ NO ERES YUMI"

            t "<3 jeje <3"

            t "<3 Me ha dicho cariño <3"

            y "..."

            y "Me has descubierto, Pato Tecno."

            y "No soy Yumi, soy..."

            y "..."

            y "SOY..."

            show tommy at right

            # TOMY y PATO TECNO uno al lado del otro mirando a Yumi)

            t "Espera espera, a ver si adivinamos."

            t "Mmmmmm..."

            t "Eres un extraterrestre."

            pt "KUAKUAKUAKAUAKUAK"

            pt "Cómo va a ser un extraterrestre, ¿estás tonto?"

            pt "Está claro que es un helicóptero apache de combate."

            t "Uff, de repente se me antoja una doble cheeseburguer."

            pt "Uhhh, me tecnopatoflipa como piensas Tommy, no tendrás por ahí algo suelto ¿no?"

            pt "Es que tengo muuuucha hambre"

            "La barriga de Tommy empieza a rugir"

            t "Ahora que lo dices..."

            t "Yo también tengo un hambre que te mueres"

            y "¡¿Y MI IDENTIDAD?!"

            y "¡¿ACASO NO OS IMPORTA?!"

            pt "Venga ya Yumi, ya te dije que no eras la protagonista en esta ruta."

            y "Pero, pero..."

            "Tommy y el Pato Tecno se alejan por el túnel"

            t "¿Cuánto te apuestas que nos encontramos un McDonalds abierto?"

            pt "Mientras no haya un chino que sirvan pato a la naranja"

            pt "KUAKAUAKAUAKAA"

            show bl

            "Su graznido en forma de risa empezaba a perderse en el eco del refugio..."
            jump ending

            label ruta2_final_false:

            t "Lo haré."

            t "Me transformaré en un ser gigante para vencer al bicho."

            y "Definitivamente, se te ha ido al coco."

            pt "Perfecto, pues."

            pt "Dale."

            pt "Haz tu magia."

            t "..."

            y "..."

            pt "..."

            pt "¿A QUÉ ESPERAS?"

            pt "Dale al botón que pone {b}Haz tu magia{/b}"

            t "Ah, vale."

            "Tommy pulsa el botón."

            "Entre una variedad de personajes variopintos, a Tommy le tocó..."

            play sound pep3

            "PEPSIMAAAAN"

            scene bunker1

            "De repente, a Tommy le entran unas ganas irrefrenables de tomar una Pepsi, por lo que corre con una velocidad supersónica hacia la máquina de Pepsi más próxima."

            "Al beber su lata, Tommy comienza a crecer de tamaño, destrozando el techo y convirtiéndose en..."

            play sound pep3

            "PEPSIMAAAAAN"

            show bl

            "..."

            scene bunker2

            play music pep2

            "GIGANTE"

            scene city

            show pepsi at right

            pm "¡EH, TÚ!"

            pm "¡EL BICHO!"

            show k at left

            k "(ruge)" # Plagiamos el sonido del T-Rex de Jurassic Park o algo

            pm "¡IT'S PEPSIN' TIME!"

            k "Por favor, não grite comigo dessa maneira."

            pm "Vale vale, perdón creía que irías a atacarme..."

            k "Quem você acha que eu sou, um monstro?"

            pm "No, hombre, no."

            pm "No quería molestar."

            k "Isso me machuca, eu só vim pra visitar Akihabara e você até quer me atacar."

            pm "No llores, anda."

            pm "Te invito a una Pepsi."

            pm "¿Quieres que te acompañe para que no sientas solo?"

            k "Ok, mas eu ainda não perdoei você."

            "Y los dos juntos, se fueron al SEGA PARK a jugar al Fighting Vipers."

            k "Tenho o entendimento da cual o Pepsiman sai neste jogo de video."

            pm "Ay, bicho, por desgracia solo en la versión japonesa para Sega Saturn. Y encima, has destruido las pocas Saturn que quedaban en Tokio."

            k "Com estas patinhas de dinossauro, espero alcançar o joystick de arcada."

            stop music

            jump ending



    label ruta3:

            # Ruta Meta

            t "Yumi, tenemos que encontrar una solución."

            t "Será mejor que te quedes aquí mientras inspecciono el lugar."

            y "Bueno, yo..."

            y "..."

            y "Está bien..."

            y "Veo en tus ojos que estás seguro de lo que vas a hacer."

            y "De acuerdo."

            y "Confío en ti."

            y "Es peligroso ir solo, llévate esto."

            "Yumi le dio a Tommy un poco de comida que tenía guardada en su bolso."

            "Eran bolas de arroz espachurradas..."

            t "..."

            y "Tienes que quitarle un poco de polvo, pero están hechas con todo el cariño del mundo"

            t "..."

            t "Gracias."

            t "Si te pasa algo, simplemente pégame un grito"

            t "Esto..."

            t "Yo..."

            t "Volveré..."

            hide yumi

            "..."

            scene bunker6

            "Tommy caminó durante un largo rato, perdiendo la noción del tiempo."

            "La luz que entraba del exterior iba menguando conforme se adentraba en la oscuridad."

            "De vez en cuando, Tommy daba algún pequeño mordisco a las bolas de arroz, para calmar su ansiedad."

            "Estaban horribles."

            "Sabían a arena."

            "..."

            "Los temblores iban produciéndose cada vez con más frecuencia."

            "Tenía miedo de que el techo se derrumbará sobre sus hombros, por lo que caminaba cada vez más deprisa."

            "Sin saber si estaba huyendo o cumpliendo con su destino."

            t "Debo darme prisa, Yumi está esperándome..."

            play music ser

            "..."

            "Tommy consiguió ver la luz al final del túnel."

            "Una puerta con un pequeño foco de emergencia le indicaba el camino a seguir."

            "Conforme se acercaba a ella, el ambiente comenzó a hacerse más denso, más opresivo."

            "Un hedor nauseabundo salía de aquella dirección, impregnando con su miasma el poco aire que quedaba en el subsuelo."

            "Con dificultades para respirar, Tommy contuvo su aliento, y decidió abrir esa puerta."

            scene bl

            "..."

            show k3

            "Cuando su vista comenzó a acostumbrarse a la oscuridad, Tommy se encontró frente a frente a la bestia."

            "Su mirada cristalina se clavó en la de Tommy."

            "Mientras Tommy no sabía como reaccionar ante semejante visión, la bestia soltó un rugido, provocando temblores."

            "Sin embargo, su expresión no era de amenaza."

            "Más bien parecía que estaba clamando un grito de auxilio."

            "En un acto de compasión, Tommy decidió darle la comida que le quedaba."

            "(...)"

            # telepatía, textbox en negrita sin sprites con solo bg

            "{b}Humano.{/b}"

            "{b}Una voz sibilina resonó en lo más profundo de su alma.{/b}"

            "{b}No temas.{/b}"

            "{b}No voy a hacerte nada.{/b}"

            "{b}No voy a hacerte daño.{/b}"

            t "¿Q-Qué eres?"

            "{b}Tu raza me ha dado varios nombres a lo largo de su existencia.{/b}"

            "{b}Los de esta tierra me conocen como...{/b}"

            "{b}Godzilla.{/b}"

            "{b}Al contrario que los de tu especie, a los nuestros no se nos ha permitido existir.{b}"

            "{b}Fuimos obligados a desaparecer.{/b}"

            "{b}O dicho de otro modo, fuimos desaparecidos, obligados a escondernos en lo más profundo de la corteza terrestre{/b}"

            "{b}Sin recursos, me ví obligado a volver hasta la superficie para salvar a los mios.{/b}"

            "{b}Y aquí, solo me he encontrado el más profundo de los desprecios hacía algo que con vuestro limitado entendimiento no sois capaces de explicar.{/b}"

            "{b}Solo queríamos vivir en paz.{/b}"

            t "Es la ley de la evolución, si no te adaptas a tu entorno entonces..."

            "{b}CÁLLATE{/b}"

            play music embro

            "La rabía provocó un zumbido intenso en la mente de Tommy"

            "Al mismo tiempo, uno de los temblores causó un desprendimiento del techo que taponó la puerta y, con ella, la única salida que le quedaba"

            "{b}¿QUÉ FUE LO QUE HICIMOS PARA QUE SE NOS CASTIGASE ASÍ?{/b}"

            "{b}¿ES ACASO ESTO A LO QUE LLAMAIS CIVILIZACIÓN ALGO NATURAL?{/b}"

            "{b}SOLO VEO GUERRA ENTRE VUESTROS SEMEJANTES.{/b}"

            "{b}SOLO DEJAIS MISERIA ALREDEDOR DE VUESTRO SUPUESTO PROGRESO.{/b}"

            "{b}TODOS LOS SERES VIVOS VENIMOS DEL CAOS, Y AL CAOS OS HARÉ VOLVER.{/b}"

            "{b}AHORA, CONVIÉRTETE EN UNO CON MI ESPECIE{/b}"

            "El cuerpo de Tommy fue paralizado, no podía controlar ninguno de sus miembros."

            "Escapando de su control, su cuerpo empezó a aproximarse hasta la bestia."

            "La voluntad de Tommy estaba siendo doblegada."

            "Sin embargo, en un atisbo de determinación, consiguió enfrentarse a si mismo."


    menu:

            "Tommy decide aliviar su dolor":
                jump ruta3_final_true

            "Tommy decide convertirse en un héroe":
                jump ruta3_final_false

                label ruta3_final_true:
                    "Tommy decide aliviar su dolor"

                    "Conforme iba acercándose a la bestia, pudo ver como una vara de hierro perforaba sus escamas"

                    "En un último acto de humanidad, consiguió quitarle lo incrustado"

                    "(...)"

                    play music p3

                    "De una forma incluso grotesca, la herida fue recuperándose instantaneamente, las escamas fueron cuajando la sangre hasta su estado natural."

                    "Sin mediar palabra, la bestia cavó un profundo agujero destinado hacia los confines de la tierra."

                    hide k3

                    stop music

                    "(...)"

                    "Pasaron las horas..."

                    "Con las últimas fuerzas que le quedaban, Tommy conseguía quitar poco a poco los escombros que cubrían la puerta."

                    "De repente, se escucho un grito agudo..."

                    play music blich

                    "TOOOOOMMYYYYYYY"

                    "Se escucharon unos pasos distantes al otro lado de la puerta"

                    "TODO HA TERMINADOOOO"

                    "El volumen parecía cada vez más cercano"

                    "PODREMOS SALIR DE AQUIIII"

                    "La voz de Yumi retumbaba como un eco a lo largo del refugio."

                    "JUNTOOOOOS"
                    jump ending

                label ruta3_final_false:
                    "Tommy decide convertirse en un héroe"

                    "Conforme iba acercándose a su presa, pudo ver como una vara de hierro perforaba sus escamas"

                    "En un último acto de humanidad, consiguió hurgar más en su herida"

                    scene bl

                    "(...)"

                    "Tommy apretaba la vara mientras los rugidos agonizantes de su presa causaban temblores cada vez más fuertes"

                    "La herida de la presa se hacía cada vez más profunda"

                    "Tommy continuaba apretando"

                    "Y apretando..."

                    "La sangre fluía a borbotones, cubriendo todo el cuerpo de Tommy"

                    stop music

                    "(...)"

                    "Los temblores pararon"

                    "Los rugidos cesaron"

                    "Solo se oía silencio"

                    play music bnc

                    "(...)"

                    "Como si su mente reptiliana se activase, en un acto reflejo relamió la sangre del animal"

                    "(...)"

                    "Los ojos de Tommy empezaron a tomar un color cristalino"

                    "(...)"

                    "Mientras caminaba, sus pasos hacían mover el mundo"

                    "(...)"

                    "Un grito agudo rompió el silencio"

                    "(...)"

                    "{b}La humanidad ha evolucionado{/b}"

                    stop music
                    
                    jump ending

    label ending:

    scene bl

    "..."

    "{i}Sea cual sea la ruta que hayas escogido...{/i}"

    "{i}¡Gracias por jugar!{/i}"

    return
