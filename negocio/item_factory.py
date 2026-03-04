# Capa de Negocio — Patrón Factory Method
# Delega la creación de ítems a fábricas especializadas,
# desacoplando el código cliente de las clases concretas

from abc import ABC, abstractmethod


class Item(ABC):
    # Product: abstracción común para todos los ítems de un pedido

    nombre: str
    precio: float

    @abstractmethod
    def tipo(self) -> str:
        pass

    def __str__(self):
        return f"{self.tipo()}: {self.nombre} — Q{self.precio:.2f}"


class Repuesto(Item):

    def tipo(self) -> str:
        return "Repuesto"


class Servicio(Item):

    def tipo(self) -> str:
        return "Servicio"


class ItemFactory(ABC):
    # Creator: declara el factory method

    @abstractmethod
    def crear_item(self, nombre: str, precio: float) -> Item:
        pass


class RepuestoFactory(ItemFactory):

    def crear_item(self, nombre: str, precio: float) -> Item:
        item = Repuesto()
        item.nombre = nombre
        item.precio = precio
        return item


class ServicioFactory(ItemFactory):

    def crear_item(self, nombre: str, precio: float) -> Item:
        item = Servicio()
        item.nombre = nombre
        item.precio = precio
        return item
