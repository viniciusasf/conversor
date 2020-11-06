from tkinter import *
from tkinter.ttk import *


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
    medidas = {"KM": 1, "MT": 1000, "CM": 100000, "ML": 1e+6}

    medida1 = ler_medida("PRIMEIRA MEDIDA", medidas)
    valor = ler_valor(medida1)
    medida2 = ler_medida("SEGUNDA MEDIDA", medidas)

    resultado = calc(medida1, medida2, valor, medidas)
    print(f'\n\nA conversão de {valor} {medida1} para {medida2} é de {resultado} {medida2}(s)\n')



def limpar():
    combo.set("")
    spin.set("")
    combo2.set("")


janela = Tk()

medidas = {"KM": 1, "MT": 1000, "CM": 100000, "ML": 1e+6}


janela.title("PRIMEIRA JANELA")
#larguraxAltura+DistanciaDireita+DistanciaTopo
janela.geometry("250x250+800+300")

title = Label(janela, text="CONVERSOR DE MEDIDA")
title.pack()

combo = Combobox(janela, width=35, height=5)
combo["values"] = ("KM", 'MT', 'CM')
combo.place(x=190, y=300)
combo.pack()

spin = Spinbox(janela, from_=1, to=100, width=10)
spin.pack()

combo2 = Combobox(janela, width=35)
combo2["values"] = ("KM", 'MT', 'CM')
combo2.pack()

resultado = Label(janela, text="RESULTADO")
resultado.pack()


bt = Button(janela, width=20, text="LIMPAR", command=limpar)
bt.place(x=100, y=100)
bt.pack()


janela.mainloop()
