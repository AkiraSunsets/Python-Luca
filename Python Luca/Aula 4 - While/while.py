print("While")

#exemplo

i = 1
while i <= 5:
    print(i)
    i += 1
#(imprime lista)

#======================
x = True
while x:
    print("Estou rodando")
    x = False #quebra o loop do código

#=======================
pedido = ''

while pedido != "quero sair":
    pedido = input("Você não vai sair: ")
    #loop infinito

#=======================
contador = 0

while contador < 9:
    print(contador,end='')
    contador = contador + 1
    if contador == 5:
        continue  #ou break, irá sair instantaneamente do loop

#=========================
contador = 0

while contador < 9:
    print("sla")
    break

#=========================

