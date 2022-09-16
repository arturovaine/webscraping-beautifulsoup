# https://stackoverflow.com/questions/28259301/how-to-convert-an-xml-file-to-nice-pandas-dataframe

#%%
# Importing BeautifulSoup and 
# it is in the bs4 module
from bs4 import BeautifulSoup

#%%
# Opening the html file. If the file
# is present in different location, 
# exact location need to be mentioned
HTMLFileToBeOpened = open("Produtos.html", "r")
  
# Reading the file and storing in a variable
contents = HTMLFileToBeOpened.read()
  
# Creating a BeautifulSoup object and
# specifying the parser 
beautifulSoupText = BeautifulSoup(contents, 'lxml')
  
# Using the prettify method to modify the code
#  Prettify() function in BeautifulSoup helps
# to view about the tag nature and their nesting
# print(beautifulSoupText.body.prettify())

#%%
print('1', type(beautifulSoupText)) # <class 'bs4.BeautifulSoup'>
print('2', type(beautifulSoupText.body)) # <class 'bs4.element.Tag'>
print('3', type(beautifulSoupText.body.prettify())) # <class 'str'>

#%%
import pandas as pd
import xml.etree.ElementTree as ET
import io

#%%
xml_data = io.StringIO(beautifulSoupText.body.prettify())

etree = ET.parse(xml_data) #create an ElementTree object 
doc_df = pd.DataFrame(list(iter_docs(etree.getroot())))

doc_df
# %%
print(doc_df)
# %%
print(etree)
# %%
# print(beautifulSoupText.body.prettify())
# %%
teste = pd.read_xml(path_or_file)
print(type(teste))
# %%
import pandas as pd
data=pd.read_html('Produtos.html',skiprows=0)[0]
# %%
data
# %%
data.head()
# %%
type(data)
# %%
df = pd.DataFrame(data)
# %%
data[0,1,1]
# %%
data.columns = [
'CODIGO',
'ATIVO',
'DESCRICAO',
'REFERENCIA',
'BARRAS',
'GRUPO',
'SUBGRUPO',
'FAMILIA',
'FORNEC',
'PR_NOTA',
'PR_MEDIO',
'PR_CUSTO',
'PR_VEND',
'PR_VENDAP',
'MARGEM_L',
'ULT_COMP',
'ULT_VENDA',
'ULT_ATUL',
'ULT_ALTE',
'ESTOQUE',
'ESTOQUED',
'EST_MIN',
'ALIQ',
'COMISSAO',
'EDITAPRECO',
'COTAR',
'GOND',
'CUSTO_CAL',
'DIASCOMPRA',
'FATOR',
'CODPRINC',
'CATEGORIA',
'DESC_CATEG',
'VET_PART',
'VET_VENCTO',
'ULT_MOVI',
'USUARIO',
'EMBALAGEM',
'PRECO_MIN',
'CODFORNEC',
'NCM',
'EQUIVAL',
'CODEQUIVAL',
'VET_FABRI',
'PISCOFINS',
'LIMITEAP',
'PRATELEIRA',
'COR',
'UN',
'TAB_DESC',
'COD_GEN',
'COD_EX_IPI',
'COD_COMB',
'TIPO_ITEM',
'OBS2',
'TIPO_MARG',
'PIS_NATCRE',
'BLOQEST',
'VET_LABO',
'TIPO_COMP',
'UNDFISCAL',
'ATAC_QTD',
'ATAC_PRECO',
'UNDCOMPRA',
'CEST',
'ATAC_DESCM',
'DT_REG',
'SERIAL',
'OBS',
'EANTRIB'
]

data.head()
# %%
# %%
df = data.drop(0)
df

# %%
import openpyxl
df.to_excel('Produtos.xlsx')
# %%
df.to_csv('Produtos.csv')
# %%
