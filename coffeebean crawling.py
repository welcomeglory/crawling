from chrome.chrome_driver import chrome_driver
from selenium.webdriver.common.by import By
import pandas as pd
import time, random
from bs4 import BeautifulSoup
import re





if __name__ == "__main__":

    df = pd.DataFrame(columns=['메뉴', '설명', '열량', '포화지방', '나트륨', '탄수화물', '당', '카페인', '단백질'])

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
    ul = soup.select_one('''#contents > div > div > ul''')
    lis = ul.find_all('li')
    jdx = 0
    page =4
    while(1):
        try:
            for i, li in enumerate(lis):
                menu = li.select_one(f'''#contents > div > div > ul > li:nth-child({i+1}) > dl > dt > span.kor''').text
                des = li.select_one(f'''#contents > div > div > ul > li:nth-child({i+1}) > dl > dd''').text.strip()
                dls = li.find_all('dl')
                tmpList = [menu, des]
                for idx, dl in enumerate(dls):
                    if idx == 0: continue
                    numbers = re.sub(r'[^0-9]', '', dl.text)
                    tmpList.append(numbers)
                df.loc[jdx] = tmpList
                jdx += 1
            if page == 4:
                driver.find_element(By.XPATH, f'''//*[@id="contents"]/div/div/div/a[{page}]''').click()
                page += 1
            else:
                driver.find_element(By.XPATH, f'''//*[@id="contents"]/div/div/div/a[{page}]''').click()
            time.sleep(random.uniform(1, 4))

            # 다음 페이지 이동(화살표 클릭)
            # driver.find_element(By.XPATH, '''//*[@id="contents"]/div/div/div/a[4]''').click()
        except Exception as e:
            print(e)
            break
    print(df.to_csv("data/coffeebean.csv"))




    # df.loc[0] = [menu, des, dls[1].text.strip(), dls[2].text.strip(), dls[3].text.strip(),
    #              dls[4].text.strip(), dls[5].text.strip(), dls[6].text.strip(), dls[7].text.strip()]
    # print(df)






