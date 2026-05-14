# 📊 Análise de Vendas com Python e Excel

Projeto desenvolvido por **Raphael Campos Squilaro** para realizar análise de vendas utilizando arquivos Excel com Python, através das bibliotecas **Pandas** e **OpenPyXL**.

---

# 🚀 Objetivo do Projeto

Este projeto realiza a leitura de uma planilha Excel contendo informações de vendas de produtos.

O sistema:

- Agrupa os dados por:
  - ID do Produto
  - Nome do Produto
- Soma a quantidade total vendida de cada item
- Exibe os resultados no terminal

---

# 🛠️ Tecnologias Utilizadas

- Python 3
- Pandas
- OpenPyXL
- Excel (.xlsx)

---

# 📂 Estrutura do Projeto

```bash
📁 projeto-vendas/
│
├── vendas.xlsx
├── analytics_vendas.py
└── README.md
```

---

# 📥 Instalação do Python

Caso ainda não tenha o Python instalado:

## Windows

1. Acesse:
   
   https://www.python.org/downloads/

2. Faça o download da versão mais recente.

3. Durante a instalação:
   - Marque a opção:

```bash
Add Python to PATH
```

4. Finalize a instalação.

---

# 📦 Instalação das Bibliotecas

Após instalar o Python, abra o terminal ou CMD e execute:

```bash
pip install pandas openpyxl
```

---

# 📄 Estrutura da Planilha Excel

O arquivo `vendas.xlsx` deve possuir as seguintes colunas:

| ID_Produto | Nome_Produto | Quantidade_Vendida |
|------------|--------------|--------------------|
| 101 | Notebook | 5 |
| 101 | Notebook | 3 |
| 202 | Mouse | 10 |

---

# 🧠 Explicação do Código

## 1. Importação do Pandas

```python
import pandas as pd
```

O Pandas é utilizado para leitura e manipulação de dados.

---

## 2. Leitura da Planilha Excel

```python
planilha = pd.read_excel('vendas.xlsx')
```

Aqui o Python realiza a leitura do arquivo Excel e transforma os dados em um DataFrame.

---

## 3. Agrupamento dos Dados

```python
resultado = planilha.groupby(["ID_Produto", "Nome_Produto"])["Quantidade_Vendida"].sum()
```

O método:

```python
groupby()
```

agrupa os dados por:

- ID do Produto
- Nome do Produto

Depois:

```python
sum()
```

realiza a soma da quantidade vendida de cada produto.

---

## 4. Exibição dos Resultados

```python
for (identificacao, nome), quantidade in resultado.items():
    print(f'{identificacao} - {nome} - {quantidade}')
```

O `for` percorre todos os dados agrupados e exibe os resultados no terminal.

---

# 💻 Código Completo

```python
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
```

---

# ▶️ Como Executar o Projeto

No terminal, dentro da pasta do projeto, execute:

```bash
python analytics_vendas.py
```

---

# ✅ Exemplo de Saída

```bash
101 - Notebook - 8
202 - Mouse - 10
```

---

# 📈 Possíveis Melhorias Futuras

- Exportar relatório consolidado para Excel
- Criar gráficos automáticos de vendas
- Dashboard com Power BI
- Integração com banco de dados
- Sistema de análise de estoque
- Interface gráfica para usuários

---

# 👨‍💻 Autor

## Raphael Campos Squilaro

Projeto desenvolvido para estudos de análise de dados, automação e analytics com Python.
