import tkinter as tk
from tkinter import filedialog
from PIL import Image

root = tk.Tk()

canvas1 = tk.Canvas(root, width=300, height = 250, bg='azure3', relief = 'raised')
canvas1.pack()

label1 = tk.Label(root, text= 'File Conversion Tool', bg='azure3')
label2 = tk.Label(root, text= 'Made By Behigu', bg='azure3')
label2.config(font=('helvetica', 14))
label1.config(font=('helvetica', 20))

canvas1.create_window(150,60, window=label1)
canvas1.create_window(150,24, window=label2)

def getPNG():
    global iml

    import_file_path = filedialog.askopenfilename()
    iml= Image.open(import_file_path)

browseButton_PNG = tk.Button(text = '    Import PNG files',
command=getPNG, bg='royalblue', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150,130,window=browseButton_PNG)

def convertToJPG():
    global iml
    export_file_path = filedialog.asksaveasfilename(defaultextension= '.jpg')
    iml.convert('RGB').save(export_file_path)

saveAsButtone_JPG = tk.Button(text='Convert PNG to JPG', command=convertToJPG,
bg='royalblue', fg='white', font=('helvetica', 12, 'bold'))

canvas1.create_window(150,180, window= saveAsButtone_JPG)

root.mainloop()
