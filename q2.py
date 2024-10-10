resp = 'S'
while resp == "S":
    valor = float(input("Digite o valor da compra: "))
    if valor > 100:
        valor = valor * 0.90
        print(f"Você recebeu um desconto de 10%, sua compra ficou no valor de {valor}")
    elif valor <= 100:
        print(f"Você não recebeu nenhum desconto, sua compra ficou no valor de {valor}")
    resp = str(input("VocÊ deseja fazer novamente?(S/N): "))
