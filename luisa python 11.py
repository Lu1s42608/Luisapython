precio_normal = 3.49 # precio de una barra de pan normal en pesos

descuento = 0.60 # descuento del 60% por no ser del día

barras_no_dia = int(input("Ingrese el número de barras de pan no del día vendidas: "))

costo_total_sin_descuento = barras_no_dia * precio_normal

descuento_aplicado = costo_total_sin_descuento * descuento

costo_final = costo_total_sin_descuento - descuento_aplicado

print(f"Precio habitual de una barra de pan: ${precio_normal:.2f} pesos")

print(f"Descuento aplicado por no ser del día: {descuento * 100}%")

print(f"Costo final total: ${costo_final:.2f} pesos")