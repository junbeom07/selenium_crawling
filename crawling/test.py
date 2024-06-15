from selenium import webdriver 
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.common.by import By 
import time 
import urllib.request 
import os 
from tqdm.notebook import tqdm 

key = input("이미지 찾을 대상을 입력해주세요.")


folder_name = key + time.strftime('%Y%m%d%H%M%S')
os.mkdir(folder_name)  

driver= webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get('https://www.google.com/?hl=ko')
driver.implicitly_wait(20)

driver.find_element(By.CLASS_NAME,"gLFyf").send_keys(key)

driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]").click()
driver.implicitly_wait(20)

driver.find_element(By.XPATH,'//*[@id="hdtb-sc"]/div/div/div[1]/div/div[2]/a/div').click()
driver.implicitly_wait(20)

SCROLL_PAUSE_TIME = 1
    

last_height = driver.execute_script("return document.body.scrollHeight")
    
while True:

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    time.sleep(SCROLL_PAUSE_TIME)

    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        try:
            time.sleep(SCROLL_PAUSE_TIME)
            driver.find_element(By.CLASS_NAME,'mye4qd').click()
        except: break
    last_height = new_height

driver.execute_script("window.scrollTo(0, 0)") 
driver.implicitly_wait(20)

links = driver.find_elements(By.CSS_SELECTOR,'#rso > div > div > div.wH6SXe.u32vCb > div > div > div > div.czzyk.XOEbc > h3 > a')

for i, link in tqdm(enumerate(links)):
    link.click()
    driver.implicitly_wait(10)
    imgUrl = driver.find_element(By.CSS_SELECTOR, '#Sva75c > div.A8mJGd.NDuZHe > div.LrPjRb > div.AQyBn > div.BIB1wf.EIehLd.fHE6De > c-wiz > div > div.v6bUne > div.p7sI2.PUxBg > a > img:nth-child(2)').get_attribute("src")
    urllib.request.urlretrieve(imgUrl, f"./{folder_name}/{i+1}.jpg")
 
driver.close()