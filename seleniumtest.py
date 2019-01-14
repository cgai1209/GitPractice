from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--headless')

#解凍したchromedriverが置いてあるパスを指定
driver = webdriver.Chrome('/home/ec2-user/environment/chromedriver', chrome_options=options)

driver.get('https://www.google.co.jp/search?q=chrome')
driver.save_screenshot('screenshot.png')
driver.quit()



