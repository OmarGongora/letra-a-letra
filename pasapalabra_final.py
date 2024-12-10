import random
import re
from datetime import datetime
from functools import reduce
import questionary

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
                
        except ValueError as e:
            print("El valor ingresado no es valido, por favor ingrese un numero entero entre 1 y 4: ")
            registrarExcepcion(e)
        except:
            print("Ocurrio un error inesperado")

    

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

calcularPorcentaje = lambda ganadas, totales: round((ganadas / totales) * 100,1) if totales > 0 else 0


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

    horario = f"{fecha}-{hora}"

    return formatearFecha(horario)

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
    except:
        print("Ocurrio un error inesperado")
    
#Funcion para mostrar en consola el historial de un jugador en especifico
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
    except:
        print("Ocurrio un error inesperado")

#Funcion para ver las estadisticas del jugador
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
    except:
        print("Ocurrio un error inesperado")

def cargarPalabras(nombreArchivo):
            palabras = []
            try:
                with open(nombreArchivo, "r", encoding="utf-8") as archivo:
                    letraActual = []
                    for linea in archivo:
                        linea = linea.strip()
                        if linea:
                            palabra, pista = linea.split("|")  # Separar palabra y pista
                            letraActual.append((palabra, pista))
                        else:
                            if letraActual:
                                palabras.append(letraActual)
                                letraActual = []
                    if letraActual:  # Añadir el último grupo si no terminó con línea vacía
                        palabras.append(letraActual)
                return palabras
            except FileNotFoundError:
                print("No se encontro ningun archivo con las palabras")
            except:
                print("Ocurrio un error inesperado")

def registrarExcepcion(e):
    try:
        archivo = open('errores.log','a')
        try:
            horario = definirHorario()
            error = f"{horario} | Tipo:{type(e)} - Mensaje: {str(e)}\n"
            print(f"Ocurrion un error: {error}")
            archivo.write(error)
        finally:
            archivo.close()
    except Exception as logError:
        print(f"Error al escribir en el log:{logError}")

def formatearFecha(fecha):
    return re.sub(r"(\d{4})-(\d{2})-(\d{2})", r"\3/\2/\1", fecha)

def main():

    menu = True
    jugar = False
    partida = True
    empate = False
    jugadores = []
    turno = 0

    # Seccion de codigo donde se establece el menu

    while menu:
        print("Bienvenido a Letra a Letra!!!")

        # Menú principal 
        eleccion = questionary.select(
            "Selecciona la opción que deseas realizar:",
            choices=["Jugar", "Ver historial", "Cerrar"]
        ).ask()

        if eleccion == "Jugar":
            # Preparar para jugar
            print("Iniciando juego...")
            menu = False
            jugar = True

        elif eleccion == "Ver historial":
            # Menú de historial
            historial_opcion = questionary.select(
                "Selecciona la opción para el historial:",
                choices=["Ver historial de últimos ganadores", "Ver historial de un jugador en específico"]
            ).ask()

            if historial_opcion == "Ver historial de últimos ganadores":
                verHistorialGanadores()

                volver = questionary.select("¿Deseas volver al menú?",["Si","No"]).ask()
                if volver == "No":
                    print("Muchas gracias!!!")
                    menu = False

            elif historial_opcion == "Ver historial de un jugador en específico":
                jugador = questionary.text("Ingresa el nombre del jugador: ").ask()
                verHistorialJugador(jugador)

                estadisticas = questionary.select("¿Deseas mostrar estadísticas del jugador?",choices=["Si","No"]).ask()
                if estadisticas == "Si":
                    verEstadisticasJugador(jugador)

                volver = questionary.select("¿Deseas volver al menú?",choices=["Si","No"]).ask()
                if volver == "No":
                    print("Muchas gracias!!!")
                    menu = False

        elif eleccion == "Cerrar":
            menu = False
            print("Hasta Luego")   

    # Bucle principal que se ejecuta mientras la variable 'jugar' sea verdadera
    while jugar:
        
        
        palabras = cargarPalabras("archivo_palabras")


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
            except:
                print("Ocurrio un error inesperado")
        if respuesta == 2:
            print("Muchas gracias por jugar")
            jugar = False
        else:
            empate = False
            jugadores = []
            turno = 0
            partida = True


if __name__ == "__main__":
    main()