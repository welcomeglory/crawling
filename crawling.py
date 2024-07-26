from bs4 import BeautifulSoup
import requests
import pandas as pd
from tqdm import tqdm

def crawling(soup):

    table = soup.find('table')  # 테이블만 가져옴(_all을 쓰면 []리스트에 담김)
    ths = table.find_all('th')  # <th class="noline" scope="col">지역</th>
    columns = []  # 리스트 생성
    for idx, th in enumerate(ths):
        if idx == 4: continue  # idx 4 제외
        columns.append(th.string)
    df = pd.DataFrame(columns=columns)
    trs = table.find_all('tr')
    i = 0
    for jdx, tr in enumerate(trs):
        if jdx == 0: continue
        tds = tr.find_all('td')
        temps = []
        for idx, td in enumerate(tds):
            if idx == 4: continue
            temps.append(td.text)
        df.loc[i] = temps
        i += 1
    return df





if __name__ == "__main__":

    url = f"https://www.hollys.co.kr/store/korea/korStore2.do?pageNo=1"
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    tr = soup.select("#contents > div.content > fieldset > fieldset > div.tableType01 > table > tbody > tr:nth-child(1) > td.noline.center_t")
    print(tr)
    exit()

    page = 1
    df = pd.DataFrame()
    while tqdm(1):
        try:
            url = f"https://www.hollys.co.kr/store/korea/korStore2.do?pageNo={page}"
            response = requests.get(url)
            html = response.text
            soup = BeautifulSoup(html,'html.parser')
            new_df = crawling(soup)
            page += 1
            print(page)
        except Exception as e:
            print(e)
            break
        else:
            df = pd.concat([df, new_df])
    df.reset_index(inplace=True)
    path=""
    df.to_csv("data/hollys.csv")

    #df = crawling(soup)

    # tds = trs[1].find_all('td')
    # td = tds[0]
    # print(td)
    # df = pd.DataFrame(columns=['지역', '매장명', '현황', '주소', '전화번호']) #데이터프레임 생성
    # print(df) # Columns: [지역, 매장명, 현황, 주소, 전화번호]
    #datum = ths[0].string
    #print(datum)
    # for th in ths:
    #     print(th.text) # 지역 매장명 현황 주소 매장 서비스 전화번호
    # trs = table.find_all('tr')
    # print(trs)


