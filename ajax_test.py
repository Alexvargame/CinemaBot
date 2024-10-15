from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


##driver = webdriver.Chrome()
##  
### get lambdatest
##driver.get("https://accounts.lambdatest.com/register?_gl=1*1vwy6ad*_gcl_au*MTI1ODkyNTE4MC4xNjkxMTQxMzE0")
##  
### get element 
##element = driver.find_element(By.ID,"email")
##  
### send keys 
##element.send_keys("emailid@lt.com")
##  
### get element 
##button_element = driver.find_element(By.LINK_TEXT,"SIGN UP")
##  
### click the element
##button_element.click()
#### 
driver = webdriver.Chrome()
driver.get("https://kinotochka.co/index.php?do=search")
search_form = driver.find_element(By.ID,"searchinput")
search_form.send_keys('Тор')
print(search_form.text)
button_el=driver.find_element(By.ID,'dosearch')
print(button_el)
button_el.click()
#driver.close()


##driver = webdriver.Chrome()
##driver.get("https://www.lambdatest.com")
##email_form = driver.find_element(By.ID,"testing_form")
##print(email_form)
##first_form_input = driver.find_element(By.CLASS_NAME,"form-control")
##print(first_form_input)
##name_input = driver.find_element(By.NAME,"email")
##print(name_input)
##name_input.send_keys('emailid@lambdatest.com')
##print(name_input.text)
##driver.close()
