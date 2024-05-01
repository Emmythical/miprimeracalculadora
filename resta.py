def restar_n_numeros():
    numeros_a_restar = int(input('Cuantos números quieres restar: '))
    
    resultado = float(input('Ingresa el minuendo: '))

    for numero in range(1, numeros_a_restar):
        numero_a_restar = float(input(f'Ingresa el sustraendo {numero + 1}: '))
        resultado -= numero_a_restar

    return resultado
