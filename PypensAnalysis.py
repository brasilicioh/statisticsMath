import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Analisar todos os itens vendidos em pens.csv e começar a montar gráficos e relações estatísticas.

csv = pd.read_csv("Cssales.csv")

csv_jan = pd.read_csv("Csjan.csv")
csv_feb = pd.read_csv("Csfeb.csv")
csv_mar = pd.read_csv("Csmar.csv")
csv_apr = pd.read_csv("Csapr.csv")
csv_may = pd.read_csv("Csmay.csv")
csv_jun = pd.read_csv("Csjun.csv")
csv_jul = pd.read_csv("Csjul.csv")

#funções

def calcmedia():
    numeros = []

    numeros.append(csv_jan["Quantidade"].max())
    numeros.append(csv_feb["Quantidade"].max())
    numeros.append(csv_may["Quantidade"].max())
    numeros.append(csv_apr["Quantidade"].max())
    numeros.append(csv_may["Quantidade"].max())
    numeros.append(csv_jun["Quantidade"].max())
    numeros.append(csv_jul["Quantidade"].max())

    soma = sum(numeros)
    media = soma / len(numeros)
    return media

def calcDP():
    numeros = []

    numeros.append(csv_jan["Quantidade"].max())
    numeros.append(csv_feb["Quantidade"].max())
    numeros.append(csv_may["Quantidade"].max())
    numeros.append(csv_apr["Quantidade"].max())
    numeros.append(csv_may["Quantidade"].max())
    numeros.append(csv_jun["Quantidade"].max())
    numeros.append(csv_jul["Quantidade"].max())

    media = sum(numeros) / len(numeros)

    varia = []
    for i in range(len(numeros)):
        varia.append((numeros[i] - media)**2)

    media = sum(varia) / len(varia)
    desvio = np.sqrt(media)
    return desvio

    


print(csv)


#sessão gráfico

#grafico geral de produtos/preco
plt.figure(figsize=(10, 6))
plt.barh(csv["Descricao"], csv["PrecoUnitario"], color="skyblue")
plt.xlabel("Produto")
plt.ylabel("Preço por Unidade")
plt.title("Preço por Unidade de Cada Produto")
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

#GRafico maior vendas
plt.figure(figsize=(10, 6))
plt.barh(csv["Descricao"], calcmedia(), color="skyblue") #trocar CSVdescrição pelos meses
plt.xlabel("Produto")
plt.ylabel("Quantidade de vendas")
plt.title("Maiores vendas nos ultimos 7 meses")
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()