import csv, sys
with open("saida.csv",errors="replace",encoding="UTF-8") as f:
    leitor = csv.reader(f)
    for i, linha in enumerate(leitor, start=1):
        if not linha:
            continue
        try:
            #processando
            pass
        except Exception as e:
            print(f"[WARN] linha {i} ignorada: {e}", file=sys.stderr)
   