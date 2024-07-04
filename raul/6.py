import requests
from PIL import Image
from io import BytesIO

url = "https://images-ng.pixai.art/images/orig/662eb689-faf2-4e50-b361-20445d4a952f"

response = requests.get(url)
img_data = BytesIO(response.content)

imagen = Image.open(img_data)

ancho, alto = imagen.size

print(f"Ancho: {ancho}px, Alto: {alto}px")