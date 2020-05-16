#!/usr/bin/python3
from selenium import webdriver
import hashlib
driver = webdriver.Firefox()
driver.get("http://docker.hackthebox.eu:30256")
myhash = driver.find_element_by_xpath("/html/body/h3").text
output = hashlib.md5(myhash.encode()).hexdigest()
print(output)
driver.find_element_by_xpath("/html/body/center/form/input[1]").send_keys(output)
driver.find_element_by_xpath("/html/body/center/form/input[2]").click()

