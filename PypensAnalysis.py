import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Analisar todos os itens vendidos em pens.csv e começar a montar gráficos e relações estatísticas.

csv = pd.read_csv("Cssales.csv")


print(csv)


#sessão gráfico
plt.figure(figsize=(10, 6))
plt.barh(csv["Descricao"], csv["PrecoUnitario"], color="skyblue")
plt.xlabel("Produto")
plt.ylabel("Preço por Unidade")
plt.title("Preço por Unidade de Cada Produto")
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()