class Registro:

    def __init__(self, tem=0, hum=0, pre=0):
        self.__temperatura = int(tem)
        self.__humedad = int(hum)
        self.__presionat = int(pre)

    def get_tem(self):
        return self.__temperatura

    def get_hum(self):
        return self.__humedad

    def get_pre(self):
        return self.__presionat
