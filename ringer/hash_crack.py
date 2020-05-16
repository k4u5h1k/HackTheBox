import requests
from bs4 import BeautifulSoup as bs4
from urllib3.exceptions import InsecureRequestWarning
from selenium import webdriver
from hashlib import sha1
from time import sleep
requests.packages.urllib3.disable_warnings(category = InsecureRequestWarning)


# Dont edit
driver = webdriver.Chrome()
driver.get('https://ringzer0ctf.com/login')
username = driver.find_element_by_name('username')
username.send_keys("Kaushik")
password = driver.find_element_by_name('password')
password.send_keys("mumpUv-conjuw-6hohqe")
driver.find_element_by_xpath('/html/body/div[2]/div/div/form/input[3]').click()

driver.get("https://ringzer0ctf.com/challenges/56")
question_with_wrapper = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div').text
just_question = question_with_wrapper.split('\n')[1]
for i in range(0,9999):
    to_try=f"{i}"
    encoded_trial = sha1(str.encode(to_try)).hexdigest()
    if encoded_trial ==just_question:
        answer=to_try
        check=driver.get(f"https://ringzer0ctf.com/challenges/56/{answer}")
sleep(20)
driver.quit()
