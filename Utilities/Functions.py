#All the fucntions we need to run 
import pytest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, WebDriverException, TimeoutException
from Utilities.utils import AutomationLogger
from pages.creds import *



def Xpertbbotlogin(self,username,password):
    log=AutomationLogger.automation()
    email_locator= (By.XPATH,email)
    log.info("Location email")
    try:
        WebDriverWait(self.driver,60).until(
            EC.presence_of_element_located(email_locator)
        )
    except NoSuchElementException as e:
        self.log.warning("unable to locate element")
    self.driver.find_element(By.XPATH,email).send_keys(username)
    log.info("Sent username")
    time.sleep(1)
    self.driver.find_element(By.XPATH,'//*[@id="password"]').send_keys(password)
    time.sleep(1)
    self.driver.find_element(By.XPATH,'/html/body/div/div/form/button').click()
    time.sleep(1)
    self.driver.find_element(By.XPATH,'//*[@id="nova"]/div/div[2]/div[1]/div[2]/div/button/div').click()
    time.sleep(1)
    self.driver.find_element(By.LINK_TEXT,'Logout').click()
    time.sleep(3)


def Signup(self):
        log=AutomationLogger.automation()
        email_locator= (By.XPATH,email)
        log.info("Location email")
        try:
            WebDriverWait(self.driver,60).until(
                EC.presence_of_element_located(email_locator)
            )
        except NoSuchElementException as e:
            self.log.warning("unable to locate element")
        self.driver.find_element(By.XPATH,email).send_keys(username)
        log.info("Sent username")
        time.sleep(1)
        self.driver.find_element(By.XPATH,'//*[@id="password"]').send_keys(password)
        time.sleep(1)
        self.driver.find_element(By.XPATH,'/html/body/div/div/form/button').click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,'//*[@id="nova"]/div/div[2]/div[1]/div[2]/div/button/div').click()
        time.sleep(1)
        self.driver.find_element(By.LINK_TEXT,'Logout').click()
        time.sleep(3)