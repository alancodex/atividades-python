mulher2 = mulherm = 0

for i in range(10):
    resp = int(input("Digite a quantidade de filhos: "))
    if resp > 2:
        mulher2 += 1
    elif resp <=2:
        mulherm += 1

print("Quantidade de mulheres com mais de dois filhos", mulherm)
print(f"Quantidade de mulheres com até dois filhos {mulher2}")
