from selenium.webdriver.common.by import By
from tqdm import tqdm
import time  # 시간 지연
import pandas as pd
from chrome.driver import chrome_driver













if __name__ == "__main__":

    driver = chrome_driver()
    url = 'https://www.coffeebeankorea.com/store/store.asp'
    driver.get(url)
    time.sleep(5)









