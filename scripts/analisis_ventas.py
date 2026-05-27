import csv

# Abrir archivo CSV
archivo = open("../datos/ventas.csv")

# Leer contenido del CSV
lector = csv.DictReader(archivo)

# Variable para guardar total de ventas
total = 0

# Diccionario para ventas por producto
ventas_productos = {}

print("TABLA DE VENTAS")

# Recorrer filas del archivo
for fila in lector:

    print(fila)

    producto = fila["Producto"]
    venta = int(fila["Ventas"])

    # Sumar ventas totales
    total = total + venta

    # Guardar ventas por producto
    if producto in ventas_productos:
        ventas_productos[producto] += venta
    else:
        ventas_productos[producto] = venta

# Mostrar total
print("\nTOTAL DE VENTAS:")
print(total)

# Mostrar ventas por producto
print("\nVENTAS POR PRODUCTO:")
print(ventas_productos)

# Buscar producto más vendido
mayor = 0
producto_top = ""

for producto in ventas_productos:

    if ventas_productos[producto] > mayor:
        mayor = ventas_productos[producto]
        producto_top = producto

# Mostrar producto más vendido
print("\nPRODUCTO MÁS VENDIDO:")
print(producto_top)

# Cerrar archivo
archivo.close()