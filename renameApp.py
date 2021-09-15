# Created: 2021-set-14 @ Rafael Inacio

import os
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
from tkinter.constants import X


class App():
    def __init__(self, parent):
        self.parent = parent
        self.window = tk.Toplevel()
        self.window.geometry('400x300')
        self.window.title('Rename files JAJAJAJ')
        self.window.protocol("WM_DELETE_WINDOW", self.parent.quit)

        # Buttons
        self.button = tk.Button(self.window, height=5, width=20, text="Rename all files in a  folder", command=self.app_rename_folder, )
        self.button.place(x=10, y=100)
        self.button2 = tk.Button(self.window, height=5, width=20, text="Rename files", command=self.app_rename_files)
        self.button2.place(x=240, y=100)


    def app_rename_folder(self):  

        path = filedialog.askdirectory()  # caminho para uma pasta com os arquivos
        if path:
            prefix = simpledialog.askstring('Choose a folder', 'Prefix')
            n = 0
            if prefix:
                for file_name in os.listdir(path):
                    source = os.path.join(path, file_name)
                    destination = os.path.join(path, prefix + file_name)
                    os.rename(source, destination)
                    n += 1
            # TRATAR ERROS
            messagebox.showinfo("Colcuído", f"{n} Arquivos minerad... renomeados com sucesso!") #
                
    def app_rename_files(self):

        files = filedialog.askopenfilenames()  # caminhos dos arquivos que deseja renomear
        if files:
            prefix = simpledialog.askstring('Coose files', 'Prefix')
            n = 0
            if prefix:
                for file_name in files:
                    source = file_name
                    folder = os.path.split(file_name)[0]
                    file = os.path.split(file_name)[1]
                    destination = os.path.join(folder, prefix + file)
                    os.rename(source, destination) 
                    n += 1 
            # TRATAR ERROS
            messagebox.showinfo("Colcuído", f"{n} Arquivos renomeados com sucesso!") # TRADUZIR

    
root = tk.Tk()
root.withdraw()
window1 = App(root)
root.mainloop()
