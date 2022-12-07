n1 = int(input("digite um numero : "))
n2 = int(input("digite um segundo numero :"))

print("1 - soma")
print("2 - subtrair")
print("3 multiplicar")
print("4 -dividir")

op= int(input("digite a operaçao desejada :"))

def somar(n1,n2):
    return n1 + n2    

def subtrair(n1,n2):
    return n1 -n2

def multiplicar(n1,n2):
    return n1 * n2


def dividir(n1,n2):
    return n1 / n2


if op == 1:
    print(somar(n1,n2))


if op == 2:
    print(subtrair(n1,n2))


if op == 3:
    print(multiplicar(n1,n2))


if op == 4:
    print(dividir(n1,n2))
