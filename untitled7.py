# -*- coding: utf-8 -*-
"""Untitled7.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ubH6ALPz74i3Vl2-bvt-cEitEbqvodzB
"""

#productos.csv:id_producto;nombre;precio;cantidad_bodega
#clientes.csv:rut;nombre
#ventas.csv:num_boleta;fecha;venta;rut_cliente
#items.csv:num_boleta;id_producto;cantidad

#Ejercicio 1
def producto_mas_caro(archivo):
    # Inicializamos la variable para el mayor precio
    mayor_precio = 0
    # Inicializamos la variable vacia para el nombre del producto más caro
    producto_mayor_precio = ""

    # recorremos x el archivo
    for x in archivo:
        # Empaquetamos en id, nombre, precio y cantidad, eliminando espacios innecesarios y .split para dividir los textos por ,
        id_producto, nombre, precio, cantidad_bodega = x.strip().split(",")
        # Convertimos el precio a entero
        precio = int(precio)

        # Comparamos el precio actual con el mayor precio encontrado hasta ahora
        if precio > mayor_precio:
            # Actualizamos el mayor precio y el nombre del producto correspondiente
            mayor_precio = precio
            producto_mayor_precio = nombre

    # Devolvemos el nombre del producto más caro encontrado
    return producto_mayor_precio

#Lo usamos para abrir y cerrar los archivos para despues llamar a la funcion
with open("productos.csv") as archivo:
    # Imprimimos el resultado de la función
    print(producto_mas_caro(archivo))

#Ejercicio 2
#definimos la funcion valor_total_bodega
def valor_total_bodega(archivo):
    # Inicializamos la variable para el precio total
    precio_total = 0

    # recorremos x en el archivo
    for x in archivo:
        # Empaquetamos la línea en id, nombre, precio y cantidad, eliminando espacios innecesarios
        id_producto, nombre, precio, cantidad_bodega = x.strip().split(",")
        # Creamos una lista con el precio y la cantidad en bodega convertidos a enteros
        lista = [int(precio), int(cantidad_bodega)]
        # Calculamos el valor total acumulado
        precio_total += lista[0] * lista[1]

    # Devolvemos el valor total de lo que se encuentra en bodega
    return precio_total

#Lo usamos para abrir y cerrar los archivos
with open("productos.csv") as archivo:
    # Imprimimos el resultado de la función
    print(valor_total_bodega(archivo))

#Ejercicio 3
#creamos la funcion pruducto_con_mas_ingresos
def producto_con_mas_ingresos(items, productos):
    # Creamos un diccionario para almacenar los ingresos por producto
    ingresos = {}

    #Leemos los productos y los almacenamos en un diccionario para acceder a su nombre y precio
    productos_dict = {}
    for x in productos:
        # denmpaquetamos en id, nombre, precio y cantidad, eliminando espacios innecesarios
        id_producto, nombre, precio, cantidad_bodega = x.strip().split(",")
        #asigna (nombre, int(precio)) a id_producto que se encuentra dentro del diccionario
        productos_dict[id_producto] = (nombre, int(precio))

    # reccorremos x sobre cada línea del archivo de items
    for x in items:
    #empaquetamos items en 3 variables
        num_boleta, id_producto, cantidad = x.strip().split(";")
        #transformamos catidad en entero
        cantidad = int(cantidad)

        # si id_pruducto se encuentra en el diccionario pruducto_dic
        if id_producto in productos_dict:
          #empaquetamos nombre_producto, precio_producto en id_producto que se encuentra dentro del diccionario
            nombre_producto, precio_producto = productos_dict[id_producto]
            #variable ingreso que es igual a la cantidad multiplicado por precio_producto
            ingreso = cantidad * precio_producto

            # Acumulamos los ingresos en el diccionario
            if nombre_producto in ingresos:
                ingresos[nombre_producto] += ingreso
            else:
                ingresos[nombre_producto] = ingreso

    # Encontramos el producto con más ingresos
    producto_mas_ingresos = max(ingresos, key=ingresos.get)

    return producto_mas_ingresos

# Uso del código
with open("productos.csv", "r") as productos, open("items.csv", "r") as items:
    print(producto_con_mas_ingresos(items, productos))

