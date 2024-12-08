#Ejemplos de la función print()

print("Hola mundo")
print("Hola Mundo", "otra vez")
print("Son las", 9, "de la mañana")
print("El resultado de 3 * 4 es:", 3*4)

#Ejemplos de cadenas formateadas (f"")

print("El numero 15 en sistema decimal es %d , en sistema octal es %o, en el sistema hexadecimal es %x" % (15,15,15))

pi = 3.141592
r = 5
print(f"el radio de un circulo es {r} y el area de ése circulo es {pi * r ** 2: .2f}")

print(f"El radio de un circulo es (r) y el area de ese circulo es (pi * r ** 2: .2f)")
  # x = 5.4532
  # print(f"{x:.3f}")

#Impresión de caracteres especiales

print("La letra beta es: \n\t \u03B2 ")

#Caracteres de escape

print("Hola mundo", end = " ")
print("Otra vez", end = "\t")
print("Y Otra vez")