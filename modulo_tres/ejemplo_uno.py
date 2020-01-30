
def average_temps(temps):
    sum_of_temps = 0

    for temp in temps:
        sum_of_temps += float(temp)

    return  sum_of_temps / len(temps)


if __name__ == '__main__':

    temps = []
    for i in range(7):
        number = int(input('Ingrese un numero: '))
        temps.append(number)
        

    avera = average_temps(temps)

    print('La temperatura promedio es: {}'.format(avera))
