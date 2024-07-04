def fibo(n: int = 50) -> list:
    """Devuelve los n primeros números de la serie de Fibonacci (Devuelve 50 por defecto)"""
    
    # Se inicia la serie con los dos primeros elementos
    f = [0, 1]
    a = 0
    b = 1

    #Casos especiales
    if (n < 1):
        print("Error: ingrese un número mayor que 0")

    if n == 1:
        print(f[0])
        return 0

    if n == 2:
        print(f)
        return 0

    # Se encuentran los n primeros términos
    for i in range(n-2):
        c = a + b
        a = b
        b = c
        f.append(c)
        
    print(f)
    
    return(f)

fibo()
