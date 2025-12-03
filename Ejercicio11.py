
def validacion_de_contraseña():
    contraseña_sistema = "admin123"

    Contrasena_usuario = input("ingrese contraseña: ")

    if contraseña_sistema == Contrasena_usuario:
        print("Contraseña correcta")
    else:
        print("Contraseña incorrecta")

validacion_de_contraseña()
