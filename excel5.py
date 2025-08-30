import csv
registros = [
    {"Nome": " Ana ", "Idade": 23 , "Cidade": "Sao Paulo "} ,
    {"Nome": " Bruno ", "Idade": 31 , "Cidade": " Curitiba "},
]

with open ("saida.csv","w",newline="",encoding="utf-8") as f:
    campos = ["Nome","Idade","Cidade"]
    writer = csv.DictWriter(f,fieldnames=campos, delimiter=';')
    writer.writeheader()
    writer.writerows(registros)
