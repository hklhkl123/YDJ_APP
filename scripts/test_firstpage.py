import time
import os,sys
import pytest
import allure

sys.path.append(os.getcwd())

from base.base_driver import init_driver
from page.firstpage_page import FirstPage
from base.base_yaml import yml_data_with_filename_and_key

#类的名字不需要下划线，就这个就可以
class TestIcon(object):

    def setup(self):
        self.driver = init_driver()
        self.firstpage_page = FirstPage(self.driver)
    #点击一下【精致护理】
    def test_icon1(self):
        self.firstpage_page.click_icon1()
        time.sleep(3)
        current_time = time.time()
        #使用时间戳拼起来截个图
        self.firstpage_page.screenshot("test_icon1"+"_"+str(current_time))

    def teardown(self):
        self.driver.quit()

if __name__ == "__main__":
    pytest.main(["-s", "test_firstpage.py"])