"""
 * Crea una única función (importante que sólo sea una) que sea capaz
 * de calcular y retornar el área de un polígono.
 * - La función recibirá por parámetro sólo UN polígono a la vez.
 * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
 * - Imprime el cálculo del área de un polígono de cada tipo.
"""
from time import sleep

def validar(entrada:str):
    try:
        entrada = float(entrada)
        return True
    except:
        return False

def area(poligono:str)->float:
    print("\n")
    
    if (poligono == "Triángulo") | (poligono == "Rectángulo"):
        while True:
            base  = input("base: ")
            altura  = input("altura: ")
            if validar(base) & validar(altura):
                break
            print("Valores ingresados no válidos\n")
        if poligono == "Rectángulo":
            print(f"Área del rectángulo = {float(base) * float(altura):.2f}")
        else:
            print(f"Área del triángulo = {(float(base) * float(altura))/2:.2f}")
            
    if poligono == "Cuadrado":
        while True:
            lado  = input("lado: ")
            if validar(lado):
                break
            print("Valor ingresado no válido")
        print(f"Área del cuadrado = {float(lado)**2:.2f}") 
    
    sleep(5)
    print("\n")
    
while True:
    menu = input("Escoge un polígono:" + "\n" + "1. Triángulo" + "\n" + "2. Cuadrado" + "\n" + "3. Rectángulo" + "\n" + "4. Salir" + "\n" + "-> ")
    
    if menu == "1":
        area("Triángulo")
    elif menu == "2":
        area("Cuadrado")
    elif menu == "3":
        area("Rectángulo")
    elif menu == "4":
        break
    else:
        print("Opción inválida\n")
    