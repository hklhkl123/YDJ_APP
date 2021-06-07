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

    # @pytest.mark.skipif(True, reason="已经玩过了")
    @allure.step(title="测试步骤001")
    #这里是设置用例的级别，会显示到allure报告中
    @allure.severity(allure.severity_level.CRITICAL)
    #点击一下【精致护理】
    def test_icon1(self):
        self.firstpage_page.click_icon1()
        time.sleep(3)
        #传一个文件名和一个描述字段,这里直接截个图了
        self.firstpage_page.screenshot_and_attach("test_icon1",despription_content='第一次图片')

    #这里就是往下滚动3下
    def test_move(self):
        for i in range(3):
            self.firstpage_page.scroll_page_one_time()


    def teardown(self):
        self.driver.quit()

if __name__ == "__main__":
    pytest.main(["-s", "test_firstpage.py"])