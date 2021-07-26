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

    #进入到class界面
    def test_01_class_enter(self,login_common_driver):
        self.classdetail_page = ClassPage(login_common_driver)
        self.classdetail_page.click_class_button_1()
        #这是第二种进入按键
        # self.classdetail_page.click_class_2()

    #向下滚动左侧的分类栏，最后点击【其他】
    def test_02_roll_bigclass(self,login_common_driver):
        self.classdetail_page = ClassPage(login_common_driver)
        #获取到默认进来的营养健康的x坐标
        x = self.classdetail_page.find_big_class1_positon_x()
        #传个下面的函数进行，基于x不变的向下滚动
        self.classdetail_page.roll_bigclass_find_big_class_6(x,"down")
        self.classdetail_page.click_class_10()

    #向上滚动右侧的商品栏，找到产品后点击进去，然后返回
    def test_03_roll_goodslist(self,login_common_driver):
        self.classdetail_page = ClassPage(login_common_driver)
        self.classdetail_page.roll_find_goods_and_click_goods_D200518("up")
        self.classdetail_page.click_goods_back_button()





    # def test_close_app(self,login_common_driver):
    #     login_common_driver.close_app()


if __name__ == "__main__":
    pytest.main(["-s", "test_4_classdetail.py"])