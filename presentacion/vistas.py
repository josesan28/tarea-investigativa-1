# Capa de Presentación — Vistas del menú interactivo
# Solo se encarga de mostrar información y recibir datos del usuario

from negocio.pedido_service import Pedido


def mostrar_pedido(pedido: Pedido):
    print(f"\n  {'─'*45}")
    print(f"  Pedido #{pedido.id} — Cliente: {pedido.cliente}")
    print(f"  {'─'*45}")
    for item in pedido.items:
        print(f"    • {item}")
    print(f"  {'─'*45}")
    print(f"  Subtotal:  Q{pedido.subtotal():.2f}")
    print(f"  Descuento: Q{pedido.descuento_aplicado:.2f}")
    print(f"  Total:     Q{pedido.total:.2f}")
    print(f"  {'─'*45}")


def mostrar_encabezado(titulo: str):
    print("\n" + "═"*50)
    print(f"  {titulo}")
    print("═"*50)


def mostrar_menu_principal():
    print("\n  MENÚ PRINCIPAL")
    print("  ──────────────")
    print("  1. Registrar nuevo pedido")
    print("  2. Consultar pedido por ID")
    print("  3. Ver todos los pedidos")
    print("  4. Salir")
