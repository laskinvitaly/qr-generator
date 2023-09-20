from tkinter import *
import qrcode.image.svg
from PIL import ImageTk

root = Tk()
def clear():
    editor.delete('1.0', 'end')
    canvas.delete("all")

def myqrcode():
    text = editor.get('1.0', 'end')
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=20, border=0)
    qr.add_data(text)
    img = qr.make_image(fill_color="black", back_color="white")
    image = img.get_image()
    image = image.resize(size=[90, 90])
    canvas.image = ImageTk.PhotoImage(image)
    canvas.create_image(5, 5, anchor=NW, image=canvas.image)




root.title('Генератор Qr кодов')
root.geometry('500x350')
root.resizable(width=False, height=False)


label = Label(text="Введите текст для кодирования", width=100)
label.pack(padx=30, pady=10)
editor = Text(width=50, height=5, wrap="word")
editor.pack()
frame1 = Frame(root)
frame1.place(relx=0.1, rely=0.5, relwidth=0.8)
btn1 = Button(frame1, text="Очистить", command=clear)
btn2 = Button(frame1, text="Qr code", command=myqrcode)
btn1.pack(side=LEFT)
btn2.pack(side=LEFT, padx=10)
canvas = Canvas(root, bg="white", width=100, height=100)
canvas.pack(anchor=SE, padx=50, pady=40)
label2 = Label(text="Разработчик: Ласкин Виталий", width=100)
label2.pack()

root.mainloop()