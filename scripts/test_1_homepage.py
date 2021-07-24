import time
import os,sys
import pytest
import allure

sys.path.append(os.getcwd())

from base.base_driver import init_driver
from page.homepage_page import HomePage
from base.base_yaml import yml_data_with_filename_and_key

#类的名字不需要下划线，就这个就可以
class TestIcon(object):

    # def setup(self):
    #     #最开始的时候就是运行base_driver获取到手机对象
    #     self.driver = init_driver('Moto')
    #     #这时候需要driver传给BaseAction和firstpage_page，才可以继续使用
    #     self.firstpage_page = FirstPage(self.driver)

    # # @pytest.mark.skipif(True, reason="已经玩过了")
    # @allure.step(title="测试步骤001")
    # #这里是设置用例的级别，会显示到allure报告中
    # @allure.severity(allure.severity_level.CRITICAL)

    #默认精选列表下拉，然后到底点击返回顶部
    # @pytest.mark.skipif(True, reason="已经玩过了")
    def test_01_backtop(self,login_common_driver):
        self.homepage_page = HomePage(login_common_driver)
        if self.homepage_page.roll_find_nomore_button():
            self.homepage_page.screenshot_and_attach("test_backtop", despription_content='找到底部语截图')
            time.sleep(2)
            self.homepage_page.click_back_top()

    #进入精选tab
    # @pytest.mark.skipif(True, reason="已经玩过了")
    def test_02_icon1_jingzhihuli(self,login_common_driver):
        self.homepage_page = HomePage(login_common_driver)
        self.homepage_page.click_icon1_jingzhihuli()
        time.sleep(1)
        #传一个文件名和一个描述字段,这里直接截个图了
        # self.firstpage_page.screenshot_and_attach("test_icon1",despription_content='第一次图片')

    #滚动查找元素，找到了就点击进去,最后点返回
    # @pytest.mark.skipif(True, reason="已经玩过了")
    def test_03_move_find_goods(self,login_common_driver):
        self.homepage_page = HomePage(login_common_driver)
        time.sleep(1)
        if self.homepage_page.roll_find_goods("BC07"):
            self.homepage_page.screenshot_and_attach("test_move_find_goods1", despription_content='找到素材后截图')
            self.homepage_page.click_goods("BC07")
        self.homepage_page.click_goods_back_button()

    #返回后，在顶部tab进行左右滑动，找到精选tab的y坐标，然后处理
    # @pytest.mark.skipif(True, reason="已经玩过了")
    def test_04_move_tab(self,login_common_driver):
        self.homepage_page = HomePage(login_common_driver)
        # self.homepage_page.click_icon2_yingyang()
        self.homepage_page.click_icon3_caizhuang()
        self.homepage_page.click_icon4_fuzhuang()
        self.homepage_page.click_icon5_muying()
        #到最右侧后，基于5的位置左滑
        self.homepage_page.roll_tab_icon5_muying("left")
        # time.sleep(1)

    #通过2种方式进入到class界面
    def test_05_class_enter(self,login_common_driver):
        self.homepage_page = HomePage(login_common_driver)
        self.homepage_page.click_icon0_jingxuan()
        self.homepage_page.click_class_button_1()
        self.homepage_page.click_class_back_button()
        self.homepage_page.click_icon1_jingzhihuli()
        self.homepage_page.click_class_button_2()

    def test_close_app(self,login_common_driver):
        login_common_driver.close_app()


if __name__ == "__main__":
    pytest.main(["-s", "test_1_homepage.py"])