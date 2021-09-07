from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select

class Amazon():
    def test(self):
        baseurl = "https://www.amazon.in/"
        driver = webdriver.Chrome()
        driver.get(baseurl)
        driver.maximize_window()
        driver.implicitly_wait(30)
        time.sleep(4)

        #Click on Signup
        signup= driver.find_element(By.XPATH, "//a[@id='nav-link-accountList']" ).click()
        time.sleep(5)

        #Click on Create account
        create= driver.find_element(By.XPATH, "//a[@id='createAccountSubmit']").click()
        time.sleep(5)

        #Enter name
        name = driver.find_element(By.XPATH, "//input[@name='customerName']")
        name.send_keys('Vivek')
        time.sleep(4)

        #Enter Mobile
        mobile= driver.find_element(By.XPATH, "//input[@placeholder='Mobile number']")
        mobile.send_keys('630642502')
        time.sleep(4)

        #Enter Password
        password= driver.find_element(By.XPATH, "//input[@name='password']")
        password.send_keys('Vivek111')
        time.sleep(4)

        #Click on Submit
        submit= driver.find_element(By.XPATH, "//input[@type='submit']").click()
        time.sleep(4)

        driver.close()

a = Amazon()
a.test()

