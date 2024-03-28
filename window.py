import tkinter as tk
from tkinter import filedialog, messagebox

from rename_logic import rename

root = tk.Tk()
root.title("MSC Renamer")
root.geometry("300x250")
root.resizable(False, False)
root.configure(bg="dimgray")

class Rename:
    def __init__(self):
        self.create_widgets()

    def create_widgets(self):
        self.label1 = tk.Label(root, text="Выбери папку,\n чтобы изменить файлы.", font=('Arial', 15, 'bold'), bg="dimgray", fg="white")
        self.label1.pack(pady=(14, 0))
        
        self.button1 = tk.Button(root, text="Обзор", command=self.select_directory, width=7, height=3, bg="dimgray", fg="white", font=('Arial', 12, 'bold'))
        self.button1.pack(pady=(28, 0))


    def select_directory(self):
        self.dir = filedialog.askdirectory()
        if not self.dir:
            messagebox.showwarning("Предупреждение", "Выберите директорию перед изменением")
            return
        rename(self.dir)


program = Rename()

root.mainloop()