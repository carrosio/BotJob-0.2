import pandas as pd
import json
from os import system, name
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(
    executable_path='/home/mauri/Desktop/BotJob-0.1/chromedriver')
#driver.minimize_window()

jobs_saved = pd.read_json('data.json')

if len(jobs_saved) < 1:
    xample = {
        'id': [0],
        'link': [0],
        'name': [0]
    }

    jobs_saved = pd.DataFrame(xample)

link_base = "https://ar.computrabajo.com/empleos-en-capital-federal?by=publicationtime&p="

next = True

for i in range(1, 10):

    if not next:
        break

    #CONNECT THE LINK
    driver.get(
        f'{link_base}{i}')
    
    #FIND THE JOBS IN THE WEBSITE
    article_list = driver.find_elements(By.TAG_NAME, 'article')

    if len(article_list) == 0:
        print('No more PAGES!')
        break

    print("Scanning Articles from page: ", i)

    for article in article_list:

        if article.get_attribute('id') in jobs_saved.id.array:
            print('Already Saved Job', article.get_attribute('id'))
            next = False
            break
            
        final_link = 0
        name = 0

        article_links = article.find_elements(By.TAG_NAME, 'a')

        for link_article in article_links:

            result = str(link_article.get_attribute('href'))

            if result.find('oferta-de-trabajo') != -1:
                name = link_article.text
                final_link = result

        obj = {
            "id": article.get_attribute('id'),
            "link": final_link,
            'name': name
        }

        new_series = pd.Series(obj)

        jobs_saved = pd.concat(
            [jobs_saved, new_series.to_frame().T], ignore_index=True)

        jobs_saved.to_json('data.json')

        print(f'Job {name} saved!')

jobs_saved.to_json('data.json')

driver.close()

