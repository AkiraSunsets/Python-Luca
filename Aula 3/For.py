#for elemento in sequencia: #sintaxe

#exemplo

frutas = ["maça", "banana", "laranja"]
for fruta in frutas:
    print(fruta)

nome = "Akirazinha"
print(nome[0:3])

nome = "Akirazinha"
#print(nome[1,2,5,True,"sim")

numero = range(2,10) #cria um intervalo de 2 a 9

intervalo_num = range(3,11) #valores de 3 a 10
for shrek in intervalo_num:
    print(shrek)

seriado = "Everybody hates Chris"
for letra in seriado:
    print(letra, end=".") #end coloca na mesma linha, o . separa cada caracter, é possivel deixar esse espaço em branco tbm

#Aplicações com Range()
#Complemento:
# O range () pode ser utilizado por diversas formas:
# a) range(2,10) #  Cria uma sequencia de 2 a 9
# b) range(10) #cria uma sequencia de 0 a 9
# c) range(-4, 5) #cria uma sequencia de -4 a 4
# d) range(3,19,3) #cria uma sequencia de 3 a 18 ao passo 3

print("numeros pares dentro de uma sequencia")

for num in range(2,20):
    if num % 2 == 0:
        print(num)

fruta = "abacate"
valor = range(1,4)
for letra in fruta:
    if letra == "a": #se a letra for a
        for num in valor:
            print("Achei a letra a")



string = "abcdefghijklmnop"

for letra in string:
    print(letra, end="/")
    if letra == "g":
        break


string = "abcdefghijklmnop"

#for letra in string:
   # print(letra, end="/"):
       # continue


heroi = "batman"

for valor in enumerate(heroi):
    print(valor, end=",")

for contador,letra in enumerate(heroi):
    print(f"A {contador+1} letra e: {letra}")



