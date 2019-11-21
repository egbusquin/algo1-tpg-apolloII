import random
import math
import operator


#Entidades a cargar
restaurantes=[]
clientes=[]
rappitenderos=[]
pedidos=[]

def confirm_float(valor):
    try:
        float(valor)
        return True
    except ValueError:
        return False





#Funcion que recibe las entidades con la información predefinida por entidad(Restaurantes,clientes y rappitenderos)"""
def hard(restaurantes,clientes,rappitenderos): #Punto 1
    restaurantes.append({"nombre":"el vivero", "direccion":"Primera Junta 1094", "tel":"1156223610", "lat y lon":(-34.4615385,-58.50753079), "radio":20, "platos":{"chese burguer":180, "coca cola":80, "tacos":200}, "ventas":0})
    restaurantes.append({"nombre":"MC DONNALDS", "direccion":"Avenida Centenario 200", "tel":"1156223620", "lat y lon":(-70.4615385,-40.5075307), "radio":20, "platos":{"Cuarto de libra":220,"Big Mac":200,"mcFlurry":100}, "ventas":0})
    restaurantes.append({"nombre":"BURGER KING", "direccion":"Belgrano 500", "tel":"1156223630", "lat y lon":(-80.4615385,-48.5075307), "radio":20, "platos":{"Whooper":180,"Stacker":300,"Cono Helado":50}, "ventas":0})
    restaurantes.append({"nombre":"GRIDO", "direccion":"Avenida Centenario 1100", "tel":"1156228610", "lat y lon":(-10.4615385, -60.5075307), "radio":20, "platos":{"1kilo":250,"1/2 kilo":200,"2 kilos":400}, "ventas":0})
    restaurantes.append({"nombre":"KENTUCKY", "direccion":"Avenida Rolon 1094", "tel":"1156238950", "lat y lon":(-100.4615385, -20.5075307), "radio":20, "platos":{"Pizza de Muzzarella":220,"Empanadas de carne":40,"Empanadas de Jamon y queso":40}, "ventas":0})
    clientes.append({"nombre": "Agustin Silva", "clave":"Agustin123!", "telefono": "1156223610", "direccion": "Diego Palma 21", "lat y lon":( -13.4615385, -32.4615385), "rapicredits": 500})
    clientes.append({"nombre": "juan", "clave":"Juan123!", "telefono": "1156554410", "direccion": "Julian Navarro 200", "lat y lon":( -43.4615385, -62.4615385), "rapicredits": 350})
    clientes.append({"nombre": "valen", "clave":"Valen123!", "telefono": "1169729137", "direccion": "Haedo 1969", "lat y lon":( -23.4615385, -42.4615385), "rapicredits": 2000})
    rappitenderos.append({"nombre":"Carlos", "propina":0.0, "lat y lon":(-10.4551,-60.5215) , "pedido":"None"})
    rappitenderos.append({"nombre":"pepe", "propina":0.0,"lat y lon":(-12.4551,-60.5215) , "pedido":"None"})
    rappitenderos.append({"nombre":"Alberto", "propina":0.0,"lat y lon":(-15.4551,-62.5215) , "pedido":"None"})


"""def imprimirDiccionarios(diccionario):
    for i in range (0,len(list(diccionario.keys()))):
        print(i,"-",list(diccionario.keys())[i])"""





#Segunda funcionalidad: A continuación crearemos funciones para solicitar información por cada entidad
"""Funcion para la creación de un nuevo restaurante"""


