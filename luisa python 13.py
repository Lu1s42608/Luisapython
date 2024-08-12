contrasena_guardada = "Hola123" # Ejemplo de contraseña almacenada

contrasena_usuario = input("Ingrese la contraseña: ")

if contrasena_usuario.lower() == contrasena_guardada.lower():

   print("¡La contraseña es correcta!")

else:

   print("La contraseña ingresada es incorrecta.")