#creamos una funcion que reciba año, mes, items, productos y ventas
def total_ventas_del_mes(año, mes, items, productos, ventas):
    #creamos un diccionario vacio
    precios_productos = {}
    #creamos un for que recorra productos
    for linea in productos:
        #creamos una variable que elimine los espacios en blanco y lo separamos por comas
        partes = linea.strip().split(",")
        #si la longitud de partes es igual a 4 entonces...
        if len(partes) == 4:
            #crea varias variables que son igual a "partes"
            id_producto, nombre, precio, cantidad_bodega = partes
            #dentro del diccionario crea una lista que tendra la variable "id_producto" que todo esto sera igual al flotante de la variable precio
            precios_productos[id_producto] = float(precio)

    # 2. Filtrar las ventas del mes y año proporcionados
    boletas_validas = set()
    #creamos un for que recorra ventas
    for linea in ventas:
      #creamos una variable que elimine los espacios en blanco y lo separamos por puntoycoma
        partes = linea.strip().split(";")
        #si la longitud de partes es igual a 3 entonces...
        if len(partes) == 3:
            #crea varias variables que son igual a "partes"
            num_boleta, fecha, rut_cliente = partes
            #crea varias variables que seran igual a separar fecha en "-"
            dia_venta, mes_venta, año_venta = fecha.split("-")
            #si el "año_venta" convertido a entero es igual a "año" y el "mes_venta" convertido a entero es igual a "mes" entonces...
            if int(año_venta) == año and int(mes_venta) == mes:
                #añade a "boletas_validas" la variable "num_boleta"
                boletas_validas.add(num_boleta)


    # 3. Calcular el total de ventas para las boletas válidas
    #creamos una variable que se llamara "total_ventas" e iniciara en 0
    total_ventas = 0
    #creamos un for que recorra items
    for linea in items:
        #creamos una variable que elimine los espacios en blanco y lo separamos por puntoycoma
        partes = linea.strip().split(";")
        #si la longitud de partes es igual a 3 entonces...
        if len(partes) == 3:
            #crea varias variables que seran igual a partes
            num_boleta, id_producto, cantidad = partes

            #si el num_boleta se encunetra en boletas_validas entonces...
            if num_boleta in boletas_validas:
                #se le asigna un nuevo valor a la variable cantidad que va a ser "cantidad" pero su entero
                cantidad = int(cantidad)
                #creamos una variable que va a almacenar el diccionario "precios_productos" que va a obtener un valor de "id_productos" y en caso de no estar esta llave se le asignara el valor 0
                precio_producto = precios_productos.get(id_producto, 0)

                # Sumar al total el precio del producto por la cantidad vendida
                total_ventas += cantidad * precio_producto

    # 4. Devolver el total de ventas
    #retorna la variable total_ventas
    return total_ventas

#abrimos los archivos que necesitamos y le asignamos sus respectivas variables
with open("productos.csv") as productos, open("items.csv") as items, open("ventas.csv") as ventas:
    #creamos una variable que sera igual a llamar a la funcion "total_ventas_del_mes" y le damos los datos que necesitamos
    total = total_ventas_del_mes(2010, 10, items, productos, ventas)
    #por ultimo imprimimos el total de ventas del mes
    print(f"Total de ventas del mes: {total}")

#Ejercicio 1
def producto_mas_caro(archivo):
    # Inicializamos la variable para el mayor precio
    mayor_precio = 0
    # Inicializamos la variable para el nombre del producto más caro
    producto_mayor_precio = ""

    # Iteramos sobre cada línea del archivo
    for x in archivo:
        # Empaquetamos en id, nombre, precio y cantidad, eliminando espacios innecesarios
        id_producto, nombre, precio, cantidad_bodega = x.strip().split(",")
        # Convertimos el precio a entero
        precio = int(precio)

        # Comparamos el precio actual con el mayor precio encontrado hasta ahora
        if precio > mayor_precio:
            # Actualizamos el mayor precio y el nombre del producto correspondiente
            mayor_precio = precio
            producto_mayor_precio = nombre

    # Devolvemos el nombre del producto más caro encontrado
    return producto_mayor_precio


#Ejercicio 2
def valor_total_bodega(archivo):
    # Inicializamos la variable para el precio total
    precio_total = 0

    # Iteramos sobre cada línea del archivo
    for x in archivo:
        # Empaquetamos la línea en id, nombre, precio y cantidad, eliminando espacios innecesarios
        id_producto, nombre, precio, cantidad_bodega = x.strip().split(",")
        # Creamos una lista con el precio y la cantidad en bodega convertidos a enteros
        lista = [int(precio), int(cantidad_bodega)]
        # Calculamos el valor total acumulado
        precio_total += lista[0] * lista[1]

    # Devolvemos el valor total de lo que se encuentra en bodega
    return precio_total


#Ejercicio 3

