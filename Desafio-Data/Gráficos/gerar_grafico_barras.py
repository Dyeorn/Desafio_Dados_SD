# "matplotlib.pyplot" É uma subbiblioteca do Matplotlib que fornece uma interface semelhante ao MATLAB para criar gráficos. 
# Ela é amplamente usada para visualizações de dados. 
# Neste código, o pyplot é usado para configurar e exibir os gráficos.

# "mysql.connector" É uma biblioteca que fornece uma interface para se conectar e interagir com bancos de dados MySQL. 
# Ela permite executar consultas SQL e recuperar os resultados no Python. 
# Neste código, o mysql.connector é usado para se conectar ao banco de dados MySQL e executar consultas.


# Importação das bibliotecas necessárias.
import matplotlib.pyplot as plt
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

# Executa a consulta SQL para buscar os 10 produtos mais vendidos na categoria "Bicicletas".
query = """
SELECT p.productname AS Produto, SUM(s.OrderQuantity) AS TotalVendido
FROM products AS p
JOIN sales AS s ON p.ProductKey = s.ProductKey 
JOIN product_category AS c ON p.ProductSubCategoryKey = c.productcategorykey
WHERE c.categoryname = 'Bikes'
GROUP BY p.ProductKey
ORDER BY TotalVendido DESC
LIMIT 10;
"""
cursor.execute(query)

# Busca todos os resultados.
resultados = cursor.fetchall()

# Extrai os nomes dos produtos e a quantidade total vendida dos resultados.
products = [row[0] for row in resultados]
quantity_sold = [row[1] for row in resultados]

# Fecha o cursor e a conexão.
cursor.close()
conn.close()

# Plotando o gráfico de barras.
plt.bar(products, quantity_sold, color='blue')
plt.xlabel('Produto')
plt.ylabel('Quantidade de Vendas')
plt.title('Top 10 Mais Vendidos na Categoria "Bikes"')

# Exibe o gráfico de barras.
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()