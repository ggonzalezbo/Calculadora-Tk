import tkinter as tk
from tkinter import ttk

def init_window():
    window = tk.Tk()
    window.title('Mi primera aplicacion')
    window.geometry('400x400')

    label = tk.Label(window, text = 'Calculadora', font = ('arial bold', 15))
    label.grid(column = 0, row = 0)

    entrada_1 = tk.Entry(window, width = 10)
    entrada_1.grid(column = 1, row = 1)
    entrada_2 = tk.Entry(window, width = 10)
    entrada_2.grid(column = 1, row = 2)

    label_entrada1 = tk.Label(window, text = 'Ingrese primer numero', font = ('arial bold', 10))
    label_entrada1.grid(column = 0, row = 1)
    label_entrada2 = tk.Label(window, text = 'Ingrese segundo numero', font = ('arial bold', 10))
    label_entrada2.grid(column = 0, row = 2)

    label_operador = tk.Label(window, text = 'Escoja un operador', font = ('arial bold', 10))
    label_operador.grid(column = 0, row = 3)

    combo_operador = ttk.Combobox(window)
    combo_operador['values'] = ['+', '-', '*', '/', 'pow']
    combo_operador.current(0)
    combo_operador.grid(column = 1, row = 3)

    label_resultado = tk.Label(window, text = 'Resultados', font = ('arial bold', 15))
    label_resultado.grid(column = 0, row = 5)

    boton = tk.Button(window, command = lambda: click_calcular(label_resultado, entrada_1.get(), entrada_2.get(), combo_operador.get()), text = 'Calcular', bg = 'blue', fg = 'white')
    boton.grid(column = 1, row = 4)

    window.mainloop()

def calcular(num1, num2, operador):
    if operador == '+':
        resultado = num1 + num2
    elif operador == '-':
        resultado = num1 - num2
    elif operador == '*':
        resultado = num1 * num2
    elif operador == '/':
        resultado = num1 / num2
    else:
        resultado = num1 ** num2
    return resultado

def click_calcular(label, num1, num2, operador):
    valor1 = float(num1)
    valor2 = float(num2)

    res = calcular(valor1, valor2, operador)
    label.configure(text = 'Resultado: ' + str(res))

def main():
    init_window()

main()