def nuevoRestaurante(restaurantes): 
    platito = {}
    lista =[]
    for i in restaurantes:
        lista.append(i["nombre"])
    nombre=input("Ingrese el nombre del restaurante: ")
    while nombre in lista:
        print("El restaurante ya existe, Ingrese uno nuevo:")
        nombre= input("Ingrese el nombre del restaurante: ")
    direc=input("Ingrese la dirección: ")
    tel= input("ingrese el numero de teléfono: ")
    valid = False
    while valid != "true":
        if len(tel) > 7 and len(tel) <14:
            if tel.isdigit():
                valid = "true"
        if valid == False:
            tel = input("ingrese el numero de teléfono: ")
    lat=input("Latitud: ")
    while confirm_float(lat) == False:
        lat=input("Latitud: ")
    lat=float(lat)
    lon=input("Longitud: " )
    while confirm_float(lon) == False:
        lon=input("Longitud: ")
    lon=float(lon)
    radio = input("Ingrese el radio de entrega (unidad en km)")
    while confirm_float(radio) == False:
        radio=input("Ingrese el radio de entrega (unidad en km)")
    radio=float(radio)
    bucle = "1"
    while bucle == "1":
        plato= input("ingrese el nombre del plato, en caso de que este ya se encuentre disponibler en el menu, el mismo se sobreescribira")
        precio= input("ingrese precio")
        while confirm_float(precio) == False:
            precio= input("ingrese precio")
        precio=float(precio)
        platito[plato]=precio
        bucle= input("desea añadir mas platos 1=si, 2=no")
        while bucle != "1" and bucle != "2":
            bucle= input("desea añadir mas platos 1=si, 2=no")
    
    
    restaurantes.append({"nombre":nombre, "direccion":direc, "tel":tel, "lat y lon":(lat,lon), "radio":radio, "platos":platito, "ventas":0})
    print("Se ha creado su restaurante")
    return restaurantes



"""Funcion para la creación de un nuevo plato"""
def nuevoPlato(restaurantes): 
    bucle= True
    """Solicitamos un numero de restaurante hasta que se ingrese uno de los registrados"""
    while bucle==True:
        lista = []
        x = 0
        for i in restaurantes:
            x += 1
            lista.append(i["nombre"])
            print(i["nombre"]+" "+str(x) )
        restaurant=input("Ingrese el numero del restaurante: ")
        while not restaurant.isdigit():
            restaurant=input("Ingrese el numero del restaurante: ")
        restaurant=int(restaurant)
        restaurant -= 1
        while restaurant >= x:
            restaurant=input("El restaurante no se encuentra registrado ")
            while not restaurant.isdigit():
                restaurant=input("Ingrese el numero del restaurante: ")
            restaurant=int(restaurant)
            restaurant -= 1
        bucle = False
    bucle = "1"
    while bucle == "1":
        print(restaurantes[restaurant]["platos"])
        plato= input("ingrese el nombre del plato, en caso de que este ya se encuentre disponibler en el menu, el mismo se sobreescribira ")
        precio= input("ingrese precio")
        while confirm_float(precio) == False:
            precio= input("ingrese precio")
        precio=float(precio)
        restaurantes[restaurant]["platos"][plato]=precio
        bucle= input("desea añadir mas platos 1=si, 2=no ")
        while bucle != "1" and bucle != "2":
            bucle= input("desea añadir mas platos 1=si, 2=no ")
    print(restaurantes[restaurant]["platos"])
    return restaurantes


"""Funcion para la creación de un nuevo cliente"""
def nuevoCliente(clientes):
    lista =[]
    for i in clientes:
        lista.append(i["nombre"])
    nombre=input("Ingrese su nombre: ")
    while nombre in lista:
        nombre = input("el nombre esta tomado, ingrese otro nombre de usuario ")
    direc=input("Ingrese su dirección: ")
    lat=input("Latitud: ")
    while confirm_float(lat) == False:
        lat=input("Latitud: ")
    lat=float(lat)
    lon=input("Longitud: " )
    while confirm_float(lon) == False:
        lon=input("Longitud: ")
    lon=float(lon)
    tel= input("ingrese el numero de teléfono: ")
    valid = False
    while valid != "true":
        if len(tel) > 7 and len(tel) <14:
            if tel.isdigit():
                valid = "true"
        if valid == False:
            tel= input("ingrese el numero de teléfono: ")
    loop=True
    while loop:
        contrasenia=input("ingrese su contraseña: ")
        if len(contrasenia)>7:
            loop=False
    loop2=True
    while loop2:
        checkeo= input("Vuelva a ingresar su contraseña: ")
        if checkeo==contrasenia:
            loop2= False
    clientes.append({"nombre": nombre, "clave":contrasenia, "telefono": tel, "direccion": direc, "lat y lon":( lat, lon), "rapicredits": 0})
    return clientes


"""Funcion para la creación de un nuevo rappitendero"""


