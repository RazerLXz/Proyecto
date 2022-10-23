from cgitb import text
from subprocess import list2cmdline
from tkinter import *
from tkinter import ttk
import sqlite3

con = sqlite3.connect("")
root = Tk()
root.resizable(0, 0)

root.title("Trabajo")
root.geometry("640x380")

#Marca
lbl1 = ttk.Label(root, text="Marca")
lbl1.grid(row=5, column=1, pady=3, padx=9)
ent1 = ttk.Entry(root, width=15)
ent1.grid(row=6, column=1, pady=3, padx=9)

#Set Serial Number
lbl2 = ttk.Label(root, text="Set Serial Number")
lbl2.grid(row=5, column=2, pady=3, padx=9)
ent2 = ttk.Entry(root, width=15)
ent2.grid(row=6, column=2, pady=3, padx=9)

#Numero de Certificado
lbl3 = ttk.Label(root, text="Numero de Certificado")
lbl3.grid(row=5, column=3, pady=3, padx=9)
ent3 = ttk.Entry(root, width=15)
ent3.grid(row=6, column=3, pady=3, padx=9)

#Fecha de Cerificacion
lbl4 = ttk.Label(root, text="Fecha de Certificacion")
lbl4.grid(row=5, column=4, pady=3, padx=9)
ent4 = ttk.Entry(root, width=15)
ent4.grid(row=6, column=4, pady=3, padx=9)

#Fecha de Expiracion
lbl5 = ttk.Label(root, text="Fecha de Expiración")
lbl5.grid(row=5, column=5, pady=3, padx=9)
ent5 = ttk.Entry(root, width=15)
ent5.grid(row=6, column=5, pady=3, padx=9)


#Longitud de onda

lblwl = ttk.Label(root, text="Longitud de onda")
lblwl.grid(row=10, column=3, ipady=30)



#Primera Linea
entwl = ttk.Entry(root, width=15)
entwl.grid(row=70, column=1)

entwl2 = ttk.Entry(root, width=15)
entwl2.grid(row=70, column=2)

entwl3 = ttk.Entry(root, width=15)
entwl3.grid(row=70, column=3)

entwl4 = ttk.Entry(root, width=15)
entwl4.grid(row=70, column=4)

entwl5 = ttk.Entry(root, width=15)
entwl5.grid(row=70, column=5)



#Segunda Linea

entwl6 = ttk.Entry(root, width=15)
entwl6.grid(row=80, column=1)

entwl7 = ttk.Entry(root, width=15)
entwl7.grid(row=80, column=2)

entwl8 = ttk.Entry(root, width=15)
entwl8.grid(row=80, column=3)

entwl9 = ttk.Entry(root, width=15)
entwl9.grid(row=80, column=4)

entwl0 = ttk.Entry(root, width=15)
entwl0.grid(row=80, column=5, pady=20)
 


#Tercera Linea

entwl01 = ttk.Entry(root, width=15)
entwl01.grid(row=90, column=1)

entwl02 = ttk.Entry(root, width=15)
entwl02.grid(row=90, column=2)

entwl03 = ttk.Entry(root, width=15)
entwl03.grid(row=90, column=3)

entwl04 = ttk.Entry(root, width=15)
entwl04.grid(row=90, column=4)

entwl05 = ttk.Entry(root, width=15)
entwl05.grid(row=90, column=5)



#Solo formato de Fecha con la fecha de certificacion
def Fecha(event):
    if event.char.isdigit():
        texto = ent4.get()
        letras = 0
        for i in texto:
            letras +=1

        if letras == 2:
            ent4.insert(2,"/")
        elif letras == 5:
            ent4.insert(5,"/")
    else:
        return "break"

ent4.bind("<Key>", Fecha)
ent4.bind("<BackSpace>", lambda _:ent4.delete(root.END))



#Solo formato de Fecha con la fecha de expiracion
def FechaEnt5(event):
    if event.char.isdigit():
        texto = ent5.get()
        letras = 0
        for i in texto:
            letras +=1

        if letras == 2:
            ent5.insert(2,"/")
        elif letras == 5:
            ent5.insert(5,"/")
    else:
        return "break"

ent5.bind("<Key>", FechaEnt5)
ent5.bind("<BackSpace>", lambda _:ent5.delete(root.END))

#Borrar todos los entrys
def clearTextInput():
    campos = [ent1,ent2,ent3,ent4,ent5,entwl,entwl2,entwl3,entwl4,entwl5,entwl6,entwl7,entwl8,entwl9,entwl0,entwl01,entwl02,entwl03,entwl04,entwl05]
    
    for i in campos:
        i.delete(0, END)
        

#Boton Clear
btnClear=ttk.Button(root, width=10, text="Clear", command=clearTextInput)
btnClear.grid(row=110, column=1, pady=30, ipady=15, ipadx=15)


def Save():
    pass



#Boton Save
btnSave=ttk.Button(root, width=10, text="Save", command=Save)
btnSave.grid(row=110, column=5, pady=30, ipady=15, ipadx=15)

root.mainloop()

