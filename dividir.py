def dividir_n_numeros():
    numeros_a_dividir = int(input('Cuantos números quieres dividir: '))
    resultado = float(input('Ingresa el dividendo: '))

    for numero in range(1, numeros_a_dividir):
        divisor = float(input(f'Ingresa el divisor {numero + 1}:'))
        if divisor != 0:
            resultado /= divisor
        else:
            print("Error: No se puede dividir entre cero.")
            return None