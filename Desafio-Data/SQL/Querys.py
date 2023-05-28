import csv
import mysql.connector


# Estabelece uma conexão com o banco de dados MySQL.
conexao = mysql.connector.connect(
    host='localhost',
    user='jp_sd',
    password='santodigital',
    database='Data-AdventureWorks'
)

cursor = conexao.cursor()

# Passando todas as Queries.
queries = [
    """
    SELECT CONCAT(c.FirstName, ' ', c.LastName) AS Cliente, COUNT(s.orderNumber) AS Total_Pedidos
    FROM customer AS c
    JOIN sales AS s ON c.CustomerKey = s.CustomerKey 
    GROUP BY c.CustomerKey 
    ORDER BY Total_Pedidos DESC 
    LIMIT 1;
    """,
    """
    SELECT p.productname AS produto, SUM(v.OrderQuantity) AS total_vendido
    FROM products AS p
    JOIN sales AS v ON p.ProductKey = v.ProductKey 
    JOIN product_category AS c ON p.ProductSubCategoryKey = c.productcategorykey
    WHERE c.categoryname = 'Bikes'
    GROUP BY p.ProductKey 
    ORDER BY total_vendido DESC
    LIMIT 10;
    """,
    """
    SELECT MONTH(s.OrderDate) AS mês, SUM(p.ProductPrice * s.OrderQuantity) AS valor_total
    FROM sales as s
    JOIN products as p ON s.ProductKey  = p.ProductKey 
    GROUP BY mês
    ORDER BY valor_total desc 
    LIMIT 1;
    """,
    """
    SELECT Region, Country, ROUND(media_vendas, 2) AS media_vendas
    FROM (
    SELECT Region, Country, media_vendas,
           ROW_NUMBER() OVER (PARTITION BY Region ORDER BY media_vendas DESC) AS row_num
    FROM (
            SELECT Region, Country, AVG(p.ProductPrice * s.OrderQuantity) AS media_vendas
            FROM territories AS t
            LEFT JOIN sales AS s ON t.SalesTerritoryKey = s.TerritoryKey
            LEFT JOIN products AS p ON s.ProductKey = p.ProductKey
            GROUP BY Region, Country
    ) AS vendas_por_regiao
    WHERE media_vendas > (
        SELECT AVG(media_vendas)
        FROM (
                SELECT AVG(p.ProductPrice * s.OrderQuantity) AS media_vendas
                FROM sales AS s
                JOIN products AS p ON s.ProductKey = p.ProductKey
                GROUP BY MONTH(s.OrderDate)
            ) AS media_mensal
        )
    ) AS vendas_numeradas
    WHERE row_num = 1
    ORDER BY media_vendas DESC;
    """,
    """
    SELECT ps.SubCategoryName as Sub_Categoria, p.ProductName as Nome_Produto, SUM(s.OrderQuantity) AS Total_Vendido
    FROM product_subcategories as ps
    JOIN products AS p ON ps.ProductSubCategoryKey  = p.ProductSubCategoryKey 
    JOIN sales AS s ON p.ProductKey = s.ProductKey
    GROUP BY ps.SubCategoryName, p.ProductName
    ORDER BY Total_Vendido asc
    LIMIT 10;
    """
]

# Executa as consultas e gera arquivos CSV.
for i, query in enumerate(queries):

    cursor.execute(query)

    # Busca todos os resultados.
    results = cursor.fetchall()

    # Define o caminho do arquivo CSV.
    arquivo_csv = f'query_{i}.csv'

    # Grava os resultados em um arquivo CSV.
    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)

        # Escreve o Cabeçalho.
        if i == 0:
            writer.writerow(['Cliente', 'Total_Pedidos'])
        elif i==1:
            writer.writerow(['Produto', 'Total_Vendido'])
        elif i ==2:
            writer.writerow(['Mes', 'Valor_Total'])
        elif i==3:
            writer.writerow(['Regiao', 'Pais', 'Media_Vendas'])
        else:
            writer.writerow(['Sub_Categoria', 'Nome_Produto', 'Total_Vendido'])
        

        writer.writerows(results) 

    print(f"O arquivo '{arquivo_csv}' gerado com sucesso!")

# Encerra o cursor e as conexões.
conexao.commit()
conexao.close()

print("Todos os arquivos foram gerados com sucesso!")