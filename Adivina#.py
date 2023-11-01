import random

print('¡Bienvenido al juego de adivina un número!')
print('Trata de adivinar un número entre el 1 y el 100')

num_secreto = random.randint(1, 100)

adv = False

while not adv:
    num_usuario = int(input('Ingresa un número entre el 1 y el 100: '))

    if num_usuario == num_secreto:
        print('Felicidades has acertado!')
        adv = True
    elif num_usuario < num_secreto:
        print('El número secreto es más alto')
    else:
        print('El número secreto es más bajo')