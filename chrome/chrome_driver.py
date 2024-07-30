# pip install selenium
# pip install -U user_agent
# pip install user-agents
# pip install webdriver_manager
from bs4 import BeautifulSoup
from user_agent import generate_user_agent
from user_agents import parse
from selenium import webdriver  # 자동화 툴
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from tqdm import tqdm
import time  # 시간 지연
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

# 서비스 환경별 크롬 드라이브 구분
def chrome_driver() :

   # path = crawling_path + chromedriver
   # torexe = os.popen(r'/bin/tor')
   # PROXY = "socks5://localhost:9051" # IP:PORT or HOST:PORT
   userAgent = generate_user_agent()
   user_agent = parse(userAgent)

   # 옵션 설정
   service = Service(executable_path="C:\\Users\\DESK-1\\Desktop\\crawling\\chromedriver\\chromedriver.exe")
   chrome_options = webdriver.ChromeOptions()
   #chrome_options.add_argument("--headless=new")
   chrome_options.add_argument("--disable-extensions")
   chrome_options.add_argument("disable-infobars")
   chrome_options.page_load_strategy = 'normal'
   chrome_options.add_argument('--enable-automation')
   chrome_options.add_argument('disable-infobars')
   chrome_options.add_argument('disable-gpu')
   chrome_options.add_argument('--no-sandbox')
   chrome_options.add_argument('user-agent={}'.format(user_agent))
   chrome_options.add_argument('--lang=ko_KR')
   chrome_options.add_argument('--ignore-certificate-errors')
   chrome_options.add_argument('--allow-insecure-localhost')
   chrome_options.add_argument('--allow-running-insecure-content')
   chrome_options.add_argument('--disable-notifications')
   chrome_options.add_argument('--disable-dev-shm-usage')
   chrome_options.add_argument('--disable-browser-side-navigation')
   chrome_options.add_argument('--mute-audio')
   #    Tor 프록시 설정 (ip 우회)
   # chrome_options.add_argument('--proxy-server=%s' % PROXY)
   chrome_options.add_argument("--headless=new") # bask단으로 돌림

   # 브라우저 열기
   driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
   # driver = webdriver.Chrome(service=service, options=chrome_options)

   driver.implicitly_wait(3)

   return driver


if __name__ == "__main__":
    driver = chrome_driver()
    # Your crawling code here
    # Example: driver.get("http://www.example.com")*[@id="contents"]/div[2]/fieldset/fieldset/div[2]/a[2]