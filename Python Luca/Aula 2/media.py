print("Exercicio 5")
nota1 = int(input("Digite a primeira nota: \n"))
nota2 = int(input("Digite a segunda nota: \n"))
nota3 = int(input("Digite a terceira nota: \n"))
media = nota1 + nota2 + nota3 / 3

if media >= 6 and media < 10:
    print("Aprovado!")

elif media >= 2 and media < 6:
    print("Recuperação!")

elif media >= 0 and media < 2:
    print("Reprovado!")

else:
    print("Nota fora do intervalo!")
