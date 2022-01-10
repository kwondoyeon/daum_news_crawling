from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time
from datetime import datetime
from selenium.webdriver.common.by import By
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
sports_url = "https://sports.daum.net/"
fortune_url = 'http://www.newstnt.com/news/articleList.html?sc_serial_code=SRN69'
star_fortune = 'http://www.joongboo.com/news/articleList.html?sc_serial_code=SRN362'


lists=[]
rank_title =[]

enter_list=[]
enter_title=[]

economic_list = []
economic_title=[]

lists=[]
enter_list=[]

sports_list =[]
sports_title = []

fortune_title = []
fortune_url1 = []
star_title = []
star_url =[]

#spotrs뉴스 크롤링
connect = requests.get(sports_url)
html = connect.text
soup = BeautifulSoup(html, 'html.parser')
title = soup.select_one('#cSub > div.feature_top > div.top_rank > ol:nth-child(3)')
print(title)
for href in soup.find('ol',class_='list_rank').find_all('strong',class_='tit_rank'):
    list = href.find('a')['href']
    title = href.find('a').text
    sports_list.append(list)
    sports_title.append(title)
print(sports_list)
print(sports_title)


# Top뉴스 크롤링
connect = requests.get(url)
html = connect.text
soup = BeautifulSoup(html, 'html.parser')
title = soup.select_one('#mArticle > div.rank_news.rank_kkomkkom > ul.list_news2')
for href in soup.find('div',class_='rank_news rank_kkomkkom').find_all('li',attrs={'data-tiara-layer':'news_list'}):
    list = href.find('a')['href']
    # list1 = href.find('img')['alt']
    list1 = href.find('a').text.strip()
    rank_title.append(list1)
    lists.append(list)
print(lists)
print(rank_title)
# for i in lists:
#     print(i)

# 연예뉴스 크롤링
connect = requests.get(url1)
html = connect.text
soup = BeautifulSoup(html, 'html.parser')
top = soup.select_one('#mArticle > div.rank_news.rank_kkomkkom > ul.tab_sub > li:nth-child(2) > a')
for href in soup.find('div',class_='rank_news rank_kkomkkom').find_all('li',attrs={'data-tiara-layer':'news_list'}):
    list = href.find('a')['href']
    list1 = href.find('img')['alt']

    enter_title.append(list1)
    enter_list.append(list)
print(lists)
print(enter_title)
# for i in lists:
#     print(i)

#경제뉴스 크롤링
connect = requests.get(url2)
html = connect.text

soup = BeautifulSoup(html, 'html.parser')
title = soup.select_one('#cSub > div > div.section_cate.section_headline')

li = soup.find('div',class_='item_mainnews').find('a')['href']
economic_list.append(li)

for href in soup.find('ul',class_='list_mainnews2').find_all('strong',attrs={'class':'tit_mainnews'}):
    list = href.find('a')['href']
    list1 = href.find('a').text.strip()
    economic_title.append(list1)
    economic_list.append(list)
print(economic_list)
print(economic_title)

#오늘의 운세

connect = requests.get(fortune_url)
html = connect.text
soup = BeautifulSoup(html, 'html.parser')
title = soup.find('div',class_ = 'list-titles table-cell')
title_url = title.find('a')['href']
title_name = title.find('a').text
fortune_title.append(title_name)
fortune_url1.append('http://www.newstnt.com/'+title_url)
print(fortune_title)
print(fortune_url1)

#별자리운세
star_fortune = 'http://www.joongboo.com/news/articleList.html?sc_serial_code=SRN362'
connect = requests.get(star_fortune)
html = connect.text
soup = BeautifulSoup(html, 'html.parser')
title = soup.find('ul',class_ = 'type1')
title_url = title.find('a')['href']
title_name = title.find('a').text

star_title.append(title_name)
star_url.append('http://www.joongboo.com/'+title_url)
print(star_title, star_url)



#카카오뷰
options = webdriver.ChromeOptions()
options.add_argument("User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36")
driver = webdriver.Chrome(executable_path ='chromedriver',options=options)
daum_url = 'https://creators.kakao.com/'
daum_connect = driver.get(daum_url)
driver.implicitly_wait(10)
time.sleep(3)
login = driver.find_element(By.XPATH,'//*[@id="root"]/div[2]/header/div[2]/a').click()
time.sleep(2)


