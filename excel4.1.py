import csv

with open("pessoas.csv",newline="",encoding="utf-8") as f:
    leitor = csv.DictReader(f,delimiter=",")
    for linha in leitor:
        idade = int(linha["IDADE"])
        if idade >= 30:
            print(f"{linha["NOME"]} tem {idade} anos")

