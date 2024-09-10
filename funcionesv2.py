print("Mas sobre funciones")

print("")
#Aqui se escriben las funciones
def suma_ab(a,b):
    s=a+b
    return s

def resta_cd(c,d):
    r1=c-d
    return r1

def mul_ef(e,f):
    r2=e*f
    return r2

def div_gh(g,h):
    r3=g/h
    return r3
#Llamadas a funciones
print("Calculando suma")
n1=int(input("Ingresa el primer numero "))
n2=int(input("Ingresa el segundo numero "))
suma=suma_ab(n1,n2)
print(f"La suma de {n1} + {n2} es {suma}")
print("----------------------------------------------")
print("Calculando resta")
n3=int(input("Ingresa el primer numero "))
n4=int(input("Ingresa el segundo numero "))
resta=resta_cd(n3,n4)
print(f"La resta de {n3} - {n4} es {resta}")
print("----------------------------------------------")
print("Calculando multiplicacion")
n5=int(input("Ingresa el primer numero "))
n6=int(input("Ingresa el segundo numero "))
mul=mul_ef(n5,n6)
print(f"La multiplicacion de {n5} * {n6} es {mul}")
print("----------------------------------------------")
print("Calculando division")
n7=int(input("Ingresa el primer numero "))
n8=int(input("Ingresa el segundo numero "))
div=div_gh(n7,n8)
print(f"La division de {n7} / {n8} es {div}")