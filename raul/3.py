def fibo(n: int = 50):
    f = [0, 1]
    a = 0
    b = 1

    if (n < 1):
        print("Error: ingrese un número mayor que 0")

    if n == 1:
        print(f[0])
        return 0

    if n == 2:
        print(f)
        return 0

    for i in range(n-2):
        c = a + b
        a = b
        b = c
        f.append(c)
    print(f)

fibo()
