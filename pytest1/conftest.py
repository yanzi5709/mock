import pytest
from selenium import webdriver
@pytest.fixture(name='sub11')
def sub1():
    return 9
@pytest.fixture(name='driver1')
def driver():
    driver=webdriver.Chrome()
    driver.get("http://www.baidu.com")
    yield driver #用yield 相当于yield前的是setup 后的是teardown阶段。
    driver.close()


