numero = int(input("Ingrese un número entero positivo: "))
if numero <= 0:
  print("El número ingresado no es válido. Debe ser un entero positivo.")
else:
 impares = []
for i in range(1, numero + 1, 2):
    impares.append(str(i))
    print(", ".join(impares))