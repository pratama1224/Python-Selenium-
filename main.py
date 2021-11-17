import os

WAIT_TIME = 60
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

email = 'pratamaxadjie@gmail.com'
password = '12345678'

driver = webdriver.Chrome( executable_path=os.path.abspath('chromedriver'))
driver.get(

'https://accounts.google.com/signin/v2  /identifier?service=youtube&uilel=3&passive=true&continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Den-GB%26next%3Dhttps%253A%252F%252Fwww.youtube.com%252Fwatch%253Fv%253DuoibHhLRYTM%2526feature%253Dyoutu.be&hl=en-GB&ec=65620&flowName=GlifWebSignIn&flowEntry=ServiceLogin' )
driver.find_elements_by_css_selector('VfPpkd-vQzf8d').sendkeys(email)
driver.find_elements_by_id_( 'identifierNext' ).click()
driver.find_element_by_name( ('password').send_keys(password))

# Tunggu sampai password muncul
element = WebDriverWait( driver, WAIT_TIME.until(EC.element_to_be_clickable(By.NAME, 'password')),

element.send_keys(password),
driver.find_element_by_id('password').click())

#Tunggu sampai password muncul
element = WebDriverWait( driver, WAIT_TIME.until(EC.element_to_be_clickable(By.CSS_SELECTOR, 'password')),

element.click(),
driver.find_elements_by_id('identifier-prompt-conform-button').click(),
