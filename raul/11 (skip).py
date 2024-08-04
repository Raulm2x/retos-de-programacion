import re

texto = "Contactos: juan@example.com, maria@example.org"
resultados = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", texto)
print("Correos electrónicos encontrados:", resultados)
