# letras = {"a","e","i","o"}

# letrasCompletadas = {"a","i"}

# print(letras.symmetric_difference(letrasCompletadas))

# posicion = 0

# jugar = True
# while jugar:
#     if letras[posicion] in letras.symmetric_difference(letrasCompletadas):
#         agregar = int(input(f"{letras[posicion]} 1.si 2.no "))
#         if agregar == 1:
#             letrasCompletadas.add(letras[posicion])
#     posicion += 1

diccionario = {
    "nombre":"omar",
    "apellido":"gongora",
    "edad":22,
    "letras": ["a","e","i","o","u"]
}

diccionario["nombre"] = "jorge"

print(diccionario["letras"][1])