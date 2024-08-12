peso_engrane = 112 # peso de cada engrane en gramos

peso_cilindro = 75 # peso de cada cilindro en gramos

num_engranes = int(input("Ingrese el número de engranes vendidos: "))

num_cilindros = int(input("Ingrese el número de cilindros vendidos: "))

peso_total = num_engranes * peso_engrane + num_cilindros * peso_cilindro

print(f"El peso total del paquete que será enviado es {peso_total} gramos.")