def nuevoRappitendero(rappitenderos,restaurantes): 
    lista =[]
    for i in rappitenderos:
        lista.append(i["nombre"])
    x = random.randrange(0, len(restaurantes))
    nombre=input("Ingrese su nombre: ")
    while nombre in lista:
        nombre=input("el nombre ya esta tomado: ")
    pos=restaurantes[x]["lat y lon"]
    rappitenderos.append({"nombre":nombre, "propina":0.0, "lat y lon": pos , "pedido":"None"})
    print(rappitenderos)
    return rappitenderos




#Comenzamos con la tercera funcionalidad: Pedido Manual, en ella definiremos funciones para el login y el pedido manual de articulos

"""Funcion que registra al usuario y checkea la contraseña ingresada"""

def login(clientes):
    lista =[]
    for i in clientes:
        lista.append(i["nombre"])
    bucle = True
    while bucle:
        user = input("Ingrese su usuario: ")
        if user in lista:
            bucle = False
        else:
            print("Usuario inexistente.")
    numero_cliente = 0
    while user != clientes[numero_cliente]["nombre"]:
        numero_cliente += 1
    bucle = True
    while bucle:
        contrasenia = input("Ingrese su contraseña: ")
        if contrasenia == clientes[numero_cliente]["clave"]:
            bucle = False
        else:
            print("contraseña incorrecta")
    return numero_cliente



"""Funcion que arma el pedido según el restaurante seleccionado"""

def rappipuntos_giv (monto):
    if monto < 200:
        rappi = (monto/100)*10
    if monto >= 200 and monto <= 500:
        rappi = (monto/100)*15
    if monto >500:
        rappi = (monto/100)*20
    return rappi

def armarPedido(restaurant,restaurantes,pedido,pedidos,user,rappitenderos):
    preciototal=0
    pedidoTerminado = "seguir"
    lista = list(restaurantes[restaurant]["platos"].keys())
    print("Comenzamos a armar el pedido; Por favor seleccione q desea agregar al carro, en caso de que el articulo se encuentre pedido, el mismo sera sobreescrito: ")
    while pedidoTerminado == "seguir":
        print("Los platos disponibles son: ")
        print(restaurantes[restaurant]["platos"])
        item = input("Nombre del articulo: ")
        while item not in lista:
            item = input("ingrese un articulo valido ")
        cant = 0
        while cant <= 0:
            cant = input("Ingrese cuantas unidadesdesea agregar: ")
            valid = True
            while valid != False:
                if cant.isdigit():
                    cant= int(cant)
                    if cant > 0:
                        valid = False
                if valid == True:
                    cant = input("Ingrese cuantas unidadesdesea agregar: ")
        pedido[item]=cant
        continuar = input("Para seguir agregando pedidos ingrese: 1")
        if continuar !="1":
            pedidoTerminado = "parar"
        for i in pedido:
            if i != "client":
                preciototal += (restaurantes[restaurant]["platos"][i] * pedido[i])
        pedidos.append(pedido)
    rand = random.randrange(0, len(rappitenderos))
    while rappitenderos[rand]["pedido"] != "None":
        rand = random.randrange(0, len(rappitenderos))
    return rand, preciototal

def distancia_reco (restaurantes, clientes, rappitenderos, rest, user, rep):
    lat1, lon1 = restaurantes[rest]["lat y lon"]
    lat2, lon2 = clientes[user]["lat y lon"]
    lat3, lon3 = rappitenderos[rep]["lat y lon"]
    distancia_a = math.sqrt(((lat3-lat1)*(lat3-lat1))+((lon3-lon1)*(lon3-lon1)))
    distancia_b = math.sqrt(((lat1-lat2)*(lat1-lat2))+((lon1-lon2)*(lon1-lon2)))
    distancia=100 * (distancia_a + distancia_b)
    return distancia

