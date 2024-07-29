from selenium.webdriver.common.by import By
from tqdm import tqdm
import time  # 시간 지연
import pandas as pd
from chrome.driver import chrome_driver













if __name__ == "__main__":
    url = 'https://www.hollys.co.kr/store/korea/korStore2.do'

    driver = chrome_driver()
    driver.get(url)

    df = pd.DataFrame(columns=['지역', '매장명', '영업중', '주소', '전환번호'])
    driver.maximize_window()

    time.sleep(2)
    i = 0
    page = 9
    tmp = 10
    while (1):
        try:
            trs = driver.find_elements(By.XPATH, '''//[@id="contents"]/div[2]/fieldset/fieldset/div[1]/table/tbody/tr''')
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
                    driver.find_element(By.XPATH, f'''//[@id="contents"]/div[2]/fieldset/fieldset/div[2]/a[{tmp}]/img''').click()
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
            time.sleep(2)
        except Exception as e:
            print(e)
            break
        else:
            print(page)
    print(df)










