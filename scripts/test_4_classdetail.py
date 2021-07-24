import time
import os,sys
import pytest
import allure

sys.path.append(os.getcwd())

from base.base_driver import init_driver
from page.classdetail_page import ClassPage
from base.base_yaml import yml_data_with_filename_and_key

#类的名字不需要下划线，就这个就可以
class TestClass(object):

    # # @pytest.mark.skipif(True, reason="已经玩过了")
    # @allure.step(title="测试步骤001")
    # #这里是设置用例的级别，会显示到allure报告中
    # @allure.severity(allure.severity_level.CRITICAL)

    #通过2种方式进入到class界面
    def test_01_class_enter(self,login_common_driver):
        self.classdetail_page = ClassPage(login_common_driver)
        self.classdetail_page.click_class_button_1()
        self.classdetail_page.click_class_2()



    # def test_close_app(self,login_common_driver):
    #     login_common_driver.close_app()


if __name__ == "__main__":
    pytest.main(["-s", "test_4_classdetail.py"])