# Definiendo clase base
import math
import numpy as np
from Base import Figuras


class Circulo (Figuras):
    def __init__(self, radio):
        self.__radio = radio

    @property

    def radio(self):
        return self.__radio
    
    @radio.setter

    def radio(self, radio):
        self.__radio = radio

    def perimetro(self):

        return 2 * math.pi * self.__radio
    
    def area(self):
        return  math.pi * (np.square(self.__radio))
    
    def __str__(self):
        return "Radio circulo: (%.2f)" % (self.__radio)
    

class Elipse(Figuras):
    def __init__(self, radio_menor = 0, radio_mayor = 0):
        self.__radio_menor = radio_menor
        self.__radio_mayor = radio_mayor

    @property

    def radio_menor(self):
        return self.__radio_menor

    @property

    def radio_mayor(self):
        return self.__radio_mayor
    
    @radio_menor.setter

    def radio_menor(self, radio_menor):
        self.__radio_menor = radio_menor

    @radio_mayor.setter

    def radio_mayor(self, radio_mayor):
        self.__radio_mayor = radio_mayor  

    def perimetro(self):

        return 2 * math.pi * np.sqrt((np.square(self.__radio_menor) + np.square(self.__radio_mayor)) / 2)
    
    def area(self):
        return  math.pi * self.radio_mayor * self.radio_menor
    
    def __str__(self):
        return "Elipse: (%.2f, %.2f )" % (self.__radio_menor, self.__radio_mayor)
    

class Anillo(Figuras):
    def __init__(self, radio_externo, radio_interno):
        self.__radio_externo = radio_externo
        self.__radio_interno = radio_interno

    @property

    def radio_externo(self):
        return self.__radio_externo
    
    @property

    def radio_interno(self):
        return self.__radio_interno
    
    @radio_externo.setter

    def radio_externo(self, radio_externo):
        self.__radio_externo = radio_externo

    @radio_interno.setter

    def radio_interno(self, radio_interno):
        self.__radio_interno = radio_interno

    def perimetro(self):
        return 2 * math.pi * self.__radio_externo + 2 * math.pi * self.__radio_interno
    
    def area(self):

        return math.pi * (np.square(self.__radio_externo) - np.square(self.__radio_interno))
    
    def __str__(self):
        return "Anillo: (%.2f, %.2f )" % (self.__radio_externo, self.__radio_interno)






