import csv
import pandas as pd
import mysql.connector

# Estabelece conexão com o banco de dados MYSQL.
conexao = mysql.connector.connect(
    host='localhost',
    user='jp_sd',
    password='santodigital',
    database='Data-AdventureWorks'
)

# O cursor é criado para executar as consultas no banco de dados.
cursor = conexao.cursor()

caminho_csv1 = 'F:\REPOSITORIOS\Repositorio-SantoDigital\Desafio-Data\Datasets\Calendar\AdventureWorks_Calendar_tratado.csv'
tabela1 = 'calendar'

# Os dados do arquivo CSV são lidos usando o pd.read_csv(), que retorna um DataFrame do pandas contendo os dados do arquivo CSV.
dados_csv = pd.read_csv(caminho_csv1)

# O arquivo CSV é aberto em modo de leitura usando open() e o csv.reader() é criado passando o arquivo aberto.
with open(caminho_csv1, 'r') as arquivo_csv:
    leitor_csv = csv.reader(arquivo_csv)

    # A primeira linha do arquivo CSV é lida como cabeçalho usando next(leitor_csv).
    cabecalho = next(leitor_csv)

    # Em um loop for, cada linha do arquivo CSV é iterada.
    for linha in leitor_csv:

        # Os valores da linha são convertidos em uma tupla usando tuple(linha).
        valores = tuple(linha) 

        # O cabeçalho das colunas é convertido em uma string usando ', '.join(cabecalho).
        colunas = ', '.join(cabecalho)

        # Os marcadores de posição dos valores são criados usando ', '.join(['%s'] * len(cabecalho)).
        valores_placeholder = ', '.join(['%s'] * len(cabecalho)) 

        # Uma consulta SQL de inserção é construída usando as variáveis tabela1, colunas e valores_placeholder.
        query = f"INSERT INTO {tabela1} ({colunas}) VALUES ({valores_placeholder})" 

         # A consulta SQL é executada pelo cursor usando cursor.execute() e os valores da linha são passados como argumento.
        cursor.execute(query, valores)

# A mesma coisa se repete durante o código, mudando apenas a variavel "caminho_csv" e "tabela".
caminho_csv2 = 'F:\REPOSITORIOS\Repositorio-SantoDigital\Desafio-Data\Datasets\Products\AdventureWorks_Product_Categories.csv'
tabela2 = 'product_category'

with open(caminho_csv2, 'r') as arquivo_csv:
    leitor_csv = csv.reader(arquivo_csv)

    cabecalho = next(leitor_csv)

    for linha in leitor_csv:
        valores = tuple(linha)
        colunas = ', '.join(cabecalho)
        valores_placeholder = ', '.join(['%s'] * len(cabecalho))
        query = f"INSERT INTO {tabela2} ({colunas}) VALUES ({valores_placeholder})"
        cursor.execute(query, valores)


caminho_csv3 = 'F:\REPOSITORIOS\Repositorio-SantoDigital\Desafio-Data\Datasets\Products\AdventureWorks_Product_Subcategories.csv'
tabela3 = 'product_subcategories'

with open(caminho_csv3, 'r') as arquivo_csv:
    leitor_csv = csv.reader(arquivo_csv)

    cabecalho = next(leitor_csv)

    for linha in leitor_csv:
        valores = tuple(linha)
        colunas = ', '.join(cabecalho)
        valores_placeholder = ', '.join(['%s'] * len(cabecalho))
        query = f"INSERT INTO {tabela3} ({colunas}) VALUES ({valores_placeholder})"
        cursor.execute(query, valores)

caminho_csv4 = 'F:\REPOSITORIOS\Repositorio-SantoDigital\Desafio-Data\Datasets\Products\AdventureWorks_Products.csv'
tabela4 = 'products'

with open(caminho_csv4, 'r') as arquivo_csv:
    leitor_csv = csv.reader(arquivo_csv)

    cabecalho = next(leitor_csv)

    for linha in leitor_csv:
        valores = tuple(linha)
        colunas = ', '.join(cabecalho)
        valores_placeholder = ', '.join(['%s'] * len(cabecalho))
        query = f"INSERT INTO {tabela4} ({colunas}) VALUES ({valores_placeholder})"
        cursor.execute(query, valores)


