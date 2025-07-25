print("Exercicio 3")

idade = int(input("Digite a sua idade: \n"))

if idade < 13:
    print("Criança")

elif idade < 18:
    print("Adolescente")

elif idade < 60:
    print("Adulto")

elif idade >= 60:
    print("Idoso")

else:
    print("")
