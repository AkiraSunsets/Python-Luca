# Exercício 1
def soma_todos(*args):
    return sum(args)

print("Exercício 1:", soma_todos(1, 2, 3, 4))  #


# Exercício 2
def retorna_dicionario(**kwargs):
    return kwargs

print("Exercício 2:", retorna_dicionario(nome="Kety", idade=20))  


# Exercício 3
def concatena_tudo(*args, **kwargs):
    return ''.join(str(x) for x in args) + ''.join(str(v) for v in kwargs.values())

print("Exercício 3:", concatena_tudo("Hello ", "World"))


# Exercício 4
def maior_valor(*args):
    return max(args)

print("Exercício 4:", maior_valor(4, 100, 23, 56))  


# Exercício 5
def media_kwargs(**kwargs):
    return sum(kwargs.values()) / len(kwargs) if kwargs else 0

print("Exercício 5:", media_kwargs(a=7, b=8, c=9))  
