while True:

    nombre0 = str(input("Nombre(s):\t"))
    if nombre0.isidentifier():
        break
    else: 
        print("Debes ingresar solo letras y espacios con _ ó - ")
while True:
    
    apellido_p = input("Apellido Paterno:\t")
    if apellido_p.isidentifier():
        break
    else:
        print("Debes ingresar solo letras")
while True:
    
    apellido_m = input("Apellido Materno:\t")
    if apellido_p.isidentifier():
        break
    else:
        print("Debes ingresar solo letras")
while True:

    edad = (input("Edad:\t"))
    if edad.isnumeric():
        break
    else:
        print("Debe ser un número")
while True:

    peso = (input("Peso(Kg):\t"))
    if peso.isdigit():
        break
    else:
        print("Debe ser un número")
    
while True:

    estatura = (input("Estatura(en centrimetros):\t"))
    if estatura.isdigit():
        break
    else:
        print("Debe ser un número")

peso = float(peso)
estatura = float(estatura)
nombre_c = str(f"{apellido_p} {apellido_m} {nombre0}")
estaturaM = estatura / 100
imc = float(peso / estaturaM **2)

print("Nombre:\t" +nombre_c.title())
print(f"{"Edad: "}{edad}{" años"}")
print(f"{"Peso: "}{peso}{" Kg"}")
print(f"{"Estatura: "}{estaturaM}{" Mts"}")
print("El Indice de Masa Muscular es: {:.2f}".format(imc))