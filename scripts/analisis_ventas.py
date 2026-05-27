import csv

# Abrir archivo CSV
archivo = open(r"C:\Users\Usuario\OneDrive\TECNICATURA EN PROGRAMACION\1er Cuatrimestre\Organización Empresarial\Unidad 4\tp-organizacion-empresarial\datos\ventas.csv", encoding="utf-8-sig")

# Leer contenido del CSV
lector = csv.DictReader(archivo, delimiter=";")

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


# Crear archivo de resultados
resultado = open("c:/Users/Usuario/OneDrive/TECNICATURA EN PROGRAMACION/1er Cuatrimestre/Organización Empresarial/Unidad 4/tp-organizacion-empresarial/resultados/resumen.txt", "w")

resultado.write("TOTAL DE VENTAS:\n")
resultado.write(str(total))

resultado.write("\n\nPRODUCTO MAS VENDIDO:\n")
resultado.write(producto_top)

resultado.close()

print("\nResumen generado correctamente.")