from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time
driver = webdriver.Chrome(executable_path="C:\selenium browser drivers\chromedriver.exe")
# Sign In to Brownells
driver.get("https://www.brownells.com/aspx/account/login.aspx")
driver.implicitly_wait(30)
inputElement=driver.find_element_by_xpath('/html/body/form/div[3]/div/div[3]/section/section/div[1]/fieldset/ul/li[1]/input')
inputElement.send_keys('atnavy90@hotmail.com')
inputElement=driver.find_element_by_xpath('/html/body/form/div[3]/div/div[3]/section/section/div[1]/fieldset/ul/li[2]/input')
inputElement.send_keys('tizzle11')
driver.implicitly_wait(5)
driver.find_element_by_id("ctl00_ContentPlaceHolderColMain_btnSignIn").click()
driver.implicitly_wait(10)

# Navigate to CCI Pistol Primers Page
Mags = 'https://www.brownells.com/magazines/rifle-magazines/magazines/ar-15-30rd-pmag-gen-m3-window-magazine-223-5-56-prod54911.aspx'
CCIprimers = 'https://www.brownells.com/reloading/primers/pistol-primers/pistol-primers-prod79081.aspx'
driver.get(CCIprimers)
try:
        driver.find_element_by_id('btnAdd')
except NoSuchElementException:
        while NoSuchElementException:
                time.sleep(2)
                driver.refresh()


driver.find_element_by_id('btnAdd').click()
driver.find_element_by_id('btnAdd').click()
# Go to Cart and Checkout

driver.get('https://www.brownells.com/aspx/store/checkout.aspx')
driver.find_element_by_id('btnSaveAndContinue').click()
driver.implicitly_wait(2)
inputElement=driver.find_element_by_id('txtCreditCardNumber')
inputElement.send_keys('4000220502689934')
inputElement=driver.find_element_by_id('ccExpirationMonth')
inputElement.send_keys('07')
inputElement=driver.find_element_by_id('ccExpirationYear')
inputElement.send_keys('22')
inputElement=driver.find_element_by_id('txtCVV')
inputElement.send_keys('564')
inputElement=driver.find_element_by_id('txtPhone')
inputElement.send_keys('2312456051')
driver.find_element_by_id('btnSaveAndContinue').click()
driver.implicitly_wait(5)
print('GOT EM')
driver.get(CCIprimers)
try:
        driver.find_element_by_id('btnAdd')
except NoSuchElementException:
        while NoSuchElementException:
                time.sleep(2)
                driver.refresh()


driver.find_element_by_id('btnAdd').click()
driver.find_element_by_id('btnAdd').click()
# Go to Cart and Checkout

driver.get('https://www.brownells.com/aspx/store/checkout.aspx')
driver.find_element_by_id('btnSaveAndContinue').click()
driver.implicitly_wait(2)
inputElement=driver.find_element_by_id('txtCreditCardNumber')
inputElement.send_keys('4000220502689934')
inputElement=driver.find_element_by_id('ccExpirationMonth')
inputElement.send_keys('07')
inputElement=driver.find_element_by_id('ccExpirationYear')
inputElement.send_keys('22')
inputElement=driver.find_element_by_id('txtCVV')
inputElement.send_keys('564')
inputElement=driver.find_element_by_id('txtPhone')
inputElement.send_keys('2312456051')
driver.find_element_by_id('btnSaveAndContinue').click()
driver.implicitly_wait(5)
print('GOT EM TWICE')
driver.get(CCIprimers)
try:
        driver.find_element_by_id('btnAdd')
except NoSuchElementException:
        while NoSuchElementException:
                time.sleep(2)
                driver.refresh()


driver.find_element_by_id('btnAdd').click()
driver.find_element_by_id('btnAdd').click()
# Go to Cart and Checkout

driver.get('https://www.brownells.com/aspx/store/checkout.aspx')
driver.find_element_by_id('btnSaveAndContinue').click()
driver.implicitly_wait(2)
inputElement=driver.find_element_by_id('txtCreditCardNumber')
inputElement.send_keys('4000220502689934')
inputElement=driver.find_element_by_id('ccExpirationMonth')
inputElement.send_keys('07')
inputElement=driver.find_element_by_id('ccExpirationYear')
inputElement.send_keys('22')
inputElement=driver.find_element_by_id('txtCVV')
inputElement.send_keys('564')
inputElement=driver.find_element_by_id('txtPhone')
inputElement.send_keys('2312456051')
driver.find_element_by_id('btnSaveAndContinue').click()
driver.implicitly_wait(5)
print('GOT EM FOR 3')
