from bs4 import BeautifulSoup
import requests
import pandas as pd

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

    df = pd.DataFrame() #데이터프레임 생성

    url = "https://www.hollys.co.kr/store/korea/korStore2.do"
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html,'html.parser')
    #print(response.text)
    #print(soup)

    print(crawling(soup))

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


