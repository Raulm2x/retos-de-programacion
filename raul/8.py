"""
 * Crea un programa que cuente cuantas veces se repite cada palabra
 * y que muestre el recuento final de todas ellas.
 * - Los signos de puntuación no forman parte de la palabra.
 * - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
 * - No se pueden utilizar funciones propias del lenguaje que
 *   lo resuelvan automáticamente.
"""

def contar(frase:str):
    dicc = {}
    frase = frase.lower()
    frase = frase.split(" ")
    
    for palabra in frase:
        if palabra in dicc:
            dicc[palabra] += 1
        else:
            dicc[palabra] = 1
            
    for palabra, cantidad in dicc.items():
        print(f"{palabra}: {cantidad}")

contar("lol lolzalo lol laosl lozalo lolazo lol")