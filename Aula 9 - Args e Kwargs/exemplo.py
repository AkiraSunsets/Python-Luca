#Args
#é uma tupla que permite passar um número variavel de argumentos posicionais para uma função

def minha_funcao(*args):
    for arg in args:
        print(arg)
minha_funcao(1, 2, 3)
