# Capa de Negocio — Modelo Pedido y Servicio
# PedidoService se encarga de la creación, cálculo y persistencia del pedido
# Depende únicamente de abstracciones (interfaces), nunca de implementaciones concretas

from datos.pedido_dao import IPedidoDAO
from datos.pago_adaptador import IPasarelaPago
from negocio.descuento_strategy import IDescuentoStrategy

_contador_pedidos = 0


class Pedido:

    id: int
    cliente: str
    items: list
    descuento_aplicado: float
    total: float

    def subtotal(self) -> float:
        return sum(item.precio for item in self.items)


class PedidoService:
    # Capa de negocio: depende de abstracciones inyectadas, no de clases concretas

    _dao: IPedidoDAO
    _pasarela: IPasarelaPago

    def registrar_dao(self, dao: IPedidoDAO):
        self._dao = dao

    def registrar_pasarela(self, pasarela: IPasarelaPago):
        self._pasarela = pasarela

    def crear_pedido(self, cliente: str, items: list, estrategia: IDescuentoStrategy) -> Pedido:
        global _contador_pedidos
        _contador_pedidos += 1

        pedido = Pedido()
        pedido.id = _contador_pedidos
        pedido.cliente = cliente
        pedido.items = items

        subtotal = pedido.subtotal()
        pedido.descuento_aplicado = estrategia.calcular_descuento(subtotal)
        pedido.total = subtotal - pedido.descuento_aplicado

        print(f"\n  [Negocio] Estrategia: {estrategia.descripcion()}")
        print(f"  [Negocio] Subtotal: Q{subtotal:.2f} | "
              f"Descuento: Q{pedido.descuento_aplicado:.2f} | "
              f"Total: Q{pedido.total:.2f}")

        exito = self._pasarela.realizar_pago(pedido.total, cliente)
        if exito:
            self._dao.save(pedido)

        return pedido

    def obtener_pedido(self, pedido_id: int) -> Pedido:
        return self._dao.find_by_id(pedido_id)

    def listar_pedidos(self) -> list:
        return self._dao.find_all()
