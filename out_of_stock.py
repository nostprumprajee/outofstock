import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

#from twilio.rest import Client

#client = Client("your_twillio_keys", "your_twillio_id")
driver = webdriver.Chrome('./chromedriver')
# driver = webdriver.Chrome(ChromeDriverManager().install())
# enter items link below
driver.get("https://www.apple.com/th/shop/buy-iphone/iphone-14-pro/%E0%B8%88%E0%B8%AD%E0%B8%A0%E0%B8%B2%E0%B8%9E%E0%B8%82%E0%B8%99%E0%B8%B2%E0%B8%94-6.7-%E0%B8%99%E0%B8%B4%E0%B9%89%E0%B8%A7-256gb-%E0%B9%80%E0%B8%87%E0%B8%B4%E0%B8%99")

print(driver.title)
# el = driver.find_element_by_tag_name('body')
# el = driver.find_element_by_class_name("rf-productlocator-buttontitle")
buttons = driver.find_element(By.XPATH,'//button[@class="rf-pickup-quote-overlay-trigger as-buttonlink"]')
driver.execute_script("arguments[0].click();", buttons)
time.sleep(2)
f = driver.find_element(By.XPATH,'//input[@class="form-textbox-input rf-productlocator-form-textinput"]')
f.send_keys("10220")
f.send_keys(Keys.ENTER)
time.sleep(2)
el = driver.find_element(By.XPATH, '//span[@class="rf-productlocator-buttontitle"]')
# search_box.send_keys('ChromeDriver')

# search_box.submit()
str = el.text 
print(str)
if(str.find("ไม่มีจำหน่ายที่ร้าน 2 ที่ใกล้ที่สุดวันนี้") != -1):
    print("It's still not available my guy")
# else: 
    #client.messages.create(to = "+xxxxxxxxxxxx", from_ = "+xxxxxxxxxxxx", body = "its available")      
    #create a twillio account and use the assigned "from" number
    
driver.close()


