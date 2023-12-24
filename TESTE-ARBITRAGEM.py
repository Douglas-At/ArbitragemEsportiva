import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
from lxml import etree
import os 
import xlwings as xw
from datetime import datetime,timedelta
import shutil
import logging


PATH = r"C:\Users\dougl\OneDrive\Documentos\chromedriver.exe"
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_experimental_option("debuggerAddress", "localhost:9191")
driver = webdriver.Chrome(PATH, options=chrome_options)


#driver.get('https://oddspedia.com/basketball/odds')


# Find the 'img' tag and get the value of the 'alt' attribute
'''img_tag = soup.find_all('img',class_="lazyLoad isLoaded")
lista_casas= []
print(img_tag)
for alt in img_tag:
    alt_attribute = alt.get('alt')
    print(alt_attribute)
    lista_casas.append(alt_attribute)
print(lista_casas)
'''
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
table = soup.find('div', class_="ml__wrap ml__wrap--is-odds")
print(table)
linha =[]
for row in table.find_all("div",class_="match-list-item match-list-item--with-odds match-list-item--no-score"):
    #print(row)
    
    nome1 = row.find_all("div",class_="match-team__name")
    nomes = [td.text.strip() for td in nome1]

    odds1  = row.find_all("span",class_="odd__value")
    odds = [td.text.strip() for td in odds1]

    if odds == []:
        odds = [0,0]
    
    lista = nomes+ odds
    
    try:
        linha.append(lista)
    except:
        print(lista)
    #lista com os 2 nomes 
    #pegar as odds agora 
    
print(linha)
df = pd.DataFrame(linha)
df.columns = ['home','away','odd h','odd a']
df = df[df['odd a'] != 0]
df['odd a'] =pd.to_numeric(df['odd a'])
df['odd h'] =pd.to_numeric(df['odd h'])
df['inverso'] = 1/df['odd h'] + 1/df['odd a']
df['aposta1'] = 1000/(df['inverso']*df['odd h'])
df['aposta2'] = 1000/(df['inverso']*df['odd a'])
df['ganho'] = 1000/df['inverso']
df['entrada'] = False
df.loc[df['ganho']>1000, "entrada"] = True

df.to_excel("teste_ARBITRAGEM.xlsx")
            
            
            
    
    
quit()
    	
df = pd.read_html(str(table))
data_atual = datetime.today().date()
df[0].to_excel(fr"\\10.0.0.29\projetos BI\CRM\campanhas\{data_atual}_regua relacionamento.xlsx")
driver.execute_script("document.body.style.zoom='100%'")
