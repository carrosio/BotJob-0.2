import pandas as pd
import json
from os import system, name

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(
    executable_path='chromedriver')
driver.minimize_window()

jobs_saved = pd.read_json('data.json')

if len(jobs_saved) < 1:
    xample = {
        'id': [0],
        'link': [0],
        'name': [0]
    }

    jobs_saved = pd.DataFrame(xample)

config = pd.read_json('config.json')
link_base = config.link[0]
limit_find = config.limit_jobs[0]
#temp_json = []

next = True

for i in range(1, 999):
    
    if i == int(limit_find):
        break

    driver.get(f'{link_base}{i}')

    #driver.find_element(By.TAG_NAME, next_btm).click()

    article_list = driver.find_elements(By.TAG_NAME, 'article')

    if len(article_list) == 0:
        print('No more PAGES!')
        break

    print("Scanning Articles from page: ", i)

    for article in article_list:

        if article.get_attribute('id') in jobs_saved.id.array:
            print('Already Saved Job', article.get_attribute('id'))
            continue

        final_link = 0
        name = 0

        article_links = article.find_elements(By.TAG_NAME, 'a')

        #link_direct = article.find_element(By.XPATH, '//*[@id="0976EABFF3F479EA61373E686DCF3405"]/div[1]/h1/a').get_attribute('href')

        # print(link_direct)

        for link_article in article_links:

            result = str(link_article.get_attribute('href'))

            if result.find('oferta-de-trabajo') != -1:
                name = link_article.text
                final_link = result

        # link = f'https://ar.computrabajo.com/ofertas-de-trabajo/oferta-de-trabajo-de-{article.get_attribute("id")}#lc=ListOffers-Score-0'

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

# print(jobs_saved)

jobs_saved.to_json('data.json')

driver.close()

# except:

# driver.close()
