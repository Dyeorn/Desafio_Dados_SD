# SANTO DIGITAL 2023
### Desafio de Dados

## Linguagem utilizada para realização do desafio de Lógica de Progamação: 
* Python

## Linguagens e frameworks utilizados para a realização do desafio de Dados:
* Python;
* MySQL;
* DBeaver.

### Etapas realizadas:
1. Analise básica dos CSV's do Database AdventureWorks;
2. Modelagem do DER (Diagrama de Entidade-Relacionamento) Diretamente do MySQL Workbench;
3. Modelagem do Banco de Dados pelo MySQL Workbench;
4. Alteração das datas para a forma aceita pelo MySQL;
5. Abastecimento do Banco de Dados via Python (Pandas, mysql.connector, CSV) e via DBeaver (através da importação do CSV);
6. Visualização dos dados pelo framework DBeaver;
7. Querys (MySQL Workbench);
8. Uso do Python para gerar os CSVs;

### Diretórios
* Desafio_Logica_Progamação -> Possui os 3 arquivos .py das questões;
* Desafio_Data_ -> Possui as pastas separadas de cada ação (Datasets, Gráficos, SQL);
* Datasets -> Possui os arquivos com a extensão .CSV disponibilizados;
* Gráficos -> Possui todos os arquivos relacionados a criação dos gráficos;
* SQL -> Possui o arquivo .SQL da criação do banco de dados, o diagrama (em .MWB, .PNG e .PDF), os arquivos .PY (formatação de data e abastecimento do banco de dados);
* Queries -> Possui os arquivos .CSV gerados pelas Queries.

### Observação:
Durante a Query do 4° item da tarefa II, e após análise dos arquivos disponibilizados, foi percebido que não tem uma tabela para "Vendedores", ficando assim uma dúvida de como faria para calcular "Quais vendedores tiveram vendas com valor acima da média no
último ano fiscal?".

* A decisão que tomei foi em fazer essa média usando o parametro "Regiões" em vez de "Vendedores".

* Os arquivos na pasta "Dataset" que contém "_tratado.csv" foram alterados (formato das datas).
