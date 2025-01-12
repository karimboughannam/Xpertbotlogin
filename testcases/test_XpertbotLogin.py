import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException , TimeoutException
from pages.creds import *
from pages.XpertbotLogin import Xpert
from Utilities.utils import AutomationLogger


@pytest.mark.usefixtures("LunchDriver")

class TestXperbotlogin:
    log= AutomationLogger.automation()
    test_date=AutomationLogger.get_newest_excel_file("testdata","Sheet1")
    @pytest.mark.parametrize("test_data",test_date)
    # @pytest.mark.parametrize("test_data", [{"username":"karimbou","password":"123456","expected_result":"Invalid credentials"}])
    def test_xpertbotlogin(self,test_data):
        
        try:    
            self.log.info("Test Started")
            X=Xpert(self.driver)
            self.log.info("Sent Driver")
            X.Xpertbottesting(**test_data)
            self.log.info("Sent Data")
        except Exception as e:
            self.log.Error(f"Test Failed {e}")
            pytest.fail()

        
@pytest.mark.usefixtures("LunchDriver")
class TestXperbotSignup:
    log= AutomationLogger.automation()
    test_date=AutomationLogger.get_newest_excel_file("testdata","Sheet2")
    @pytest.mark.parametrize("test_data",test_date)
    # @pytest.mark.parametrize("test_data", [{"username":"karimbou","password":"123456","expected_result":"Invalid credentials"}])
    def test_xpertbotSigup(self,test_data):
        
        try:    
            self.log.info("Test Started")
            X=Xpert(self.driver)
            self.log.info("Sent Driver")
            X.XpertSign(**test_data)
            self.log.info("Sent Data")
        except Exception as e:
            self.log.Error(f"Test Failed {e}")
            pytest.fail()