#Sobre as chaves
#Devem ser unicas
#Podem ser de qualquer tipo

#Sobre os dados:
#podem ser duplicados


times_futebol = {"RJ":"Flamengo","SP":"Corinthians"}
print(times_futebol.get("RJ")) #buscar valor dentro da chave ex: flamengo


times_futebol = {"RJ":"Flamengo","SP":"Corinthians"}
print(times_futebol.get("BH", "chave inexistente")) #quando o

times_futebol = {"RJ":"Flamengo","SP":"Corinthians"}
print("BH" in times_futebol) #Retorna true ou false se não existir

#======================================
print("None")

#Utilizado para declarar uma variavel que vc não sabe o tipo

dado = None
print(type(dado))
dado = "s"
print(type(dado)) #mostra o tipo do dado

#=======================================================
#exemplos dicionario

sagas = {
    (1,2):"HP",
    (3,4):"PJ",
    (5,6):"JV"
}

sagas[(7,8)] = "MR"
sagas[(1,2)] = "Digimon"
print(sagas) #define os dados do dicionario


#segunda forma

sagas = {
    (1,2):"HP",
    (3,4):"PJ",
    (5,6):"JV"
}

dado_novo = {(7,8):"MR"}
sagas.update(dado_novo) #atualizar dado
sagas.update({(1,2):"Digimon"})
print(sagas)

#====================================================
#remover itens do dicionario

pokemon = {
    "Agua" : "Squirtle",
    "Fogo" : "Chamander",
    "Grama" : "Bulbassauro"
}

dado = pokemon.pop("Agua")
print(dado)
print(pokemon)
#o metodo pop serve para retornar o elemento anterior

#===============================================
pokemon = {
    "Agua" : "Squirtle",
    "Fogo" : "Chamander",
    "Grama" : "Bulbassauro"
}

del pokemon["Agua"] #apagara o dado
print(pokemon)
