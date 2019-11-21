import random
#Entidades a cargar
restaurantes={}
clientes={}
rappitenderos={}
pedidos={}


#Funcion que recibe las entidades con la información predefinida por entidad(Restaurantes,clientes y rappitenderos)"""
def hard(restaurantes,clientes,rappitenderos): #Punto 1
    restaurantes["el vivero"]=["Primera Junta 1094","1156223610",( -34.4615385, -58.5075307),20,0, [("Cheese Burger",180),("Coca Cola",80),("Tacos",200) ],0]
    restaurantes["MC DONNALDS"]=["Avenida Centenario 200","1156223620",( -70.4615385, -40.5075307),20,0, [("Cuarto de libra" ,220),("Big Mac",200),("mcFlurry",100) ],0]
    restaurantes["BURGER KING"]= ["Belgrano 500","1156223630",( -80.4615385, -48.5075307),20,0, [("Whooper",180),("Stacker",300),("Cono Helado",50) ],0]
    restaurantes["GRIDO"]=["Avenida Centenario 1100","1156228610",( -10.4615385, -60.5075307),20,0, [("1kilo",250),("1/2 kilo",200),("2 kilos",400) ],0]
    restaurantes["KENTUCKY"]= ["Avenida Rolon 1094","1156238950",( -100.4615385, -20.5075307),20,0, [("Pizza de Muzzarella",220),("Empanadas de carne",40),("Empanadas de Jamon y queso",40) ],0]
    clientes["Agustin Silva"]=["Agustin123!","1156223610","Diego Palma 21",( -13.4615385, -32.4615385),500]
    clientes["juan"] =["Juan123!","1156554410","Julian Navarro 200",( -43.4615385, -62.4615385),350]
    clientes["valen"]= ["Valen123!","1169729137","Haedo 1969",( -23.4615385, -42.4615385),2000]
    rappitenderos["Carlos"]= [0.0,(-10.4551,-60.5215) , ["none"]]
    rappitenderos["pepe"]= [0.0,(-12.4551,-60.5215) , ["none" ]]
    rappitenderos["Alberto"]= [0.0,(-15.4551,-62.5215) , ["none"]]
   

def imprimirDiccionarios(diccionario):
    for i in range (0,len(list(diccionario.keys()))):
        print(i,"-",list(diccionario.keys())[i])


#Segunda funcionalidad: A continuación crearemos funciones para solicitar información por cada entidad

"""Funcion para la creación de un nuevo restaurante"""

def nuevoRestaurante(restaurantes): 
    nombre=input("Ingrese el nombre del restaurante: ")
    while nombre in list(restaurantes.keys()):
        print("El restaurante ya existe, Ingrese uno nuevo:")
        nombre= input("Ingrese el nombre del restaurante: ")
    direc=input("Ingrese la dirección: ")
    tel= input("ingrese el numero de teléfono: ")
    ##AGREGAR VERIFICACION DE TEL
    lat=float (input("Latitud: "))
    long=float(input("Longitud: " ))
    rad=float(input("Ingrese el radio de entrega (unidad en km)"))
    platos= []
    restaurantes[nombre]= [direc,tel,(lat,long),rad,0,platos,0]
    print("Se ha creado su restaurante")
    imprimirDiccionarios(restaurantes)

"""Funcion para la creación de un nuevo plato"""
def nuevoPlato(restaurantes): 
    bucle= True
    """Solicitamos un numero de restaurante hasta que se ingrese uno de los registrados"""
    while bucle==True:
        imprimirDiccionarios(restaurantes)
        restaurant=int((input("Ingrese el numero del restaurante:")))
        try:
            if list(restaurantes.keys())[restaurant]:
                bucle=False
        except IndexError:
            print("El restaurante no se encuentra registrado")


        
    plato=input("ingrese plato: ")
    precio=float(input("Ingrese el precio: "))
    aux=list(restaurantes.values())[restaurant]
    print("DEBUG AUX ", aux)
    platos=((plato,precio))
    restaurantes[restaurant]=[aux[0],aux[1],aux[2],aux[3],aux[4],aux[5].append(platos),aux[6]]
    print("Plato agregado.")
    print(list(restaurantes.values())[restaurant])



"""Funcion para la creación de un nuevo cliente"""

