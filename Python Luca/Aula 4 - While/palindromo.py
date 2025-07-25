print("palindromo")

n1 = 999
res = 0
while n1 != 99:
    n2 = n1

    while n2 != 99:

        numero = str(n1 * n2)
        invert_numero = numero[::--1]
        if invert_numero == numero:
            num = int(numero)
            if res < num:
                res = num
                n2 -= 1
            else:
                n2 -= 1
        else:
            n2 -= 1
        n1 -= 1
    print(res)
