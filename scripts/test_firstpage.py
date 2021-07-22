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

    # def setup(self):
    #     #最开始的时候就是运行base_driver获取到手机对象
    #     self.driver = init_driver('Moto')
    #     #这时候需要driver传给BaseAction和firstpage_page，才可以继续使用
    #     self.firstpage_page = FirstPage(self.driver)

    # @pytest.mark.skipif(True, reason="已经玩过了")
    @allure.step(title="测试步骤001")
    #这里是设置用例的级别，会显示到allure报告中
    @allure.severity(allure.severity_level.CRITICAL)
    #点击一下【精致护理】

    #默认精选列表下拉，然后到底点击返回顶部
    def test_backtop(self,login_common_driver):
        self.firstpage_page = FirstPage(login_common_driver)
        if self.firstpage_page.roll_find_nomore_button():
            self.firstpage_page.click_back_top()

    #进入精选tab，然后滚动搜索产品，最后进去详情
    def test_icon1(self,login_common_driver):
        self.firstpage_page = FirstPage(login_common_driver)
        self.firstpage_page.click_icon1()
        time.sleep(1)
        #传一个文件名和一个描述字段,这里直接截个图了
        # self.firstpage_page.screenshot_and_attach("test_icon1",despription_content='第一次图片')

    #滚动查找元素，找到了就点击进去
    # @pytest.mark.skipif(True, reason="已经玩过了")
    def test_move_find_goods1(self,login_common_driver):
        self.firstpage_page = FirstPage(login_common_driver)
        time.sleep(1)
        if self.firstpage_page.roll_find_goods1():
            self.firstpage_page.click_goods1()

    # def teardown(self):
    #     self.driver.quit()

if __name__ == "__main__":
    pytest.main(["-s", "test_firstpage.py"])