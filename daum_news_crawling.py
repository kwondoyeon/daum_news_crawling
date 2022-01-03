from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time
from datetime import datetime
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

# driver = webdriver.Chrome(ChromeDriverManager().install())
# 뉴스 링크 불러오기
url = 'https://news.daum.net/ranking/kkomkkom/'
url1 = 'https://news.daum.net/ranking/kkomkkom/entertain'
url2 = 'https://news.daum.net/economic#1'
url3 = "https://partners.coupang.com/#affiliate/ws/link"


lists=[]
enter_list=[]
economic_list = []

connect = requests.get(url)
html = connect.text

lists=[]
enter_list=[]

soup = BeautifulSoup(html, 'html.parser')
title = soup.select_one('#mArticle > div.rank_news.rank_kkomkkom > ul.list_news2')
for href in soup.find('div',class_='rank_news rank_kkomkkom').find_all('li',attrs={'data-tiara-layer':'news_list'}):
    list = href.find('a')['href']
    lists.append(list)
print(lists)
for i in lists:
    print(i)

connect = requests.get(url1)
html = connect.text
soup = BeautifulSoup(html, 'html.parser')
top = soup.select_one('#mArticle > div.rank_news.rank_kkomkkom > ul.tab_sub > li:nth-child(2) > a')
for href in soup.find('div',class_='rank_news rank_kkomkkom').find_all('li',attrs={'data-tiara-layer':'news_list'}):
    list = href.find('a')['href']
    enter_list.append(list)
print(lists)
for i in lists:
    print(i)


#카카오뷰
options = webdriver.ChromeOptions()
options.add_argument("User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36")
driver = webdriver.Chrome(executable_path ='chromedriver',options=options)
daum_url = 'https://creators.kakao.com/'
daum_connect = driver.get(daum_url)
driver.implicitly_wait(10)
time.sleep(3)
login = driver.find_element_by_xpath('//*[@id="root"]/div[2]/header/div[2]/a').click()
time.sleep(2)


id = driver.find_element_by_xpath('//*[@id="id_email_2_label"]').click()
driver.find_element_by_xpath('//*[@id="id_email_2"]').send_keys('sguy000@gmail.com')

password = driver.find_element_by_xpath('//*[@id="id_password_3_label"]').click()
driver.find_element_by_xpath('//*[@id="id_password_3"]').send_keys('Aa1704207!')

log = driver.find_element_by_xpath('//*[@id="login-form"]/fieldset/div[8]/button[1]').click()
time.sleep(3)

news = driver.find_element_by_xpath('//*[@id="mainContent"]/ul/li[2]/a/div[2]/div/strong').click()
time.sleep(2)

board = driver.find_element_by_xpath('//*[@id="mainContent"]/div/div[1]/div[2]/div/a').click()
time.sleep(2)

title = driver.find_element_by_xpath('//*[@id="boardTitle"]').click()
title1 = '이시각 가장 많이 본 뉴스 ' +datetime.today().strftime('%m')+'월'+datetime.today().strftime('%d')+'일  '+datetime.today().strftime('%H')+'시'
driver.find_element_by_xpath('//*[@id="boardTitle"]').send_keys(title1)

explain = driver.find_element_by_xpath('//*[@id="boardCmt"]').click()
driver.find_element_by_xpath('//*[@id="boardCmt"]').send_keys('매일매일 가장 많이 본 뉴스들을 보여드립니다.')

news_link = driver.find_element_by_xpath('//*[@id="mainContent"]/div[2]/div/div[2]/div[2]/ul/li[2]/a').click()
time.sleep(1)

add_link = driver.find_element_by_xpath('//*[@id="mainContent"]/div[2]/div/div[2]/div[3]/form/div[1]/div/input').click()
driver.find_element_by_xpath('//*[@id="mainContent"]/div[2]/div/div[2]/div[3]/form/div[1]/div/input').send_keys(lists[0])
time.sleep(1)
close = driver.find_element_by_xpath('//*[@id="mainContent"]/div[2]/div/div[2]/div[2]/ul/li[3]/div/button').click()
time.sleep(1)

news1_search = driver.find_element_by_xpath('//*[@id="mainContent"]/div[2]/div/div[2]/div[3]/form/div[1]/div/div/button[2]').click()
time.sleep(2)
news1_click = driver.find_element_by_xpath('//*[@id="mainContent"]/div[2]/div/div[2]/div[3]/form/div[2]/ul/li/div[3]').click()
time.sleep(2)

