from cgitb import text
from re import I
from subprocess import list2cmdline
from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter import messagebox

root = Tk()
root.resizable(0, 0)

F1 = Frame(root) 
F2 = Frame(root)
F3 = Frame(root)
F4 = Frame(root)
F5 = Frame(root)
F6 = Frame(root)

F1.pack()
F2.pack()
F3.pack()
F4.pack()
F5.pack()
F6.pack()

root.title("Agregar estandar de holmio a base de datos")
root.geometry("510x320")


#Marca
lbl1 = ttk.Label(F1, text="Marca")
lbl1.grid(row=5, column=1, pady=3, padx=9)
ent1 = ttk.Entry(F1, width=13)
ent1.grid(row=6, column=1, pady=3, padx=9)

#Set Serial Number
lbl2 = ttk.Label(F1, text="Set Serial")
lbl2.grid(row=5, column=2, pady=3, padx=9)
ent2 = ttk.Entry(F1, width=13)
ent2.grid(row=6, column=2, pady=3, padx=9)

#Numero de Certificado
lbl3 = ttk.Label(F1, text="Nro Certif.")
lbl3.grid(row=5, column=3, pady=3, padx=9)
ent3 = ttk.Entry(F1, width=13)
ent3.grid(row=6, column=3, pady=3, padx=9)

#Fecha de Cerificacion
lbl4 = ttk.Label(F1, text="Fecha Certif.")
lbl4.grid(row=5, column=4, pady=3, padx=9)
ent4 = ttk.Entry(F1, width=13)
ent4.grid(row=6, column=4, pady=3, padx=9)

#Fecha de Expiracion
lbl5 = ttk.Label(F1, text="Fecha Exp")
lbl5.grid(row=5, column=5, pady=3, padx=9)
ent5 = ttk.Entry(F1, width=13)
ent5.grid(row=6, column=5, pady=3, padx=9)


#Longitud de onda

lblwl = ttk.Label(F2, text="Picos de Holmio 1.00")
lblwl.grid(row=12, column=3, pady=8)


#Primera Linea
c1 = Label(F3, text="1")

entwl = ttk.Entry(F3, width=11)
entwl.grid(row=70, column=1, padx=9)

entwl2 = ttk.Entry(F3, width=11)
entwl2.grid(row=70, column=2, padx=9)

entwl3 = ttk.Entry(F3, width=11)
entwl3.grid(row=70, column=3, padx=9)

entwl4 = ttk.Entry(F3, width=11)
entwl4.grid(row=70, column=4, padx=9)

entwl5 = ttk.Entry(F3, width=11)
entwl5.grid(row=70, column=5, padx=9, pady=10)



#Segunda Linea

entwl6 = ttk.Entry(F4, width=11)
entwl6.grid(row=80, column=1, padx=9)

entwl7 = ttk.Entry(F4, width=11)
entwl7.grid(row=80, column=2, padx=9)

entwl8 = ttk.Entry(F4, width=11)
entwl8.grid(row=80, column=3, padx=9)

entwl9 = ttk.Entry(F4, width=11)
entwl9.grid(row=80, column=4, padx=9)

entwl0 = ttk.Entry(F4, width=11)
entwl0.grid(row=80, column=5, padx=9, pady=10)
 


#Tercera Linea

entwl01 = ttk.Entry(F5, width=11)
entwl01.grid(row=90, column=1, padx=9)

entwl02 = ttk.Entry(F5, width=11)
entwl02.grid(row=90, column=2, padx=9)

entwl03 = ttk.Entry(F5, width=11)
entwl03.grid(row=90, column=3, padx=9)

entwl04 = ttk.Entry(F5, width=11)
entwl04.grid(row=90, column=4, padx=9)

entwl05 = ttk.Entry(F5, width=11)
entwl05.grid(row=90, column=5, padx=9, pady=10)



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
        

def Save():
    
    camposWL = [ent1,ent2,ent3,ent4,ent5,
                entwl,entwl2,entwl3,entwl4,entwl5,
                entwl6,entwl7,entwl8,entwl9,entwl0,
                entwl01,entwl02,entwl03,entwl04,entwl05]
    lst = []
    comprobar = False
    
    for i in camposWL:
        i=i.get()
        try:
            i=int(i)
            lst.append(i)
        except:
            try:
                i=float(i)
                lst.append(i)
            except:
                if i == "":
                    comprobar = True
                    break
                else:
                    i=str(i)
                    lst.append(i)
              
                   
                
    if comprobar == True:  
         messagebox.showerror("Error","Los campos no pueden estar vacios")
         
    else:  
        con = sqlite3.connect("test.db")
        cursor = con.cursor()
        cursor.execute("INSERT INTO test VALUES(NULL,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",lst)
        con.commit()
        con.close()


def focus_next_window(event):
    event.widget.tk_focusNext().focus()


#Boton Save
btnSave=ttk.Button(F6, width=10, text="Guardar", command=Save)
btnSave.grid(row=110, column=5, pady=30, ipady=15, ipadx=15, padx=9)


#Boton Clear
btnClear=ttk.Button(F6, width=10, text="Limpiar", command=clearTextInput)
btnClear.grid(row=110, column=1, pady=30, ipady=15, ipadx=15, padx=9)


root.bind("<Return>", focus_next_window)


root.mainloop()




