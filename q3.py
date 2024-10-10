ph = 0

while ph != -1:
    ph = int(input("Digite o valor do ph (Use -1 para sair)"))
    if ph < 7 and ph < 0:
        print("Àcida")
    if ph > 7:
        print("Básica")
    if ph == 7:
        print("Neutra")