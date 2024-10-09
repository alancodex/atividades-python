bolo = float(input("Qual o valor do bolo?: "))

s1 = float(input("Qual o valor do Salgado 1?: "))
s1c = float(input("Qual a quantidade do Salgado 1?: "))

s2 = float(input("Qual o valor do Salgado 2?: "))
s2c = float(input("Qual a quantidade do Salgado 2?:"))

s3 = float(input("Qual o valor do Salgado 3?: "))
s3c = float(input("Qual a quantidade do Salgado 3?: "))

s4 = float(input("Qual o valor do Salgado 4?: "))
s4c = float(input("Qual a quantidade do Salgando 4?: ")) 

valor = bolo + (s1 * s1c) + (s2 * s2c) + (s3 * s3c) + (s4 * s4c)

valorUnico = valor / 11

print("O valor que cada um ira pagar é: ", valorUnico)