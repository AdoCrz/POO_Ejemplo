# POO_Ejemplo

Este repositorio contiene un proyecto en Python que simula un sistema de emisión de entradas para una Cadena de Eventos, implementado con Programación Orientada a Objetos (POO). Se utilizan conceptos como clases, herencia, atributos privados, getters, setters y métodos personalizados para calcular el precio total de cada entrada según el tipo de cliente.

🧱 ¿Qué hace este proyecto?
El sistema permite crear y gestionar diferentes tipos de entradas al evento:

Entrada estándar: Incluye información del cliente, evento, precio base, impuesto y asiento.

Entrada para clientes frecuentes: Aplica un descuento sobre el precio base.

Entrada VIP: Incluye una lista de alimentos y suma su precio al total a pagar.

🧾 Lógica de cálculo:
Entrada estándar:
PrecioPagar = precioEntrada + ImpuestoVenta

Cliente frecuente:
PrecioPagar = precioEntrada + ImpuestoVenta − (descuento * precioEntrada)

Entrada VIP:
PrecioPagar = precioEntrada + ImpuestoVenta + TotalAlimentos
Donde TotalAlimentos es la suma de los precios de cada alimento incluido.

🧩 Conceptos de POO utilizados:
Encapsulamiento (getters y setters)

Herencia entre clases

Métodos personalizados (calcular_precio())

Uso de listas y composición de objetos (alimentos en Entrada VIP)

📁 Estructura sugerida:
entrada.py: Clase base Entrada

cliente_frecuente.py: Subclase EntradaClienteFrecuente

entrada_vip.py: Subclase EntradaVIP y clase Alimento

main.py: Ejecución y prueba de los diferentes tipos de entradas

🎯 Objetivo
Demostrar cómo aplicar los principios de la programación orientada a objetos para resolver un problema del mundo real, de forma estructurada y escalable.

