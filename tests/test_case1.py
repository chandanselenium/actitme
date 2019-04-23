from selenium import webdriver
from pages.loginpage.login import LoginPage
import time

class ValidLogin():

    def testCaseLogin(self):

        driver=webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get("http://localhost/login.do")

        lp=LoginPage(driver)
        lp.loginMethod("admin","manager")

        exTitle="actiTIME - Enter Time-Track"

        time.sleep(5)

        acTitle=driver.title
        print(acTitle)


        if exTitle in acTitle:
            print("loggin is successful")
        else:
            print("loggin is not successful")


obj=ValidLogin()
obj.testCaseLogin()

