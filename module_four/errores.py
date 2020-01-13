# -*- coding: utf-8 -*-

countries = {
    'mexico': 122,
    'colombia': 49,
    'argentina': 43,
    'chile': 18,
    'peru': 31
}

while True:
    country = str(input('Escribe el nombre del pais: ')).lower()
    try:
        print('La población de {} es: {} millones'.format(country, countries[country]))
    except KeyError:
        print('NO tenemos el dato de la población del pais que nos diste {}'.format(country))
