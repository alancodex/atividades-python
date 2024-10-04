femeaM2 = 0
femeaMenos2 = 0
for i in range (1, 11):
    filhos = int(input("Quantos filhos você tem?: "))
    if filhos <= 2:
        femeaM2 += 1
    elif filhos > 2:
        femeaMenos2 += 1

print("Quantidade de mulheres com até dois filhos: ", femeaMenos2)
print("Quantidade de mulheres com mais de dois filhos", femeaM2)
