import csv
with open("saida.csv","r",encoding="utf-8") as f:
    amostra = f.read(2048)
    f.seek(0)
    dialeto = csv.Sniffer().sniff(amostra)
    f.seek(0)
    leitor = csv.reader(f,dialect=dialeto)
    print(dialeto.delimiter)
    for linha in leitor:
        print(linha)