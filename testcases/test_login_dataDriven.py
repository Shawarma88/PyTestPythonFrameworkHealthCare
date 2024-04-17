import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readproperties import ReadConfig
from utilities import ExcelUtils
from utilities.customLogger import LogGen

class Test_002_Login_DataDriven:
    baseUrl = ReadConfig.getApplicationURL()
    logger = LogGen.LogGeneration()

    def test_login_datadriven(self, setup):
        self.logger.info("******************** Test_002_Login_DataDriven ***********************")
        self.logger.info("******************** Verifying the login test ***********************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()
        ObjectLogin = LoginPage(self.driver)
        MakeAppoitmentLocator = ObjectLogin.logout_xpath




        ObjectLogin.clickLogin()
        actual_title = self.driver.title
        if MakeAppoitmentLocator.is_
            self.logger.info("******************** Login test is passed ***********************")
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.logger.error("******************** Login test is failed ***********************")
            self.driver.close()
            assert False
