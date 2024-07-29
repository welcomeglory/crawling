from selenium.webdriver.common.by import By
from tqdm import tqdm
import time  # 시간 지연
import pandas as pd
from chrome.driver import chrome_driver
from tqdm import tqdm
from bs4 import BeautifulSoup



def coffeeBean_crawling():
    url = 'https://www.coffeeBeanKorea.com/store/store.asp'
    wd = chrome_driver()
    df = pd.DataFrame(columns=['store','address','phone']) # 데이터프레임 생성

    for i in range(1, 370):
        wd.get(url) #url로 이동
        try:
            wd.execute_script(f'storePops2({i})') # js 실행
            html = wd.page_source # 페이지 소스 가져오기
            soup = BeautifulSoup(html, 'html.parser') # HTML 파싱
            mName = soup.select('div.stor_txt>h2') # 매장 이름 추출
            name = mName[0].string
            # 매장 정보 추출
            info = soup.select('div.store_txt>table.store_table>tbody>tr>td')
            addresses = list(info[2])
            address = addresses[0]
            phone = info[3].string
            df.loc[i] = [name, address, phone] # 데이터프레임에 데이터 추가
        except Exception as e:
            print(e)
            continue
        else:
            print("success")

    df.to_csv("./data/coffen_info.csv") # csv 파일로 저장











if __name__ == "__main__":

    url = 'https://www.hollys.co.kr/store/korea/korStore2.do'

    driver = chrome_driver()
    driver.get(url)

    df = pd.DataFrame(columns=['지역', '매장명', '영업중', '주소', '전화번호'])
    driver.maximize_window()
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    time.sleep(2)
    i = 0
    page = 9
    tmp = 10
    while(1):
        try:
            trs = driver.find_elements(By.XPATH, '''//*[@id="contents"]/div[2]/fieldset/fieldset/div[1]/table/tbody/tr''')
            for idx, tr in enumerate(trs):
                data = tr.text
                text_list = data.split(' ')
                legion = ' '.join(text_list[:2])
                name = text_list[2]
                state = text_list[3]
                address = ' '.join(text_list[4:-1])
                phone = text_list[-1]
                df.loc[i] = [legion, name, state, address, phone]
                i += 1
            if page % 10 == 0:
                page += 1
                if tmp == 10:
                    driver.find_element(By.XPATH, f'''//*[@id="contents"]/div[2]/fieldset/fieldset/div[2]/a[{tmp}]/img''').click()
                    tmp = 11
                else:
                    driver.find_element(By.XPATH, f'''//*[@id="contents"]/div[2]/fieldset/fieldset/div[2]/a[{tmp}]/img''').click()
            elif page % 10 == 1:
                page += 1
                continue
            else:
                print(page)
                driver.find_element(By.LINK_TEXT, f"{page}").click()
                page += 1
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(2)
        except Exception as e:
            print(e)
            break
        else:
            print(page)
    print(df)




    # for page in range(1,10):
    #     for idx, tr in enumerate(trs):
    #         data = tr.text
    #         text_list = data.split(' ')
    #         legion = ' '.join(text_list[:2])
    #         name = text_list[2]
    #         state = text_list[3]
    #         address = ' '.join(text_list[4:-1])
    #         phone = text_list[-1]
    #         df.loc[idx] = [legion, name, state, address, phone]
    #         if idx < 0:
    #             driver.find_element(f'''//*[@id="contents"]/div[2]/fieldset/fieldset/div[2]/a[{idx}]''').click()
    #         else:
    #             continue

    # print(df)
    # exit()








    # coffeeBean_crawling() # 커피빈 크롤링 함수 호출(주석 처리됨)
    # driver  = chrome_driver() # chrome 드라이버 초기화
    #
    # for page in range(1,10):
    #     url = f"https://www.hollys.co.kr/store/korea/korStore2.do?pageNo={page}"
    #     driver.get(url) # 각 페이지 url로 이동
    #     time.sleep(3) # 3초 대기
    #
    #
    #
    # url = 'https://www.hollys.co.kr/store/korea/korStore2.do'
    # driver = chrome_driver()
    #
    # driver.get(url)
    #
    # path = "data/holly2.csv"
    #
    # result_df = pd.DataFrame()
    #
    # trs = driver.find_elements(By.XPATH, '''//*[@id="contents"]/div[2]/fieldset/fieldset/div[1]/table/tbody/tr''')
    # # print(list(trs))
    # time.sleep(3)
    #
    # # driver.find_element(By.XPATH, '''//*[@id="contents"]/div[2]/fieldset/fieldset/div[2]/a[2]''').click()
    # # time.sleep(3)
    #
    #
    # for idx , tr in enumerate(trs):
    #     data = tr.text
    #     print(data)
    #     data_list = data.split(" ")
    #     print(data_list)
    #     # driver.find_element(By.XPATH, f'''//*[@id="contents"]/div[2]/fieldset/fieldset/div[2]/a[{i}]''').click()
    #     # time.sleep(3)


    # url = 'https://www.coffeebeankorea.com/member/login.asp#loginArea'
    # driver.get(url)
    # time.sleep(2)

    # username = driver.find_element(By.XPATH, '''//*[@id="loginForm"]/fieldset/div/div[1]/div[1]/div/p[1]/input''')
    # password = driver.find_element(By.XPATH, '''//*[@id="loginForm"]/fieldset/div/div[1]/div[1]/div/p[2]/input''')
    # time.sleep(1)

    # username.send_keys("godbu1201")
    # password.send_keys("qwer1234")
    #
    # time.sleep(2)
    #
    # driver.find_element(By.XPATH, '''/html/body/div[3]/div[3]/div/div[2]/form/fieldset/div/div[1]/div[1]/a''').click()
    # time.sleep(5)












