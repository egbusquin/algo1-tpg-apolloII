# algo1-tpg-apolloII

## Primera entrega

Primero quiero remarcar que en ningún momento el grupo se acercó a hablar conmigo excepto la primera clase. 
Esto derivó en que no se haga ningún tipo de validación ni consulta durante el desarrollo.

No cumple con la estructura solicitada (lista de diccionarios). No hay validaciones de formato ni de tipos para varios datos, 
con lo que ingresar "j" cuando espera un int o float cuelga el programa. Mala modularización.

La experiencia del menú es bastante mala. La funcionalidad es desprolija, muestra un único menú "Regresar". No funciona bien.

Corridas:

** Pedido manual no funciona **

```Numero del articulo: 1
Ingrese cuantas unidadesdesea agregar: 2
“Para seguir agregando pedidos ingrese: “S”S
Los platos disponibles son:
1  -  ('Cheese Burger', 180)
2  -  ('Coca Cola', 80)
3  -  ('Tacos', 200)
Numero del articulo: 2
Ingrese cuantas unidadesdesea agregar: 1
“Para seguir agregando pedidos ingrese: “S”n
Este codigo de restaurante no se encuentra registrado
Traceback (most recent call last):
  File "tp rappi.py", line 375, in <module>
    menus(restaurantes,clientes,rappitenderos)
  File "tp rappi.py", line 333, in menus
    menu3()
  File "tp rappi.py", line 273, in menu3
    pedidoManual(clientes, restaurantes, rappitenderos, pedidos)
  File "tp rappi.py", line 186, in pedidoManual
    armarPedido(restElegido, restaurantes, pedido, pedidos, user, rappitenderos)
  File "tp rappi.py", line 176, in armarPedido
    restaurantes[restElegido] = [aux[0], aux[1], aux[2], aux[3], int(aux[4]) + 1, int(aux[5]) + preciototal]
IndexError: list index out of range
```

** Pedidos automáticos no funciona **


```
Seleccione una opción:
	1. Carga de información predefinida.
	2. Carga de información manual.
	3. Pedido manual.
	4. Simulación de pedidos.
	5. Informes.
	6. Salir del programa.
Seleccione una opción: 1
	a. Regresar.
Seleccione una opción: a
Seleccione una opción:
	1. Carga de información predefinida.
	2. Carga de información manual.
	3. Pedido manual.
	4. Simulación de pedidos.
	5. Informes.
	6. Salir del programa.
Seleccione una opción: 4
Porfavor ingrese la cantidad de simulaciones que desea realizar: 5
Traceback (most recent call last):
  File "tp rappi.py", line 375, in <module>
    menus(restaurantes,clientes,rappitenderos)
  File "tp rappi.py", line 342, in menus
    menu4()
  File "tp rappi.py", line 277, in menu4
    simulacion(clientes, restaurantes, rappitenderos)
  File "tp rappi.py", line 194, in simulacion
    user=list(clientes.keys())[random.randint(0,len(list(clientes.keys()-1)))]
TypeError: 'int' object is not iterable
```

No se puede probar la funcionalidad del TPG. Se requiere una reentrega donde:
1) Se pueda cargar un pedido manual
2) Se puedan cargar pedidos automáticos, incluyendo cálculo de distancia y tiempo
3) Se puedan visualizar los informes adecuadamente

## Reentrega

Problemas de usabilidad:

```ingrese el numero de teléfono: 541167999278
ingrese su contraseña: 1234
ingrese su contraseña:
ingrese su contraseña: 1234
ingrese su contraseña:
ingrese su contraseña: 1234
ingrese su contraseña: 1234
ingrese su contraseña: Abc123!
ingrese su contraseña:
ingrese su contraseña: Abc123!
ingrese su contraseña: fkdlsafkdlsakfdslafkdsa
Vuelva a ingresar su contraseña: 
```

```Bienvenido,  Eze
Los restaurantes disponibles son:
el vivero {'nombre': 'el vivero', 'direccion': 'Primera Junta 1094', 'tel': '1156223610', 'lat y lon': (-34.4615385, -58.50753079), 'radio': 20, 'platos': {'chese burguer': 180, 'coca cola': 80, 'tacos': 200}, 'ventas': 0}
MC DONNALDS {'nombre': 'MC DONNALDS', 'direccion': 'Avenida Centenario 200', 'tel': '1156223620', 'lat y lon': (-70.4615385, -40.5075307), 'radio': 20, 'platos': {'Cuarto de libra': 220, 'Big Mac': 200, 'mcFlurry': 100}, 'ventas': 0}
BURGER KING {'nombre': 'BURGER KING', 'direccion': 'Belgrano 500', 'tel': '1156223630', 'lat y lon': (-80.4615385, -48.5075307), 'radio': 20, 'platos': {'Whooper': 180, 'Stacker': 300, 'Cono Helado': 50}, 'ventas': 0}
GRIDO {'nombre': 'GRIDO', 'direccion': 'Avenida Centenario 1100', 'tel': '1156228610', 'lat y lon': (-10.4615385, -60.5075307), 'radio': 20, 'platos': {'1kilo': 250, '1/2 kilo': 200, '2 kilos': 400}, 'ventas': 0}
KENTUCKY {'nombre': 'KENTUCKY', 'direccion': 'Avenida Rolon 1094', 'tel': '1156238950', 'lat y lon': (-100.4615385, -20.5075307), 'radio': 20, 'platos': {'Pizza de Muzzarella': 220, 'Empanadas de carne': 40, 'Empanadas de Jamon y queso': 40}, 'ventas': 0}
Ingrese el numero del restaurante:
```

Todos los informes muestran el diccionario "en crudo" sin formato. Es muy difícil de entender y muy sucio. Debería mostrar solo los datos relevantes.

A diferencia de la entrega anterior, esta vez tanto la carga manual, simulaciones e informes funcionan correctamente.

Revisar los comentarios del código para tenerlos encuenta para la entrega del TPG parte 2.
