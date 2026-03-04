# Capa de Negocio — Patrón Strategy
# Encapsula cada regla de descuento en su propia clase intercambiable

from abc import ABC, abstractmethod


class IDescuentoStrategy(ABC):
    # Interfaz Strategy: contrato común para todas las estrategias de descuento

    @abstractmethod
    def calcular_descuento(self, subtotal: float) -> float:
        pass

    @abstractmethod
    def descripcion(self) -> str:
        pass


class SinDescuento(IDescuentoStrategy):

    def calcular_descuento(self, subtotal: float) -> float:
        return 0.0

    def descripcion(self) -> str:
        return "Sin descuento"


class DescuentoVolumen(IDescuentoStrategy):
    # 10% de descuento en compras mayores a Q500

    def calcular_descuento(self, subtotal: float) -> float:
        if subtotal > 500:
            return subtotal * 0.10
        return 0.0

    def descripcion(self) -> str:
        return "Descuento por volumen (10% en compras > Q500)"


class DescuentoClienteVIP(IDescuentoStrategy):
    # 15% de descuento para clientes VIP

    def calcular_descuento(self, subtotal: float) -> float:
        return subtotal * 0.15

    def descripcion(self) -> str:
        return "Descuento cliente VIP (15%)"
