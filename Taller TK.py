import tkinter as tk
from tkinter import ttk

def init_window():
    window = tk.Tk()
    window.title('Calculadora')
    window.geometry('400x320')

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

    limpiar = tk.Button(window, command = lambda: Teclado(window, entrada_1), text = 'Teclado', bg = 'blue', fg = 'white')
    limpiar.grid(column = 1, row = 6)

    window.mainloop()

def numeros(num,funcion):
    funcion.insert(str(num))

def Teclado(win, entrada):
    boton0 = tk.Button(win, command = lambda: numeros(0, entrada), text = '0', bg = 'gray', fg = 'white')
    boton1 = tk.Button(win, command = lambda: numeros(1, entrada), text = '1', bg = 'gray', fg = 'white')
    boton2 = tk.Button(win, command = lambda: numeros(2, entrada), text = '2', bg = 'gray', fg = 'white')
    boton3 = tk.Button(win, command = lambda: numeros(3, entrada), text = '3', bg = 'gray', fg = 'white')
    boton4 = tk.Button(win, command = lambda: numeros(4, entrada), text = '4', bg = 'gray', fg = 'white')
    boton5 = tk.Button(win, command = lambda: numeros(5, entrada), text = '5', bg = 'gray', fg = 'white')
    boton6 = tk.Button(win, command = lambda: numeros(6, entrada), text = '6', bg = 'gray', fg = 'white')
    boton7 = tk.Button(win, command = lambda: numeros(7, entrada), text = '7', bg = 'gray', fg = 'white')
    boton8 = tk.Button(win, command = lambda: numeros(8, entrada), text = '8', bg = 'gray', fg = 'white')
    boton9 = tk.Button(win, command = lambda: numeros(9, entrada), text = '9', bg = 'gray', fg = 'white')
    botonsum = tk.Button(win, command = lambda: calcular(1, 2, '+'), text = '+', bg = 'gray', fg = 'white')
    botonrest = tk.Button(win, command = lambda: calcular(1, 2, '+'), text = '-', bg = 'gray', fg = 'white')
    botonmult = tk.Button(win, command = lambda: calcular(1, 2, '+'), text = '*', bg = 'gray', fg = 'white')
    botondiv = tk.Button(win, command = lambda: calcular(1, 2, '+'), text = '/', bg = 'gray', fg = 'white')
    botonpow = tk.Button(win, command = lambda: calcular(1, 2, '+'), text = 'pow', bg = 'gray', fg = 'white')
    boton0.grid(column = 5, row = 10)
    boton1.grid(column = 4, row = 7)
    boton2.grid(column = 5, row = 7)
    boton3.grid(column = 6, row = 7)
    boton4.grid(column = 4, row = 8)
    boton5.grid(column = 5, row = 8)
    boton6.grid(column = 6, row = 8)
    boton7.grid(column = 4, row = 9)
    boton8.grid(column = 5, row = 9)
    boton9.grid(column = 6, row = 9)
    botonsum.grid(column = 7, row = 7)
    botonrest.grid(column = 7, row = 8)
    botonmult.grid(column = 7, row = 9)
    botondiv.grid(column = 7, row = 10)
    botonpow.grid(column = 7, row = 11)
    

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