def pedidoManual(clientes,restaurantes,rappitenderos,pedidos):
    pedido={}
    user=login(clientes)
    print ("Bienvenido, ", clientes[user]["nombre"])
    print ("Los restaurantes disponibles son: ")
    bucle = True
    while bucle==True:
        lista = []
        x = 0
        for i in restaurantes:
            x += 1
            lista.append(i["nombre"])
            print  (str(i["nombre"]+" "+str(i)))
        restaurant=input("Ingrese el numero del restaurante: ")
        while not restaurant.isdigit():
            restaurant=input("Ingrese el numero del restaurante: ")
        restaurant=int(restaurant)
        restaurant -= 1
        while restaurant >= x:
            restaurant=input("El restaurante no se encuentra registrado ")
            while not restaurant.isdigit():
                restaurant=input("Ingrese el numero del restaurante: ")
            restaurant=int(restaurant)
            restaurant -= 1
        bucle = False
    pedido["client"]=clientes[user]["nombre"]
    rand, mony = armarPedido(restaurant, restaurantes, pedido, pedidos, user, rappitenderos)
    distancia = distancia_reco (restaurantes, clientes, rappitenderos, restaurant, user, rand)
    tiempo = distancia/15
    print ("la entrega llegara en ", str(tiempo), "horas")
    rappitenderos[rand]["lat y lon"] = clientes[user]["lat y lon"]
    rappitenderos[rand]["propina"] += (mony/10)
    creditos = rappipuntos_giv (mony)
    clientes[user]["rapicredits"] += creditos
    restaurantes[restaurant]["ventas"] += 1
    
    

#Punto 4

def generar_pedido (restaurantes, rest, clientes, user, plat, pedidos):
    pedido= {"cliente":user}
    lista_productos = list(restaurantes[rest]["platos"])
    preciototal=0
    for i in range (0, plat):
        product = random.choice(lista_productos)
        cant = random.randrange (0, plat)
        pedido[product] = cant
    for x in pedido:
        if x != "cliente":
            preciototal += (restaurantes[rest]["platos"][x] * pedido[x])
    pedidos.append(pedido)
    clientes[user]["rapicredits"] += rappipuntos_giv (preciototal)
    return preciototal


def simulacion(clientes,restaurantes,rappitenderos, pedidos):
    cant = 0
    plat = 0
    while cant<=0 or cant >100:
        cant=input("Porfavor ingrese la cantidad de simulaciones que desea realizar: ")
        while not cant.isdigit():
            cant=input("Porfavor ingrese la cantidad de simulaciones que desea realizar: ")
        cant = int(cant)
    while plat<=0:
        plat=input("ingrese la cantidad maxima de platos por pedido ")
        while not plat.isdigit():
            plat=input("ingrese la cantidad maxima de platos por pedido ")
        plat = int(plat)
    for i in range(0,cant):
        user=random.randrange(0, len(clientes))
        rest=random.randrange(0, len(restaurantes))
        repa=random.randrange(0, len(rappitenderos))
        preciototal = generar_pedido (restaurantes, rest, clientes, user, plat, pedidos)
        rappitenderos[repa]["propina"] += (preciototal/10)
        rappitenderos[repa]["lat y lon"] = clientes[user]["lat y lon"]
        restaurantes[rest]["ventas"] += 1



#Punto 5



def toptop(busqueda, parametro, mensaje):
    lista=[]
    lista2=[]
    if len(busqueda) < 10:
        print(mensaje)
    for i in range (0, len(busqueda)):
        lista.append(i)
        lista2.append(busqueda[i][parametro])
    for largo in range (1, len(lista)):
        for lugar in range (len(lista)-largo):
            if lista2[lugar]< lista2[lugar + 1]:
                temporal2 = lista2[lugar]
                temporal= lista[lugar]
                lista2[lugar] = lista2[lugar + 1]
                lista[lugar] = lista[lugar + 1]
                lista2[lugar + 1] = temporal2
                lista[lugar + 1] = temporal
    if len(lista) == 0:
        print ("fail")
    elif len(lista) < 10:
        for x in range (0, len(lista)):
            print(busqueda[lista[x]])
    else:
        for x in range (0, 10):
            print(busqueda[lista[x]])

def topcreditos(clientes):
    mensaje = "no hay 10 usuarios, se realizara con los usuarios disponibles"
    toptop(clientes, "rapicredits", mensaje)

def toppropinas(rappitenderos):
    mensaje = "no hay 10 rappitenderos, se realizara con los rappitenderos disponibles"
    toptop(rappitenderos, "propina", mensaje)

def topventas(restaurantes):
    mensaje = "no hay 10 restaurantes suficientes, se realizara con los restaurantes disponibles disponibles"
    toptop(restaurantes, "ventas", mensaje)
        
