from Base_ejercicio_2 import Entrada_Evento
import numpy as np


class Alimentos:
    def __init__(self, codigo, descripcion, precio):
        self.__codigo = codigo
        self.__descripcion = descripcion
        self.__precio = precio

    @property
    def codigo(self):
        return self.__codigo

    @property
    def descripcion(self):
        return self.__descripcion

    @property
    def precio(self):
        return self.__precio

    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo

    @descripcion.setter
    def descripcion(self, descripcion):
        self.__descripcion = descripcion

    @precio.setter
    def precio(self, precio):
        self.__precio = precio 

    def __str__(self):
        return f"Código: {self.__codigo}, Descripción: {self.__descripcion}, Precio: ${self.__precio:.2f}"
    


class Entrada_Vip(Entrada_Evento):
    def __init__(self, precio_entrada, impuesto_venta, asiento, fila, cliente, evento, alimentos=None):
        super().__init__(precio_entrada, impuesto_venta, asiento, fila, cliente, evento)
        self.__alimentos = alimentos if alimentos else []  

    @property
    def alimentos(self):
        return self.__alimentos
    
    @alimentos.setter
    def alimentos(self, alimentos):
        if isinstance(alimentos, list):  
            self.__alimentos = alimentos

    def total_alimento(self):
        return sum(alimento.precio for alimento in self.__alimentos)

    def precio_pagar(self):
        return super().precio_pagar() + self.total_alimento()

    def __str__(self):
        resultado = super().__str__() + "\n"
        resultado += "Alimentos seleccionados:\n" if self.__alimentos else "No hay alimentos seleccionados."
        
        for alimento in self.__alimentos:
            resultado += f"\n{alimento}"

        resultado += f"\nTotal alimentos: ${self.total_alimento():.2f} MXN"
        return resultado
    

class Entrada_Frecuente(Entrada_Evento):
    def __init__(self, precio_entrada, impuesto_venta, asiento, fila, cliente, evento, descuento):
        super().__init__(precio_entrada, impuesto_venta, asiento, fila, cliente, evento)
        self.__descuento = descuento  

    @property
    def descuento(self):
        return self.__descuento
    
    @descuento.setter
    def descuento(self, descuento):
        self.__descuento = descuento

    # Métodos
    def precio_pagar(self):
        descuento_aplicado = self.precio_entrada * self.__descuento
        return super().precio_pagar() - descuento_aplicado  


    def __str__(self):

        str_sp = f"El descuento aplicado es de {self.__descuento * 100}% sobre el valor del boleto sin impuestos\n"
        str_sp += super().__str__() + '\n'  

        return str_sp






