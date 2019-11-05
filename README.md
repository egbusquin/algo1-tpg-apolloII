# algo1-tpg-apolloll

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
