# Definiendo clase base

from abc import ABCMeta, abstractmethod

class Figuras(metaclass = ABCMeta):

    @abstractmethod

    def perimetro(self):
        pass

    @abstractmethod

    def area(self):
        pass

    @abstractmethod
    def __str__(self):
        pass
