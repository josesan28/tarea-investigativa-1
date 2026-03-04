# Capa de Acceso a Datos — Patrón Adapter
# Permite integrar el proveedor externo de pagos sin modificar el sistema interno

from abc import ABC, abstractmethod


class ProveedorPagoExterno:
    # Adaptee: clase externa con interfaz incompatible

    def procesar_transaccion(self, datos: dict):
        print(f"  [Proveedor Externo] Transacción procesada: "
              f"Q{datos['monto']:.2f} para cliente '{datos['cliente']}'.")
        return True


class IPasarelaPago(ABC):
    # Target: interfaz interna que el sistema conoce y utiliza

    @abstractmethod
    def realizar_pago(self, monto: float, cliente: str) -> bool:
        pass


class PagoAdaptador(IPasarelaPago):
    # Adapter: traduce las llamadas internas al formato del proveedor externo

    _proveedor = ProveedorPagoExterno()

    def realizar_pago(self, monto: float, cliente: str) -> bool:
        datos = {"monto": monto, "cliente": cliente}
        return self._proveedor.procesar_transaccion(datos)
