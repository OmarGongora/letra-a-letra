import random

#Declaramos la lista de listas con las que vamos a trabajar
palabras = [
    [
        ("avion","Con la letra A, medio de transporte aereo impulsado por motores."),
        ("argentina", "Con la letra A, pais sudamericano conocido por el tango, el futbol y el mate."),
        ("aventura","Con la letra A, experiencia emocionante o riesgosa que implica desafios y exploracion."),
        ("arcoiris","Con la letra A, fenomeno optico y meteorologico que produce un espectro de luz en el cielo."),
        ("arbol","Con la letra A, planta perenne de tronco lenoso que tiene ramas desde el suelo.")
    ],
    [
        ("bosque","Con la letra B, ecosistema con abundancia de arboles y diversidad biologica."),
        ("bicicleta","Con la letra B, vehiculo de transporte de dos ruedas impulsado por pedales."),
        ("balon","Con la letra B, objeto esferico utilizado en deportes como el futbol y el basquetbol."),
        ("biblioteca","Con la letra B, lugar donde se encuentran libros y otros materiales impresos para su lectura."),
        ("botella","Con la letra B, recipiente utilizado para almacenar liquidos o sustancias.")
    ],
    [
        ("cielo", "Con la letra C, espacio sobre la Tierra donde se encuentran las nubes y se observan los astros."),
        ("carro", "Con la letra C, vehículo con cuatro ruedas utilizado para el transporte terrestre."),
        ("camino", "Con la letra C, senda o vía por la que se transita."),
        ("casa", "Con la letra C, edificio donde vive una persona o una familia."),
        ("calle", "Con la letra C, vía pública de una ciudad o pueblo, destinada a la circulación de vehículos y peatones.")
    ],
    [
        ("dinosaurio", "Con la letra D, animal prehistórico gigante que vivió hace millones de años."),
        ("diamante", "Con la letra D, piedra preciosa muy valiosa y dura."),
        ("desierto", "Con la letra D, región geográfica árida con poca vegetación y escasez de agua."),
        ("delfin", "Con la letra D, mamífero marino conocido por su inteligencia y sociabilidad."),
        ("durazno", "Con la letra D, fruta de piel suave y color entre naranja y rosado, con pulpa dulce y jugosa.")
    ],
    [
        ("elefante", "Con la letra E, mamífero terrestre de gran tamaño y trompa alargada."),
        ("espejo", "Con la letra E, superficie lisa que refleja la luz y las imágenes."),
        ("estrella", "Con la letra E, cuerpo celeste que brilla en el cielo nocturno."),
        ("escuela", "Con la letra E, institución donde se imparten conocimientos y educación."),
        ("escalera", "Con la letra E, estructura formada por peldaños que permite subir o bajar a distintos niveles.")
    ],
    [
        ("fuego", "Con la letra F, proceso de combustión que desprende luz y calor."),
        ("flauta", "Con la letra F, instrumento musical de viento."),
        ("faro", "Con la letra F, torre con una luz en su parte superior, utilizada para guiar a los barcos en el mar."),
        ("familia", "Con la letra F, conjunto de personas relacionadas por parentesco."),
        ("flor", "Con la letra F, parte de una planta que contiene sus órganos reproductivos, generalmente de colores llamativos.")
    ],
    [
        ("gato", "Con la letra G, animal doméstico de tamaño pequeño, peludo y con garras retráctiles."),
        ("globo", "Con la letra G, objeto esférico lleno de aire o gas, comúnmente utilizado en celebraciones."),
        ("guitarra", "Con la letra G, instrumento musical de cuerdas."),
        ("granja", "Con la letra G, terreno donde se crían animales y se cultivan plantas."),
        ("gorila", "Con la letra G, primate de gran tamaño, conocido por su fuerza y su vida en grupos.")
    ],
    [
        ("hoja", "Con la letra H, parte verde de una planta que realiza la fotosíntesis."),
        ("hormiga", "Con la letra H, insecto de pequeño tamaño que vive en colonias."),
        ("hielo", "Con la letra H, agua en estado sólido debido a temperaturas bajas."),
        ("héroe", "Con la letra H, persona que se distingue por realizar acciones valientes o extraordinarias."),
        ("huracán", "Con la letra H, tormenta de gran intensidad con vientos muy fuertes y destructivos.")
    ],
    [
        ("iglesia", "Con la letra I, edificio donde se celebran ceremonias religiosas."),
        ("isla", "Con la letra I, porción de tierra rodeada de agua por todas partes."),
        ("iman", "Con la letra I, objeto que tiene la propiedad de atraer metales."),
        ("insecto", "Con la letra I, pequeño animal invertebrado que tiene seis patas y a menudo alas."),
        ("idea", "Con la letra I, representación mental de algo que se quiere hacer o desarrollar.")
    ],
    [
        ("jardin", "Con la letra J, terreno donde se cultivan plantas con fines ornamentales."),
        ("jirafa", "Con la letra J, animal terrestre de gran altura y cuello largo."),
        ("juguete", "Con la letra J, objeto diseñado para entretener y divertir a los niños."),
        ("jabali", "Con la letra J, mamífero salvaje similar al cerdo, con colmillos afilados."),
        ("joya", "Con la letra J, objeto precioso que se usa como adorno, normalmente hecho de metal y piedras.")
    ],
    [
        ("kilometro", "Con la letra K, unidad de medida de longitud equivalente a mil metros."),
        ("koala", "Con la letra K, mamífero australiano que se alimenta principalmente de hojas de eucalipto."),
        ("karate", "Con la letra K, arte marcial japonés que utiliza técnicas de defensa y ataque con las manos y pies."),
        ("kilo", "Con la letra K, abreviatura de kilogramo, unidad de medida de masa."),
        ("kiosco", "Con la letra K, pequeño establecimiento comercial donde se venden golosinas, bebidas, y otros productos.")
    ],
    [
        ("leon", "Con la letra L, felino conocido como el rey de la selva."),
        ("luna", "Con la letra L, satélite natural de la Tierra que brilla de noche."),
        ("lago", "Con la letra L, gran cuerpo de agua dulce rodeado por tierra."),
        ("libro", "Con la letra L, conjunto de páginas con texto impreso, encuadernadas y ordenadas."),
        ("lapiz", "Con la letra L, instrumento para escribir o dibujar que contiene una mina de grafito.")
    ],
    [
        ("mariposa", "Con la letra M, insecto con grandes alas de colores."),
        ("montaña", "Con la letra M, elevación natural del terreno de gran altura."),
        ("mesa", "Con la letra M, mueble con una superficie horizontal y patas, utilizado para comer, escribir o trabajar."),
        ("musica", "Con la letra M, arte de combinar sonidos para crear armonía y ritmo."),
        ("mono", "Con la letra M, mamífero primate, a menudo conocido por su agilidad y comportamiento social.")
    ],
    [
        ("nube", "Con la letra N, masa visible de vapor de agua suspendida en la atmósfera."),
        ("niño", "Con la letra N, persona de corta edad, generalmente en su etapa de desarrollo inicial."),
        ("noche", "Con la letra N, periodo del día comprendido entre el anochecer y el amanecer."),
        ("naranja", "Con la letra N, fruta cítrica de color anaranjado y sabor dulce o ácido."),
        ("nido", "Con la letra N, estructura construida por aves y otros animales para depositar sus huevos o crías.")
    ],
    [
        ("orquesta", "Con la letra O, grupo de músicos que tocan instrumentos en conjunto."),
        ("oso", "Con la letra O, mamífero grande y fuerte, de pelaje espeso."),
        ("oceano", "Con la letra O, gran masa de agua salada que cubre la mayor parte de la superficie terrestre."),
        ("ojo", "Con la letra O, órgano del cuerpo responsable de la visión."),
        ("oruga", "Con la letra O, larva de mariposa que tiene un cuerpo segmentado y alargado.")
    ],
    [
        ("perro", "Con la letra P, animal doméstico conocido por ser el mejor amigo del hombre."),
        ("planeta", "Con la letra P, cuerpo celeste que gira alrededor de una estrella, como la Tierra alrededor del Sol."),
        ("pluma", "Con la letra P, estructura ligera y flexible que recubre a las aves."),
        ("pajaro", "Con la letra P, animal vertebrado con plumas y pico, capaz de volar en la mayoría de los casos."),
        ("puente", "Con la letra P, estructura que permite atravesar ríos, valles u otras barreras.")
    ],
    [
        ("queso", "Con la letra Q, alimento sólido elaborado a partir de la leche cuajada."),
        ("quimera", "Con la letra Q, criatura mitológica formada por partes de diferentes animales."),
        ("quinto", "Con la letra Q, número ordinal que indica la posición cinco en una serie."),
        ("quiosco", "Con la letra Q, pequeño establecimiento donde se venden productos variados."),
        ("quimica", "Con la letra Q, ciencia que estudia la composición y propiedades de la materia.")
    ],
    [
        ("rio", "Con la letra R, corriente natural de agua que fluye hacia otro cuerpo de agua."),
        ("raton", "Con la letra R, pequeño roedor que se encuentra en diversos hábitats."),
        ("rosa", "Con la letra R, flor de colores variados, símbolo del amor y la belleza."),
        ("roca", "Con la letra R, material sólido y mineral que forma parte de la corteza terrestre."),
        ("reloj", "Con la letra R, instrumento para medir y mostrar el tiempo.")
    ],
    [
        ("sol", "Con la letra S, estrella alrededor de la cual gira la Tierra."),
        ("silla", "Con la letra S, mueble con respaldo y asiento, utilizado para sentarse."),
        ("sombrero", "Con la letra S, prenda que cubre la cabeza, utilizada para protección o adorno."),
        ("serpiente", "Con la letra S, reptil sin patas que se desplaza arrastrándose."),
        ("sopa", "Con la letra S, alimento líquido, generalmente caliente, preparado con agua y otros ingredientes.")
    ],
    [
        ("tigre", "Con la letra T, felino salvaje de pelaje anaranjado con rayas negras."),
        ("tornillo", "Con la letra T, pieza metálica con una rosca utilizada para sujetar objetos."),
        ("tierra", "Con la letra T, planeta donde vivimos, también conocido como el mundo."),
        ("tren", "Con la letra T, medio de transporte terrestre que circula sobre vías."),
        ("telefono", "Con la letra T, dispositivo utilizado para comunicarse a distancia mediante la voz.")
    ],
    [
        ("uva", "Con la letra U, fruto pequeño y redondo que crece en racimos y se utiliza para hacer vino."),
        ("universo", "Con la letra U, conjunto de todo lo que existe: espacio, tiempo, energía y materia."),
        ("uniforme", "Con la letra U, ropa especial que utilizan las personas en ciertas profesiones o actividades."),
        ("ultrasonido", "Con la letra U, ondas sonoras de alta frecuencia utilizadas en medicina para imágenes."),
        ("urraca", "Con la letra U, ave de plumaje blanco y negro conocida por su afición a los objetos brillantes.")
    ],
    [
        ("viento", "Con la letra V, corriente de aire que se mueve por la atmósfera."),
        ("vaca", "Con la letra V, mamífero doméstico que produce leche y carne."),
        ("volcan", "Con la letra V, montaña que expulsa lava, gases y ceniza durante una erupción."),
        ("ventana", "Con la letra V, abertura en una pared que permite la entrada de luz y aire."),
        ("vela", "Con la letra V, cilindro de cera con una mecha que se enciende para dar luz.")
    ],
    [
        ("wafle", "Con la letra W, alimento dulce con forma de rejilla, generalmente servido con miel o frutas."),
        ("wifi", "Con la letra W, tecnología que permite la conexión inalámbrica a internet."),
        ("whisky", "Con la letra W, bebida alcohólica destilada, elaborada a partir de cereales."),
        ("walkman", "Con la letra W, dispositivo portátil que permite reproducir casetes de audio."),
        ("waterpolo", "Con la letra W, deporte acuático que se juega en una piscina con una pelota.")
    ],
    [
        ("xilofono", "Con la letra X, instrumento musical de percusión formado por láminas de diferentes tamaños."),
        ("xenofobia", "Con la letra X, rechazo o miedo hacia los extranjeros o lo que es desconocido."),
        ("xilografia", "Con la letra X, técnica de grabado en madera."),
        ("xilema", "Con la letra X, tejido vegetal que transporta agua y minerales desde las raíces hasta las hojas."),
        ("xenon", "Con la letra X, gas noble utilizado en lámparas y tubos de luz.")
    ],
    [
        ("yoga", "Con la letra Y, práctica física y mental originaria de la India que promueve el bienestar."),
        ("yegua", "Con la letra Y, hembra adulta del caballo."),
        ("yeso", "Con la letra Y, material blanco y suave que se utiliza para hacer moldes y reparar huesos."),
        ("yerno", "Con la letra Y, esposo de la hija de una persona."),
        ("yacimiento", "Con la letra Y, lugar donde se encuentran minerales o fósiles bajo la tierra.")
    ],
    [
        ("zorro", "Con la letra Z, mamífero salvaje de tamaño mediano, conocido por su astucia."),
        ("zapato", "Con la letra Z, prenda que cubre el pie y se utiliza para caminar."),
        ("zanahoria", "Con la letra Z, raíz comestible de color anaranjado."),
        ("zoologico", "Con la letra Z, lugar donde se exhiben animales para el público."),
        ("zigzag", "Con la letra Z, línea que va cambiando de dirección de manera alternada.")
    ]
]


