valor = 0
pergunta = True

while (pergunta):
    compra  = float(input("Digite o valor total da compra: "))
    if (compra >= 100):
        compra = compra - (compra*0.1)

        print("Você recebeu um desconto de 10%!!")
        print("Sua compra está no valor de: ", compra)
    elif (compra > 0):
        print("Digite um número posivo")
    else:
        print("Você não recebeu nenhum desconto")

