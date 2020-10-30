print("\n***CONVERSOR DE MEDIDAS***\n")
medida = ("KM", "MT", "CM")
while True:
    m = input(f"DIGITE A PRIMEIRA MEDIDA, VALORES VALIDOS {medida}: ")
    medida1 = m.upper() #<-- transformei em maiuscula
    if not medida1.isalpha(): #<-- verifico se digitou numero(se não for string)
        print(f"\n\nALERTA 1: Não digite numeros ({medida1})"
              f" os valores válidos são {medida}\n") #não digite numeros, volta inicio

    elif medida1 not in medida:
        print (f"\n\nALERTA 1.1: Valor {medida1} incorreto, digite corretamente o valor da área,"
               f"os valores aceitos são {medida}\n")
    else:
        break

while True:
    valor = str(input(f"\nQUANTOS {medida1}(S) VAI CONVERTER?: "))

    if valor.isalpha(): #<-- Verifica se o valor é letra, retorna para inicio
        print(f"\n\nALERTA 2: Digite apenas NUMEROS, O valor digitado foi {valor} : \n")

    else:
        break

while True:
    c = input(f"\nDIGITE A MEDIDA A SER CONVERTIDA EM {medida1}, VALORES VÁLIDOS {medida}: ")
    medida2 = c.upper()  # <-- transformei em maiuscula
    if not medida2.isalpha():  # <-- verifico se digitou numero(se não for string)
        print (f"\n\nALERTA 3: Não digite numeros ({medida2})"
               f" os valores válidos são {medida}\n")  # não digite numeros, volta inicio

    elif medida2 not in medida:
        print (f"\n\nALERTA 1.1: Valor {medida2} incorreto, digite corretamente o valor da área,"
               f"os valores aceitos são {medida}\n")
    else:
        break


if medida1 == "KM" and medida2 == "MT":
    basekm = 10000
    v = float(valor)
    calculo = v * basekm
    print(f'\n\n{v} KILOMETRO(s) É IGUAL A {calculo} {medida2} METRO(s)\n')

if medida1 == "MT" and medida2 == "KM":
    basekm = 1000
    v = float(valor)
    calculo = v / basekm
    print(f'\n\nA conversão de {v} METROS(s) para {medida2} é de {calculo} KILOMETROS(s)\n')

if medida1 == "MT" and medida2 == "CM":
    basecm = 100
    v = float(valor)
    calculo = v * basecm
    print(f'\n\nA conversão de {v} METROS(s) para {medida2} é de {calculo} CENTÍMETROS(s)\n')

if medida1 == "CM" and medida2 == "MT":
    basecm = 100
    v = float(valor)
    calculo = v/basecm
    print(f'\n\nA conversão de {v} CENTÍMETRO(s) para {medida2} é de {calculo} METROS(s)\n')

if medida1 == "KM" and medida2 == "CM":
    basekm = 100000
    v = float(valor)
    calculo = v * basekm
    print(f'\n\nA conversão de {v} KILOMETRO(s) para {medida2} é de {calculo} CENTÍMETRO(s)\n')

if medida1 == "CM" and medida2 == "KM":
    basecm = 100000
    v = float(valor)
    calculo = v / basecm
    print('\n\nA conversão de {0} CENTÍMENTRO(s) para {1} é de {2:f} KILOMETROS(s)\n'.format(v, medida2, calculo))