id = driver.find_element(By.XPATH,'//*[@id="id_email_2_label"]').click()
driver.find_element(By.XPATH,'//*[@id="id_email_2"]').send_keys('sguy000@gmail.com')

password = driver.find_element(By.XPATH,'//*[@id="id_password_3_label"]').click()
driver.find_element(By.XPATH,'//*[@id="id_password_3"]').send_keys('Aa1704207!')

log = driver.find_element(By.XPATH,'//*[@id="login-form"]/fieldset/div[8]/button[1]').click()
time.sleep(3)

news = driver.find_element(By.XPATH,'//*[@id="mainContent"]/ul/li[2]/a/div[2]/div/strong').click()
time.sleep(2)

board = driver.find_element(By.XPATH,'//*[@id="mainContent"]/div/div[1]/div[2]/div/a').click()
time.sleep(2)

title = driver.find_element(By.XPATH,'//*[@id="boardTitle"]').click()
# title1 = driver.find_element(By.XPATH,'//*[@id="boardTitle"]').send_keys(rank_title[0])
title1 = '이시각 가장 많이 본 Top10 뉴스 ' #+datetime.today().strftime('%m')+'월'+datetime.today().strftime('%d')+'일  '+datetime.today().strftime('%H')+'시'
driver.find_element(By.XPATH,'//*[@id="boardTitle"]').send_keys(title1)

explain = driver.find_element(By.XPATH,'//*[@id="boardCmt"]').click()
driver.find_element(By.XPATH,'//*[@id="boardCmt"]').send_keys('오늘의 최신 뉴스!')
driver.find_element(By.XPATH,'//*[@id="boardCmt"]').send_keys(datetime.today().strftime('%m')+'월'+datetime.today().strftime('%d')+'일  '+datetime.today().strftime('%H')+'시 기준')
driver.find_element(By.XPATH,'//*[@id="boardCmt"]').send_keys(Keys.ENTER)
driver.find_element(By.XPATH, '//*[@id="boardCmt"]').send_keys('## 매일매일 업데이트 뉴스를 보고 싶으시면 오른쪽 위의 Ch+ 를 눌러주세요! ##')

content_click = driver.find_element(By.XPATH,'//*[@id="mainContent"]/div[2]/div/div[1]/div[2]/div[2]/ul/li[4]/button/span').click()

news_link = driver.find_element(By.XPATH,'//*[@id="mainContent"]/div[2]/div/div[2]/div[2]/ul/li[2]/a').click()
time.sleep(1)

add_link = driver.find_element(By.XPATH,'//*[@id="mainContent"]/div[2]/div/div[2]/div[3]/form/div[1]/div/input').click()
driver.find_element(By.XPATH,'//*[@id="mainContent"]/div[2]/div/div[2]/div[3]/form/div[1]/div/input').send_keys(lists[0])
time.sleep(1)
close = driver.find_element(By.XPATH,'//*[@id="mainContent"]/div[2]/div/div[2]/div[2]/ul/li[3]/div/button').click()
time.sleep(1)

news1_search = driver.find_element(By.XPATH,'//*[@id="mainContent"]/div[2]/div/div[2]/div[3]/form/div[1]/div/div/button[2]').click()
time.sleep(2)
news1_click = driver.find_element(By.XPATH,'//*[@id="mainContent"]/div[2]/div/div[2]/div[3]/form/div[2]/ul/li/div[3]').click()
time.sleep(2)

