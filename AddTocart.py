from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select

class Amazonitem():
    def test(self):
        baseurl = "https://www.amazon.in/"
        driver = webdriver.Chrome()
        driver.get(baseurl)
        driver.maximize_window()
        driver.implicitly_wait(30)
        time.sleep(4)

        #click on search
        search = driver.find_element(By.XPATH, "//input[@id = 'twotabsearchtextbox']")
        search.send_keys('Redmi 9 Power')
        time.sleep(5)

        #Click on Search
        button = driver.find_element(By.XPATH, "//input[@Value='Go']").click()
        time.sleep(4)

        #click on item
        item= driver.find_element(By.XPATH, "//div/img[@alt='Redmi 9 Power (Blazing Blue, 4GB RAM, 64GB Storage) - 6000mAh Battery |FHD+ Screen| 48MP Quad Camera | Alexa Hands-Free Ca...']").click()
        time.sleep(4)

        #Add to cart
        cart= driver.find_element(By.XPATH, "//input[@title= 'Add to Shopping Cart']").click()
        time.sleep(4)



        driver.close()

a = Amazonitem()
a.test()
