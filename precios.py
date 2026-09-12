def calcular_total(precio, cantidad):
    return precio * cantidad

def aplicar_descuento(total, porcentaje):
    return total - (total * porcentaje / 100)

def mostrar_total(precio, cantidad, descuento=0):
    total = calcular_total(precio, cantidad)
    if descuento > 0:
        total = aplicar_descuento(total, descuento)
    print(f"Total compra: ${total}")

mostrar_total(5000, 3, 10)