from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time
import lxml
from datetime import datetime
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

# driver = webdriver.Chrome(ChromeDriverManager().install())
# 뉴스 링크 불러오기
url = 'https://www.youtube.com/feed/explore'
url1 = 'https://news.daum.net/ranking/kkomkkom/entertain'

options = webdriver.ChromeOptions()
options.add_argument("User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36")
driver = webdriver.Chrome(executable_path ='chromedriver',options=options)
youtube_connect = driver.get(url)
driver.implicitly_wait(10)
time.sleep(3)

link = driver.find_element_by_xpath('//*[@id="grid-container"]/ytd-video-renderer[1]')
print(link)