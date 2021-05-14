import pytest
from time import sleep

@pytest.mark.skip #跳过这条不执行
def test_sub(sub11):#引入conftest.py的值
    assert sub11==10

@pytest.fixture(name='ad')
def add1():
    return 6

def test_add1(ad):
    assert 6==ad #传参直接传函数名，先本py搜名，在conftest中搜索

def add(x,y):
    return x+y
data=[
    (2,3,5),
    (3,3,6),
    (7,8,15)
]

@pytest.mark.parametrize('x,y,z',data)

def test_add(x,y,z):
    assert x+y==z
@pytest.mark.parametrize('x,y,z',data)
def test_add(x,y,z,sub11):  #结合conftest中的变量来用，这个变量不用parametrize里面写入
    try:
        assert x+y+z==sub11
    except:
        print("error")
@pytest.mark.parametrize('x,y,z',data)
class Test_add:
    def test_add(self,x,y,z):
        assert add(x,y)==z #引入别的方法，本py多次调用相同传参

'''
def test_baidu(driver1):
    driver=driver1
    driver.find_element_by_id("kw").send_keys("刘德华")
    driver.find_element_by_id("su").click()
    sleep(3)
'''
pytest.main (['testmock.py'])

