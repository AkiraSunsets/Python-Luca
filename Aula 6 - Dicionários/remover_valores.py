#print("Exercicio 3 - Dado o dicionário abaixo, remova a chave "idade".
#pessoa = {"nome": "Carlos", "idade": 40, "cidade": "Belo Horizonte"}")
pessoa = {
    "nome" : "Carlos",
    "idade" : 40,
    "cidade" : "Belo Horizonte"
}
del pessoa["cidade"]
print(pessoa)