def producto_con_mas_ingresos(items, productos):
    # Creamos un diccionario para almacenar los ingresos por producto
    ingresos = {}

    # Leemos los productos y los almacenamos en un diccionario para acceder a su nombre y precio
    productos_dict = {}
    for x in productos:
        id_producto, nombre, precio, cantidad_bodega = x.strip().split(",")
        productos_dict[id_producto] = (nombre, int(precio))  # Guardamos nombre y precio como tupla

    # Iteramos sobre cada línea del archivo de items
    for x in items:
        num_boleta, id_producto, cantidad = x.strip().split(";")
        cantidad = int(cantidad)

        # Calculamos el ingreso para el producto actual
        if id_producto in productos_dict:
            nombre_producto, precio_producto = productos_dict[id_producto]  # Desempaquetamos la tupla
            ingreso = cantidad * precio_producto

            # Acumulamos los ingresos en el diccionario
            if nombre_producto in ingresos:
                ingresos[nombre_producto] += ingreso
            else:
                ingresos[nombre_producto] = ingreso

    # Encontramos el producto con más ingresos
    producto_mas_ingresos = max(ingresos, key=ingresos.get)

    return producto_mas_ingresos




# Función 4: Total de ventas en el mes 10/2010
#creamos una funcion que reciba año, mes, items, productos y ventas
def total_ventas_del_mes(año, mes, items, productos, ventas):
    #creamos un diccionario vacio
    precios_productos = {}
    #creamos un for que recorra productos
    for linea in productos:
        #creamos una variable que elimine los espacios en blanco y lo separamos por comas
        partes = linea.strip().split(",")
        #si la longitud de partes es igual a 4 entonces...
        if len(partes) == 4:
            #crea varias variables que son igual a "partes"
            id_producto, nombre, precio, cantidad_bodega = partes
            #dentro del diccionario crea una lista que tendra la variable "id_producto" que todo esto sera igual al flotante de la variable precio
            precios_productos[id_producto] = float(precio)

    # 2. Filtrar las ventas del mes y año proporcionados
    boletas_validas = set()
    #creamos un for que recorra ventas
    for linea in ventas:
      #creamos una variable que elimine los espacios en blanco y lo separamos por puntoycoma
        partes = linea.strip().split(";")
        #si la longitud de partes es igual a 3 entonces...
        if len(partes) == 3:
            #crea varias variables que son igual a "partes"
            num_boleta, fecha, rut_cliente = partes
            #crea varias variables que seran igual a separar fecha en "-"
            dia_venta, mes_venta, año_venta = fecha.split("-")
            #si el "año_venta" convertido a entero es igual a "año" y el "mes_venta" convertido a entero es igual a "mes" entonces...
            if int(año_venta) == año and int(mes_venta) == mes:
                #añade a "boletas_validas" la variable "num_boleta"
                boletas_validas.add(num_boleta)


    # 3. Calcular el total de ventas para las boletas válidas
    #creamos una variable que se llamara "total_ventas" e iniciara en 0
    total_ventas = 0
    #creamos un for que recorra items
    for linea in items:
        #creamos una variable que elimine los espacios en blanco y lo separamos por puntoycoma
        partes = linea.strip().split(";")
        #si la longitud de partes es igual a 3 entonces...
        if len(partes) == 3:
            #crea varias variables que seran igual a partes
            num_boleta, id_producto, cantidad = partes

            #si el num_boleta se encunetra en boletas_validas entonces...
            if num_boleta in boletas_validas:
                #se le asigna un nuevo valor a la variable cantidad que va a ser "cantidad" pero su entero
                cantidad = int(cantidad)
                #creamos una variable que va a almacenar el diccionario "precios_productos" que va a obtener un valor de "id_productos" y en caso de no estar esta llave se le asignara el valor 0
                precio_producto = precios_productos.get(id_producto, 0)

                # Sumar al total el precio del producto por la cantidad vendida
                total_ventas += cantidad * precio_producto

    # 4. Devolver el total de ventas
    #retorna la variable total_ventas
    return total_ventas


# Carga de archivos
productos_file = "productos.csv"
items_file = "items.csv"
ventas_file = "ventas.csv"

# Ejecutamos las funciones con los archivos
with open(productos_file, "r") as productos:
    producto_caro = producto_mas_caro(productos)

with open(productos_file, "r") as productos:
    valor_bodega = valor_total_bodega(productos)

with open(productos_file, "r") as productos, open(items_file, "r") as items:
    producto_mas_ingresos = producto_con_mas_ingresos(items, productos)

with open(productos_file, "r") as productos, open(items_file, "r") as items, open(ventas_file, "r") as ventas:
    total_ventas_octubre = total_ventas_del_mes(2010, 10, items, productos, ventas)

# Creamos el informe
informe = f"""El producto más caro es {producto_caro}
El valor total de la bodega es de ${valor_bodega}
El producto con más ingresos es {producto_mas_ingresos}
En el período de 10/2010, el total de ventas es de ${total_ventas_octubre}
"""

# Guardamos el informe en un archivo
with open("informe.txt", "w") as informe_file:
    informe_file.write(informe)

print("El informe ha sido generado correctamente.")