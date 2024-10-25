# import requests
# from bs4 import BeautifulSoup

# url = "https://www.melon.com/chart/"
# r = requests.get(url)
# print(r)

# headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
# data = requests.get(url, headers=headers)
# print(data)

# soup = BeautifulSoup(data.text, 'html.parser', from_encoding="cp949")


from selenium import webdriver
import time

from selenium.webdriver.common.by import By
import urllib.request

driver = webdriver.Chrome()
driver.get(f'https://naver.com')
time.sleep(3)
s = driver.find_element(By.CSS_SELECTOR, "title")

print(s)
print(s.text)

         
        

# driver.quit()