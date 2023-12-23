from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time 
import pandas as pd


browser = webdriver.Chrome("D:/Setup/chromedriver_win32/chromedriver.exe")
browser.get(START_URL)

scraped_data = []


#Define data scrapping method
def scrape():

#find <table>
 bright_star_table = soup.find("table", attrs={"class","wikitable"})

#find <body>
 table_body = bright_star_table.find('tbody')

#find <tr>
 table_rows = table_body.find_all('tr')

#find <td> tags by looping all <tr> tags and get all column data

#get data from <td>
 for row in table_rows:
    table_cols+ row.find_all('td')
    print(table_cols)

    temp_list= []

    for col_data in table_cols:
        #print only columns textual data using ".text" property
        print(col_data.text)

        #remove extra while spaces using strip()method
        data = col_data.text.strip()
        print(data)

    temp_list.append(data)

    #append data to star data list
    scraped_data.append(temp_list)

    stars_data=[]

    for i in range(0,len(scraped_data)):

        Star_names = scraped_data[i][1]
        Distance = scraped_data[i][3]
        Mass = scraped_data[i][5]
        Radius = scraped_data[i][6]
        Lum = scraped_data[i][7]
