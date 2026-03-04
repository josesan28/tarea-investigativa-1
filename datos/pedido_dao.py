# Capa de Acceso a Datos — Patrón DAO
# Separa la lógica de negocio del mecanismo de persistencia

from abc import ABC, abstractmethod

# Simula la base de datos relacional en memoria
_base_de_datos = {}


class IPedidoDAO(ABC):
    
    # Interfaz DAO: define las operaciones disponibles sobre la entidad Pedido

    @abstractmethod
    def save(self, pedido):
        pass

    @abstractmethod
    def find_by_id(self, pedido_id):
        pass

    @abstractmethod
    def find_all(self):
        pass


class PedidoDAOMemoria(IPedidoDAO):
    # Implementación concreta: persiste pedidos en memoria

    def save(self, pedido):
        _base_de_datos[pedido.id] = pedido
        print(f"  [DAO] Pedido #{pedido.id} guardado en base de datos.")

    def find_by_id(self, pedido_id):
        return _base_de_datos.get(pedido_id)

    def find_all(self):
        return list(_base_de_datos.values())
