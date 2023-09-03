from tkinter import *
from math import *

ventana = Tk()
ventana.title("Calculadora UCO")
ventana.geometry("480x580")
ventana.resizable(False, False)
ventana.configure(background="gray1")

# Definir el color de los botones
color_boton = "gray15"
# Definir el ancho y alto de los botones
ancho_boton = 10
alto_boton = 3

# Variable para almacenar la operación actual
operador = " "
# Variable para mostrar el contenido en la pantalla de la calculadora
texto_pantalla = StringVar()

# borrar la pantalla
def clear():
    global operador
    operador = ""
    texto_pantalla.set("0")

# Función para manejar los clics en los botones
def click(b):
    global operador
    operador += str(b)
    texto_pantalla.set(operador)

# Función para mostrar el resultado en la pantalla
def resultado():
    global operador
    try:
        r = str(eval(operador))
    except:
        r = "Math ERROR"
    texto_pantalla.set(r)

# Crear botones para la calculadora
# ... (botones de números y operadores con funciones de clic)

Boton7 = Button(ventana,text="7",bg=color_boton,width=ancho_boton,height=alto_boton,fg="white", command=lambda:click(7)).grid(row=1,column=0,pady=10)
Boton8 = Button(ventana,text="8",bg=color_boton,width=ancho_boton,height=alto_boton, fg="white",command=lambda:click(8)).grid(row=1,column=1,pady=10)
Boton9 = Button(ventana,text="9",bg=color_boton,width=ancho_boton,height=alto_boton,fg="white", command=lambda:click(9)).grid(row=1,column=2,pady=10)
BotonClear = Button(ventana,text="C",bg=color_boton,width=ancho_boton,height=alto_boton,fg="white", command=clear).grid(row=1,column=3,pady=10)
BotonMod = Button(ventana,text="%",bg=color_boton,width=ancho_boton,height=alto_boton, fg="white",command=lambda:click("%")).grid(row=1,column=4,pady=10)

Boton4 = Button(ventana,text="4",bg=color_boton,width=ancho_boton,height=alto_boton, fg="white", command=lambda:click(4)).grid(row=2,column=0,pady=10)
Boton5 = Button(ventana,text="5",bg=color_boton,width=ancho_boton,height=alto_boton,fg="white", command=lambda:click(5)).grid(row=2,column=1,pady=10)
Boton6 = Button(ventana,text="6",bg=color_boton,width=ancho_boton,height=alto_boton, fg="white",command=lambda:click(6)).grid(row=2,column=2,pady=10)
BotonMultiplicar = Button(ventana,text="*",bg=color_boton,width=ancho_boton,height=alto_boton,fg="white", command=lambda:click("*")).grid(row=2,column=3,pady=10)
BotonDivision = Button(ventana,text="/",bg=color_boton,width=ancho_boton,height=alto_boton,fg="white", command=lambda:click("/")).grid(row=2,column=4,pady=10)

Boton1 = Button(ventana,text="1",bg=color_boton,width=ancho_boton,height=alto_boton,fg="white", command=lambda:click(1)).grid(row=3,column=0,pady=10)
Boton2 = Button(ventana,text="2",bg=color_boton,width=ancho_boton,height=alto_boton,fg="white", command=lambda:click(2)).grid(row=3,column=1,pady=10)
Boton3 = Button(ventana,text="3",bg=color_boton,width=ancho_boton,height=alto_boton, fg="white",command=lambda:click(3)).grid(row=3,column=2,pady=10)
BotonSuma = Button(ventana,text="+",bg=color_boton,width=ancho_boton,height=alto_boton, fg="white",command=lambda:click("+")).grid(row=3,column=3,pady=10)
BotonResta = Button(ventana,text="-",bg=color_boton,width=ancho_boton,height=alto_boton,fg="white", command=lambda:click("-")).grid(row=3,column=4,pady=10)

Boton_0 = Button(ventana,text="0",bg=color_boton,width=ancho_boton,height=alto_boton,fg="white", command=lambda:click(0)).grid(row=4,column=0,pady=10)
BotonPunto = Button(ventana,text=".",bg=color_boton,width=ancho_boton,height=alto_boton,fg="white", command=lambda:click(".")).grid(row=4,column=1,pady=10)
BotonPi = Button(ventana,text="π",bg=color_boton,width=ancho_boton,height=alto_boton,fg="white", command=lambda:click("pi")).grid(row=4,column=2,pady=10)
BotonParenIzq = Button(ventana,text="(",bg=color_boton,width=ancho_boton,height=alto_boton, fg="white",command=lambda:click("(")).grid(row=4,column=3,pady=10)
BotonParenDer = Button(ventana,text=")",bg=color_boton,width=ancho_boton,height=alto_boton,fg="white", command=lambda:click(")")).grid(row=4,column=4,pady=10)

BotonSen = Button(ventana,text="sen",bg=color_boton,width=ancho_boton,height=alto_boton,fg="white", command=lambda:click("sin(")).grid(row=5,column=0,pady=10)
BotonCos = Button(ventana,text="cos",bg=color_boton,width=ancho_boton,height=alto_boton,fg="white", command=lambda:click("cos(")).grid(row=5,column=1,pady=10)
BotonTan = Button(ventana,text="tan",bg=color_boton,width=ancho_boton,height=alto_boton, fg="white",command=lambda:click("tan(")).grid(row=5,column=2,pady=10)
BotonRaiz = Button(ventana,text="√",bg=color_boton,width=ancho_boton,height=alto_boton, fg="white",command=lambda:click("sqrt(")).grid(row=5,column=3,pady=10)
BotonEXP = Button(ventana,text="e",bg=color_boton,width=ancho_boton,height=alto_boton,fg="white", command=lambda:click("exp")).grid(row=5,column=4,pady=10)

BotonArcSin = Button(ventana, text="sin^-1", bg=color_boton, width=ancho_boton, height=alto_boton,fg="white", command=lambda: click("asin(")).grid(row=6, column=0, pady=10)
BotonArcSin = Button(ventana, text="sin^-1", bg=color_boton, width=ancho_boton, height=alto_boton,fg="white", command=lambda: click("asin(")).grid(row=6, column=1, pady=10)
BotonArcTan = Button(ventana, text="tan^-1", bg=color_boton, width=ancho_boton, height=alto_boton,fg="white", command=lambda: click("atan")).grid(row=6, column=2, pady=10)
BotonLN = Button(ventana,text="LN",bg=color_boton,width=ancho_boton,height=alto_boton, fg="white",command=lambda:click("log")).grid(row=6,column=3,pady=10)
BotonIgual = Button(ventana,text="=",bg=color_boton,width=ancho_boton,height=alto_boton, fg="white",command=resultado).grid(row=6,column=4,pady=10)

# Crear la pantalla de la calculadora
Pantalla = Entry(ventana, font=("arial", 20, "bold"), width=22, borderwidth=10, background="grey50", textvariable=texto_pantalla)
# Colocar la pantalla en la cuadrícula de la ventana
Pantalla.grid(row=0, column=0, columnspan=4, padx=20, pady=20)

# Iniciar el bucle principal de la interfaz gráfica para que la ventana sea interactiva
ventana.mainloop()