li = 1
for li in range(10) :
    #2번 뉴스
    news_clear = driver.find_element(By.XPATH,'//*[@id="mainContent"]/div[2]/div/div[2]/div[3]/form/div[1]/div/div/button[1]').click()
    time.sleep(0.5)

    add_link = driver.find_element(By.XPATH,'//*[@id="mainContent"]/div[2]/div/div[2]/div[3]/form/div[1]/div/input').click()
    driver.find_element(By.XPATH,'//*[@id="mainContent"]/div[2]/div/div[2]/div[3]/form/div[1]/div/input').send_keys(lists[li])
    time.sleep(1)
    news1_search = driver.find_element(By.XPATH,'//*[@id="mainContent"]/div[2]/div/div[2]/div[3]/form/div[1]/div/div/button[2]').click()
    time.sleep(2)
    news1_click = driver.find_element(By.XPATH,'//*[@id="mainContent"]/div[2]/div/div[2]/div[3]/form/div[2]/ul/li/div[3]').click()
    time.sleep(2)

excute = driver.find_element(By.XPATH,'//*[@id="mainContent"]/div[3]/div[2]/button[2]').click()
time.sleep(2)

category = driver.find_element(By.XPATH,'//*[@id="layer"]/div/div/div[2]/div/div[3]/dl/dd/div/div[1]/label').click()
category2 = driver.find_element(By.XPATH,'//*[@id="layer"]/div/div/div[2]/div/div[3]/dl/dd/div/div[3]/label').click()
time.sleep(1)
excute2 = driver.find_element(By.XPATH,'//*[@id="layer"]/div/div/div[2]/div/div[5]/button[2]').click()
#
#

confirm = driver.find_element(By.XPATH,'//*[@id="layer"]/div/div/div[3]/div/button').click()

#연예뉴스

board = driver.find_element(By.XPATH,'//*[@id="mainContent"]/div[1]/div/a').click()
time.sleep(2)

title = driver.find_element(By.XPATH,'//*[@id="boardTitle"]').click()
# title1 = driver.find_element(By.XPATH,'//*[@id="boardTitle"]').send_keys(enter_title[0])
title1 = '이시각 가장 많이 본 연예 뉴스 ' +datetime.today().strftime('%m')+'월'+datetime.today().strftime('%d')+'일  '+datetime.today().strftime('%H')+'시'
driver.find_element(By.XPATH,'//*[@id="boardTitle"]').send_keys(title1)

explain = driver.find_element(By.XPATH,'//*[@id="boardCmt"]').click()
driver.find_element(By.XPATH,'//*[@id="boardCmt"]').send_keys('오늘의 최신 연예 뉴스!')
driver.find_element(By.XPATH,'//*[@id="boardCmt"]').send_keys(datetime.today().strftime('%m')+'월'+datetime.today().strftime('%d')+'일  '+datetime.today().strftime('%H')+'시 기준')
driver.find_element(By.XPATH,'//*[@id="boardCmt"]').send_keys(Keys.ENTER)
driver.find_element(By.XPATH, '//*[@id="boardCmt"]').send_keys('## 매일매일 업데이트 뉴스를 보고 싶으시면 오른쪽 위의 Ch+ 를 눌러주세요! ##')

news_link = driver.find_element(By.XPATH,'//*[@id="mainContent"]/div[2]/div/div[2]/div[2]/ul/li[2]/a').click()
time.sleep(1)

add_link = driver.find_element(By.XPATH,'//*[@id="mainContent"]/div[2]/div/div[2]/div[3]/form/div[1]/div/input').click()
driver.find_element(By.XPATH,'//*[@id="mainContent"]/div[2]/div/div[2]/div[3]/form/div[1]/div/input').send_keys(enter_list[0])
time.sleep(1)
# close = driver.find_element(By.XPATH,'//*[@id="mainContent"]/div[2]/div/div[2]/div[2]/ul/li[3]/div/button').click()
# time.sleep(1)

news1_search = driver.find_element(By.XPATH,'//*[@id="mainContent"]/div[2]/div/div[2]/div[3]/form/div[1]/div/div/button[2]').click()
time.sleep(2)
news1_click = driver.find_element(By.XPATH,'//*[@id="mainContent"]/div[2]/div/div[2]/div[3]/form/div[2]/ul/li/div[3]').click()
time.sleep(2)


