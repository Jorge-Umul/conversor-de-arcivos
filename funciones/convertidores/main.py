from  explorador_de_archivos import abrir_archivos
import convertir_pngajpg as fcp
"""este main sera la parte mas importante por que aqui mandare todas las funciones de mi app"""

print("""
    Hola usuario, esta es una aplicacion de consola creada por jorgais!!
        ¿Que quieres hacer?

        -cambiar de formato de imagenes
            opcion 1. -png convertir a jpg

            opcion 2. -jpg a png

""")


ingreso=input("ingresa lo que quieres hacer")

#convercion a png a jpg
if ingreso == "1":
    print("indica que imagen quieres cambiar de formato")
    ventana= abrir_archivos.abrir_archivo()
    imagen= fcp.convercion_jpg(ventana)
    print(f"tu archivo se escuentra en esta ruta: {ventana} ")

elif ingreso == "2":
    print("indica que imagen quieres cambiar de formato")
    ventana= abrir_archivos.abrir_archivo()
    imagen= fcp.convercion_pgn(ventana)
    #print(f"tu archivo se escuentra en esta ruta: {ventana} ")
