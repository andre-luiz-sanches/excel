with open ("pessoas.csv", "r", encoding ="utf -8") as f:
    cabecalho = f . readline () . strip () . split (",") # [ ’ Nome ’,’ Idade ’,’Cidade ’]

    for linha in f :
        if not linha . strip () :
            continue # pula linhas vazias
        campos = linha . strip () . split (",")
        registro = dict (zip ( cabecalho , campos ))
        print ( registro )
        #if registro[1] == "Andre":
            #print("sou eu")
        #else:
            #print("não")