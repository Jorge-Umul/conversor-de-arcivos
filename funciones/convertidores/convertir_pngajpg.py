
from PIL import Image

#convertidor de png a jpg

def convercion_jpg(ruta):
    imagen1= Image.open(ruta )
    im= imagen1.convert('RGB')
    im.save(f"{ruta}.jpg")
    return im
def convercion_pgn(ruta):
    imagen1= Image.open(ruta)
    im= imagen1.convert('RGB')
    path= ruta
    print(path)
    #im.save(f" {ruta}.png")   


  





