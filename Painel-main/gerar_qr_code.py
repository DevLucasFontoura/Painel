# https://www.youtube.com/watch?v=QXuxZExCznQ&ab_channel=DynamicCoding

# pip install qrcode pillow

import qrcode, PIL
import tkinter as tk
from PIL import ImageTk
from tkinter import ttk, filedialog, messagebox


def createQR(*args):
    data = text_entry.get()

    if data:
        img = qrcode.make(data)
        resized_img = img.resize((280, 250))
        tkimage = ImageTk.PhotoImage(resized_img)
        qr_canvas.delete("all")
        qr_canvas.create_image(0,0, anchor=tk.NW, image=tkimage)
        qr_canvas.image = tkimage
    else: 
        messagebox.showwarning("Error","Escreva um URL válido!")

def saveQR(*args):
    data = text_entry.get()

    if data:
        img = qrcode.make(data)
        resized_img = img.resize((280, 250))
        
        path = filedialog.asksaveasfilename(defaultextension=".png")
        
        if path:
            resized_img.save(path)
            messagebox.showinfo("Sucess","QR Code foi salvo!")
    else: 
        messagebox.showwarning("Error","Escreva um URL válido!")



root = tk.Tk()
root.title("Gerador de QR Code")
# root.geometry("300x380")
root.config(bg="White")
root.resizable(0,0)

height = 380
width = 300

x = (root.winfo_screenwidth()//2) - (width//2)
y = (root.winfo_screenheight()//2) - (height//2)
root.geometry('{}x{}+{}+{}'.format(width, height, x, y))


frame1 = tk.Frame(root, bd=2, relief=tk.RAISED)
frame1.place(x=10, y=0, width=280, height=250)

frame2 = tk.Frame(root, bd=2, relief=tk.SUNKEN)
frame2.place(x=10, y=260, width=280, height=100)

cover_img = tk.PhotoImage(file="images/logo.png")

qr_canvas = tk.Canvas(frame1)
qr_canvas.create_image(0,0, anchor=tk.NW, image=cover_img)
qr_canvas.image = cover_img
qr_canvas.bind("<Double-1>", saveQR)
qr_canvas.pack(fill=tk.BOTH)

text_entry = ttk.Entry(frame2, width=26, font=("Sitka Small", 11), justify=tk.CENTER)
text_entry.bind("<Return>", createQR)
text_entry.place(x=5, y=5)

btn_1 = ttk.Button(frame2, text="Criar", width=10, command=createQR)
btn_1.place(x=25, y=50)

btn_2 = ttk.Button(frame2, text="Salvar", width=10, command=saveQR)
btn_2.place(x=100, y=50)

btn_3 = ttk.Button(frame2, text="Sair", width=10, command=root.quit)
btn_3.place(x=175, y=50)


root.mainloop()