li = 2
for li in range(10) :
    #2번 뉴스
    news_clear = driver.find_element(By.XPATH,'//*[@id="mainContent"]/div[2]/div/div[2]/div[3]/form/div[1]/div/div/button[1]').click()
    time.sleep(0.5)

    add_link = driver.find_element(By.XPATH,'//*[@id="mainContent"]/div[2]/div/div[2]/div[3]/form/div[1]/div/input').click()
    driver.find_element(By.XPATH,'//*[@id="mainContent"]/div[2]/div/div[2]/div[3]/form/div[1]/div/input').send_keys(enter_list[li])
    time.sleep(1)
    news1_search = driver.find_element(By.XPATH,'//*[@id="mainContent"]/div[2]/div/div[2]/div[3]/form/div[1]/div/div/button[2]').click()
    time.sleep(2)
    news1_click = driver.find_element(By.XPATH,'//*[@id="mainContent"]/div[2]/div/div[2]/div[3]/form/div[2]/ul/li/div[3]').click()
    time.sleep(2)

excute = driver.find_element(By.XPATH,'//*[@id="mainContent"]/div[3]/div[2]/button[2]').click()
time.sleep(2)

schedule = driver.find_element(By.XPATH,'//*[@id="layer"]/div/div/div[2]/div/div[2]/dl/dd/div/div[2]/label/span[1]').click()

hour_click = driver.find_element(By.XPATH,'//*[@id="layer"]/div/div/div[2]/div/div[2]/dl/dd/div/div[5]/div/a').click()
sc_time = driver.find_element(By.XPATH,'//*[@id="layer"]/div/div/div[2]/div/div[2]/dl/dd/div/div[5]/div/div/ul/li['+str(int(datetime.today().strftime('%H'))+2)+']').click()

minute_click = driver.find_element(By.XPATH,'//*[@id="layer"]/div/div/div[2]/div/div[2]/dl/dd/div/div[6]/div/a').click()
minute_time = driver.find_element(By.XPATH,'//*[@id="layer"]/div/div/div[2]/div/div[2]/dl/dd/div/div[6]/div/div/ul/li[1]').click()


category = driver.find_element(By.XPATH,'//*[@id="layer"]/div/div/div[2]/div/div[3]/dl/dd/div/div[1]/label').click()
category2 = driver.find_element(By.XPATH,'//*[@id="layer"]/div/div/div[2]/div/div[3]/dl/dd/div/div[3]/label').click()
time.sleep(1)
excute2 = driver.find_element(By.XPATH,'//*[@id="layer"]/div/div/div[2]/div/div[5]/button[2]').click()
confirm = driver.find_element(By.XPATH,'//*[@id="layer"]/div/div/div[3]/div/button').click()



#경제뉴스

board = driver.find_element(By.XPATH,'//*[@id="mainContent"]/div[1]/div/a').click()
time.sleep(2)

title = driver.find_element(By.XPATH,'//*[@id="boardTitle"]').click()
# title1 = driver.find_element(By.XPATH,'//*[@id="boardTitle"]').send_keys(economic_title[0])
title1 = '이시각 가장 많이 본 경제 뉴스 ' #+datetime.today().strftime('%m')+'월'+datetime.today().strftime('%d')+'일  '+datetime.today().strftime('%H')+'시'
driver.find_element(By.XPATH,'//*[@id="boardTitle"]').send_keys(title1)

explain = driver.find_element(By.XPATH,'//*[@id="boardCmt"]').click()
driver.find_element(By.XPATH,'//*[@id="boardCmt"]').send_keys('오늘의 최신 경제 뉴스!')
driver.find_element(By.XPATH,'//*[@id="boardCmt"]').send_keys(datetime.today().strftime('%m')+'월'+datetime.today().strftime('%d')+'일  '+str(int(datetime.today().strftime('%H'))+2)+'시 기준')
driver.find_element(By.XPATH,'//*[@id="boardCmt"]').send_keys(Keys.ENTER)
driver.find_element(By.XPATH, '//*[@id="boardCmt"]').send_keys('## 매일매일 업데이트 뉴스를 보고 싶으시면 오른쪽 위의 Ch+ 를 눌러주세요! ##')


news_link = driver.find_element(By.XPATH,'//*[@id="mainContent"]/div[2]/div/div[2]/div[2]/ul/li[2]/a').click()
time.sleep(1)

