pi = 3.1416

# Pedir al usuario el radio del círculo
radio = float(input("Introduce el radio del círculo: "))

# Calcular el área y el perímetro
area = pi * radio**2
perimetro = 2 * pi * radio

# Mostrar los resultados
print(f"Área del círculo: {area:.2f}")
print(f"Perímetro del círculo: {perimetro:.2f}")