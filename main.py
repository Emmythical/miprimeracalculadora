from multiplicar import multiplicar_n_numeros
from dividir import dividir_n_numeros
from suma import sumar_dos_numeros
from resta import restar_n_numeros
from suma_avanzada import sumar_n_numeros

while True:
    print('''
    Bienvenido a mi calculadora, por favor ingresa la opción que desees.
        
    1) Hacer una suma de N números.
    2) Hacer una multiplicación de N números.
    3) Hacer una división de 2 números.
    4) Hacer una suma de 2 números.
    5) Hacer una resta de N números.
        
    0) Salir del programa.
        ''')

    opcion = int(input('> '))

    if opcion == 0:
        break



    elif opcion == 1:
        resultado = sumar_n_numeros()
        print(f'el resultado es {resultado}')
        

    elif opcion == 2:
        resultado = multiplicar_n_numeros()
        print(f'el resultado es {resultado}')
       

    elif opcion == 3:
        resultado = dividir_n_numeros()
        print(f'el resultado es {resultado}')
        

    elif opcion == 4:
        resultado = sumar_dos_numeros()
        print(f'el resultado es {resultado}')
        

    elif opcion == 5:
        resultado = restar_n_numeros()
        print(f'el resultado es {resultado}')        
        

