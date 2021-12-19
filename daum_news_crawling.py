
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

# driver = webdriver.Chrome(ChromeDriverManager().install())

url = 'https://news.daum.net/ranking/kkomkkom/'
#
# driver = webdriver.Chrome(executable_path ='chromedriver')
connect = requests.get(url)
html = connect.text

soup = BeautifulSoup(html, 'html.parser')
title = soup.select_one('#mArticle > div.rank_news.rank_kkomkkom > ul.list_news2')

print(title)
#mArticle > div.rank_news.rank_kkomkkom > ul.list_news2


time.sleep(3600)