li = 1
for li in range(6) :
    #2번 뉴스

    add_link = driver.find_element(By.XPATH,'//*[@id="mainContent"]/div[2]/div/div[2]/div[3]/form/div[1]/div/input').click()
    driver.find_element(By.XPATH,'//*[@id="mainContent"]/div[2]/div/div[2]/div[3]/form/div[1]/div/input').send_keys(economic_list[li])
    time.sleep(1)
    news1_search = driver.find_element(By.XPATH,'//*[@id="mainContent"]/div[2]/div/div[2]/div[3]/form/div[1]/div/div/button[2]').click()
    time.sleep(2)
    news1_click = driver.find_element(By.XPATH,'//*[@id="mainContent"]/div[2]/div/div[2]/div[3]/form/div[2]/ul/li/div[3]').click()
    time.sleep(2)
    news_clear = driver.find_element(By.XPATH,
        '//*[@id="mainContent"]/div[2]/div/div[2]/div[3]/form/div[1]/div/div/button[1]').click()
    time.sleep(0.5)

excute = driver.find_element(By.XPATH,'//*[@id="mainContent"]/div[3]/div[2]/button[2]').click()
time.sleep(2)

schedule = driver.find_element(By.XPATH,'//*[@id="layer"]/div/div/div[2]/div/div[2]/dl/dd/div/div[2]/label/span[1]').click()

hour_click = driver.find_element(By.XPATH,'//*[@id="layer"]/div/div/div[2]/div/div[2]/dl/dd/div/div[5]/div/a').click()
sc_time = driver.find_element(By.XPATH,'//*[@id="layer"]/div/div/div[2]/div/div[2]/dl/dd/div/div[5]/div/div/ul/li['+str(int(datetime.today().strftime('%H'))+3)+']').click()

minute_click = driver.find_element(By.XPATH,'//*[@id="layer"]/div/div/div[2]/div/div[2]/dl/dd/div/div[6]/div/a').click()
minute_time = driver.find_element(By.XPATH,'//*[@id="layer"]/div/div/div[2]/div/div[2]/dl/dd/div/div[6]/div/div/ul/li[1]').click()

category = driver.find_element(By.XPATH,'//*[@id="layer"]/div/div/div[2]/div/div[3]/dl/dd/div/div[1]/label').click()
category2 = driver.find_element(By.XPATH,'//*[@id="layer"]/div/div/div[2]/div/div[3]/dl/dd/div/div[2]/label').click()

time.sleep(1)
excute2 = driver.find_element(By.XPATH,'//*[@id="layer"]/div/div/div[2]/div/div[5]/button[2]').click()
confirm = driver.find_element(By.XPATH,'//*[@id="layer"]/div/div/div[3]/div/button').click()


# 스포트 뉴스
board = driver.find_element(By.XPATH,'//*[@id="mainContent"]/div[1]/div/a').click()
time.sleep(2)

title = driver.find_element(By.XPATH,'//*[@id="boardTitle"]').click()
# title1 = driver.find_element(By.XPATH,'//*[@id="boardTitle"]').send_keys(economic_title[0])
title1 = '이시각 가장 많이 본 스포츠 뉴스 ' #+datetime.today().strftime('%m')+'월'+datetime.today().strftime('%d')+'일  '+datetime.today().strftime('%H')+'시'
driver.find_element(By.XPATH,'//*[@id="boardTitle"]').send_keys(title1)

explain = driver.find_element(By.XPATH,'//*[@id="boardCmt"]').click()
driver.find_element(By.XPATH,'//*[@id="boardCmt"]').send_keys('오늘의 최신 스포츠 뉴스!')
driver.find_element(By.XPATH,'//*[@id="boardCmt"]').send_keys(datetime.today().strftime('%m')+'월'+datetime.today().strftime('%d')+'일  '+str(int(datetime.today().strftime('%H'))+3)+'시 기준')
driver.find_element(By.XPATH,'//*[@id="boardCmt"]').send_keys(Keys.ENTER)
driver.find_element(By.XPATH, '//*[@id="boardCmt"]').send_keys('## 매일매일 업데이트 뉴스를 보고 싶으시면 오른쪽 위의 Ch+ 를 눌러주세요! ##')



