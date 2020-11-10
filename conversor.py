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
    return (float(valor.replace(",", ".")) / medidas[medida1]) * medidas[medida2]

def main():
    medidas = {"KM": 1, "MT": 1000, "CM": 100000, "ML": 1e+6}

    medida1 = combo.get()
    valor = qtde.get()
    medida2 = combo2.get()
    resultado = calc(medida1, medida2, valor, medidas)
    resultadof = f'\n\nA conversão de {valor} {medida1} para {medida2} é de {resultado} {medida2}(s)\n'
    labelresultado["text"] = resultadof


def limpar():
    combo.set("")
    qtde.set("")
    combo2.set("")
    labelresultado['text']=0


janela = Tk()

janela.title("PRIMEIRA JANELA")
#larguraxAltura+DistanciaDireita+DistanciaTopo
janela.geometry("500x500+300+300")
fontPadrao = ("Courier", 10, "bold")

title = Label(janela, text="CONVERSOR DE MEDIDA", font=fontPadrao, background="red", foreground="white")
title.place()

combo = Combobox(janela, width=35, values=["KM", 'MT', 'CM'], state="readonly")
combo.set("SELECIONE A PRIMEIRA MEDIDA")
combo.place(x=190, y=500)

qtde = Spinbox(janela, from_=1, to=100, width=10)
qtde.set("VALOR")

combo2 = Combobox(janela, width=35, values=["KM", 'MT', 'CM'], state="readonly")
combo2.set("SELECIONE A SEGUNDA MEDIDA")

labelresultado = Label(janela, text="0")

btresultado = Button(janela, width=20, text="RESULTADO", command=main)

bt = Button(janela, width=20, text="LIMPAR", command=limpar)


title.pack(padx='10', pady='10')
combo.pack(padx='10', pady='10')
qtde.pack(padx='10', pady='10')
combo2.pack(padx='10', pady='10')
labelresultado.pack(padx='10', pady='10')
btresultado.pack()
bt.pack()


janela.mainloop()