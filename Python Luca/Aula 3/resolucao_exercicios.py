print("Imprimir os números de 1 a 5:")

numero = range(1,6)
for number in numero:
    print(number)
#==============================================================
print("Calcular a média de uma lista de números")
lista = [1,2,3,4,5]

soma = 0
for item in lista:
    soma = soma + item

media = soma / len(lista)
print(media)
#==============================================================
print("Imprimir cada caractere de uma string em uma linha separada:")
word = "example"
for caracter in word:
    print(caracter)
#===============================================================
print("Verificar se um número é primo")
num = int(input("Digite um número: "))

primo = True

for i in range(2, num):
    if num % i == 0:
        primo = False
        break
if primo:
    print(num, "é primo")

else:
    print("não é primo")
#===============================================================
print("Criar uma lista com o quadrado de cada número em outra lista:")
numeros = [1,2,3,4,5]
quadrados = []
for numero in numeros:
    quadrados.append(numero ** 2) #numero vezes ele mesmo.
print(quadrados)
#================================================================
print("desafio - Faça um programa que calcule a soma dos divisores de um número inteiro definido pelo usuário.Ex: Se o usuário escolheu 10, temos 1 + 2 + 5 + 10 = 18")

soma = 0 #inicializa variavel soma
numero = int(input("Digite um número: \n"))

for num in range(1,num+1): #para cada num dentro do intervalo 1 e numero +1 faça
    if num % 1 == 0:      # se o resto da divisão de número por num for zero faça
        soma = soma + num  #atualiza soma com num
print(soma)

#================================================================
print("Faça um programa que imprima os n primeiros múltiplos de 5, sendo n definido pelo usuárioEx: Se o usuário escolheu n=3, será impresso 5,10,15.")
num = int(input("Digite o numero multiplo de 5 que deseja: \n"))

for num in range(1,num): #para cada num no intervalo de 1 a numero+1 faça:
    print(f'{5 * num}') #imprime 5 vezes num
#================================================================
