#Variables globales
Clientes = []

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
            self.masota = []
            
            

    class Mascota:
        pass

    class Citas:
        pass
    
#Funcion del sistema
def registrar_cliente():
    pass

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
            pass
        elif opcion == "2":
            pass
        elif opcion == "3":
            pass
        elif opcion == "4"
            pass
        else:
            print("Opción inválida. Intente nuevamente.")
        