from tkinter import ttk, Tk, PhotoImage, Button, Text, Menu, END
from transliterate import to_latin, to_cyrillic
from tkinter.messagebox import *
import webbrowser

root=Tk()
root.title("Transliterator")
root.resizable(0,0)

img = PhotoImage(file='D:\pictures\latin.png')
root.tk.call('wm', 'iconphoto', root._w, img)

def app_msg():
    showinfo("Dastur haqida", "Ushbu dasturda siz to`g`ridan-to`g`ri Kirildan Lotinga, Lotindan Kiril harflariga avtomatik o`tqizishingiz mumkin!\n - \"O`chirish\" tugmasi orqali barcha yozuvlarni o`chirib tashlang.\n - \"Transliterate\" tugmasi orqali harflarni lotindan kirilga, kirildan lotinga o`tqizing.\n - \"Nusxalash\" tugmasi orqali barcha yozuvlardan nusxa oling va kerakli joyga CTRL+V tugmasini bosing.")

def cr_msg():
    showinfo("Dasturchi haqida", "Salom! Men Otabek Rizayev \"Beginner junior\" bosqichidagi dasturchi bo`laman. Meni qo`llab-quvvatlash va dasturlarimni rivojlantirishga o`z hissangizni qo`shishni istasangiz, ijtimoiy tarmoqlardagi sahifalarimni kuzatib boring.")

def app_about():
    Button(root, command=app_msg())

def cr_about():
    Button(root, command=cr_msg())

def issue():
    webbrowser.open_new(r"https://github.com/Otabek-Rizayev/Transliterator/issues")

def telegram():
    webbrowser.open_new(r"https://t.me/OtabekRizayev")

def instagram():
    webbrowser.open_new(r"https://instagram/Otabek_Rizayev")

def github():
    webbrowser.open_new(r"https://github.com/Otabek-Rizayev/Transliterator")

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="MENU ☰", menu=filemenu)
filemenu.add_command(label="Dastur haqida", command=app_about)
filemenu.add_command(label="Dasturchi haqida", command=cr_about)
filemenu.add_command(label="Xato haqida habar bering", command=issue)
submenu = Menu(filemenu, tearoff=0)
submenu.add_command(label="Telegram", command=telegram)
submenu.add_command(label="Instagram", command=instagram)
submenu.add_command(label="Github", command=github)
filemenu.add_cascade(label="Ijtimoiy tarmoqlar", menu=submenu)

filemenu.add_separator()
filemenu.add_command(label="Chiqish", command=root.destroy)
root.config(menu=menubar)

inputtxt=Text(root, bg='light cyan', fg='black', bd='20', font='family', height=10, width=70)
Output=Text(root, bg='light green', fg='black', bd='20', font='family', height=10, width=70)


def trans():
    inp = inputtxt.get("1.0", "end-1c")
    if inp.isascii():
        Output.insert(END, to_cyrillic(inp))
    elif inp.isascii() != to_cyrillic:
        Output.insert(END, to_latin(inp))
    elif not to_latin() in inp:
        showerror("Xatolik yuz berdi", "Bunday harf mavjud emas.")
    

#  مة معاهدة الأمن الجماعي تغاد
#   Ê Î Ô Û Ŷ Ĉ Ĝ Ĥ Ĵ Ŝ Ŵ Ẑ
#   片仮名
def copy():
    cliptext = Output.get("1.0", 'end-1c')
    root.clipboard_clear()
    root.clipboard_append(cliptext)
    
def delete():
    Output.delete(1.0,END)
    inputtxt.delete(1.0,END)

button1=Button(root, justify="center", bd="3", fg="white", bg="#0BADCF", height=2, width=20, text="NUSXALASH", command=lambda:copy())
button=Button(root, fg="white", bd="3", bg="#0BCF60", height=2, width=20, text="TRANSLITERATE", command = lambda:trans()).place(x=340, y=543)
button2=Button(root, justify="center", bd="3", fg="white", bg="#FF2A00", height=2, width=20, text="O`CHIRISH", command=lambda:delete())

inputtxt.pack()
Output.pack()
#button.pack(side="top")
#button.grid(row=1,column=0)
button1.pack(side="right")
button2.pack(side="left")

root.mainloop()
