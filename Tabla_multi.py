def tabla_mult(tabla, limite):
    for i in range(1, limite):
        resultado = tabla * i
        print(f'{tabla} x {i} = {resultado}')

tabla = int(input('Que tabla de multiplicar quieres saber?: '))

tabla_mult(tabla, 21)