news_link = driver.find_element(By.XPATH,'//*[@id="mainContent"]/div[2]/div/div[2]/div[2]/ul/li[2]/a').click()
time.sleep(1)

li = 1
for li in range(6) :
    #2번 뉴스

    add_link = driver.find_element(By.XPATH,'//*[@id="mainContent"]/div[2]/div/div[2]/div[3]/form/div[1]/div/input').click()
    driver.find_element(By.XPATH,'//*[@id="mainContent"]/div[2]/div/div[2]/div[3]/form/div[1]/div/input').send_keys(sports_list[li])
    time.sleep(1)
    news1_search = driver.find_element(By.XPATH,'//*[@id="mainContent"]/div[2]/div/div[2]/div[3]/form/div[1]/div/div/button[2]').click()
    time.sleep(2)
    news1_click = driver.find_element(By.XPATH,'//*[@id="mainContent"]/div[2]/div/div[2]/div[3]/form/div[2]/ul/li/div[3]').click()
    time.sleep(2)
    news_clear = driver.find_element(By.XPATH,
        '//*[@id="mainContent"]/div[2]/div/div[2]/div[3]/form/div[1]/div/div/button[1]').click()
    time.sleep(0.5)

excute = driver.find_element(By.XPATH,'//*[@id="mainContent"]/div[3]/div[2]/button[2]').click()
time.sleep(2)

schedule = driver.find_element(By.XPATH,'//*[@id="layer"]/div/div/div[2]/div/div[2]/dl/dd/div/div[2]/label/span[1]').click()

hour_click = driver.find_element(By.XPATH,'//*[@id="layer"]/div/div/div[2]/div/div[2]/dl/dd/div/div[5]/div/a').click()
sc_time = driver.find_element(By.XPATH,'//*[@id="layer"]/div/div/div[2]/div/div[2]/dl/dd/div/div[5]/div/div/ul/li['+str(int(datetime.today().strftime('%H'))+4)+']').click()

minute_click = driver.find_element(By.XPATH,'//*[@id="layer"]/div/div/div[2]/div/div[2]/dl/dd/div/div[6]/div/a').click()
minute_time = driver.find_element(By.XPATH,'//*[@id="layer"]/div/div/div[2]/div/div[2]/dl/dd/div/div[6]/div/div/ul/li[1]').click()

category = driver.find_element(By.XPATH,'//*[@id="layer"]/div/div/div[2]/div/div[3]/dl/dd/div/div[1]/label').click()
category2 = driver.find_element(By.XPATH,'//*[@id="layer"]/div/div/div[2]/div/div[3]/dl/dd/div/div[9]/label').click()

time.sleep(1)
excute2 = driver.find_element(By.XPATH,'//*[@id="layer"]/div/div/div[2]/div/div[5]/button[2]').click()
confirm = driver.find_element(By.XPATH,'//*[@id="layer"]/div/div/div[3]/div/button').click()



#오늘의 운세
board = driver.find_element(By.XPATH,'//*[@id="mainContent"]/div[1]/div/a').click()
time.sleep(2)

title = driver.find_element(By.XPATH,'//*[@id="boardTitle"]').click()
title1 = driver.find_element(By.XPATH,'//*[@id="boardTitle"]').send_keys(fortune_title[0])
# title1 = '이시각 가장 많이 본 스포츠 뉴스 ' #+datetime.today().strftime('%m')+'월'+datetime.today().strftime('%d')+'일  '+datetime.today().strftime('%H')+'시'
# driver.find_element(By.XPATH,'//*[@id="boardTitle"]').send_keys(title1)

explain = driver.find_element(By.XPATH,'//*[@id="boardCmt"]').click()
driver.find_element(By.XPATH,'//*[@id="boardCmt"]').send_keys('오늘의 운세!')
# driver.find_element(By.XPATH,'//*[@id="boardCmt"]').send_keys(datetime.today().strftime('%m')+'월'+datetime.today().strftime('%d')+'일  '+str(int(datetime.today().strftime('%H'))+3)+'시 기준')
driver.find_element(By.XPATH,'//*[@id="boardCmt"]').send_keys(Keys.ENTER)
driver.find_element(By.XPATH, '//*[@id="boardCmt"]').send_keys('## 매일매일 오늘의 운세를 보고 싶으시면 오른쪽 위의 Ch+ 를 눌러주세요! ##')

