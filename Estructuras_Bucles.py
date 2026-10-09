'''numeros = [1,2,3]
for i in range(10, 101, 10):
    print(i)'''

'''estructuras = ["pilas", "colas", "listas"]
for i, nombre in enumerate(estructuras):
    print(f"Indice: {1} Valor: {nombre}")'''

'''suma = 0
contar = 0
for i in range(1,101):
    if i % 2 != 0:
        suma += i
    else:
        contar += 1
print(f"Suma de numeros impares del 1 al 100: {suma} y hay {contar} impares")'''

'''embutidos = ["salchicha", "chorizo", "mortadela"]
for i in (embutidos):
    if i == "salchicha":
        print("Para las tiendas")
    elif i == "chorizo":
        print("Para el restaurante")
    else:
        print("Para la cena")'''

'''numero = int(input("Ingrese el numero de la tabla que desea visualizar: "))
mul = 0
if numero <= 100:
    for i in range(1,11):
        mul = numero * i
        print(f"{numero} * {i} = {mul}")
else:
    print("numero entre 1 y 100")'''

'''datos = {'nombre':'Alejandra','nota':4.2}
for clave, valor in datos.items():
    print(f"{clave} -> {valor}")'''

'''pisos = ['soporte','tesoreria','administrativo','gerencia']

for i in (pisos):
    if i == "administrativo":
        print(i)
        break
    print(i)'''

'''for i in range(5):
    numero = int(input("Ingrese un numero: "))
    if numero == 3:
        print(numero)
        break
    print(numero)'''

'''edad = int(input("Ingrese su edad: "))
if edad > 20:
    for i in range(2):
        gusto = input("Escriba su gusto musical: ")
        if gusto == "rock":
            print("Te ganaste una boleta para un concierto")
            break'''

'''bandera = True

while bandera:
    n = int(input("Digite un numero del 1 al 10: "))
    if n == 2:
        bandera = False'''

'''activo = True
total, contador = 0, 1

while activo:
    total += contador
    contador += 1
    print(contador)
    if contador > 5:
        activo = False'''

'''opc = 0
while opc != 3:
    print("-----MENU-----")
    print("1: Saludar")
    print("2: Ingresar")
    print("3: Salir")
    opc = int(input("Digite la opcion: "))
    if opc == 1:
        print("Hola")
    elif opc == 2:
        print("Ingrese")
    elif opc == 3:
        print("Hasta pronto")
    elif opc > 3 or opc == 0:
        print("Digite un numero del 1 al 3")'''

'''while True:

    print("\n==== MENU ====")
    print("1. Mostrar numeros aleatorios")
    print("2. Mostrar tabla de multiplicar")
    print("3. Saludar")
    print("4. Salir")

    opcion = int(input("Digite una opcion segun el menu: "))

    if opcion == 1:
        for i in range(1,11):
            print(f"- {i}")

    elif opcion == 2:
        tabla = int(input("Digite el numero de la tabla de multiplicar: "))
        for i in range(1,11):
            print(f"- {tabla} * {i} = {tabla*i}")

    elif opcion == 3:
        nombre = input("Ingrese su nombre: ")
        print(f"Hola: {nombre}")

    elif opcion == 4:
        print("Hasta pronto... 😊")
        break

    else:
        print("Digite una opcion valida 😒")'''

'''Bandera = True
while Bandera:

    print("\n==== SISTEMA ACADEMICO ====")
    print("1. Registrar materia y nota")
    print("2. Promediar notas")
    print("3. Pierde o pasa la materia")

    opc = int(input("Digite la opcion que desea: "))

    if opc == 1:
        materia = input("Que materia desea registrar?: ")
        print(materia)
        numnotas = int(input("Cuantas notas quiere registar?: "))
        for i in range (1,numnotas + 1):
            nota = int(input(f"Nota numero {i}: "))
            print(nota)'''

'''def saludar (nombre):
    #Esta funcion recibe un nombre personalizado y lo muestra en la consola
    print(f"Hola {nombre}. Bienvenido@")

saludar("Jeremy")'''

'''def suma(a,b):
    suma = a + b
    print(f"El resultado de {a} + {b} es: {suma}")

suma (5,7)'''

'''class calculadora:
    def sumar(self, a,b,c):
        return a+b+c

calc = calculadora()
resul = calc.sumar(8,2,12)
print(f"Resultado: {resul}")'''

'''class Estudiante():
    def datos(self, nombre, apellido, edad, genero):
        print(f"Se realizo el registro de: {nombre} y {apellido} en el sistema")
        return edad

est = Estudiante()
eda = est.datos("Maria", "Diaz", 3, "Femenino")
if eda >= 18:
    print("Mayor de edad")
else: 
    print("Menor de edad")'''

'''class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)

r1 = Rectangulo(4,5)
r2 = Rectangulo(5,8)

print(r1.area(), r1.perimetro())
print(r2.area(), r2.perimetro())'''

'''class Usuario:

    def __init__(self, username, password):

        self.username = username
        self.password = password

    def verificar_password(self, password2):
        if password2 == self.password:
            print("Contraseña correcta")
        else:
            print("Contraseña incorrecta")

us1 = Usuario("Admin", "123")
us1.verificar_password("1234")'''

'''pila = []

pila.append("Ana")
pila.append("Carlos")
pila.append("Maria")
pila.append("Tania")

print(f"Elementos de la pila: {pila}")

salida = pila.pop()
print(f"El elemto que sale es: {salida}")

print(f"Elementos de la pila: {pila}")

print(f"Elementos de la pila: {pila[0]}")

print(f"Elementos de la pila: {pila[-1]}")'''

pila = [] 

while True:
    print("\n ----- MENU -----")
    print("1. Agregar Elementos a la pila")
    print("2. Eliminar elementos de la pila")
    print("3. Ver elemetos de la pila")
    print("4. Mostrar la pila")
    print("5. Salir")

    opcion = int(input("Ingrese una opcion "))

    if opcion == 1:
        cantidad = int(input("Ingrese cuantos elementos desee agregar: "))
        for i in range (cantidad):
            dato = input(f"Ingrese el elemento {i+1} a agregar:")
            pila.append(dato)
            print(f"Elemento agregado {dato} correctamente")
        print(f"Los elementos agregados son: {pila}")

    elif opcion == 2:
        if len(pila) > 0:
            elem = pila.pop()
            print(f"Elemento eliminado: {elem}")
        else:
            print("La pila esta vacia")

    elif opcion == 3:
        if len(pila) > 0:
            print(f"El elemento superior es: {pila[-1]}")
        else:
            print("\n La pila esta vacia")

    elif opcion == 4:
        if len(pila) > 0:
            print(f"Elementos de la pila: {pila}")
        else:
            print("\n La pila esta vacia")

    elif opcion == 5:
         print(f"Saliendo del sistema...")
         break

    else:
         print("Opcion invalida")