#print("Exercicio 2 - Dado o dicionário abaixo, adicione a chave "profissão" com o valor "engenheiro".
#pessoa = {"nome": "Maria", "idade": 30, "cidade": "Rio de Janeiro"}")

pessoa = {
    "nome":"Maria",
    "idade":30,
    "cidade":"Rio de Janeiro"
}

novo_pessoa = {"profissao":"engenheiro"}
pessoa.update(novo_pessoa)
print(pessoa)
