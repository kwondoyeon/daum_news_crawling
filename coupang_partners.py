# coding: utf-8
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
import hmac
import hashlib
import os
import time
import requests
import json
import urllib.request
from selenium import webdriver
import secrets
from urllib.parse import urlencode

__author__ = "Jaejin Jang<jaejin_me@naver.com>"


class cupangMgr:
    DOMAIN = "https://api-gateway.coupang.com"

    def generateHmac(self, method, url, secretKey, accessKey):
        path, *query = url.split("?")
        os.environ["TZ"] = "GMT+0"
        datetime = time.strftime('%y%m%d') + 'T' + time.strftime('%H%M%S') + 'Z'
        message = datetime + method + path + (query[0] if query else "")
        signature = hmac.new(bytes(secretKey, "utf-8"), message.encode("utf-8"), hashlib.sha256).hexdigest()

        return "CEA algorithm=HmacSHA256, access-key={}, signed-date={}, signature={}".format(accessKey, datetime,
                                                                                              signature)

    def get_productsdata(self, request_method, authorization):
        # URL = "/v2/providers/affiliate_open_api/apis/openapi/products/search?keyword=" + urllib.parse.quote(
        #     keyword) + "&limit=" + str(limit)
        URL = "/v2/providers/affiliate_open_api/apis/openapi/products/goldbox?subId=AF0863723"
        url = "{}{}".format(self.DOMAIN, URL)

        response = requests.request(method=request_method, url=url, headers={"Authorization": authorization,
                                                                             "Content-Type": "application/json;charset=UTF-8"})
        retdata = json.dumps(response.json(), indent=4).encode('utf-8')
        jsondata = json.loads(retdata)
        productdata = jsondata['data']
        # productdata = data['productData']

        return productdata

    def shopping(self):
        # ????????????
        options = webdriver.ChromeOptions()
        options.add_argument(
            "User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36")
        driver = webdriver.Chrome(executable_path='chromedriver', options=options)
        daum_url = 'https://creators.kakao.com/'
        daum_connect = driver.get(daum_url)
        driver.implicitly_wait(10)
        time.sleep(3)
        login = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/header/div[2]/a').click()
        time.sleep(2)

        id = driver.find_element(By.XPATH, '//*[@id="id_email_2_label"]').click()
        driver.find_element(By.XPATH, '//*[@id="id_email_2"]').send_keys('sguy000@gmail.com')

        password = driver.find_element(By.XPATH, '//*[@id="id_password_3_label"]').click()
        driver.find_element(By.XPATH, '//*[@id="id_password_3"]').send_keys('Aa1704207!')

        log = driver.find_element(By.XPATH, '//*[@id="login-form"]/fieldset/div[8]/button[1]').click()
        time.sleep(3)

        shopping = driver.find_element(By.XPATH, '//*[@id="mainContent"]/ul/li[3]/a/div[2]/div').click()
        time.sleep(2)

        board = driver.find_element(By.XPATH, '//*[@id="mainContent"]/div/div[1]/div[2]/div/a').click()
        time.sleep(2)

        title = driver.find_element(By.XPATH, '//*[@id="boardTitle"]').click()
        title1 = '????????? ???????????? ????????? ' + datetime.today().strftime('%m') + '???' + datetime.today().strftime('%d') + '???  '
        driver.find_element(By.XPATH, '//*[@id="boardTitle"]').send_keys(title1)

        explain = driver.find_element(By.XPATH, '//*[@id="boardCmt"]').click()
        driver.find_element(By.XPATH, '//*[@id="boardCmt"]').send_keys('?????? ?????? ?????? ?????? ???????????? ??????????????????.')

        news_link = driver.find_element(By.XPATH, '//*[@id="mainContent"]/div[2]/div/div[2]/div[2]/ul/li[2]/a').click()
        time.sleep(1)

        add_link = driver.find_element(By.XPATH,
                                       '//*[@id="mainContent"]/div[2]/div/div[2]/div[3]/form/div[1]/div/input').click()
        driver.find_element(By.XPATH,
                            '//*[@id="mainContent"]/div[2]/div/div[2]/div[3]/form/div[1]/div/input').send_keys(
            goldbox[0])
        time.sleep(1)
        close = driver.find_element(By.XPATH,
                                    '//*[@id="mainContent"]/div[2]/div/div[2]/div[2]/ul/li[3]/div/button').click()
        time.sleep(1)

        news1_search = driver.find_element(By.XPATH,
                                           '//*[@id="mainContent"]/div[2]/div/div[2]/div[3]/form/div[1]/div/div/button[2]').click()
        time.sleep(2)
        news1_click = driver.find_element(By.XPATH,
                                          '//*[@id="mainContent"]/div[2]/div/div[2]/div[3]/form/div[2]/ul/li/div[3]').click()
        time.sleep(2)

        li = 1
        for li in range(9):
            # 2??? ??????
            news_clear = driver.find_element(By.XPATH,
                                             '//*[@id="mainContent"]/div[2]/div/div[2]/div[3]/form/div[1]/div/div/button[1]').click()
            time.sleep(0.5)

            add_link = driver.find_element(By.XPATH,
                                           '//*[@id="mainContent"]/div[2]/div/div[2]/div[3]/form/div[1]/div/input').click()
            driver.find_element(By.XPATH,
                                '//*[@id="mainContent"]/div[2]/div/div[2]/div[3]/form/div[1]/div/input').send_keys(
                goldbox[li])
            time.sleep(1)
            news1_search = driver.find_element(By.XPATH,
                                               '//*[@id="mainContent"]/div[2]/div/div[2]/div[3]/form/div[1]/div/div/button[2]').click()
            time.sleep(2)
            news1_click = driver.find_element(By.XPATH,
                                              '//*[@id="mainContent"]/div[2]/div/div[2]/div[3]/form/div[2]/ul/li/div[3]').click()
            time.sleep(2)

        excute = driver.find_element(By.XPATH, '//*[@id="mainContent"]/div[3]/div[2]/button[2]').click()
        time.sleep(2)

        category = driver.find_element(By.XPATH, '//*[@id="layer"]/div/div/div[2]/div/div[3]/dl/dd/div/div[12]').click()
        category2 = driver.find_element(By.XPATH,
                                        '//*[@id="layer"]/div/div/div[2]/div/div[3]/dl/dd/div/div[21]').click()
        time.sleep(1)
        category3 = driver.find_element(By.XPATH, '//*[@id="layer"]/div/div/div[2]/div/div[4]/div/label').click()
        time.sleep(1)

        excute2 = driver.find_element(By.XPATH, '//*[@id="layer"]/div/div/div[2]/div/div[5]/button[2]').click()
        #
        #

        confirm = driver.find_element(By.XPATH, '//*[@id="layer"]/div/div/div[3]/div/button').click()


