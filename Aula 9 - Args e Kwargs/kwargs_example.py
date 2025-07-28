#Kwargs
#é um dicionário que permite passar um número variavel de argumentos nomeados
#para uma função. Ex:

def minha_funcao(**kwargs):
    for chave, valor in kwargs.items():
        print(f'{chave}: {valor}')

minha_funcao(nome='João', idade=30, cidade='São Paulo')

#============================================================================
def cadastro(nome, idade, *args):
    print(f'Nome: {nome}')
    print(f'Idade: {idade}')
    print(args)
    print(f'Profissão: ', end='')
    for prof in args:
        print(prof, end='')

cadastro("Agnaldo", 87, "carpinteiro", "lutador", "garçom")

#===============================================================================
def cadastro(nome, idade, *args):
    print(f'Nome: {nome}')
    print(f'Idade: {idade}')
    print(args)
    print(f'Profissão: ', end='')
    for prof in args:
        print(prof, end='')

cadastro("Agnaldo", 87, "carpinteiro",  "lutador",  "garçom")

#--------------------------------------------------------------------------------
def media(num1, num2, *args):
    print(args)
    print(sum(args)/len(args))

media(1,2,3, 4, 5)

notas = [9, 8.5, 10, 9.0, 5, 3, 10, 10]

def somarNotas(*args):
    print(args)
    print(sum(args))

#somarNotas(notas)
somarNotas(*notas)
#somarNotas()
#=====================================================================
def idades(**kwargs):
    print(kwargs)
    for nome, idade in kwargs.items():
        print(f'A idade de {nome} é {idade}')

idades(maria=5, isadora=20, pedro=14)

#======================================================================
def jogadas(nome, **kwargs):
    print(kwargs)
    for jogada in kwargs:
        print(kwargs[jogada])
        if kwargs[jogada] == 10:
            return f'{nome} ganhou!'
        return f'{nome} perdeu!'

print(jogadas("Marcelo", j1=9, j2=8, j3=10, j4=9, j5=6))

#=====================================================================
def apresentarNotas(**kwargs):
    print(kwargs)
    for aluno in kwargs:
        print(f'{aluno}: {kwargs[aluno]}')

notas = {'joao': 8, 'Carlos': 10, "Jessica": 5}

apresentarNotas(**notas)
