# -*- coding: utf-8 -*-

foreign_exchange_calculator(ammount):
    max_to_col_rate = 145.97

    return max_to_col_rate * ammount

def run():
    print('C A L C U L A D O R A  D E  D I V I S A S')
    print('Convierte pesos mexicanos a pesos colombianos')
    print('')
    
    ammount = float(raw_input('Ingrese la cantidad de pesos mexicanos que quieres convertir'))

    result = foreign_exchange_calculator(ammount)

    print('${} pesos mexicanos son ${} pesos colombianos'.format(ammount, result))
    print('')



if __name__ == '__main__':
    run()