content_click = driver.find_element(By.XPATH,'//*[@id="mainContent"]/div[2]/div/div[1]/div[2]/div[2]/ul/li[4]/button/span').click()

news_link = driver.find_element(By.XPATH,'//*[@id="mainContent"]/div[2]/div/div[2]/div[2]/ul/li[2]/a').click()
time.sleep(1)


add_link = driver.find_element(By.XPATH,'//*[@id="mainContent"]/div[2]/div/div[2]/div[3]/form/div[1]/div/input').click()
driver.find_element(By.XPATH,'//*[@id="mainContent"]/div[2]/div/div[2]/div[3]/form/div[1]/div/input').send_keys(fortune_url1[0])
time.sleep(1)
news1_search = driver.find_element(By.XPATH,'//*[@id="mainContent"]/div[2]/div/div[2]/div[3]/form/div[1]/div/div/button[2]').click()
time.sleep(2)
news1_click = driver.find_element(By.XPATH,'//*[@id="mainContent"]/div[2]/div/div[2]/div[3]/form/div[2]/ul/li/div[3]').click()
time.sleep(2)
news_clear = driver.find_element(By.XPATH,
    '//*[@id="mainContent"]/div[2]/div/div[2]/div[3]/form/div[1]/div/div/button[1]').click()


#별자리 운세 추가
time.sleep(0.5)
driver.find_element(By.XPATH,'//*[@id="mainContent"]/div[2]/div/div[2]/div[3]/form/div[1]/div/input').send_keys(star_url[0])
time.sleep(1)
news1_search = driver.find_element(By.XPATH,'//*[@id="mainContent"]/div[2]/div/div[2]/div[3]/form/div[1]/div/div/button[2]').click()
time.sleep(2)
news1_click = driver.find_element(By.XPATH,'//*[@id="mainContent"]/div[2]/div/div[2]/div[3]/form/div[2]/ul/li/div[3]').click()
time.sleep(2)
news_clear = driver.find_element(By.XPATH,
    '//*[@id="mainContent"]/div[2]/div/div[2]/div[3]/form/div[1]/div/div/button[1]').click()
time.sleep(0.5)


excute = driver.find_element(By.XPATH,'//*[@id="mainContent"]/div[3]/div[2]/button[2]').click()
time.sleep(2)

# schedule = driver.find_element(By.XPATH,'//*[@id="layer"]/div/div/div[2]/div/div[2]/dl/dd/div/div[2]/label/span[1]').click()
#
# hour_click = driver.find_element(By.XPATH,'//*[@id="layer"]/div/div/div[2]/div/div[2]/dl/dd/div/div[5]/div/a').click()
# sc_time = driver.find_element(By.XPATH,'//*[@id="layer"]/div/div/div[2]/div/div[2]/dl/dd/div/div[5]/div/div/ul/li['+str(int(datetime.today().strftime('%H'))+4)+']').click()
#
# minute_click = driver.find_element(By.XPATH,'//*[@id="layer"]/div/div/div[2]/div/div[2]/dl/dd/div/div[6]/div/a').click()
# minute_time = driver.find_element(By.XPATH,'//*[@id="layer"]/div/div/div[2]/div/div[2]/dl/dd/div/div[6]/div/div/ul/li[1]').click()

category = driver.find_element(By.XPATH,'//*[@id="layer"]/div/div/div[2]/div/div[3]/dl/dd/div/div[4]/label').click()
category2 = driver.find_element(By.XPATH,'//*[@id="layer"]/div/div/div[2]/div/div[3]/dl/dd/div/div[11]/label').click()

time.sleep(1)
excute2 = driver.find_element(By.XPATH,'//*[@id="layer"]/div/div/div[2]/div/div[5]/button[2]').click()
confirm = driver.find_element(By.XPATH,'//*[@id="layer"]/div/div/div[3]/div/button').click()


time.sleep(3600)

