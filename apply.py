
from var import FINAL_LINK, MAXIMIZE, COUNTRY, POSTULATE, LOGGIN_TEXT, CONTINUE
from os import system, name

import pandas as pd
import json
import time
import os

from selenium import webdriver
from selenium.webdriver.common.by import By

def clear():
 
    # for windows
    if name == 'nt':
        _ = system('cls')
 
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def loggin():
    try:
        #driver.find_element(By.ID, POSTULATE)
        mail_btm = driver.find_element(
            By.XPATH, '/html/body/section/div/form/div[1]/div[3]/input')
        
        mail = "carrosiomauricio@gmail.com"
        #if COUNTRY == 'ar':
        #    mail = "pepemauri25@gmail.com"
        mail_btm.send_keys(mail)

        continue_btm = driver.find_element(
            By.XPATH, "/html/body/section/div/form/div[1]/a")
        continue_btm.click()
        time.sleep(2)

        password_btm = driver.find_element(
            By.XPATH, "/html/body/section/div/form/div[2]/input")
        password_btm.send_keys("Loco8Molina")
        next_btm = driver.find_element(
            By.XPATH, "/html/body/section/div/form/div[2]/button")
        next_btm.click()
        pass

        """driver.get(job)
        driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div[2]/div[2]/div[2]/div/a").click()"""
    except:

        pass

def process(id=0):
    text_areas = driver.find_elements(By.CLASS_NAME, 'field_textarea')
    for area in text_areas:
        print(area.find_element(By.TAG_NAME, 'label').text)
        questions.append(area.find_element(By.TAG_NAME, 'label').text)
        
clear()

# Selenium Conections
driver = webdriver.Chrome(executable_path='/home/mauri/Desktop/BotJob-0.1/chromedriver')
#driver.minimize_window()

postulated = 0
new_jobs_applayed = []

questions = []

data_jobs = pd.read_json('data.json')
jobs_links_arr = data_jobs.link.array


with open('used.json', 'r') as openfile:
    used_jobs = json.load(openfile)

questions_df = pd.read_json('questions.json')

#with open('questions.json', 'r') as openfile:
#    questions_file = json.load(openfile)


#print(data_jobs)
for i, job in enumerate(jobs_links_arr):

    proceded = round((i / len(jobs_links_arr))* 100) 

    print("Proceded Jobs: ", proceded, "%")

    if job in used_jobs:
        #data_jobs_filter = data_jobs.filter(items=[i], axis=0)
        #print("Already used", data_jobs_filter.name )
    
        continue
    
    try:
        driver.get(job)
    except:
        continue

    try:
        driver.find_element(By.XPATH, POSTULATE).click()
        loggin()
        
        try:
            input_btm = driver.find_element(By.TAG_NAME, 'input')
            process()
            pd.DataFrame(questions, index=['Question']).to_json('questions.json')


        except:
            pass
        
        print("Posutlated!", job)
        new_jobs_applayed.append(job)
        used_jobs.append(job)
        
        with open("used.json", "w") as outfile:
                    json.dump(used_jobs, outfile)


    except:
        continue
    
print("New jobs applayed: ", len(new_jobs_applayed))


driver.close()