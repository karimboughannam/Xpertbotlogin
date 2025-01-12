import pytest
from selenium import webdriver
from time import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from Utilities.Functions import *



class Xpert():

    def __init__(self, driver):
        self.driver = driver

    def Xpertbottesting(self,username,password):
        Xpertbbotlogin(self,username,password)

    def XpertSign(self,username,password,confirmpass,email):
        XpertbotSignuptest(self,username,password,confirmpass,email)