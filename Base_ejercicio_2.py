# Definiendo clase base

## Componente Cliente

class Cliente:
    def __init__(self, nombre, direccion, telefono):
        self.__nombre = nombre
        self.__direccion = direccion
        self.__telefono = telefono

    @property
    def nombre(self):
        return self.__nombre

    @property
    def direccion(self):
        return self.__direccion

    @property
    def telefono(self):
        return self.__telefono

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @direccion.setter
    def direccion(self, direccion):
        self.__direccion = direccion

    @telefono.setter
    def telefono(self, telefono):
        self.__telefono = telefono

    def __str__(self):
        return f"La entrada está a nombre de: {self.__nombre} con dirección en: {self.__direccion} y con el número celular: {self.__telefono}"


# Componente Evento
class Evento:
    def __init__(self, nombre, fecha, ubicacion):
        self.__nombre = nombre
        self.__fecha = fecha
        self.__ubicacion = ubicacion

    @property
    def nombre(self):
        return self.__nombre

    @property
    def fecha(self):
        return self.__fecha

    @property
    def ubicacion(self):
        return self.__ubicacion

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @fecha.setter
    def fecha(self, fecha):
        self.__fecha = fecha

    @ubicacion.setter
    def ubicacion(self, ubicacion):
        self.__ubicacion = ubicacion


    def __str__(self):
        return f"El evento registrado es: {self.__nombre} con fecha para el día: {self.__fecha} en el lugar ubicado en: {self.__ubicacion}"



## Base

class Entrada_Evento():
    def __init__(self, precio_entrada, impuesto_venta, asiento, fila, cliente, evento):
        self.__precio_entrada = precio_entrada
        self.__impuesto_venta = impuesto_venta
        self.__asiento = asiento
        self.__fila = fila
        self.__cliente = cliente
        self.__evento = evento
    
    @property

    def precio_entrada(self):
        return self.__precio_entrada
    
    @property

    def impuesto_venta(self):
        return self.__impuesto_venta
    
    @property

    def asiento(self):
        return self.__asiento
    
    @property

    def fila(self):
        return self.__fila
    
    @property

    def cliente(self):
        return self.__cliente

    @property 

    def evento(self):
        return self.__evento

    @precio_entrada.setter
    
    def precio_entrada(self, precio_entrada):
        self.__precio_entrada = precio_entrada

    @impuesto_venta.setter

    def impuesto_venta(self, impuesto_venta):
        self.__impuesto_venta = impuesto_venta

    @asiento.setter

    def asiento(self, asiento):
        self.__asiento = asiento

    @fila.setter

    def fila(self, fila):
        self.__fila = fila



    def precio_pagar(self):
        return self.__precio_entrada + self.__impuesto_venta
    
    
    def __str__(self):
        resultado = (f'{self.__cliente}\n'
                     f'{self.__evento}\n'
                     f'El asiento es el número {self.__asiento}, en la fila {self.__fila}\n'
                    f'El precio del boleto es de ${self.__precio_entrada} + impuestos de ${self.__impuesto_venta}\n'
                    f'El precio total es de ${self.precio_pagar()}')
        return resultado


