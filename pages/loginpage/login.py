from selenium.webdriver.common.by import By


class LoginPage():

    def __init__(self,driver):
        self.driver=driver


    _usnTextField="username"
    _pwdTextField="pwd"
    _loginButton="loginButton"

    def getusnTextfield(self):
        return self.driver.find_element(By.ID,self._usnTextField)

    def getpwdTextField(self):
        return self.driver.find_element(By.NAME,self._pwdTextField)

    def getLoginButton(self):
        return self.driver.find_element(By.ID, self._loginButton)


    def enterUSN(self,usn1):
        self.getusnTextfield().send_keys(usn1)

    def enterPwd(self,pwd1):
        self.getpwdTextField().send_keys(pwd1)

    def clickLoginButton(self):
        self.getLoginButton().click()




    def loginMethod(self,usn,pwd):
        self.enterUSN(usn)
        self.enterPwd(pwd)
        self.clickLoginButton()




