import re
import csv

arquivosTxt = ["Txsales.txt", "Txjan.txt", "Txfeb.txt", "Txmar.txt", "Txapr.txt", "Txmay.txt", "Txjun.txt", "Txjul.txt"]
arquivosCsv = ["Cssales.csv", "Csjan.csv", "Csfeb.csv", "Csmar.csv", "Csapr.csv", "Csmay.csv", "Csjun.csv", "Csjul.csv"]

for index in range(len(arquivosTxt)):
    with open(arquivosTxt[index], "r", encoding="utf-8") as arquivoTxt:
        linhas = arquivoTxt.readlines()

    informacoes = []

    regex = re.compile(r"\|\s*([A-Z0-9\s\-\.]+?)\s*\|\s*([\d,.]+)\|\s*([\d,.]+)\|")

    for linha in linhas:
        if regex.search(linha):
            descricao = regex.search(linha).group(1).strip()
            quantidade = regex.search(linha).group(2).replace(".", "").replace(",", ".")
            total_venda = regex.search(linha).group(3).replace(".", "").replace(",", ".")
            if (descricao.split()[0] == "PINCEL" and descricao.split()[1] == "ATOMICO") or descricao.split()[0] in ["CAN", "CANETA", "CANETE", "CANTETA", "MARC", "MARCADOR", "CONPACTOR"]:
                informacoes.append([descricao, float(quantidade), float(total_venda), round((float(total_venda) / float(quantidade)), 2)])

    with open(arquivosCsv[index], "w", newline='', encoding="utf-8") as arquivoCsv:
        writer = csv.writer(arquivoCsv)
        writer.writerow(["Descricao", "Quantidade", "TotalVenda", "PrecoUnitario"])
        writer.writerows(informacoes)
