from pasapalabra_final import calcularPorcentaje,actualizarPosicion,ordenamientoBurbujaRecursivo

#Tests calculador de porcentaje
def test_calcularPorcentaje():
    assert calcularPorcentaje(10,20) == 50
    assert calcularPorcentaje(10,25) == 40
    assert calcularPorcentaje(2,33) == 6.1
    assert calcularPorcentaje(90,91) == 98.9


#Tests Actualizar posicion
def test_actualizarPosicion():
    jugadores = [{"rosco": ["a", "b", "c"], "palabrasCompletadas": ["a"], "posicion": 1}]
    turno = 0

    actualizarPosicion(jugadores, turno)

    assert jugadores[0]["posicion"] == 2  # Avanza a la siguiente posición

def test_actualizarPosicionRreinicia():
    jugadores = [{"rosco": ["a", "b", "c"], "palabrasCompletadas": ["a"], "posicion": 2}]
    turno = 0

    actualizarPosicion(jugadores, turno)

    assert jugadores[0]["posicion"] == 0  # Vuelve al inicio del "rosco"


#Tests Ordenamiento burbuja con recursividad

# Lista vacía 
def test_ordenamiento_burbuja_lista_vacia():
    lista = []
    ordenamientoBurbujaRecursivo(lista)
    assert lista == []  

# Ordenado de menor a mayor
def test_ordenamientoBurbujaRecursivo():
    lista = [
        {"aciertos": 5, "nombre": "Jugador 3"},
        {"aciertos": 3, "nombre": "Jugador 1"},
        {"aciertos": 4, "nombre": "Jugador 2"},
    ]
    ordenamientoBurbujaRecursivo(lista)
    assert lista == [
        {"aciertos": 3, "nombre": "Jugador 1"},
        {"aciertos": 4, "nombre": "Jugador 2"},
        {"aciertos": 5, "nombre": "Jugador 3"},
    ]  

#Se mantiene igual
def test_ordenamiento_burbuja_ya_ordenado():
    lista = [
        {"aciertos": 1, "nombre": "Jugador A"},
        {"aciertos": 2, "nombre": "Jugador B"},
        {"aciertos": 3, "nombre": "Jugador C"},
    ]
    ordenamientoBurbujaRecursivo(lista)
    assert lista == [
        {"aciertos": 1, "nombre": "Jugador A"},
        {"aciertos": 2, "nombre": "Jugador B"},
        {"aciertos": 3, "nombre": "Jugador C"},
    ]  