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

# Executa a consulta SQL para buscar o total de vendas por mês.
query = """
SELECT DATE_FORMAT(s.OrderDate, '%Y-%m') AS Month, SUM(s.OrderQuantity) AS TotalSales
FROM sales AS s
GROUP BY Month
ORDER BY Month;
"""
cursor.execute(query)

# Busca todos os resultados.
resultados = cursor.fetchall()

# Extrai os dados de vendas mensais e totais dos resultados.
months = [row[0] for row in resultados]
total_sales = [row[1] for row in resultados]

# Fecha o cursor e a conexão.
cursor.close()
conn.close()

# Plotando o gráfico de linhas.
plt.plot(months, total_sales, marker='o', linestyle='-', color='blue')
plt.xlabel('Meses')
plt.ylabel('Vendas Totais')
plt.title('Tendência de vendas totais mensais')

# Encontra os meses de pico de vendas.
pico_vendas_meses = [month for month, sales in zip(months, total_sales) if sales == max(total_sales)]
for month in pico_vendas_meses:
    plt.annotate('Pico', xy=(month, max(total_sales)), xytext=(month, max(total_sales) + 100),
                 arrowprops=dict(arrowstyle='->'))

# Exibe o gráfico de linhas.
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()