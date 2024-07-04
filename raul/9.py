def dec_bin(dec:int):
    num = dec
    bin = ""
    
    if dec < 1:
        if dec == 0:
            bin += f"{0}"
        else:
            print("Error: debes ingresar un entero positivo")
            return 0

    while dec > 0:
        bin += f"{dec % 2}"
        dec = dec//2
    
    bin = bin[::-1]
    
    print(f"{num} en binario es {bin}")      
    return bin
 
dec_bin(-20)