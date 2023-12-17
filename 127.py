from bs4 import BeautifulSoup
import time 
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

START_URL = "https://en.wikipedia.org/wiki/Lists_of_stars"

browser = webdriver.Chrome("C:/Users/Asus/Downloads/pro127/chromedriver_win32/chromedriver.exe")
browser.get(START_URL)

time.sleep(10)

scrapped_data = []

def scrape():

    soup = BeautifulSoup(browser.page_source, "html.parser")

    bright_star_table = soup.find("table",attrs = {"class","wikitable"})

    table_body = bright_star_table.find('tbody')

    table_rows = table_body.find_all('tr')

    for row in table_rows:
        table_cols = row.find_all('td')
        #print(table_cols)

        temp_list = []

        for col_data in table_cols:
            #print(col_data.text)
            data = col_data.text.strip()
            #print(data)
            temp_list.append(data)
        
        scrapped_data.append(temp_list)
        
scrape()

stars_data = []


for i in range(0,len( scrapped_data)):
    
    Star_names =  scrapped_data[i][1]
    Distance =  scrapped_data[i][3]
    Mass =  scrapped_data[i][5]
    Radius =  scrapped_data[i][6]
    Lum =  scrapped_data[i][7]

    required_data = [Star_names, Distance, Mass, Radius, Lum]
    stars_data.append(required_data)

print(stars_data)

headers = ['Star_name','Distance','Mass','Radius','Luminosity']  
 
star_df_1 = pd.DataFrame(stars_data, columns=headers)

star_df_1.to_csv('scrapped_data.csv',index=True, index_label="id")