li = 2
for li in range(10) :
    #2번 뉴스
    news_clear = driver.find_element_by_xpath('//*[@id="mainContent"]/div[2]/div/div[2]/div[3]/form/div[1]/div/div/button[1]').click()
    time.sleep(0.5)

    add_link = driver.find_element_by_xpath('//*[@id="mainContent"]/div[2]/div/div[2]/div[3]/form/div[1]/div/input').click()
    driver.find_element_by_xpath('//*[@id="mainContent"]/div[2]/div/div[2]/div[3]/form/div[1]/div/input').send_keys(lists[li])
    time.sleep(1)
    news1_search = driver.find_element_by_xpath('//*[@id="mainContent"]/div[2]/div/div[2]/div[3]/form/div[1]/div/div/button[2]').click()
    time.sleep(2)
    news1_click = driver.find_element_by_xpath('//*[@id="mainContent"]/div[2]/div/div[2]/div[3]/form/div[2]/ul/li/div[3]').click()
    time.sleep(2)

excute = driver.find_element_by_xpath('//*[@id="mainContent"]/div[3]/div[2]/button[2]').click()
time.sleep(2)

category = driver.find_element_by_xpath('//*[@id="layer"]/div/div/div[2]/div/div[3]/dl/dd/div/div[1]/label').click()
category2 = driver.find_element_by_xpath('//*[@id="layer"]/div/div/div[2]/div/div[3]/dl/dd/div/div[3]/label').click()
time.sleep(1)
excute2 = driver.find_element_by_xpath('//*[@id="layer"]/div/div/div[2]/div/div[5]/button[2]').click()
#
#

confirm = driver.find_element_by_xpath('//*[@id="layer"]/div/div/div[3]/div/button').click()

#연예뉴스

# options = webdriver.ChromeOptions()
# options.add_argument("User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36")
# driver = webdriver.Chrome(executable_path ='chromedriver',options=options)
# daum_url = 'https://creators.kakao.com/'
# daum_connect = driver.get(daum_url)
# driver.implicitly_wait(10)
# time.sleep(3)
# login = driver.find_element_by_xpath('//*[@id="root"]/div[2]/header/div[2]/a').click()
# time.sleep(2)
#
# id = driver.find_element_by_xpath('//*[@id="id_email_2_label"]').click()
# driver.find_element_by_xpath('//*[@id="id_email_2"]').send_keys('sguy000@gmail.com')
#
# password = driver.find_element_by_xpath('//*[@id="id_password_3_label"]').click()
# driver.find_element_by_xpath('//*[@id="id_password_3"]').send_keys('Aa1704207!')
#
# log = driver.find_element_by_xpath('//*[@id="login-form"]/fieldset/div[8]/button[1]').click()
# time.sleep(3)
#
# news = driver.find_element_by_xpath('//*[@id="mainContent"]/ul/li[2]/a/div[2]/div/strong').click()
# time.sleep(2)

board = driver.find_element_by_xpath('//*[@id="mainContent"]/div[1]/div/a').click()
time.sleep(2)

title = driver.find_element_by_xpath('//*[@id="boardTitle"]').click()
title1 = '이시각 가장 많이 본 연예뉴스 ' +datetime.today().strftime('%m')+'월'+datetime.today().strftime('%d')+'일  '+datetime.today().strftime('%H')+'시'
driver.find_element_by_xpath('//*[@id="boardTitle"]').send_keys(title1)

explain = driver.find_element_by_xpath('//*[@id="boardCmt"]').click()
driver.find_element_by_xpath('//*[@id="boardCmt"]').send_keys('매일매일 가장 많이 본 뉴스들을 보여드립니다.')

news_link = driver.find_element_by_xpath('//*[@id="mainContent"]/div[2]/div/div[2]/div[2]/ul/li[2]/a').click()
time.sleep(1)

add_link = driver.find_element_by_xpath('//*[@id="mainContent"]/div[2]/div/div[2]/div[3]/form/div[1]/div/input').click()
driver.find_element_by_xpath('//*[@id="mainContent"]/div[2]/div/div[2]/div[3]/form/div[1]/div/input').send_keys(enter_list[0])
time.sleep(1)
# close = driver.find_element_by_xpath('//*[@id="mainContent"]/div[2]/div/div[2]/div[2]/ul/li[3]/div/button').click()
# time.sleep(1)

news1_search = driver.find_element_by_xpath('//*[@id="mainContent"]/div[2]/div/div[2]/div[3]/form/div[1]/div/div/button[2]').click()
time.sleep(2)
news1_click = driver.find_element_by_xpath('//*[@id="mainContent"]/div[2]/div/div[2]/div[3]/form/div[2]/ul/li/div[3]').click()
time.sleep(2)


