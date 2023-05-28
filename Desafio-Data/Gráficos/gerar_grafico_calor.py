# "seaborn" - Biblioteca de visualização de dados baseada no Matplotlib. 
# Ela fornece uma interface de alto nível para criar gráficos estatísticos atraentes e informativos. 
# No código fornecido, o seaborn é usado para criar gráficos de calor.

# "matplotlib.pyplot" É uma subbiblioteca do Matplotlib que fornece uma interface semelhante ao MATLAB para criar gráficos. 
# Ela é amplamente usada para visualizações de dados. 
# Neste código, o pyplot é usado para configurar e exibir os gráficos.

# "Pandas" É uma biblioteca popular para análise e manipulação de dados. 
# Ela fornece estruturas de dados de alto desempenho e fáceis de usar, como o DataFrame, que permite trabalhar com dados tabulares. 
# Neste código, o pandas é usado para carregar e manipular os dados do arquivo CSV.

# "mysql.connector" É uma biblioteca que fornece uma interface para se conectar e interagir com bancos de dados MySQL. 
# Ela permite executar consultas SQL e recuperar os resultados no Python. 
# Neste código, o mysql.connector é usado para se conectar ao banco de dados MySQL e executar consultas.


# Importação das bibliotecas necessárias.
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