caminho_csv5 = 'F:\REPOSITORIOS\Repositorio-SantoDigital\Desafio-Data\Datasets\Territories\AdventureWorks_Territories.csv'
tabela5 = 'territories'

with open(caminho_csv5, 'r') as arquivo_csv:
    leitor_csv = csv.reader(arquivo_csv)

    cabecalho = next(leitor_csv)

    for linha in leitor_csv:
        valores = tuple(linha)
        colunas = ', '.join(cabecalho)
        valores_placeholder = ', '.join(['%s'] * len(cabecalho))
        query = f"INSERT INTO {tabela5} ({colunas}) VALUES ({valores_placeholder})"
        cursor.execute(query, valores)


caminho_csv6 = 'F:\REPOSITORIOS\Repositorio-SantoDigital\Desafio-Data\Datasets\Customers\AdventureWorks_Customers_tratado.csv'
tabela6 = 'customer'

with open(caminho_csv6, 'r') as arquivo:
    leitor_csv = csv.DictReader(arquivo)
    
    cabecalho = next(leitor_csv)

    for linha in leitor_csv:
        valores = tuple(linha)
        colunas = ', '.join(cabecalho)
        valores_placeholder = ', '.join(['%s'] * len(cabecalho))
        query = f"INSERT INTO {tabela6} ({colunas}) VALUES ({valores_placeholder})"
        cursor.execute(query, valores)

caminho_csv7 = 'F:\REPOSITORIOS\Repositorio-SantoDigital\Desafio-Data\Datasets\Returns\AdventureWorks_Returns_tratado.csv'
tabela7 = 'returns'

with open(caminho_csv7, 'r') as arquivo_csv:
    leitor_csv = csv.reader(arquivo_csv)

    cabecalho = next(leitor_csv)

    for linha in leitor_csv:
        valores = tuple(linha)
        colunas = ', '.join(cabecalho)
        valores_placeholder = ', '.join(['%s'] * len(cabecalho))
        query = f"INSERT INTO {tabela7} ({colunas}) VALUES ({valores_placeholder})"
        cursor.execute(query, valores)

caminho_csv8 = 'F:\REPOSITORIOS\Repositorio-SantoDigital\Desafio-Data\Datasets\Sales\AdventureWorks_Sales_2015_tratado.csv'
tabela8 = 'sales'

with open(caminho_csv8, 'r') as arquivo_csv:
    leitor_csv = csv.reader(arquivo_csv)

    cabecalho = next(leitor_csv)

    for linha in leitor_csv:
        valores = tuple(linha)
        colunas = ', '.join(cabecalho)
        valores_placeholder = ', '.join(['%s'] * len(cabecalho))
        query = f"INSERT INTO {tabela8} ({colunas}) VALUES ({valores_placeholder})"
        cursor.execute(query, valores)


caminho_csv9 = 'F:\REPOSITORIOS\Repositorio-SantoDigital\Desafio-Data\Datasets\Sales\AdventureWorks_Sales_2016_tratado.csv'
tabela9 = 'sales'

with open(caminho_csv9, 'r') as arquivo_csv:
    leitor_csv = csv.reader(arquivo_csv)

    cabecalho = next(leitor_csv)

    for linha in leitor_csv:
        valores = tuple(linha)
        colunas = ', '.join(cabecalho)
        valores_placeholder = ', '.join(['%s'] * len(cabecalho))
        query = f"INSERT INTO {tabela9} ({colunas}) VALUES ({valores_placeholder})"
        cursor.execute(query, valores)


caminho_csv10 = 'F:\REPOSITORIOS\Repositorio-SantoDigital\Desafio-Data\Datasets\Sales\AdventureWorks_Sales_2017_tratado.csv'
tabela10 = 'sales'

with open(caminho_csv10, 'r') as arquivo_csv:
    leitor_csv = csv.reader(arquivo_csv)

    cabecalho = next(leitor_csv)

    for linha in leitor_csv:
        valores = tuple(linha)
        colunas = ', '.join(cabecalho)
        valores_placeholder = ', '.join(['%s'] * len(cabecalho))
        query = f"INSERT INTO {tabela10} ({colunas}) VALUES ({valores_placeholder})"
        cursor.execute(query, valores)

# Após a execução de todas as linhas, as alterações no banco de dados são confirmadas usando conexao.commit().
conexao.commit()
# Fechando a conexão
conexao.close()

