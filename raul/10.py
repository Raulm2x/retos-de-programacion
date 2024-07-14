d_morse = {
    "A": "._",
    "B": "_...",
    "C": "_._.",
    "CH": "____",
    "D": "_..",
    "E": ".",
    "F": ".._.",
    "G": "__.",
    "H": "....",
    "I": "..",
    "J": ".___",
    "K": "_._",
    "L": "._..",
    "M": "__",
    "N": "_.",
    "Ñ": "__.__",
    "O": "___",
    "P": ".__.",
    "Q": "__._",
    "R": "._.",
    "S": "...",
    "T": "_",
    "U": ".._",
    "V": "..._",
    "W": ".__",
    "X": "_.._",
    "Y": "_.__",
    "Z": "__..",
    "0": "_____",
    "1": ".____",
    "2": "..___",
    "3": "...__",
    "4": "...._",
    "5": ".....",
    "6": "_....",
    "7": "__...",
    "8": "___..",
    "9": "____.",
    ".": "._._._",
    ",": "__..__",
    "?": "..__..",
    '"': "._.._.",
    "/": "_.._.",
}

d_letras = {v: k for k, v in d_morse.items()}


def a_morse(texto: str):
    """Convierte un texto a código morse. 
    **Muchos caracteres especiales no son soportados**"""
    texto = texto.upper()
    texto = texto.split(" ")
    texto_morse = []

    for palabra in texto:
        palabra_morse = ""
        for index, caracter in enumerate(palabra):
            spc = " " if index < len(palabra)-1 else ""
            if caracter in d_morse:
                palabra_morse += f"{d_morse[caracter]}{spc}"
            else:
                palabra_morse += f"*{spc}"
        texto_morse.append(palabra_morse)

    txt = ""
    for index, palabra_morse in enumerate(texto_morse):
        spc = "  " if index < len(texto_morse)-1 else ""
        txt += f"{palabra_morse}{spc}"

    print(txt)
    return txt


def a_texto(morse: str):
    """Convierte código morse a texto normal."""
    texto_morse = morse.split("  ")
    texto = []

    for palabra_morse in texto_morse:
        palabra = ""
        palabra_morse = palabra_morse.split(" ")

        for codigo in palabra_morse:
            if codigo in d_letras:
                palabra += f"{d_letras[codigo]}"
            else:
                palabra += "*"
        texto.append(palabra)

    txt = ""
    for index, palabra in enumerate(texto):
        spc = " " if index < len(texto)-1 else ""
        txt += f"{palabra}{spc}"

    print(txt)
    return (txt)


txt = a_morse("hice un codigo que convierte de texto a morse y de morse a texto, sera que me quedo genial?")
a_texto(txt)
