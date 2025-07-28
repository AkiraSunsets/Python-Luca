#Args e Kwargs

#Args
#é uma tupla que permite passar um número variavel de argumentos posicionais para uma função

def minha_funcao(*args):
    for arg in args:
        print(arg)
minha_funcao(1, 2, 3)


#Kwargs
#é um dicionário que permite passar um número variavel de argumentos nomeados
#para uma função. Ex

def minha_funcao(**kwargs):
    for chave, valor in kwargs.items():
        print(f'{chave}: {valor}')

minha_funcao(nome='João', idade=30, cidade='São Paulo')
