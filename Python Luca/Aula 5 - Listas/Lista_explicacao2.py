lista1 = list("0i")
print(lista1) #transformou em lista lista com caractere separado
#============================================================
lista2 = list("123456")
print(lista2)
#===========================================================
listaNova = []
for numero in range(1,11):
    listaNova.append(numero) #incluir cada elemento dentro do [] vazio
print(listaNova)
#==========================================================
listaNova2 = list(range(1,11))
print(listaNova2)
#==========================================================
#Obter indices da lista
jogos = ['sonic','Super Mario', 'GTA', 'GoW', 'PES']
for indice, jogo in enumerate(jogos):
    print(jogos.index('Super Mario'))

lista = [1,2,3,4,5,6,2,3,3,3]
print(lista.index(5,2,8))
#============================================================
lista5 = ['cachorro','amarelo','a']
animal,cor,letra = lista5
print(animal)
print(letra)
print(cor)
#===========================================================
lista12 = [1,2,3,4,5,6,7,8,9]

print(sum(lista12)) #Retorna a soma dos elementos
print(max(lista12))#Retorna o maior dos elementos
print(min(lista12))#Retorna o menor dos elementos
#============================================================
listaPlana = [1.22, 2.000888, 9.8888888, 1]
for elemento in listaPlana:
    print(round(elemento))
#============================================================
listaPessimista = [-1,-2,-3,-50,-100]

for numero in listaPessimista:
    print(abs(numero))
#============================================================
lista22 = [1,2,3]
print(lista22)
lista23 = lista22.copy()
print(lista23)

lista23.append(11)
print(lista22)
print(lista23)
#============================================================
