import ticket_master as tm

# Agregar un usuario y mostrar la lista de usuarios
gestion_usuarios = tm.GestionUsuarios()

print("*****************")
print("* TICKET MASTER * ")
print("*****************")

print("INGRESE DATOS DEL USUARIO")

correo_usuario = input("Ingrese correo del usuario: ")
nombre_usuario = input("Ingrese nombre del usuario: ")

gestion_usuarios.agregar_usuario(correo_usuario, nombre_usuario)

gestion_usuarios.mostrar_usuarios()

# Agregar un evento y mostrar la lista de eventos
print("INGRESE DATOS DEL EVENTO")

nombre_evento = input("Ingrese nombre del evento: ")
fecha_evento = input("Ingrese fecha del evento: ")
lugar_evento = input("Ingrese lugar del evento: ")
entradas_disponibles = int(input("Ingrese cantidad de entradas disponibles: "))

gestion_usuarios.agregar_evento(
    nombre_evento, fecha_evento, lugar_evento, entradas_disponibles
)
gestion_usuarios.mostrar_eventos()

# Compra de entradas
print("COMPRAR ENTRADAS")

correo_usuario = input("Ingrese correo del usuario: ")
nombre_evento = input("Ingrese nombre del evento: ")
costo_entrada = float(input("Ingrese costo de la entrada: "))
cantidad_entradas = int(input("Ingrese cantidad de entradas: "))

gestion_usuarios.comprar_entradas(
    correo_usuario, nombre_evento, costo_entrada, cantidad_entradas
)
