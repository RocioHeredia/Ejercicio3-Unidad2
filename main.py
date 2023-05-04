from ListaBidimensional import ListaBidimensional


def menu():
    print('Menu de Opciones')
    print('1. Mostrar para cada variable el día y hora de menor y mayor valor.')
    print('2. Indicar la temperatura promedio mensual por cada hora.')
    print('3. Dado un número de día listar los valores de las tres variables para cada hora del día dado. ')


def funciones(opcion, lista_B):
    while opcion != 0:
        if opcion == 1:
            lista_B.menorvalordiayhora()
            lista_B.mayorvalordiayhora()
        if opcion == 2:
            lista_B.promMensualTemperatura()
        if opcion == 3:
            dia = int(input('Ingrese dia: '))
            lista_B.mostrarporhora(dia)

        opcion = int(input('Ingrese una opcion o 0 para finalizar: '))


if __name__ == '__main__':
    d = int(31)
    h = int(24)
    lista = ListaBidimensional(d, h)
    lista.leerArch()
    menu()
    op = int(input('Ingrese una opcion o 0 para finalizar: '))
    funciones(op, lista)
