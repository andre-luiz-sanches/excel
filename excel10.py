import csv
soma = 0
cont = 0
with open("pessoas.csv", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        try:
            idade = int(row["IDADE"])
        except ValueError:
            continue
        soma += idade
        cont += 1
    media = soma / cont if cont else 0
    print("media de idade:", media)
