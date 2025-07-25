#funções com parametros
def saudacao(nome):
    print("Olá, " + nome + "!")
saudacao("Maria")

#===================================
#def imparPar(numero):
#    if numero % 2 == 0:
#    print(f"{numero} é par")
#    else:
#    print(f"{numero} é impar")
#
#imparPar(10)
#imparPar(27)
#===================================
def soma(num1, num2):
    print(num1 + num2)

def subtracao(num1, num2):
    print(num1 - num2)

def divisao(num1, num2):
    print(num1 / num2)

def multiplicacao(num1, num2):
    print(num1 * num2)

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

soma(n1,n2)
subtracao(n1, n2)
divisao(n1, n2)
multiplicacao(n1, n2)
#=============================================
def separar(lista):
    for item in lista:
        if item > 10:
            print(item, end="")

listaCriada = [21, 1, 2, 3, 4, 5, 6, 2, 3, 434, 5]
separar(listaCriada)

#==============================================
def cidade(parte1, parte2):
    print(parte1 + " " + parte2)

cidade("São", "Paulo")
cidade("Paulo", "São")

#==============================================
def medida(numero, referencia=60):
    if numero > referencia:
        print(f"{numero} é maior que {referencia}")
    else:
        print(f"{numero} é menor que {referencia}")
medida(40, 30)

#==============================================
def comida():
    nome = "arroz"
    nome = nome + " " "e pizza"
    print(nome)
comida()

#================================================