li = 2
for li in range(10) :
    #2번 뉴스
    news_clear = driver.find_element_by_xpath('//*[@id="mainContent"]/div[2]/div/div[2]/div[3]/form/div[1]/div/div/button[1]').click()
    time.sleep(0.5)

    add_link = driver.find_element_by_xpath('//*[@id="mainContent"]/div[2]/div/div[2]/div[3]/form/div[1]/div/input').click()
    driver.find_element_by_xpath('//*[@id="mainContent"]/div[2]/div/div[2]/div[3]/form/div[1]/div/input').send_keys(enter_list[li])
    time.sleep(1)
    news1_search = driver.find_element_by_xpath('//*[@id="mainContent"]/div[2]/div/div[2]/div[3]/form/div[1]/div/div/button[2]').click()
    time.sleep(2)
    news1_click = driver.find_element_by_xpath('//*[@id="mainContent"]/div[2]/div/div[2]/div[3]/form/div[2]/ul/li/div[3]').click()
    time.sleep(2)

excute = driver.find_element_by_xpath('//*[@id="mainContent"]/div[3]/div[2]/button[2]').click()
time.sleep(2)

category = driver.find_element_by_xpath('//*[@id="layer"]/div/div/div[2]/div/div[3]/dl/dd/div/div[1]/label').click()
category2 = driver.find_element_by_xpath('//*[@id="layer"]/div/div/div[2]/div/div[3]/dl/dd/div/div[3]/label').click()
time.sleep(1)
excute2 = driver.find_element_by_xpath('//*[@id="layer"]/div/div/div[2]/div/div[5]/button[2]').click()
confirm = driver.find_element_by_xpath('//*[@id="layer"]/div/div/div[3]/div/button').click()



#경제뉴스
connect = requests.get(url2)
html = connect.text

soup = BeautifulSoup(html, 'html.parser')
title = soup.select_one('#cSub > div > div.section_cate.section_headline')

li = soup.find('div',class_='item_mainnews').find('a')['href']
economic_list.append(li)

for href in soup.find('ul',class_='list_mainnews2').find_all('strong',attrs={'class':'tit_mainnews'}):
    list = href.find('a')['href']
    economic_list.append(list)
    print(list)
print(economic_list)


board = driver.find_element_by_xpath('//*[@id="mainContent"]/div[1]/div/a').click()
time.sleep(2)

title = driver.find_element_by_xpath('//*[@id="boardTitle"]').click()
title1 = '이시각 가장 많이 본 경제 뉴스' +datetime.today().strftime('%m')+'월'+datetime.today().strftime('%d')+'일  '+datetime.today().strftime('%H')+'시'
driver.find_element_by_xpath('//*[@id="boardTitle"]').send_keys(title1)

explain = driver.find_element_by_xpath('//*[@id="boardCmt"]').click()
driver.find_element_by_xpath('//*[@id="boardCmt"]').send_keys('매일매일 가장 많이 본 경제 뉴스들을 보여드립니다.')

news_link = driver.find_element_by_xpath('//*[@id="mainContent"]/div[2]/div/div[2]/div[2]/ul/li[2]/a').click()
time.sleep(1)


li = 1
for li in range(6) :
    #2번 뉴스

    add_link = driver.find_element_by_xpath('//*[@id="mainContent"]/div[2]/div/div[2]/div[3]/form/div[1]/div/input').click()
    driver.find_element_by_xpath('//*[@id="mainContent"]/div[2]/div/div[2]/div[3]/form/div[1]/div/input').send_keys(economic_list[li])
    time.sleep(1)
    news1_search = driver.find_element_by_xpath('//*[@id="mainContent"]/div[2]/div/div[2]/div[3]/form/div[1]/div/div/button[2]').click()
    time.sleep(2)
    news1_click = driver.find_element_by_xpath('//*[@id="mainContent"]/div[2]/div/div[2]/div[3]/form/div[2]/ul/li/div[3]').click()
    time.sleep(2)
    news_clear = driver.find_element_by_xpath(
        '//*[@id="mainContent"]/div[2]/div/div[2]/div[3]/form/div[1]/div/div/button[1]').click()
    time.sleep(0.5)

excute = driver.find_element_by_xpath('//*[@id="mainContent"]/div[3]/div[2]/button[2]').click()
time.sleep(2)

category = driver.find_element_by_xpath('//*[@id="layer"]/div/div/div[2]/div/div[3]/dl/dd/div/div[1]/label').click()
category2 = driver.find_element_by_xpath('//*[@id="layer"]/div/div/div[2]/div/div[3]/dl/dd/div/div[2]/label').click()

time.sleep(1)
excute2 = driver.find_element_by_xpath('//*[@id="layer"]/div/div/div[2]/div/div[5]/button[2]').click()
confirm = driver.find_element_by_xpath('//*[@id="layer"]/div/div/div[3]/div/button').click()





time.sleep(3600)

