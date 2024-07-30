from chrome.chrome_driver import chrome_driver
from selenium.webdriver.common.by import By
import pandas as pd
import time, random
from bs4 import BeautifulSoup




if __name__ == "__main__":

    df = pd.DataFrame(columns=['메뉴', ' 설명', '포화지방', '나트륨', '탄수화물', '당', '카페인', '단백질'])

    url = "https://www.coffeebeankorea.com/member/login.asp#loginArea"
    driver = chrome_driver()
    driver.get(url)
    driver.maximize_window()
    time.sleep(random.uniform(1,4))
    # login
    username = driver.find_element(By.XPATH, '''//*[@id="loginForm"]/fieldset/div/div[1]/div[1]/div/p[1]/input''')
    password = driver.find_element(By.XPATH, '''//*[@id="loginForm"]/fieldset/div/div[1]/div[1]/div/p[2]/input''')
    username.send_keys("godbu1201")
    time.sleep(random.uniform(1,4))
    password.send_keys("qwer1234")
    time.sleep(random.uniform(1,4))
    # button click
    driver.find_element(By.XPATH, '''//*[@id="loginForm"]/fieldset/div/div[1]/div[1]/a''').click()
    time.sleep(random.uniform(1,4))
    # menu click
    driver.find_element(By.XPATH, '''//*[@id="gnb"]/ul/li[3]/a''').click()
    time.sleep(random.uniform(1,4))
    # 정적 크롤링
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    print(soup)













