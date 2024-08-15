import tkinter as tk
from calculator import suma, resta, multiplicacion, division

def calcular():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    operacion = variable.get()

    if operacion == "+":
        resultado = suma(num1, num2)
    elif operacion == "-":
        resultado = resta(num1, num2)
    elif operacion == "*":
        resultado = multiplicacion(num1, num2)
    elif operacion == "/":
        resultado = division(num1, num2)

    label_resultado.config(text=f"Resultado: {resultado}")

root = tk.Tk()
root.title("Calculadora Básica")

entry1 = tk.Entry(root)
entry1.pack()

entry2 = tk.Entry(root)
entry2.pack()

variable = tk.StringVar(root)
variable.set("+")  # valor por defecto

operaciones = ["+", "-", "*", "/"]
option_menu = tk.OptionMenu(root, variable, *operaciones)
option_menu.pack()

button_calcular = tk.Button(root, text="Calcular", command=calcular)
button_calcular.pack()

label_resultado = tk.Label(root, text="Resultado: ")
label_resultado.pack()

root.mainloop()
