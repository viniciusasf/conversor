import tkinter as tk
from tkinter import ttk

def ler_medida(texto_medida, medidas):
    opcoes = ','.join(medidas.keys())
    param = input(f"DIGITE A {texto_medida}, VALORES VALIDOS {opcoes}: ").upper()
    if param not in medidas.keys():
        print(f"\n\nALERTA 1.1: Valor {param} incorreto, digite corretamente o valor da área,"
              f"os valores aceitos são {medidas.keys()}\n")
        param = ler_medida(texto_medida, medidas)
    return param


def ler_valor(medida1):
    valor = str(input(f"\nQUANTOS {medida1}(S) VAI CONVERTER?: "))
    if valor.isalpha():
        print(f"\n\nALERTA 2: Digite apenas NUMEROS, O valor digitado foi {valor} : \n")
        valor = ler_valor(medida1)
    return valor


def calc(medida1, medida2, valor, medidas):
    return (float(valor) / medidas[medida1]) * medidas[medida2]


def main():
    print("\n***CONVERSOR DE MEDIDAS***\n")
    medidas = {"KM": 1, "MT": 1000, "CM": 100000, "ML":1e+6}

    medida1 = ler_medida("PRIMEIRA MEDIDA", medidas)
    valor = ler_valor(medida1)
    medida2 = ler_medida("SEGUNDA MEDIDA", medidas)

    resultado = calc(medida1, medida2, valor, medidas)
    print(f'\n\nA conversão de {valor} {medida1} para {medida2} é de {resultado} {medida2}(s)\n')


def build_form():
    # Setup the root UI
    root = tk.Tk()
    root.title("CONVERSOR DE MEDIDAS")

    left_frame = tk.Frame(root)

    # Setup filter frame
    ttk.Label(left_frame, text="DE2 :").grid(row=0, column=0, sticky=tk.NSEW)
    entry = ttk.Entry(left_frame)
    entry.insert(1, "")
    entry.grid(row=0, column=2)

    left_frame.grid(row=0, column=0)


    ttk.Button(left_frame,
               text="search").grid(row=0, column=3)

    ttk.Button(left_frame,
               text="reset").grid(row=0, column=4)

    ttk.Button(left_frame,
               text="open file").grid(row=0, column=5)

    tk.Grid.rowconfigure(root, 1, weight=1)
    tk.Grid.columnconfigure(root, 2, weight=1)
    root.update_idletasks()
    #root.attributes('-zoomed', True)

    root.mainloop()


if __name__ == '__main__':
    build_form()

