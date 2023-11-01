# Cálcular el precio total de una Compra

# Estamos trabajando en una pequeña empresa que vende productos y necesitamos crear un programa 
# que calcule el precio total de la compra incluyendo el impuesto (19%) de las ventas.
# El prorama  deberá solicitar al usuario el nombre del producto, la catidad comprada y el precio
# unitario del producto.
# Luego calculará el precio total y mostrará un resumen de la compra.

def precio_total(cantidad, precio_uni):
    pt = cantidad * precio_uni
    return pt

def main():
    print('Bienvenido a tu tienda')
    nmbr_producto = str(input('Ingrese el nombre del producto: '))
    cantidad = int(input('Ingrese la cantidad comprada del producto: '))
    precio_uni = float(input('Ingrese el precio unitario del producto en USD: '))

    if cantidad <= 0 or precio_uni <= 0:
        print('El importe introducido no es correcto')
    else:
        pt = precio_total(cantidad, precio_uni)
        impuesto = pt * 0.19
        pt_imp = pt + impuesto

        # Mostrar el resumen de la compra
        print('El resumen de la compra: ')
        print('Producto: ', nmbr_producto)
        print('Cantidad: ', cantidad)
        print(f'Precio unitario: {precio_uni:.2f} USD')
        print(f'IVA 19%: {impuesto:.2f} USD')
        print(f'Precio final: {pt_imp:.2f} USD')

main()