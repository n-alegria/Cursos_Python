from tkinter import *

main = Tk()
main.geometry("800x500")

encabezado = Label(main, text="Formularios")
encabezado.config(
    padx = 15,
    pady = 15,
    fg = "white",
    bg = "green",
    font = ("Consolas", 20)
)
encabezado.grid(row=0, column=0, columnspan=5, sticky=W)

# Botones check
# Creo las funciones donde almacenare el ingreso de los checkbuttons
def mostarProfesion():
    texto = ""
    if web.get():
        texto += "Desarrollo web"
    if movil.get():
        if(web.get()):
            texto += " y Desarrollo movil"
        else:
            texto += "Desarrollo movil"
    mostrar.config(
        text = texto, 
        bg="green",
        fg = "white"
    )

web = IntVar()
movil = IntVar()

Label(main, text="A que te dedicas").grid(row=1, column=0)
Checkbutton(main, 
    text="Desarrollo Web", 
    variable = web,
    onvalue = 1,
    offvalue = 0,
    command = mostarProfesion
).grid(row=2, column=0)

Checkbutton(main, 
    text="Desarrollo Movil",
    variable = movil,
    onvalue = 1,
    offvalue = 0,
    command = mostarProfesion
).grid(row=3, column=0)

mostrar = Label(main)
mostrar.grid(row = 4, column=0)


# Radio buttons
def marcar():
    marcado.config(text=opcion.get())

opcion = StringVar()
opcion.set(None)

Label(main, text="Cual es tu genero").grid(row=5)
Radiobutton(
    main, 
    text="Masculino",
    value = "Masculino",
    variable = opcion,
    command = marcar
).grid(row=6)

Radiobutton(
    main, 
    text="Femenino",
    value = "Femenino",
    variable = opcion,
    command = marcar
).grid(row=7)

marcado = Label(main)
marcado.grid(row = 8)


# Menu de opciones
def seleccionar():
    seleccionado.config(text=opcion.get())

opcion = StringVar()
opcion.set("Opcion 1")
Label(main, text="Selecciona una opcion").grid(row=5, column=1)
select = OptionMenu(main, opcion, "Opcion 1", "Opcion 2", "Opcion 3")
select.grid(row = 6, column=1)
Button(main, text="Ver", command=seleccionar).grid(row=7, column=1)


seleccionado = Label(main)
seleccionado.grid(row = 8, column = 1)


main.mainloop()