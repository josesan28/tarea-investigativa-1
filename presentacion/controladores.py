# Capa de Presentación — Controladores
# Reciben input del usuario, coordinan con la capa de negocio y delegan la visualización

from negocio.pedido_service import PedidoService
from negocio.item_factory import RepuestoFactory, ServicioFactory
from negocio.descuento_strategy import SinDescuento, DescuentoVolumen, DescuentoClienteVIP
from presentacion.vistas import mostrar_encabezado, mostrar_pedido


def _leer_estrategia():
    print("\n  Estrategias de descuento disponibles:")
    print("  1. Sin descuento")
    print("  2. Descuento por volumen (10% en compras > Q500)")
    print("  3. Descuento cliente VIP (15%)")
    opcion = input("  Selecciona estrategia [1-3]: ").strip()

    if opcion == "2":
        return DescuentoVolumen()
    if opcion == "3":
        return DescuentoClienteVIP()
    return SinDescuento()


def _leer_items():
    fabricas = {
        "1": (RepuestoFactory(), "Repuesto"),
        "2": (ServicioFactory(), "Servicio"),
    }
    items = []
    seguir = True

    while seguir:
        print("\n  ¿Qué tipo de ítem desea agregar?")
        print("  1. Repuesto")
        print("  2. Servicio")
        print("  0. Terminar de agregar ítems")
        tipo = input("  Opción: ").strip()

        if tipo == "0":
            if not items:
                print("  Debe agregar al menos un ítem.")
            else:
                seguir = False

        elif tipo in fabricas:
            fabrica, etiqueta = fabricas[tipo]
            nombre = input(f"  Nombre del {etiqueta}: ").strip()
            try:
                precio = float(input("  Precio (Q): ").strip())
                item = fabrica.crear_item(nombre, precio)
                items.append(item)
                print(f"  [Factory Method] Ítem creado → {item}")
            except ValueError:
                print("  Precio inválido.")
        else:
            print("  Opción inválida.")

    return items


def registrar_pedido(servicio: PedidoService):
    mostrar_encabezado("NUEVO PEDIDO")
    cliente = input("  Nombre del cliente: ").strip()

    if not cliente:
        print("  Nombre inválido.")
        return

    items = _leer_items()
    estrategia = _leer_estrategia()

    print("\n  Procesando pedido...")
    pedido = servicio.crear_pedido(cliente, items, estrategia)
    print("\n  Pedido registrado exitosamente.")
    mostrar_pedido(pedido)


def consultar_pedido(servicio: PedidoService):
    mostrar_encabezado("CONSULTAR PEDIDO")
    try:
        pedido_id = int(input("  ID del pedido: ").strip())
    except ValueError:
        print("  ID inválido.")
        return

    pedido = servicio.obtener_pedido(pedido_id)
    if pedido:
        mostrar_pedido(pedido)
    else:
        print(f"  No se encontró el pedido #{pedido_id}.")


def listar_pedidos(servicio: PedidoService):
    mostrar_encabezado("TODOS LOS PEDIDOS")
    pedidos = servicio.listar_pedidos()

    if not pedidos:
        print("  No hay pedidos registrados.")
        return

    for pedido in pedidos:
        mostrar_pedido(pedido)
