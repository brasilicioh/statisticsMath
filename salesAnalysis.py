import re
import csv

arquivosTxt = ["allSales.txt", "jan.txt", "feb.txt", "mar.txt", "apr.txt", "may.txt", "jun.txt", "jul.txt"]
arquivosCsv = ["allSales.csv", "jan.csv", "feb.csv", "mar.csv", "apr.csv", "may.csv", "jun.csv", "jul.csv"]


for index in range(len(arquivosTxt)):
    with open(f"txt/{arquivosTxt[index]}", "r", encoding="latin1") as arquivoTxt:
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

    with open(f"csv/{arquivosCsv[index]}", "w", newline='', encoding="utf-8") as arquivoCsv:
        writer = csv.writer(arquivoCsv)
        writer.writerow(["Descricao", "Quantidade", "TotalVenda", "PrecoUnitario"])
        writer.writerows(informacoes)
