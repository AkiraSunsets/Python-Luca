print("Encontrar o primeiro número da sequencia de fibonacci maior que 100")
a,b = 0, 1
while a <= 100:
    a, b = b, a + b
print("O primeiro número da sequencia de Fibonacci maior que 100 é", a)
