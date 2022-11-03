from tkinter import *
from tkinter import filedialog
import os

#clase para abrir el explorador de archivos
class abrir_ventana:
    def ventan():
        ventana=Tk()
        ventana.geometry("100x100")
        ventana.mainloop()
        



class abrir_archivos:       
    def abrir_archivo():
        ventana1=abrir_ventana.ventan()
        boton= Button(text="abrir explorador de archivos", command=ventana1)
        boton.pack()
        filepath = filedialog.askopenfilename()
        ruta= os.path.abspath(filepath)
        return ruta 
    def localizacion():
        pass








        
    
   


   

 





    

