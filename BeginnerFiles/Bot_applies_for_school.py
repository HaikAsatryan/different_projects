from selenium.webdriver.common.keys import Keys
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

Path = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(Path)

driver.get('https://hayt.emis.am/')

dropdown = driver.find_element('name', 'marzField')

Select(dropdown).select_by_value('5')

search = driver.find_element('name', 'searchSchoolField')

search.send_keys(55)

#driver.implicitly_wait(1)

school_button = driver.find_element(by=By.XPATH, value='//input[@value="Դիտել դպրոցները"]')
school_button.click()

school_55 = driver.find_element(by=By.XPATH, value='(//a[@class="submit_button mt-3 mb-2 pt-2 pb-2 pl-4 pr-4 font_size_18"])[2]')
school_55.click()

child_soc = driver.find_element('name', 'child_soc')
child_soc.send_keys('5125160172')

parent_soc = driver.find_element('name', 'parent_soc')
parent_soc.send_keys('6601900737')

parent_firstname = driver.find_element('name', 'parent_firstname')
parent_firstname.send_keys('Արփինե')

parent_lastname = driver.find_element('name', 'parent_lastname')
parent_lastname.send_keys('Սարգսյան')

parent_email = driver.find_element('name', 'parent_email')
parent_email.send_keys('93402203')



