# "Pandas" É uma biblioteca popular para análise e manipulação de dados. 
# Ela fornece estruturas de dados de alto desempenho e fáceis de usar, como o DataFrame, que permite trabalhar com dados tabulares. 
# Neste código, o pandas é usado para carregar e manipular os dados do arquivo CSV.

# Importação do Pandas.
import pandas as pd

# O caminho do arquivo CSV é definido usando a variável path.
path = r"F:\REPOSITORIOS\Repositorio-SantoDigital\Desafio-Data\AdventureWorks_Sales_2017.csv"

# O pandas lê o arquivo CSV usando o método pd.read_csv().
df = pd.read_csv(
    path,
    parse_dates=["OrderDate", "StockDate"],
    dayfirst=True,
    encoding="latin1",
)

# O código converte as colunas "OrderDate" e "StockDate" em strings com o formato "%Y/%m/%d" usando o método dt.strftime().
df["OrderDate"] = df["OrderDate"].dt.strftime("%Y/%m/%d")
df["StockDate"] = df["StockDate"].dt.strftime("%Y/%m/%d")


# O caminho para o novo arquivo CSV é definido usando a variável new_path.
new_path = r"F:\REPOSITORIOS\Repositorio-SantoDigital\Desafio-Data\formatado\AdventureWorks_Sales_2017_tratado.csv"

#DataFrame resultante é salvo em um novo arquivo CSV usando o método to_csv(). Algumas opções são fornecidas:
df.to_csv(new_path, index=False)