if __name__ == '__main__':
    method = 'GET'  # ????????? ??????????????? ????????? GET
    keyword = '????????????'  # ????????? ?????????, ???????????? ?????????????????? ????????? ???????????????.
    limit = 5  # ????????? ????????? ???????????? ??????. ???????????? ???????????????.
    access_key = 'c56a1184-e722-4227-84af-0577f0fd20c7'  # API access key
    secret_key = '74c26426479c2279a16a300685820e7f835d0c0e'  # API secret key
    # URL = "/v2/providers/affiliate_open_api/apis/openapi/products/search?keyword=" + urllib.parse.quote(
    #     keyword) + "&limit=" + str(limit)
    URL = "/v2/providers/affiliate_open_api/apis/openapi/products/goldbox?subId=AF0863723"
    test = cupangMgr()
    authorization = test.generateHmac(method, URL, secret_key, access_key)  # HMAC ??????
    # productdata = test.get_productsdata(method, authorization, keyword, limit)  # API ??????
    productdata = test.get_productsdata(method, authorization)  # API ??????
    goldbox=[]
    i = 0
    for i in range(9):
        list =productdata[i]['productUrl']
        goldbox.append(list)
    print(goldbox)
        # print(productdata[0]['productUrl'])  # ?????? ??????

    test.shopping()
    time.sleep(3600)