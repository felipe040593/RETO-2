#Variables globales
clientes = [] #Creamos la lista donde guardaremos los datos de cada uno de los clientes registrados.

#Creación de clases principales
class SistemaVeterinaria: #Super Clase que permite heredar atributos y métodos a las demas clases.
    class Persona:  #Clase que permite guardar en cada atributos los datos del cliente.
        def __init__(self,nombre,num_cedula, contacto): #Funcion que guarda datos datos relevantes del cliente.
            self.num_cedula = num_cedula
            self.nombre = nombre
            self.contacto = contacto
            
    class Cliente(Persona): #Hereda tos los datos de la clase persona adicionando los datos de cada mascota.
        def __init__(self, nombre, num_cedula, contacto, direccion):
            super().__init__(nombre,num_cedula, contacto) #Llamamos los datos solicitados en la clase persona para complementar la informacion en la clase cliente
            self.direccion = direccion
            self.mascotas = [] #Listamos dentro de la clase cliente las mascotas asociadas a su respectivo dueño

        def agregar_mascota(self, mascota):  #Función para agregar en la lista mascotas [] cada mascota(s) al respectivo cliente.
            self.mascotas.append(mascota)
            
    class Mascota: #Clase que permite guardar en cada atributos los datos de la mascota.
        def __init__(self, nombre, especie, raza, edad):
            self.nombre = nombre
            self.especie = especie
            self.raza = raza
            self.edad = edad
            self.historial_clinico=[] #Listamos dentro de la clase mascota el historial clinico de cada mascota.

    class Citas: #Clase que permite guardar en cada atributos los datos de la cita.
        def __init__(self,num_cedula, fecha, hora, servicio, veterinario):
            self.num_cedula = num_cedula
            self.fecha = fecha
            self.hora = hora
            self.servicio = servicio
            self.veterinario = veterinario

    
#Funcion del sistema
def registrar_cliente(): #Función que permite registrar un cliente y su respectiva mascota.
    print("----------REGISTRO DE CLIENTE----------")
    nombre = input("Ingrese nombre del cliente: ")
    num_cedula = input("Ingrese número de cédula del cliente: ")
    contacto = input("Ingrese número de contacto del cliente: ")
    direccion = input("Ingrese dirección del cliente: ")
    cliente = SistemaVeterinaria.Cliente(nombre,num_cedula, contacto, direccion) #Creamos el objeto cliente
    print("---------------------------------------")

    print("----------REGISTRO DE MASCOTAS----------")
    nombre_mascota = input("Nombre de la mascota: ")
    especie = input("Especie de la mascota: ")
    raza = input("Raza de la mascota: ")
    edad =  input("Ingrese edad de la mascota: ")
    mascota = SistemaVeterinaria.Mascota(nombre_mascota, especie, raza, edad) #Creamos el objeto mascota

    cliente.agregar_mascota(mascota) #Agregamos la mascota al cliente

    clientes.append(cliente) #Agregamos el cliente a la lista de clientes
    print("Cliente y mascota agregados correctamente")
    print("---------------------------------------")

def programar_cita(): #Función que permite programar una cita para un cliente.
    print("----------PROGRAMAR CITA----------")
    num_cedula = input("Ingrese el número de cédula del cliente: ")
    
    # Buscar el cliente en la lista de clientes
    cliente_encontrado = None #Inicializamos la variable cliente_encontrado en None
    for cliente in clientes:
        if cliente.num_cedula == num_cedula: #Si el número de cédula ingresado es igual al número de cédula del cliente
            cliente_encontrado = cliente
            break
    
    if cliente_encontrado: #Si el cliente fue encontrado
        print(f"Cliente encontrado: {cliente_encontrado.nombre}") 
        fecha = input("Ingrese la fecha de la cita (DD/MM/AAAA): ")
        hora = input("Ingrese la hora de la cita (HH:MM): ")
        servicio = input("Ingrese el servicio requerido: ")
        veterinario = input("Ingrese el nombre del veterinario: ")
        
        # Crear la cita
        cita = SistemaVeterinaria.Citas(num_cedula, fecha, hora, servicio, veterinario) #Creamos el objeto cita
        
        # Aquí podrías agregar la cita a una lista de citas o al historial del cliente
        print("Cita programada exitosamente.")
    else:
        print("Cliente no encontrado. Verifique el número de cédula.")
    print("----------------------------------")

def consultar_historia(): #Función que permite consultar el historial clínico de un cliente.
    if not clientes: #Si no hay clientes registrados imprimimos mensaje y retornamos
        print("No hay clientes registrados.")
        return

    num_cedula = input("Ingrese el número de cédula del cliente: ") #Solicitamos el número de cédula del cliente
    cliente = next((c for c in clientes if c.num_cedula == num_cedula), None) #Buscamos el cliente en la lista de clientes

    if cliente is None:
        print("Cliente no encontrado.")
        return

    print(f"Historial clínico del cliente {cliente.nombre} identificado con cédula {num_cedula}: ") #Imprimimos el historial clínico del cliente con el número de cédula ingresado
    for mascota in cliente.mascotas: 
        print(f"- Mascota: {mascota.nombre}")
        if mascota.historial_clinico: 
            for entrada in mascota.historial_clinico:
                print(f"  * {entrada}")
        else:
            print("  * Sin historial clínico registrado.")
            
#Menú principal
def menu_principal(): #Función que muestra el menú principal del sistema
    while True:
        print("----------------MENÚ PRINCIPAL----------------")
        print("1. Registrar cliente y mascotas")
        print("2. Programar cita")
        print("3. Consultar historial de servicios")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            registrar_cliente()
        elif opcion == "2":
            programar_cita()
        elif opcion == "3":
            consultar_historia()
        elif opcion == "4":
            print("Gracias por usar el sistema. ¡Adiós!")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

menu_principal()
        