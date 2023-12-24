import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pathlib import Path
from pyshadow.main import Shadow
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import re
import time
from bs4 import BeautifulSoup
import requests
import os 

#  chrome.exe --remote-debugging-port=9191 --user-data-dir=""C:\Users\dougl\OneDrive\Documentos\robo1"


PATH = r"C:\Users\dougl\OneDrive\Documentos\chromedriver.exe"
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_experimental_option("debuggerAddress", "localhost:9191")
driver = webdriver.Chrome(PATH, options=chrome_options)

def betway():
    #odd time esquer /html/body/div[1]/div/div[3]/div/div[1]/div/div[2]/div[4]/div/div[3]/div/div[2]/div/div[3]/div/div[1]/div[2]/div/div[4]/div/div[1]/div[1]/div[2]/div/div[3]/div
    odd_1 = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div/div[1]/div/div[2]/div[4]/div/div[3]/div/div[2]/div/div[3]/div/div[1]/div[2]/div/div[4]/div/div[1]/div[1]/div[2]/div/div[3]/div').text
    odd_1_titulo = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div/div[1]/div/div[2]/div[4]/div/div[3]/div/div[2]/div/div[3]/div/div[1]/div[2]/div/div[3]/div[1]').text
    #emapte
    odd_2 = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div/div[1]/div/div[2]/div[4]/div/div[3]/div/div[2]/div/div[3]/div/div[1]/div[2]/div/div[4]/div/div[1]/div[2]/div[2]/div/div[3]/div').text
    odd_2_titulo = "Empate"
    #time direita
    odd_3 = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div/div[1]/div/div[2]/div[4]/div/div[3]/div/div[2]/div/div[3]/div/div[1]/div[2]/div/div[4]/div/div[1]/div[3]/div[2]/div/div[3]/div').text
    odd_3_titulo = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div/div[1]/div/div[2]/div[4]/div/div[3]/div/div[2]/div/div[3]/div/div[1]/div[2]/div/div[3]/div[3]').text
    print(odd_1,odd_1_titulo)
    print(odd_2,odd_2_titulo)
    print(odd_3,odd_3_titulo)
    return float(odd_1),float(odd_2),float(odd_3)
def bet365():
    #odd time esquer 
    odd_1 = driver.find_element(By.XPATH, '/html/body/div/div/div[3]/div[3]/div/div/div/div[1]/div/div/div[2]/div/div/div[2]/div[2]/div/div/div[1]/span[2]').text
    odd_1_titulo = driver.find_element(By.XPATH, '/html/body/div/div/div[3]/div[3]/div/div/div/div[1]/div/div/div[2]/div/div/div[2]/div[2]/div/div/div[1]/span[1]').text
    #emapte
    odd_2 = driver.find_element(By.XPATH, '/html/body/div/div/div[3]/div[3]/div/div/div/div[1]/div/div/div[2]/div/div/div[2]/div[2]/div/div/div[2]/span[2]').text
    odd_2_titulo = "Empate"
    #time direita
    odd_3 = driver.find_element(By.XPATH, '/html/body/div/div/div[3]/div[3]/div/div/div/div[1]/div/div/div[2]/div/div/div[2]/div[2]/div/div/div[3]/span[2]').text
    odd_3_titulo = driver.find_element(By.XPATH, '/html/body/div/div/div[3]/div[3]/div/div/div/div[1]/div/div/div[2]/div/div/div[2]/div[2]/div/div/div[3]/span[1]').text
    print(odd_1,odd_1_titulo)
    print(odd_2,odd_2_titulo)
    print(odd_3,odd_3_titulo)
    return odd_1,odd_2,odd_3
def rivalry():
    #odd time esquer //*[@id="__layout"]/div/div[1]/div[1]/div/div[3]/div/div[2]/div[3]/span/div/div/a[1]/div[2]/span
    odd_1 = driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[1]/div[1]/div/div[3]/div/div[2]/div[3]/span/div[1]/div/a[1]/div[2]/span').text
    odd_1_titulo = driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[1]/div[1]/div/div[3]/div/div[2]/div[3]/span/div[1]/div/a[1]/div[1]').text
    #emapte
    odd_2 = driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[1]/div[1]/div/div[3]/div/div[2]/div[3]/span/div[1]/div/a[3]/div[2]/span').text
    odd_2_titulo = "Empate"
    #time direita
    odd_3 = driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[1]/div[1]/div/div[3]/div/div[2]/div[3]/span/div[1]/div/a[2]/div[2]/span').text
    odd_3_titulo = driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[1]/div[1]/div/div[3]/div/div[2]/div[3]/span/div[1]/div/a[2]/div[1]').text
    print(odd_1,odd_1_titulo)
    print(odd_2,odd_2_titulo)
    print(odd_3,odd_3_titulo)
    return float(odd_1),float(odd_2),float(odd_3)
#driver.execute_script("window.open('https://betway.com/pt/sports/evt/11408303')")
#driver.execute_script("window.open('https://www.bet365.com/#/AC/B1/C1/D8/E135944930/F3/I0/')")    
#driver.execute_script("window.open('https://www.rivalry.com/pt/match/football/brazil-serie-a/855581-vasco-da-gama-vs-bahia')")
dict_defs = {"betway":betway,"rivalry":rivalry}
#time.sleep(2)
direita= []
empate = []
esquerda = []
casas = []
while True:
    direita= []
    empate = []
    esquerda = []
    casas = []
    for handle in driver.window_handles:
        driver.switch_to.window(handle)
        link = driver.current_url 
        for j,i in dict_defs.items():
            if j in link:
                print(j)
                x,y,z = i()
                casas.append(j)
                esquerda.append(x)
                empate.append(y)
                direita .append(z)
    value = 1/max(esquerda)+ 1/max(empate) + 1/max(direita)
    if value < 1:
        print("APOSTA")
        break


            


quit()

actions = ActionChains(driver)
time.sleep(1.3)
start = time.time()
###BETWAY

print(time.time() - start)



print(odd_1,odd_1_titulo)
print(odd_2,odd_2_titulo)
print(odd_3,odd_3_titulo)