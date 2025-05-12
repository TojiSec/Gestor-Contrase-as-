import string
import secrets
import os

def generar_contraseña(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(caracteres) for _ in range(longitud))

def guardar_contraseña(servicio, usuario, contraseña, ruta_archivo):
    try:
        with open(ruta_archivo, 'a', encoding='utf-8') as archivo:
            archivo.write(f"{servicio} | {usuario} | {contraseña}\n")
        print("✅ Contraseña guardada correctamente.")
    except Exception as e:
        print("❌ Error al guardar la contraseña:", e)

def main():
    print("🔐 Generador de Contraseñas Seguras\n")

    servicio = input("Escribe el servicio (ej. Gmail, Facebook): ").strip()
    usuario = input("Escribe el usuario o correo: ").strip()

    try:
        longitud = int(input("Escribe la longitud de tu contraseña: "))
        if longitud < 6:
            print("❌ La longitud mínima recomendada es 6 caracteres.")
            return
    except ValueError:
        print("❌ Longitud inválida. Debes ingresar un número.")
        return

    contraseña = generar_contraseña(longitud)
    print(f"\n🔑 Contraseña generada para {servicio}:\n{contraseña}\n")

    # Guardar archivo en la carpeta del usuario
    carpeta_usuario = os.path.expanduser("~")
    ruta = os.path.join(carpeta_usuario, "Mis_contraseñas.txt")

    guardar_contraseña(servicio, usuario, contraseña, ruta)

    print(f"📁 Contraseña guardada en: {ruta}")

if __name__ == "__main__":
    main()
