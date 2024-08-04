from unidecode import unidecode
import string

def eliminar_puntuacion(texto):
    return ''.join([caracter for caracter in texto if caracter not in string.punctuation])

def palindromo(txt:str):
    txt = txt.replace(" ","").lower() # Eliminar espacios y convertir a minusculas
    txt = unidecode(txt) # Eliminar tildes
    txt = eliminar_puntuacion(txt) # Eliminar puntuación
        
    if txt == txt[::-1]:
        return True
    return False

print(palindromo("Ana llevá al oso la avellana!"))
print(palindromo("Ola Ke asé tú?"))