print("Exercicios")

print("Imprimir os números de 1 a 5")
i = 1
while i <= 5:
    print(i)
    i += 1
#(imprime lista)
#=====================================
print("Calcular a soma dos números de 1 a 10")
soma = 0
i = 1
while i <= 10:
    soma += i
    i += 1

print("A soma dos números de 1 a 10 é: ", soma)
#====================================
print("imprimir os 5 numeros pares")
i = 1
contador = 0
while contador < 5:
    if i % 2 == 0:
        print(i)
        contador += 1
    i += 1
#====================================
print("Calcular o fatorial de um número")
numero = 5
fatorial = 1
i = 1
while i <= numero:
    fatorial *= i
    i += 1
print("O fatorial de", numero, "é", fatorial)

#====================================
print("Encontrar o primeiro número da sequencia de fibonacci maior que 100")
a,b = 0, 1
while a <= 100:
    a, b = b, a + b
print("O primeiro número da sequencia de Fibonacci maior que 100 é", a)
#====================================
