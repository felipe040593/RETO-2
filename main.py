#Variables globales
clientes = []

#Creación de clases principales
class SistemaVeterinaria:
    class Persona: 
        def __init__(self,nombre,num_cedula, contacto):
            self.num_cedula = num_cedula
            self.nombre = nombre
            self.contacto = contacto
            
    class Cliente(Persona):
        def __init__(self, nombre, num_cedula, contacto, direccion):
            super().__init__(nombre,num_cedula, contacto)
            self.direccion = direccion
            self.mascotas = []

        def agregar_mascota(self, mascota):
            self.mascotas.append(mascota)
            

    class Mascota:
        def __init__(self, nombre, especie, raza, edad):
            self.nombre = nombre
            self.especie = especie
            self.raza = raza
            self.edad = edad
            self.historial_clinico=[]

    class Citas:
        def __init__(self,num_cedula, fecha, hora, servicio, veterinario):
            self.num_cedula = num_cedula
            self.fecha = fecha
            self.hora = hora
            self.servicio = servicio
            self.veterinario = veterinario

    
#Funcion del sistema
def registrar_cliente():
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

    cliente.agregar_mascota(mascota)

    clientes.append(cliente)
    print("Cliente y mascota agregados correctamente")
    print("---------------------------------------")

def programar_cita():
    if not clientes:
        print("No hay clientes registrados.")
        return

    num_cedula = input("Ingrese el número de cédula del cliente: ")
    cliente = next((c for c in clientes if c.num_cedula == num_cedula), None)

    if cliente is None:
        print("Cliente no encontrado.")
        return

    fecha = input("Ingrese la fecha de la cita (DD/MM/AAAA): ")
    hora = input("Ingrese la hora de la cita (HH:MM): ")
    servicio = input("Ingrese el servicio solicitado: ")
    veterinario = input("Ingrese el nombre del veterinario asignado: ")

    cita = SistemaVeterinaria.Cita(num_cedula, fecha, hora, servicio, veterinario)
    print(f"Cita programada exitosamente para el cliente {cliente.nombre} el {fecha} a las {hora}.")

def consultar_historia():
    pass

#Menú principal
def menu_principal():
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
            pass
        elif opcion == "4":
            break
        else:
            print("Opción inválida. Intente nuevamente.")

menu_principal()
        