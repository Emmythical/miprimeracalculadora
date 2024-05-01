def sumar_n_numeros():
    numeros_a_sumar = int(input('Cuantos números quieres sumar: '))

    lista_numeros = [] 

    for numero in range (0, numeros_a_sumar):
        numero_a_sumar = float(input(f'Ingresa el numero {numero + 1} a sumar:'))
        lista_numeros.append(numero_a_sumar)

    return sum(lista_numeros)