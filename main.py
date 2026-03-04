# Punto de entrada — Composición de dependencias y ciclo del menú
# Las capas superiores dependen de abstracciones inyectadas aquí

import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

from datos.pedido_dao import PedidoDAOMemoria
from datos.pago_adaptador import PagoAdaptador
from negocio.pedido_service import PedidoService
from presentacion.vistas import mostrar_menu_principal
from presentacion.controladores import registrar_pedido, consultar_pedido, listar_pedidos


def iniciar_servicio() -> PedidoService:
    servicio = PedidoService()
    servicio.registrar_dao(PedidoDAOMemoria())
    servicio.registrar_pasarela(PagoAdaptador())
    return servicio


def ejecutar_opcion(opcion: str, servicio: PedidoService) -> bool:
    match opcion:
        case "1":
            registrar_pedido(servicio)
        case "2":
            consultar_pedido(servicio)
        case "3":
            listar_pedidos(servicio)
        case "4":
            print("\n  Hasta luego.\n")
            return False
        case _:
            print("  Opción inválida.")
    return True


def main():
    servicio = iniciar_servicio()

    print("\n" + "═"*50)
    print("  SISTEMA DE GESTIÓN DE PEDIDOS")
    print("  Taller Automotriz — Grupo 1 UVG 2026")
    print("═"*50)

    activo = True
    while activo:
        mostrar_menu_principal()
        opcion = input("\n  Selecciona una opción: ").strip()
        activo = ejecutar_opcion(opcion, servicio)


main()
