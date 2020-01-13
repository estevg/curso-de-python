# -*- coding: utf-8 -*-

# Declaramos una clase con mayuscula Lamp
class Lamp():

    _LAMPS = ['''
          .
     .    |    ,
      \   '   /
       ` ,-. '
    --- (   ) ---
         \ /
        _|=|_
       |_____|
    ''',
    '''
         ,-.
        (   )
         \ /
        _|=|_
       |_____|
    ''' ]

    # Metodo de instacia "Self"
    # Metodo __init__ es el constructor es el primer metodo que se llamara 
    def __init__(self, is_turned_on):
        self._is_turned_on = False

    # Metodos publicos
    def turn_on(self):
        self._is_turned_on = True
        self.__display_images()

    def turn_off(self):
        self._is_turned_on = False
        self.__display_images()
    
    # Metodos privados
    def __display_images(self):
        if self._is_turned_on:
            print(self._LAMPS[0])
        else:
            print(self._LAMPS[1])

def run():
    lamp = Lamp(is_turned_on=False)

    while True:
        command = str(input('''
            ¿Qué deseas hacer?

            [p]render
            [a]pagar
            [s]alir
        '''))

        if command == 'p':
            lamp.turn_on()
        elif command == 'a':
            lamp.turn_off()
        else:
            break


if __name__ == '__main__':
    run()