def crearJugadores():
    """
    Crea una lista de jugadores a partir de la entrada del usuario.

    Return: 
        una lista de diccionarios donde cada diccionario representa la informacion del jugador
    """
    listaJugadores = []

    # Solicita al usuario la cantidad de jugadores, con rango válido entre 1 y 5
    # y captura el error en caso de ingresar un dato invalido
    valido = False
    while valido == False:
        try:
            cantidadJugadores = int(input("¿Cuántos jugadores formarán parte de la partida? \nEl rango debe ser entre 1 y 5 jugadores: "))
            
            # Verifica que el número esté dentro del rango permitido
            if 1 <= cantidadJugadores <= 5:
                valido = True
            else:
                print("Por favor, ingresa un número entre 1 y 5.")
                
        except ValueError:
            print("El valor ingresado no es valido, por favor ingrese un numero entero entre 1 y 5")

    

    # Itera según la cantidad de jugadores especificada
    for i in range(cantidadJugadores):
        nombre = input(f"ingrese el nombre del jugador numero {i+1}: ")

        # Crea un diccionario para representar al jugador
        jugador = {
            "jugador": i,
            "nombre": nombre,
            "errores": 0,
            "aciertos": 0,
            "posicion": 0,
            "rosco": [],
            "letrasCompletadas": [],
            "completado": False
        }
        listaJugadores.append(jugador)
    return listaJugadores



def crearRosco(listaJugadores, palabras):
    """
    Crea un "rosco" para cada jugador a partir de una lista de palabras.

    Argumentos:
        listaJugadores:lista de diccionarios que representan a los jugadores
        palabras:lista de palabras

    Returns:
        La funcion retorna la lista de jugadores actualizada
    """

    # Itera sobre cada jugador en la lista de jugadores
    for jugador in listaJugadores:
        nuevoRosco = []
        palabrasCompletadas = []

        # Itera sobre cada palabra en la lista de palabras
        for palabra in palabras:
            aux = random.randint(0, len(palabra)-1)
            nuevoRosco.append(palabra[aux])
            palabra.pop(aux)
        # Crea un diccionario con el rosco generado
        rosco = {"rosco": nuevoRosco}

        # Crea un diccionario para llevar el seguimiento de letras completadas
        listaPalabrasCompletadas = {"letrasCompletadas": palabrasCompletadas}

        # Actualiza el diccionario del jugador con el rosco y las letras completadas
        jugador.update(rosco)
        jugador.update(listaPalabrasCompletadas)
  



jugadores = crearJugadores()

crearRosco(jugadores,palabras)

print(jugadores)