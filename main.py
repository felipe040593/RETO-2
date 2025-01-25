#Variables globales
clientes = []

#Creación de clases principales
class SistemaVeterinaria:
    class Persona: 
        id_counter = 1
        def __init__(self,nombre, contacto):
            self.id = SistemaVeterinaria.Persona.id_counter
            self.nombre = nombre
            self.contacto = contacto
            
            SistemaVeterinaria.Persona.id_counter += 1
            
    class Cliente(Persona):
        def __init__(self, nombre, contacto, direccion):
            super().__init__(nombre, contacto)
            self.direccion = direccion
            self.mascota = []

        def agregar_mascota(self, mascota):
            self.mascota.append(mascota)
            

    class Mascota:
        id_counter = 1
        def __init__(self, nombre, especie, raza, edad):
            self.id = SistemaVeterinaria.Mascota.id_counter
            self.nombre = nombre
            self.especie = especie
            self.raza = raza
            self.edad = edad
            self.historial_clinico=[]

            SistemaVeterinaria.Mascota.id_counter += 1


    class Citas:
        id_counter = 1
        def __init__(self, fecha, hora, servicio, veterinario):
            self.id = SistemaVeterinaria.Citas.id_counter
            self.fecha = fecha
            self.hora = hora
            self.servicio = servicio
            self.veterinario = veterinario

            SistemaVeterinaria.Citas.id_counter += 1

    
#Funcion del sistema
def registrar_cliente():
    print("----------REGISTRO DE CLIENTE----------")
    nombre = input("Ingrese nombre del cliente: ")
    contacto = input("Ingrese número de contacto del cliente: ")
    direccion = input("Ingrese dirección del cliente: ")
    cliente = SistemaVeterinaria(nombre, contacto, direccion) #Creamos el objeto cliente
    print("---------------------------------------")

    print("----------REGISTRO DE MASCOTAS----------")
    nombre_mascota = input("Nombre de la mascota: ")
    especie = input("Especie de la mascota: ")
    raza = input("Raza de la mascota: ")
    mascota = SistemaVeterinaria (nombre_mascota, especie, raza) #Creamos el objeto mascota

    cliente.agregar_mascota(mascota)

    clientes.append(cliente)
    print("Cliente y mascota agregados correctamente")
    print("---------------------------------------")

def programar_cita():
    pass

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
            pass
        elif opcion == "3":
            pass
        elif opcion == "4":
            pass
        else:
            print("Opción inválida. Intente nuevamente.")
        