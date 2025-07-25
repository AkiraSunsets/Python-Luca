print("desafio - número primo")

num = int(input("Digite um número: \n"))

if num > 1:
    for i in range(2, num): #range cria um intervalo de 2 até o número que ele digitar
        if (num % i) == 0:
            print("Não é primo")
            break
    else:
        print("É primo")

else:
    print("Não é primo")
