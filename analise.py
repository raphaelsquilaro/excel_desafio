#Author: Raphael Campos Squilaro
#Project: Excel painel analytics with python and imported of pandas and openpyxl

#Import the dependencies pandas
import pandas as pd

#Insert the excel for reading
planilha = pd.read_excel('vendas.xlsx')

#Group by name
resultado = planilha.groupby(["ID_Produto" , "Nome_Produto"])["Quantidade_Vendida"].sum()

#loop for sum
for (identificacao, nome), quantidade in resultado.items():
        print(f'{identificacao} - {nome} - {quantidade}')