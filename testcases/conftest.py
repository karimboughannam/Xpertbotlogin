import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def LunchDriver(request):
    driver = webdriver.Chrome()
    driver.get("https://xpertbotacademy.online/nova/login")
    request.cls.driver = driver
    yield driver
    driver.quit()