def nuevoCliente(clientes):
    nombre=input("Ingrese su nombre: ")
    direc=input("Ingrese su dirección: ")
    lat=float(input("Ingrese su latitud: "))
    long=float(input("Ingrese su longitud: "))
    tel=input("ingrese su telefono: ")
    loop=True
    while loop:
        contrasenia=input("ingrese su contraseña: ")
        #if verificarContraseña():  HAY Q ARMAR ESTA FUNCION
        loop=False
    loop2=True
    while loop2:
        checkeo= input("Vuelva a ingresar su contraseña: ")
        if checkeo==contrasenia:
            loop2= False
    clientes[nombre]= [contrasenia,tel,direc,(lat,long),0]
    imprimirDiccionarios(clientes)

"""Funcion para la creación de un nuevo rappitendero"""

def nuevoRappitendero(rappitenderos,restaurantes): 
    nombre=input("Ingrese su nombre: ")
    while nombre in list(rappitenderos.keys()):
        nombre=input("Ingrese nuevamente el nombre: ")
    rand=random.randint(0,len(list(restaurantes.keys())))
    pos=restaurantes[list(restaurantes.keys())[rand]][2]
    rappitenderos[nombre]=[0,pos,["none"]]
    imprimirDiccionarios(rappitenderos)


#Comenzamos con la tercera funcionalidad: Pedido Manual, en ella definiremos funciones para el login y el pedido manual de articulos



"""Funcion que registra al usuario y checkea la contraseña ingresada"""
def login(clientes):
    bucle = True
    while bucle:
        user = input("Ingrese su usuario: ")
        if user in list(clientes.keys()):
            bucle = False
        else:
            print("Usuario inexistente.")
    bucle = True
    while bucle:
        contrasenia = input("Ingrese su contraseña: ")
        if contrasenia == clientes[user][0]:
            bucle = False
        else:
            print("Usuario inexistente.")
    return user

"""Funcion que arma el pedido según el restaurante seleccionado"""

def armarPedido(restElegido,restaurantes,pedido,pedidos,user,rappitenderos):
    preciototal=0
    pedidoTerminado = False
    print("Comenzamos a armar el pedido; Por favor seleccione q desea agregar al carro: ")
    while not pedidoTerminado:
        print("Los platos disponibles son: ")
        
        for i in range(0, len(restaurantes[list(restaurantes.keys())[int(restElegido) - 1]][5])):
            print(i+1, " - ", restaurantes[list(restaurantes.keys())[int(restElegido)-1]][5][i])
        item = input("Numero del articulo: ")
        cant = 0
        while cant <= 0:
            cant = int(input("Ingrese cuantas unidadesdesea agregar: "))
        preciototal += cant * int(restaurantes[list(restaurantes.keys())[int(restElegido)-1]][5][int(item) - 1][1])
        # Armo condición de si ya existe pedido
        if not item in pedido:
            pedido.append((cant, item))
        
           
        continuar = input("“Para seguir agregando pedidos ingrese: “S”")
        if continuar !="S":
            pedidoTerminado = True
    pedidos[user] = pedido
    rappivalido = False
    while not rappivalido:
        rand = random.randint(0, len(list(rappitenderos.keys())))
    # rappitendero= {Nombre;[Propina,Posicion,PedidoActual]}
        rappivalido = True
    aux = rappitenderos[list(rappitenderos.keys())[rand-1]]
    rappitenderos[rand] = [int(aux[0]) + preciototal * 10 / 100, clientes[user][2], ["none"]]
    
    aux = clientes[user]
    if preciototal <= 200:
        clientes[user] = [aux[0], aux[1], aux[2], aux[3], int(aux[4]) + preciototal * 10 / 100]
    elif preciototal <= 500:
        clientes[user] = [aux[0], aux[1], aux[2], aux[3], int(aux[4]) + preciototal * 15 / 100]
    else:
        clientes[user] = [aux[0], aux[1], aux[2], aux[3], int(aux[4]) + preciototal * 20 / 100]
    try:
        aux = restaurantes[restElegido]
    except KeyError:
        print("Este codigo de restaurante no se encuentra registrado")

    
    restaurantes[restElegido] = [aux[0], aux[1], aux[2], aux[3], int(aux[4]) + 1, int(aux[5]) + preciototal]

