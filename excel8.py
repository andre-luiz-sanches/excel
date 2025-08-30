import csv
def to_int(v):
    try:
        return int (v)
    except ValueError:
        return None
with open("pessoas.csv","r",encoding="utf-8") as f:
    for row in csv.DictReader(f):
        row["IDADE"] = to_int(row["IDADE"])
        if row["IDADE"] is None:
            print("linha invalida",row)