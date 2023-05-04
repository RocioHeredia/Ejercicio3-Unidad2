from ClassRegistro import Registro
import csv


class ListaBidimensional:

    def __init__(self, dia, hora):
        self.__ListaBidimensional = [[None for _ in range(hora)] for _ in range(dia)]

    def __str__(self):
        print(str(self.__ListaBidimensional))

    def agregar(self, dia, hora, re):
        self.__ListaBidimensional[dia - 1][hora] = re

    def leerArch(self):
        archivo = open('VariablesMeteorologicas.csv')
        reader = csv.reader(archivo, delimiter=';')
        for fila in reader:
            registro = Registro(int(fila[2]), int(fila[3]), int(fila[4]))
            self.agregar(int(fila[0]), int(fila[1]), registro)
        archivo.close()

    def mostrardatos(self):
        for dia in range(len(self.__ListaBidimensional)):
            for hora in range(len(self.__ListaBidimensional[dia])):
                print(f"Día {dia + 1}, Hora {hora}: {self.__ListaBidimensional[dia][hora]}")

    def menorvalordiayhora(self):

        min_temp = min_hum = min_pres = None

        for dia in range(len(self.__ListaBidimensional)):
            for hora in range(len(self.__ListaBidimensional[dia])):
                registro = self.__ListaBidimensional[dia][hora]
                if registro is not None:
                    if min_temp is None or registro.get_tem() < min_temp.get_tem():
                        min_temp = registro
                        min_temp_dia_hora = (dia + 1, hora)

                    if min_hum is None or registro.get_hum() < min_hum.get_hum():
                        min_hum = registro
                        min_hum_dia_hora = (dia + 1, hora)

                    if min_pres is None or registro.get_pre() < min_pres.get_pre():
                        min_pres = registro
                        min_pres_dia_hora = (dia + 1, hora)

        print('(Dia: {}, Hora: {}) -> Temperatura Minima: {}'.format(*min_temp_dia_hora, min_temp.get_tem()))
        print('(Dia: {}, Hora: {}) -> Humedad Minima: {}'.format(*min_hum_dia_hora, min_hum.get_hum()))
        print('(Dia: {}, Hora: {}) -> Presión Atmosférica Minima: {}'.format(*min_pres_dia_hora, min_pres.get_pre()))

    def mayorvalordiayhora(self):
        max_pres = max_hum = max_tem = None

        for dia in range(len(self.__ListaBidimensional)):
            for hora in range(len(self.__ListaBidimensional[dia])):
                registro = self.__ListaBidimensional[dia][hora]
                if registro is not None:
                    if max_tem is None or registro.get_tem() > max_tem.get_tem():
                        max_tem = registro
                        max_tem_dia_hora = (dia + 1, hora)

                    if max_hum is None or registro.get_hum() > max_hum.get_hum():
                        max_hum = registro
                        max_hum_dia_hora = (dia + 1, hora)

                    if max_pres is None or registro.get_pre() > max_pres.get_pre():
                        max_pres = registro
                        max_pres_dia_hora = (dia + 1, hora)
        print('(Dia: {}, Hora: {}) -> Temperatura Maxima: {} '.format(*max_tem_dia_hora, max_tem.get_tem()))
        print('(Dia: {}, Hora: {}) -> Humedad Maxima: {} '.format(*max_hum_dia_hora, max_hum.get_hum()))
        print('(Dia: {}, Hora: {})-> Presión Atmosférica Maxima: {} '.format(*max_pres_dia_hora, max_pres.get_pre()))

    def promMensualTemperatura(self):
        for hora in range(len(self.__ListaBidimensional[0])):
            sumador = 0
            cont = 0
            prom = 0.0
            for dia in range(len(self.__ListaBidimensional)):
                registro = self.__ListaBidimensional[dia][hora]
                if registro is not None:
                    sumador += registro.get_tem()
                    cont += 1
                    prom = sumador / cont
            print('El promedio mensual de temperatura de la hora {} es: {:.1f}'.format(hora, prom))

    def mostrarporhora(self, di):

        print('|{:^10}| {:^13}| {:^13}| {:^13}|'.format('Hora', 'Temperatura', 'Humedad', 'Presión'))
        print('-' * 57)
        for hora in range(len(self.__ListaBidimensional[0])):
            registro = self.__ListaBidimensional[di - 1][hora]
            if registro is not None:
                print('|{:^10}| {:^13}| {:^13}| {:^13}|'.format(hora, registro.get_tem(), registro.get_hum(), registro.get_pre()))


