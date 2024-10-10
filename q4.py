resp = 'S'
while resp == "S":
    valorC = float(input("Digite o valor da casa: "))
    valorS = float(input("Digite o valor do seu salário: "))
    valorP = float(input("Digite o valor do prazo: "))
    
    valor = valorC/(valorP*12)
    valorS = valorS*0.3

    if valor > valorS:
        print("Negado")
    elif valor < valorS:
        print("Aceito")
    