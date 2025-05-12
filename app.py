import tkinter as tk
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from openpyxl import load_workbook
from datetime import datetime, time
from tkinter import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time




root = tk.Tk()
pointer = 1


root.title("Temperature Catcher - São Paulo")
#root.configure(background="white")
root.minsize(200, 200)
root.maxsize(500, 500)
root.geometry("100x100+25+25")

tk.Label(root, text = "Atualizar Previsão na planilha")

curTime=datetime.now()


tk.Label(root, text=curTime.date()).pack(side=tk.BOTTOM)


tk.Label(root, text='Buscar dados de Temperatura').pack()
searchButton=tk.Button(root,text="Buscar").pack()


def obter_temperatura_sao_paulo():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(options=options)
    try:
        driver.get("https://www.google.com/search?q=previsao+do+tempo+em+sao+paulo")
        driver.get("https://www.climatempo.com.br/previsao-do-tempo/agora/cidade/558/saopaulo-sp")

        temperatura = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "span.-bold.-gray-dark-2.-font-55._margin-l-20._center"))).text
        

        return temperatura
    finally:
        driver.quit()

temp = obter_temperatura_sao_paulo()


print(f"Temperatura em São Paulo: {temp}°C")


root.mainloop()



