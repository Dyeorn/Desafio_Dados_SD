import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import mysql.connector

# Estabelece uma conexão com o banco de dados MySQL.
conn = mysql.connector.connect(
    host='localhost',
    user='jp_sd',
    password='santodigital',
    database='Data-AdventureWorks'
)

# O cursor é criado para executar as consultas no banco de dados.
cursor = conn.cursor()

# Executa a consulta SQL para buscar vendas por região e mês.
query = """
SELECT t.Region AS Region, DATE_FORMAT(s.OrderDate, '%Y-%m') AS Month, SUM(s.OrderQuantity) AS TotalSales
FROM sales AS s
JOIN territories AS t ON s.TerritoryKey = t.SalesTerritoryKey
GROUP BY Region, Month
ORDER BY Region, Month;
"""
cursor.execute(query)

# Busca todos os resultados.
resultados = cursor.fetchall()

# Cria um DataFrame pandas a partir dos resultados da consulta.
df = pd.DataFrame(resultados, columns=['Region', 'Month', 'TotalSales'])

# Converte a coluna TotalSales em tipo numérico.
df['TotalSales'] = pd.to_numeric(df['TotalSales'])

# Gira o DataFrame para ter regiões como linhas, meses como colunas e vendas totais como valores.
heatmap_data = df.pivot('Region', 'Month', 'TotalSales')

# Fecha o cursor e a conexão.
cursor.close()
conn.close()

# Cria o mapa de calor.
plt.figure(figsize=(10, 8))
sns.heatmap(heatmap_data, cmap='YlOrRd', annot=True, fmt='g')
plt.title('Vendas Por Regiao e Mes')
plt.xlabel('Mes')
plt.ylabel('Regiao')

# Exibe o mapa de calor.
plt.tight_layout()
plt.show()