# Implementar una estructura básica para almacenar información de usuarios (nombre, correo electrónico, historial de compras, etc.).
class GestionUsuarios:
    def __init__(self):
        self.usuarios = {}
        self.eventos = {}
        self.historial_transacciones = {}

    # Usuarios
    def agregar_usuario(self, correo_usuario, nombre_usuario):
        if correo_usuario not in self.usuarios:
            self.usuarios[correo_usuario] = {
                "nombre": nombre_usuario,
                "historial_compras": [],
            }
            print(f"Usuario {nombre_usuario} registrado exitosamente.")
        else:
            print("El usuario ya existe.")

    def mostrar_usuarios(self):
        print("Lista de Usuarios:")
        for correo_usuario, detalles_usuario in self.usuarios.items():
            print(f"Correo: {correo_usuario}, Nombre: {detalles_usuario['nombre']}")

    # Eventos
    def agregar_evento(
        self, nombre_evento, fecha_evento, lugar_evento, entradas_disponibles
    ):
        if nombre_evento not in self.eventos:
            self.eventos[nombre_evento] = {
                "fecha": fecha_evento,
                "lugar": lugar_evento,
                "entradas_disponibles": entradas_disponibles,
            }
            print(f"Evento '{nombre_evento}' agregado correctamente.")
        else:
            print("El evento ya existe.")

    def mostrar_eventos(self):
        print("Lista de Eventos:")
        for nombre_evento, detalles_evento in self.eventos.items():
            print(
                f"Nombre: {nombre_evento}, Fecha: {detalles_evento['fecha']}, Lugar: {detalles_evento['lugar']}, Entradas Disponibles: {detalles_evento['entradas_disponibles']}"
            )

    # Compra y devolución de entradas
    def comprar_entradas(
        self, correo_usuario, nombre_evento, costo_entrada, cantidad_entradas
    ):
        if correo_usuario in self.usuarios and nombre_evento in self.eventos:
            if cantidad_entradas <= self.eventos[nombre_evento]["entradas_disponibles"]:
                costo_total = cantidad_entradas * costo_entrada
                self.eventos[nombre_evento]["entradas_disponibles"] -= cantidad_entradas
                self.usuarios[correo_usuario]["historial_compras"].append(
                    {
                        "evento": nombre_evento,
                        "cantidad": cantidad_entradas,
                        "costo_total": costo_total,
                    }
                )
                print(
                    f"Compra exitosa para el evento '{nombre_evento}'. Total: ${costo_total}"
                )
            else:
                print("No hay suficientes entradas disponibles.")
        else:
            print("Usuario o evento no encontrado.")

    

