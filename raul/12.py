def limpiar(str1:str, str2:str):
    out= ""
    for c in str1:
        if c not in str2:
            out += c
    return out
    
def eliminar(str1:str, str2:str):
    out1 = limpiar(str1,str2)
    out2 = limpiar(str2,str1)
            
    return (out1, out2)

print(eliminar("hola","señora"))