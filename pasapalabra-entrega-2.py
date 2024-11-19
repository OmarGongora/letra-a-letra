import random
from datetime import datetime
from functools import reduce

#Declaramos la lista de listas con las que vamos a trabajar


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
            cantidadJugadores = int(input("¿Cuántos jugadores formarán parte de la partida? \nEl rango debe ser entre 1 y 4 jugadores: "))
            
            # Verifica que el número esté dentro del rango permitido
            if 1 <= cantidadJugadores <= 4:
                valido = True
            else:
                print("Por favor, ingresa un número entre 1 y 4: ")
                
        except ValueError:
            print("El valor ingresado no es valido, por favor ingrese un numero entero entre 1 y 4: ")

    

    # Itera según la cantidad de jugadores especificada
    for i in range(cantidadJugadores):
        nombre = str(input(f"ingrese el nombre del jugador numero {i+1}: "))

        # Crea un diccionario para representar al jugador
        jugador = {
            "jugador": i,
            "nombre": nombre,
            "errores": 0,
            "aciertos": 0,
            "posicion": 0,
            "rosco": [],
            "palabrasCompletadas": [],
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
        listaPalabrasCompletadas = {"palabrasCompletadas": palabrasCompletadas}

        # Actualiza el diccionario del jugador con el rosco y las letras completadas
        jugador.update(rosco)
        jugador.update(listaPalabrasCompletadas)

def actualizarPosicion(listaJugadores, turno):
    """
        Esta funcion sirve para actualizar el turno del jugador correspondiente
    """
    if len(set(listaJugadores[turno]["rosco"]).difference(set(listaJugadores[turno]["palabrasCompletadas"]))) > 0:  # Si aún hay letras por completar               
        if listaJugadores[turno]["posicion"] == len(listaJugadores[turno]["rosco"]) - 1:
            listaJugadores[turno].update({"posicion": 0})  # Vuelve al inicio si está en la última letra
        else:
            listaJugadores[turno].update({"posicion": listaJugadores[turno]["posicion"] + 1})  # Avanza a la siguiente letra

def ordenamientoBurbujaRecursivo(lista, n=None):
    """
    Esta funcion ordena una lista de menor a mayor dependiendo la cantidad de acierto de los jugadores
    """
    if n is None:
        n = len(lista)
    
    if n <= 1:
        return
    
    for i in range(n-1):
        if lista[i]["aciertos"] > lista[i+1]["aciertos"]:
            aux = lista[i]
            lista[i] = lista[i+1]
            lista[i+1] = aux
    
    ordenamientoBurbujaRecursivo(lista, n-1)

calcularPorcentaje = lambda ganadas, totales: (ganadas / totales) * 100 if totales > 0 else 0


# Funciones para historial con manejo de archivos 

# Funcion para definir fecha y hora
def definirHorario():
    """
    Crea y devuelve la fecha y la hora del momento en que se ejecuta

    return:
        una tupla con 2 variables donde indica por un lado la fecha y por el otro la hora
    """
    #Funcion para definir fecha y hora del momento en que se ejecuta

    fechaHora = str(datetime.now())

    partes = fechaHora.split(" ")

    fecha = partes[0]
    hora = partes[1][:5] 

    horario = f"{fecha}|{hora}"

    return horario


#Funcion para almacenar historial de jugadores ganadores
def guardarHistorialGanador(ganador):
    """
        Abre el archivo de texto donde se escribira y guardara el ganador y el horario de la partida jugada
    """
    historial = open("archivos/historial_ganadores.txt","a")

    historial.write(f"{ganador['nombre']} | {definirHorario()}\n")

    print("Se registraron los datos de la partida en el historial")
    historial.close()


#Funcion para definir historial de cada jugador
def guardarHistorialJugador(jugador,resultado):
    """
        Abre el archivo de texto donde se escribira y guardara el jugador y el horario de la partida jugada
  
    """
    historialNombre = f"archivos/historial_{jugador['nombre']}.txt"
    historial = open(historialNombre,"a")

    historial.write(f'{definirHorario()} | {jugador["nombre"]} | {jugador["aciertos"]} | {jugador["errores"]} | {resultado} \n')

    historial.close()

#Funcion para mostrar en consola el historial de ganadores
def verHistorialGanadores():
    """
        Esta funcion sirve para mostrar el historial de todos los ganadores
    """
    try:
        archivo = open("archivos/historial_ganadores.txt", "r")
        contenido = archivo.read()
        renglones = contenido.split("\n")
        historial = []
        for renglon in renglones:
            aux = renglon.split("|")
            historial.append(aux)
        for i in range(len(historial)-1):
            print(f'Partida del{historial[i][1]} a las {historial[i][2]} - ganador: {historial[i][0]}')
        archivo.close()
    except FileNotFoundError:
        print("No se encontro un historial previo")
    

def verHistorialJugador(jugador):
    """
        Esta funcion sirve para mostrar el historial de un jugador en especifico
    """
    try:
        archivo = open(f"archivos/historial_{jugador}.txt", "r")
        contenido = archivo.read()
        renglones = contenido.split("\n")
        historial = []
        for renglon in renglones:
            aux = renglon.split("|")
            historial.append(aux)
        print("-----------------------------------------")
        print(f"Historial de {jugador} ")
        print("-----------------------------------------")
        for i in range(len(historial)-1):
            print(f'Partida del{historial[i][0]} a las {historial[i][1]} - Aciertos: {historial[i][3]} - Errores: {historial[i][4]} - Resultado: {historial[i][5]}')
        archivo.close()
    except FileNotFoundError:
        print("No se encontro un historial previo para esta persona")

def verEstadisticasJugador(jugador):
    """
        Funcion que sirve para mostrar el porcentaje de efectividad que tuvo un jugador en especifico en respecto a aciertos y partidas
    """
    try:
        archivo = open(f"archivos/historial_{jugador}.txt", "r")
        contenido = archivo.read()
        renglones = contenido.split("\n")
        historial = []

        aciertos = []
        errores = []
        victorias = []
        derrotas = []


        for renglon in renglones:
            aux = renglon.split("|")
            historial.append(aux)


        for i in range(len(historial)-1):
            aciertos.append(historial[i][3])
            errores.append(historial[i][4]) 

            # Clasificar la partida como victoria o derrota
            if historial[i][5].strip() == 'ganador':
                victorias.append(1)
            else:
                derrotas.append(1)

        aciertos = map(int, aciertos)
        errores = map(int, errores)

        totalAciertos = reduce(lambda x, y: x + y, aciertos, 0) 
        totalErrores = reduce(lambda x, y: x + y, errores, 0)
        totalPuntos = totalAciertos + totalErrores
        totalVictorias = len(victorias)
        totalDerrotas = len(derrotas)
        totalPartidas = totalVictorias + totalDerrotas


        print(f'El jugador {jugador} tuvo un total de {totalAciertos} aciertos en todas sus partidas y {totalErrores} errores \nDando asi un {calcularPorcentaje(totalAciertos,totalPuntos)}% de efectividad al contestar')
        print(f'Por otra parte {jugador} presenta {totalVictorias} victorias y {totalDerrotas} derrotas, dando un {calcularPorcentaje(totalVictorias,totalPartidas)}% de efectividad en partidas')

        
        archivo.close()
    except FileNotFoundError:
        print("No se encontro un historial previo para esta persona")




menu = True
jugar = False
partida = True
empate = False
jugadores = []
turno = 0


while menu:
    eleccion = 0
    print("Bienvenido a Letra a Letra!!!")

    valido = False
    while not valido:
        try:
            eleccion = int(input("Selecciona la opcion que deseas realizar\n 1. Jugar 2. Ver historial 3. Cerrar \n"))
            valido = True
        except ValueError:
            print("El valor ingresado no es valido, por favor ingresa 1 para jugar, 2 para ver historial o 3 para cerrar: ")
    
    if eleccion == 1:
        jugar = True
        menu = False
    elif eleccion == 2:
        valido = False
        while not valido:
            try:
                eleccion = int(input("1.Ver historial de ultimos ganadores \n2.Ver historial de un jugador en especifico\n"))
                valido = True
            except ValueError:
                print("El valor ingresado no es valido, por favor ingresa 1 para ver el historial de ultimos ganadores o 2 para ver un historial en especifico: ")
            if eleccion == 1:
                verHistorialGanadores()
                valido = False
                while not valido:
                    try:
                        eleccion = int(input("Deseas volver al menu? 1.Si 2.No: \n"))
                        valido = True
                    except ValueError:
                        print("El valor ingresado no es valido, por favor ingresa 1 si desea volver al menu, 2 para no: ")
                if eleccion == 2:
                    print("Muchas gracias!!!")
                    jugar = False
                    menu = False
                    eleccion = None
                
            if eleccion == 2:
                verHistorial = str(input("Ingrese el nombre del jugador: "))
                verHistorialJugador(verHistorial)

                valido = False
                while not valido:
                    try:
                        eleccion = int(input("Deseas mostrar estadisticas del jugador? 1.Si 2.No: "))
                        valido = True
                    except ValueError:
                        print("El valor ingresado no es valido, por favor ingresa 1 para si, 2 para no: ")
                if eleccion == 2:
                    valido = False
                    while not valido:
                        try:
                            eleccion = int(input("Deseas volver al menu? 1.Si 2.No: "))
                            valido = True
                        except ValueError:
                            print("El valor ingresado no es valido, por favor ingresa 1 si desea volver al menu, 2 para no: ")
                    if eleccion == 2:
                        print("Muchas gracias!!!")
                        menu = False
                else:
                    verEstadisticasJugador(verHistorial)
                    valido = False
                    while not valido:
                        try:
                            eleccion = int(input("Deseas volver al menu? 1.Si 2.No: "))
                            valido = True
                        except ValueError:
                            print("El valor ingresado no es valido, por favor ingresa 1 si desea volver al menu, 2 para no: ")
                    if eleccion == 2:
                        print("Muchas gracias!!!")
                        menu = False
    else:
        menu = False




                



# Bucle principal que se ejecuta mientras la variable 'jugar' sea verdadera
while jugar:
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




    jugadores = crearJugadores()  # Llama a la función para crear jugadores y almacena la lista resultante
    crearRosco(jugadores, palabras)  # Llama a la función para crear el rosco para cada jugador

    # Bucle principal de la partida que se ejecuta mientras 'partida' sea verdadera
    while partida:

        # Verifica si es el turno del jugador actual
        if jugadores[turno]["completado"] == False:
            # Verifica si la letra en la que estamos posicionados no esta completada
            if jugadores[turno]["rosco"][jugadores[turno]["posicion"]] not in set(jugadores[turno]["rosco"]).intersection(set(jugadores[turno]["palabrasCompletadas"])):
                
                # Mensaje de turno para el jugador actual
                print("----------------------------------------------------------")
                print(f"Turno de {jugadores[turno]['nombre']}. Recuerda que si no quieres arriesgar y prefieres pasar tu turno, debes enviar el mensaje sin nada escrito")

                # Solicita la respuesta del jugador
                respuesta = input(f"{jugadores[turno]['rosco'][jugadores[turno]['posicion']][1]}: ")
                # Convierte la respuesta a minusculas y elimina posibles espacios a los lados 
                respuesta = respuesta.lower()
                respuesta = respuesta.strip()

                # Verifica si la respuesta es correcta
                if respuesta == jugadores[turno]["rosco"][jugadores[turno]["posicion"]][0]:
                    # Respuesta correcta
                    print("La respuesta es Correcta!!!")

                    # Actualiza la cantidad de aciertos del jugador
                    jugadores[turno].update({"aciertos": jugadores[turno]["aciertos"] + 1})

                    # Actualiza la lista de letras completadas
                    jugadores[turno]["palabrasCompletadas"].append(jugadores[turno]["rosco"][jugadores[turno]["posicion"]])

                    # Actualiza la posición del jugador
                    actualizarPosicion(jugadores,turno)
                
                # Verifica si el jugador eligió pasar su turno
                elif respuesta == "":
                    print("Elegiste saltar tu turno, podrás intentarlo de nuevo más tarde")
                    # Actualiza la posición del jugador
                    actualizarPosicion(jugadores,turno)

                    # Cambia al siguiente turno
                    if turno == len(jugadores) - 1:
                        turno = 0  # Vuelve al primer jugador si estaba en el último
                    else:
                        turno += 1  # Avanza al siguiente jugador

                # El jugador fallo su turno
                else:
                    print(f"La respuesta es incorrecta, la respuesta correcta era {jugadores[turno].get('rosco')[jugadores[turno].get('posicion')][0]}")

                    # Actualiza la cantidad de errores del jugador
                    jugadores[turno].update({"errores": jugadores[turno]["errores"] + 1})

                    # Actualiza la lista de letras completadas
                    jugadores[turno]["palabrasCompletadas"].append(jugadores[turno]["rosco"][jugadores[turno]["posicion"]])

                    # Actualiza la posición del jugador
                    actualizarPosicion(jugadores,turno)

                    # Cambia al siguiente turno
                    if turno == len(jugadores) - 1:
                        turno = 0  # Vuelve al primer jugador si estaba en el último
                    else:
                        turno += 1  # Avanza al siguiente jugador
            else:
                # Si la letra fue completada avanza a la siguiente
                jugadores[turno].update({"posicion": jugadores[turno]["posicion"] + 1})
        
        # Verifica si el jugador ha completado todas sus letras
        if len(set(jugadores[turno]["rosco"]).difference(set(jugadores[turno]["palabrasCompletadas"]))) == 0:
            # Termina el turno del jugador si completó todas sus letras
            jugadores[turno].update({"completado": True}) 

            # Cambia al siguiente turno
            if turno == len(jugadores) - 1:
                turno = 0  # Vuelve al primer jugador si estaba en el último
            else:
                turno += 1  # Avanza al siguiente jugador

        # Verifica cuántos jugadores aún están activos en la partida
        aux = 0
        for jugador in jugadores:
            if jugador["completado"] == False:
                aux += 1  # Cuenta los jugadores que aún tienen turnos activos
        
        # Si todos los jugadores han terminado sus turnos
        if aux == 0:
            print("----------------------------------------")
            print("FINAL DE LA PARTIDA\n")

            # Ordenar de mayor a menor los jugadores segun sus puntajes
            ordenamientoBurbujaRecursivo(jugadores)
            jugadores = jugadores[::-1]

            #Se imprimen los resultados
            for i in range(len(jugadores)):
                print(f"{i + 1} - {jugadores[i].get('nombre')} - Aciertos: {jugadores[i].get('aciertos')} - Errores: {jugadores[i].get('errores')} ")
                print("----------------------------------------")
    


            # Verificar si hay algun empate
            jugadoresEmpatados = []
            if len(jugadores) > 1:
                
                #Funcion lambda en un filter para separar los jugadores que tuvieron la misma cantidad de aciertos
                jugadoresEmpatados = list(filter(lambda jugador: jugador["aciertos"] == jugadores[0]["aciertos"], jugadores))

                # En caso de empate se pone en juego un desempate
                if len(jugadoresEmpatados) > 1:
                    empate = True

                    print("Se detecto un empate entre los siguientes jugadores: ")
                    print("")
                    for i in range(len(jugadoresEmpatados)):
                        print(f"{i + 1} - {jugadores[i]['nombre']} - Aciertos: {jugadores[i]['aciertos']} - Errores: {jugadores[i]['errores']} ")
                        print("----------------------------------------")

                    # Se hace una ronda express para definir un ganador
                    print("A continuacion se llevara a cabo una ronda express para determinar el ganador")
                    print("")

                    ganador = False
                    jugadorFallido = []
        
                    while ganador == False:
                        # iterar sobre jugadores restantes
                        
                        for jugador in jugadoresEmpatados:
                            auxLetra = random.randint(0, len(palabras) - 1)
                            auxPalabra = random.randint(0, len(palabras[auxLetra]) - 1)

                            print("----------------------------------------------------------")
                            print(f"Turno de {jugador['nombre']}.")
                            print("Es obligatorio arriesgar. En caso de no hacerlo, se considerara erroneo.")
                            respuesta = input(f"{palabras[auxLetra][auxPalabra][1]}: ")

                            # Validar respuesta
                            if respuesta == palabras[auxLetra][auxPalabra][0]:
                                print("CORRECTO!!!")
                            else:
                                print("INCORRECTO :(")
                                jugadorFallido.append(jugador)

                            # Eliminar palabra usada
                            palabras[auxLetra].pop(auxPalabra)
                            
                        # Determinar el estado del juego
                        if len(jugadorFallido) == len(jugadoresEmpatados):  # Todos fallaron
                            print("Todos los jugadores fallaron. Continua la ronda.")
                            jugadorFallido = []
                        else:
                            # Eliminar jugadores que fallaron
                            jugadoresEmpatados = [
                                jugador for jugador in jugadoresEmpatados if jugador not in jugadorFallido
                            ]
                            jugadorFallido = []  # Reiniciar lista de fallidos
                            
                        # Verificar si hay un ganador y termina la partida en caso de haberlo
                        if len(jugadoresEmpatados) == 1:
                            print(f"¡El ganador es {jugadoresEmpatados[0]['nombre']}!")
                            guardarHistorialGanador(jugadoresEmpatados[0])
                            for jugador in jugadores:
                                if jugador == jugadoresEmpatados[0]:
                                    guardarHistorialJugador(jugador,'ganador')
                                else:
                                    guardarHistorialJugador(jugador,'no ganador')
                            ganador = True
                            partida = False


            if not empate:
                guardarHistorialGanador(jugadores[0])

                for jugador in jugadores:
                    if jugadores[0] == jugador:
                        guardarHistorialJugador(jugador,'ganador')
                    else:
                        guardarHistorialJugador(jugador,'no ganador')
                partida = False     

    # Consulta para volver a jugar o si se desea terminar la ejecucion del programa                                   
    valido = False
    while valido == False:
        try:
            respuesta = int(input("Te gustaria jugar otra partida? 1.Si 2.No"))
            
            # Verifica que el número esté dentro del rango permitido
            if respuesta == 1 or respuesta == 2:
                valido = True
            else:
                print("Por favor, ingresa un 1-Para si y 2-Para no")
                
        except ValueError:
            print("El valor ingresado no es valido, por favor ingrese 1-Para si y 2-Para no")
    if respuesta == 2:
        print("Muchas gracias por jugar")
        jugar = False
    else:
        empate = False
        jugadores = []
        turno = 0
        partida = True