def menu():
    print("Seleccione una opción: ")
    print("\t1. Carga de información predefinida.")
    print("\t2. Carga de información manual.")
    print("\t3. Pedido manual.")
    print("\t4. Simulación de pedidos.")
    print("\t5. Informes.")
    print("\t6. Salir del programa.")


def menu1(restaurantes,clientes,rappitenderos): #Carga de info predefinida
    hard(restaurantes,clientes,rappitenderos)
    print("\ta. Regresar.")


def menu2(): #Carga de info manual
    print("Seleccione una opción: ")
    print("\ta. Un nuevo restaurante.")
    print("\tb. Un nuevo plato.")
    print("\tc. Un nuevo cliente.")
    print("\td. Un nuevo rappitendero.")
    print("\te. Regresar.")


def menu3(): #Pedido Manual
    pedidoManual(clientes, restaurantes, rappitenderos, pedidos)
    print("\ta. Regresar.")


def menu4(): #Simulacion de pedidos
    simulacion(clientes, restaurantes, rappitenderos, pedidos)
    print("\ta. Regresar.")


def menu5(): #Informes
    print("Seleccione un opción: ")
    print("\ta. Los 10 Clientes con mayor cantidad de Rappicréditos.")
    print("\tb. Rappitenderos con mayor propina acumulada.")
    print("\tc. Restaurantes que mas ventas tuvieron.")
    print("\td. Regresar.")


#Aqui ejecutaremos todas las funcionalidades por menu

def menus(restaurantes,clientes,rappitenderos):
    salir_menu = False
    while not salir_menu:
        salir_menu1 = False
        salir_menu2 = False
        salir_menu3 = False
        salir_menu4 = False
        salir_menu5= False
        menu()
        opcionMenu = input("Seleccione una opción1: ")
        #Menu predefinido
        if opcionMenu == "1": 
            while not salir_menu1:
                menu1(restaurantes,clientes,rappitenderos)
                opcionMenu1 = input("Seleccione una opción2: ")
                if opcionMenu1 == 'a':
                    salir_menu1 = True
                else:
                    print("No ingreso ninguna opcion correcta")
        #Carga de info manual
        elif opcionMenu == "2": 
            while not salir_menu2:
                menu2()
                opcionMenu2= input("Seleccione una opción3: ")
                if opcionMenu2 == "a":
                    print("Ha elegido opción a")
                    nuevoRestaurante(restaurantes)
                elif(opcionMenu2 == 'b'):
                    print("Ha elegido opción b")
                    nuevoPlato(restaurantes)
                elif(opcionMenu2 == 'c'):
                    print("Ha elegido opción c")
                    nuevoCliente(clientes)
                elif (opcionMenu2 == 'd'):
                    print("Ha elegido opción d")
                    nuevoRappitendero(rappitenderos,restaurantes)
                elif opcionMenu2 == 'e':
                    salir_menu2 = True
                else:
                    print("No ingreso ninguna opcion correcta")
        #Pedido Manual
        elif opcionMenu == "3": 
            while not salir_menu3:
                menu3()
                opcionMenu3 = input("Seleccione una opción4: ")
                if opcionMenu3 == "a":
                    salir_menu3 = True
                else:
                    print("No ingreso ninguna opcion correcta")
        #Simulacion de pedidos
        elif opcionMenu == "4": 
            while not salir_menu4:
                menu4()
                opcionMenu4 = input("Seleccione una opción5: ")
                if opcionMenu4 == 'a':
                    salir_menu4 = True
                else:
                    print("No ingreso ninguna opcion correcta")
        #Informes
        elif opcionMenu=="5": 
            while not salir_menu5:
                menu5()
                opcionMenu5=input("Seleccione una opcion6: ")
                if opcionMenu5 == "a":
                    print("Ha elegido opción a")
                    topcreditos(clientes)
                elif (opcionMenu5 == 'b'):
                    print("Ha elegido opción b")
                    toppropinas(rappitenderos)
                elif (opcionMenu5 == 'c'):
                    print("Ha elegido opción c")
                    topventas(restaurantes)
                elif (opcionMenu5 == 'd'):
                    salir_menu5 = True
                else:
                    print("No ingreso ninguna opcion correcta")
        #Salir
        elif opcionMenu == "6": 
            salir_menu = True
        else:
            input("No has elegido ninguna opción correcta. Pulsa una tecla para continuar")
menus(restaurantes,clientes,rappitenderos)




