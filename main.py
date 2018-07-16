import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Chromのパス
CHROME_BIN = '/usr/bin/chromium'

# Seleniumドライバーのパス
CHROME_DRIVER = os.path.expanduser('/usr/bin/chromedriver')

# DMMMobile用のログインページURL
URL = 'https://accounts.dmm.com/service/login/password/=/path=DRVESRUMTh1VE19XHVILWk8GWVsfVB1JAwVSSQ__'

# ログイン用情報
LOGIN_ID = os.environ['DMM_ID']
PASSWORD = os.environ['DMM_PASSWORD']

# 各待機時間
WAIT_TIME = 1.0

# Chromeの初期設定
options = Options()
options.binary_location = CHROME_BIN
options.add_argument('--headless')
options.add_argument('--window-size=1280,3000')
driver = webdriver.Chrome(CHROME_DRIVER, chrome_options=options)

# DMMMobileのログインページにアクセス
driver.get(URL)

# メールアドレスとパスワードを入力
driver.find_element_by_id('login_id').send_keys(LOGIN_ID)
driver.find_element_by_id('password').send_keys(PASSWORD)
time.sleep(WAIT_TIME)

# ログインボタン押下
driver.find_element_by_xpath("//form[@name='loginForm']//input[@type='submit']").click()

# 通信量が表示されるまで待機
WebDriverWait(driver, WAIT_TIME * 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'number')))

# 通信量を出力
print(driver.find_element_by_class_name('number').text)

# Chromeを終了
driver.quit()
