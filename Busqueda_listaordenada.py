def busqueda_binaria(lista, objetivo):
    izquierda, derecha = 0, len(lista) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        valor_medio = lista[medio]

        if valor_medio == objetivo:
            return True
        elif valor_medio < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1

    return False

# Ejemplo de uso
lista_ordenada = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
objetivo = 7

if busqueda_binaria(lista_ordenada, objetivo):
    print(f"El numero {objetivo} esta en la lista.")
else:
    print(f"El numero {objetivo} no esta en la lista.")
