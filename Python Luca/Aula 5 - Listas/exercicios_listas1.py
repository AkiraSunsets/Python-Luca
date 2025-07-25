print("Imprimir todos os elementos de uma lista com for Escreva um programa que receba uma lista de nomes e imprima cada nome usando um loop for.")
nomes = ["Ana", "Bruno", "Carla", "Renata"]
for nome in nomes:
    print(nome)
#=======================================================================================================================
print("Soma dos elementos de uma lista com for Escreva um programa que receba uma lista de números e retorne a soma de todos os elementos usando um loop for.")
lista = [1,2,3,4,5,6]
soma = 0
for num in lista:
    soma += num
print(soma)
#=======================================================================================================================
print("Multiplicação de todos os elementos de uma lista com for Escreva um programa que receba uma lista de números e retorne o resultado da multiplicação de todos os elementos usando um loop for.")
lista = [1,2,3,4]
resultado = 1
for num in lista:
    resultado *= num
print(resultado)
#=======================================================================================================================
print("Contagem de vogais em uma lista de palavras com while Crie um programa que receba uma lista de palavras e retorne a quantidade total de vogais em todas as palavras usando um loop while.")
palavras = ["something", "anything", "somebody", "anybody"]
vogais = "aeiouAEIOU"
total_vogais = 0
i = 0

while i < len(palavras):
    palavra = palavras[i]
    for letra in palavra:
        if letra in vogais:
            total_vogais += 1
i += 1

print(total_vogais)
#=======================================================================================================================
print("Verificar se um elemento está presente na lista com while Crie um programa que receba uma lista de números e um número específico, e verifique se o número está presente na lista usando um loop while.")
numeros = [1, 2, 3, 4, 5]
numero_especifico = 3
encontrado = False
i = 0
while i < len(numeros):
 if numeros[i] == numero_especifico:
     encontrado = True
     break
 i += 1
print(encontrado)  # Saída: True
#=======================================================================================================================
'''Crie duas listas, uma para o carrinho do supermercado que irá receber produtos comprados e outra 
para os preços dos produtos. Utilizando um loop, preencha as listas com 5 produtos e 5 preços, 
recebendo estes dados do usuário (input). Por fim, some os preços, imprima o valor total e os
produtos do carrinho.'''
listaCarrinho = []
listaPrecos = []
contProdutos = []
valorTotal = 0
produto = ''

while contProdutos < 5: #loop acrescentar 5 itens nas listas
    produto = input("produto: ")
    listaCarrinho.append(produto)
    preco = float(input("Preço: "))
    listaPrecos.append(preco)
    contProdutos += 1

for id in range(0,5)
    valorTotal += listaPrecos[id]

print(f'Produtos comprados: {listaCarrinho}')
print(f'Valor total: R${valorTotal}')
#===========================================================================================================================
