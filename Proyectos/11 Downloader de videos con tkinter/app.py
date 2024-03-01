#Librerias usadas
from tkinter import * #https://docs.python.org/es/3/library/tk.html
from pytube import YouTube #https://pytube.io/en/latest/
import os #https://docs.python.org/es/3.10/library/os.html

#Creacion del display
root = Tk()
root.geometry('700x300')
root.resizable(0, 0)
root.title("Dowloader de videos de YouTube")

Label(root, text='Copia el link de tu video de youtube', font='Montserrat 15 bold').pack(pady=10)

#Label de entrada
link = StringVar()
link_label_frame = Frame(root)
link_label_frame.pack()
Label(link_label_frame, text='Pega el link aqui:', font='Montserrat 15 bold').pack(side=LEFT, padx=10)

#Entrada
entry_frame = Frame(root)
entry_frame.pack()
Entry(entry_frame, width=80, textvariable=link).pack(pady=10)

#Funcion encargada de la descarga y redireccionamiento a la carpeta descargas
def Descargar():
    url = YouTube(str(link.get()))
    video = url.streams.get_highest_resolution()  # Obtiene la mejor resolución disponible
    # Obtenemos la ruta de la carpeta Descargas en Windows
    download_path = os.path.join(os.path.expanduser('~'), 'Downloads')
    video.download(download_path)
    Label(root, text='DESCARGADO EN Descargas', font='Montserrat 15 bold').pack(pady=10)

#Boton salto accion descarga
Button(root, text='DESCARGAR', font='Montserrat 15 bold', bg='white', padx=2, command=Descargar).pack(pady=10)

root.mainloop()