def pedidoManual(clientes,restaurantes,rappitenderos,pedidos):
    
    pedido=[]
    user=login(clientes)
    print("Bienvenido, ", user)
    print("Los restaurantes disponibles son: ")
    imprimirDiccionarios(restaurantes)
    restElegido=input("Ingrese el numero de su restaurante: ")
    armarPedido(restElegido, restaurantes, pedido, pedidos, user, rappitenderos)
#Punto 4
def simulacion(clientes,restaurantes,rappitenderos):
    preciototal=0
    cant=0
    while cant<=0 or cant >100:
        cant=int(input("Porfavor ingrese la cantidad de simulaciones que desea realizar: "))
    for i in range(0,cant):
        user=list(clientes.keys())[random.randint(0,len(list(clientes.keys()-1)))]
        rest=list(restaurantes.keys())[random.randint(0,len(list(restaurantes.keys()-1)))]
        max=random.randint(1,len(restaurantes[rest][5]))
        cant=random.randint(0,50)
        rappi=list(rappitenderos.keys())[random.randint(0,len(list(rappitenderos.keys()-1)))]
        precio=0
        for i in range(0,max):
            precio +=restaurantes[rest][5][i][1]*cant
        aux=rappitenderos[rappi]
        rappitenderos[rappi]=[int(aux[0])+precio*10/100,clientes[user][2],["none"]]
        aux = clientes[user]
        if preciototal <= 200:
            clientes[user] = [aux[0], aux[1], aux[2], aux[3], int(aux[4]) + precio * 10 / 100]
        elif preciototal <= 500:
            clientes[user] = [aux[0], aux[1], aux[2], aux[3], int(aux[4]) + precio * 15 / 100]
        else:
            clientes[user] = [aux[0], aux[1], aux[2], aux[3], int(aux[4]) + precio * 20 / 100]
        print(rappi,"le llevo su pedido a ", user, " El monto fue de: ", precio )
        aux=restaurantes[rest]
        restaurantes[rest]=[aux[0],aux[1],aux[2],aux[3],int(aux[4])+1,int(aux[5])+precio]


#Punto 5

def topCreditos(diccionario,cant):
    users=list(diccionario.keys())
    datos=list(diccionario.values())
    info=[]
    if cant==10:
        if len(users)<cant:
            print("No se puede calcular un top 10 sin 10 clientes en la base de datos.")
        for i in range(0,10):
            info.append((users[i],datos[i][4]))
        info.sort(key=lambda x: x[1], reverse=True)
        for i in range(0,len(users)):
            print(i+1," - ",info[i][0]," Con : ", info[i][1])
    else:
        for i in range(0,10):
            info.append((users[i],datos[i][cant]))
        info.sort(key=lambda x: x[1], reverse=True)
        for i in range(0,len(users)):
            print(i+1," - ",info[i][0]," Con : ", info[i][1])









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
    simulacion(clientes, restaurantes, rappitenderos)
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
        opcionMenu = input("Seleccione una opción: ")
        #Menu predefinido
        if opcionMenu == "1": 
            while not salir_menu1:
                menu1(restaurantes,clientes,rappitenderos)
                opcionMenu1 = input("Seleccione una opción: ")
                if opcionMenu1 == 'a':
                    salir_menu1 = True
                else:
                    print("No ingreso ninguna opcion correcta")
        #Carga de info manual
        elif opcionMenu == "2": 
            while not salir_menu2:
                menu2()
                opcionMenu2= input("Seleccione una opción: ")
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
                opcionMenu3 = input("Seleccione una opción: ")
                if opcionMenu3 == "a":
                    salir_menu3 = True
                else:
                    print("No ingreso ninguna opcion correcta")
        #Simulacion de pedidos
        elif opcionMenu == "4": 
            while not salir_menu4:
                menu4()
                opcionMenu4 = input("Seleccione una opción: ")
                if opcionMenu4 == 'a':
                    salir_menu4 = True
                else:
                    print("No ingreso ninguna opcion correcta")
        #Informes
        elif opcionMenu=="5": 
            while not salir_menu5:
                opcionMenu5=input("Seleccione una opcion: ")
                if opcionMenu5 == "a":
                    print("Ha elegido opción a")
                    topCreditos(clientes,10)

                elif (opcionMenu5 == 'b'):
                    print("Ha elegido opción b")
                    topCreditos(rappitenderos,0)

                elif (opcionMenu5 == 'c'):
                    print("Ha elegido opción c")
                    topCreditos(restaurantes,4)

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
