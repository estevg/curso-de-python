# -*- coding: utf-8 -*-
import random

def run():
    number_found = False
    random_number = random.randint(0, 20)

    while not number_found:
        number = int(input('Ingresa un numero: '))

        if number == random_number:
            print('Felicidades encontraste el numero')
            number_found = True
        elif number > random_number:
            print('El numero es más pequeño')
        else:
            print('El numero es más grande')

if __name__ == '__main__':
    run()