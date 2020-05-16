import requests
from bs4 import BeautifulSoup as bs4
from urllib3.exceptions import InsecureRequestWarning
from selenium import webdriver
import re
requests.packages.urllib3.disable_warnings(category = InsecureRequestWarning)
driver = webdriver.Chrome()
driver.get('https://ringzer0ctf.com/login')
username = driver.find_element_by_name('username')
username.send_keys("Kaushik")
password = driver.find_element_by_name('password')
password.send_keys("mumpUv-conjuw-6hohqe")
driver.find_element_by_xpath('/html/body/div[2]/div/div/form/input[3]').click()
driver.get("https://ringzer0ctf.com/challenges/32")
question_with_wrapper = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]').text
just_question = question_with_wrapper.split('\n')[1][:-3]
print(question_with_wrapper.split('\n')[1])
numbers = list(map(lambda x: x.strip(),re.split('[+-]',just_question)))
print(numbers)
answer = int(numbers[0])+int(numbers[1],16)-int(numbers[2],2)
print(answer)
check=driver.get(f"https://ringzer0ctf.com/challenges/32/{answer}")
