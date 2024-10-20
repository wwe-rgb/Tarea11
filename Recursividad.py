
print("Conteo Regresivo")
def printRev(m):
    
    if m > 0:
        print(m)  
        printRev(m - 1) 
        
 
# Definimos n fuera de la función
n = 10
printRev(n)

pila = []

# Agregando elementos a la pila
pila.append(1)
pila.append(2)
pila.append(3)
pila.append(4)
pila.append(5)
print("Pila")
pila = []

# Agregando elementos a la pila
pila.append(1)
pila.append(2)
pila.append(3)
pila.append(4)
pila.append(5)

print("Pila inicial:", pila)

# Definiendo la función para eliminar un elemento específico
def eliminarElemento(pila, elemento):
    # Comprobamos si la pila está vacía
    if not pila:
        return False  # Elemento no encontrado
    
    # Sacamos el último elemento (LIFO)
    ultimo_elemento = pila.pop()

    # Si el último elemento es el que queremos eliminar
    if ultimo_elemento == elemento:
        print(f"Elemento {elemento} eliminado.")
        return True  # Elemento encontrado y eliminado
    
    # Llamada recursiva
    encontrado = eliminarElemento(pila, elemento)

    # Si no encontramos el elemento, lo volvemos a agregar
    if not encontrado:
        pila.append(ultimo_elemento)
    else:
        print(f"Elemento {ultimo_elemento} restaurado en la pila.")
    
    return encontrado

# Llamamos a la función para eliminar el 3
eliminarElemento(pila, 3)

print("Pila final:", pila)
