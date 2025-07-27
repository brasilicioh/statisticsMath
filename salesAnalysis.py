import re
import csv

with open("sales.txt", "r", encoding="utf-8") as file:
    linhas = file.readlines()

informacoes = []

regex = re.compile(r"\|\s*([A-Z0-9\s\-\.]+?)\s*\|\s*([\d,.]+)\|\s*([\d,.]+)\|")

for linha in linhas:
    if regex.search(linha):
        descricao = regex.search(linha).group(1).strip()
        quantidade = regex.search(linha).group(2).replace(".", "").replace(",", ".")
        total_venda = regex.search(linha).group(3).replace(".", "").replace(",", ".")
        if descricao.split()[0] in ["CAN", "CANETA", "CANETE", "CANTETA", "MARC", "MARCADOR", "PINCEL"]:
            informacoes.append([descricao, float(quantidade), float(total_venda)])

with open("items.csv", "w", newline='', encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Descricao", "Quantidade", "TotalVenda"])
    writer.writerows(informacoes)
