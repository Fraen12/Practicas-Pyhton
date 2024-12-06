# texto_variado = "Palabra 123 +¿-#"
# print(type(texto_variado))

# #Podemos utilizar comillas triples para que el texto se muestre como la cadena que hemos escrito

# print("""
# Funcionamiento de \
# programa: (opciones)
#     1- Para acceder a opciones
# 2- Para salir 
# """)
# ###################################################################################

# #Subscripting e indexado 

# texto = "Python"

# print(texto[0])
# print(texto[5])
# print(texto[-1])
# print(texto[-6])

# #error fuera de rango (no podemos acceder a una posicion que no existe)
# # print(texto[6])
# # print(texto[-7])

# letra = texto[0]
# print(letra)

# # texto[0] = "P" Error ya que no se puede redefinir una cadena de texto 

# # letra = "p"
# print(letra)

# texto_compuesto = letra + texto[1] # Concatenación 
# print(texto_compuesto)

##################################################################################

# Slicing o Substrining 

# texto = "Pyton"
# print(texto[0:3])
# print(texto[0:-3])
# print(texto[0:-2])
# print(texto[2:])
# print(texto[:2])

# print(texto[-3::-1])
# print(texto[::-1])

# print(texto[1:50])
# print(texto[0:0])

################################################################################

#Cadenas y Formatos 

# texto = "Hola mundo! Buenastardes"
# print(texto.lower())
# print(texto.upper())
# print(texto.capitalize())
# print(texto.title())
# print(texto.swapcase())

# texto = texto.upper()
# print(texto)

print("{} + {} = {}" .format(2, 3, 2 + 3))
print("{} + {} = {}" .format("Hola", "Mundo", "Hola Mundo"))
print("{:.3f} + {:.4f} = {}" .format(2, 3, 2 + 3))
print("{1} + {0} = {2}" .format(2, 3, 2 + 3))
print("{1} + {0} = {2}" .format("Hola", "Mundo", "Hola Mundo"))
print("{:d} = {:b} = {:o} = {:x}" .format(15, 15, 15, 15))
 
# dir(str) metodos
