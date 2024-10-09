import pandas as pd 

tabela = pd.read_csv("cancelamentos.csv")

tabela= tabela.drop(collumns="CustomerID")
display(tabela)

display(tabela.info())

