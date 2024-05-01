def multiplicar_n_numeros():
    numeros_a_multiplicar = int(input('Cuantos números quieres multiplicar: '))
    producto = 1

    for numero in range(0, numeros_a_multiplicar):
        numero_a_multiplicar = float(input(f'Ingresa el numero {numero + 1} a multiplicar:'))
        producto *= numero_a_multiplicar

    return producto