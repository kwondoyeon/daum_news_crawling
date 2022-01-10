from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time
import json
from datetime import datetime
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

options = webdriver.ChromeOptions()
options.add_argument("User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36")
driver = webdriver.Chrome(executable_path ='chromedriver',options=options)
partners = 'https://partners.newspic.kr/'
partners_connect = driver.get(partners)
driver.implicitly_wait(10)
time.sleep(3)

login_button = driver.find_element_by_xpath('/html/body/div/main/section[1]/div[2]/div/a[2]').click()

login_button = driver.find_element_by_xpath('/html/body/div/section/div[2]/div/div[1]/ul/li[1]/button').click()


login = driver.find_element_by_xpath('/html/body/div/section/div[2]/div/div[1]/form/div[1]/input').click()
driver.find_element_by_xpath('/html/body/div/section/div[2]/div/div[1]/form/div[1]/input').send_keys('sguy00@naver.com')

password = driver.find_element_by_xpath('/html/body/div/section/div[2]/div/div[1]/form/div[2]/input').click()
driver.find_element_by_xpath('/html/body/div/section/div[2]/div/div[1]/form/div[2]/input').send_keys('Aa1704207!kdy')

log = driver.find_element_by_xpath('/html/body/div/section/div[2]/div/div[1]/form/button').click()
time.sleep(3)

url = 'https://partners.newspic.kr/main/contentList'

headers = {'content-type':'application/x-www-form-urlencoded; charset=UTF-8'}
cookie = {'cookie':'SESSION=Nzc1ZjhhZjgtZTE4YS00Nzk1LTg1MGYtNjFhNzkxNjk3NTgy; partnersLongTermLogin=f581f266-1d90-41f8-976f-ca2b9db99168; _ga=GA1.2.1499947029.1640973116; _gid=GA1.2.502959532.1640973116; _gat=1'}
connect = requests.post(url,headers,cookies = cookie)
time.sleep(3)
html = connect.text
soup = BeautifulSoup(html, 'html.parser')
data = json.loads(soup.text)
print(data['contentList'][0]['link'])

news_pick =[]

list = (data['contentList'])
li= 0
for li in range(9) :
    link = data['contentList'][li]['link']
    news_pick.append(link)
print(news_pick)
