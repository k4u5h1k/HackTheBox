import requests
from bs4 import BeautifulSoup as bs4
from urllib3.exceptions import InsecureRequestWarning
from selenium import webdriver
from hashlib import sha512
requests.packages.urllib3.disable_warnings(category = InsecureRequestWarning)


# Dont edit
driver = webdriver.Chrome()
driver.get('https://ringzer0ctf.com/login')
username = driver.find_element_by_name('username')
username.send_keys("Kaushik")
password = driver.find_element_by_name('password')
password.send_keys("mumpUv-conjuw-6hohqe")
driver.find_element_by_xpath('/html/body/div[2]/div/div/form/input[3]').click()
def bitstring_to_bytes(s):
    v = int(s, 2)
    b = bytearray()
    while v:
        b.append(v & 0xff)
        v >>= 8
    return bytes(b[::-1])


driver.get("https://ringzer0ctf.com/challenges/14")
question_with_wrapper = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div').text
just_question = question_with_wrapper.split('\n')[1]
byte_string=bitstring_to_bytes(just_question)
answer=sha512(byte_string).hexdigest()
check=driver.get(f"https://ringzer0ctf.com/challenges/14/{answer}")
