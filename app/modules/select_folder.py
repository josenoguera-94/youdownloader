from tkinter import filedialog as fd
import tkinter as tk
import os


def select_dir():
    """ejecuta una ventana que permite seleeccionar
    la carpeta o ruta destino del archivo"""

    title = "Selecciona la ubicación de descarga"
    path = "./app/static/img/icon_64px.png"
    path = os.path.abspath(path)

    root = tk.Tk()
    root.title(title)
    icon = tk.PhotoImage(file=path)
    root.iconphoto(False, icon)
    root.focus_force()
    root.attributes("-alpha", 0)
    root.lift()
    root.attributes("-topmost", 1)
    root.attributes("-topmost", 0)
    root.update()

    dirname = fd.askdirectory(parent=root, title=title, initialdir="/")
    root.destroy()

    return dirname
