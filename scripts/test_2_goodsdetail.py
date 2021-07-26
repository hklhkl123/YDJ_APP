import time
import os,sys
import pytest
import allure

sys.path.append(os.getcwd())
from page.goodsdetail_page import GoodsDetail
from page.homepage_page import HomePage
from base.base_yaml import yml_data_with_filename_and_key

#类的名字不需要下划线，就这个就可以
class TestBuy(object):

    #进入精选tab
    @pytest.mark.skipif(True, reason="已经玩过了")
    def test_01_icon1_jingzhi(self,login_common_driver):
        self.homepage_page = HomePage(login_common_driver)
        self.homepage_page.click_icon1_jingzhihuli()
        time.sleep(1)

    #滚动查找元素，找到了就点击进去
    @pytest.mark.skipif(True, reason="已经玩过了")
    def test_02_move_find_goods(self,login_common_driver):
        self.homepage_page = HomePage(login_common_driver)
        time.sleep(1)
        if self.homepage_page.roll_find_goods("BC07"):
            self.homepage_page.click_goods("BC07")


    # @allure.step(title="测试步骤001")
    # #这里是设置用例的级别，会显示到allure报告中
    # @allure.severity(allure.severity_level.CRITICAL)
    #进详情后滚动商品图3次
    # @pytest.mark.skipif(True, reason="已经玩过了")
    def test_03_roll_picture(self,login_common_driver):
        self.goodsdetail_page = GoodsDetail(login_common_driver)
        self.goodsdetail_page.right_roll_3_times()
        self.goodsdetail_page.left_roll_3_times()
        # time.sleep(3)

    @pytest.mark.skipif(True, reason="已经玩过了")
    #获取商品的一些参数并且打印，后面可以断言
    def test_04_getinfo(self,login_common_driver):
        self.goodsdetail_page = GoodsDetail(login_common_driver)
        self.goodsdetail_page.print_info()

    # @pytest.mark.skipif(True, reason="已经玩过了")
    def test_05_favorites(self,login_common_driver):
        self.goodsdetail_page = GoodsDetail(login_common_driver)
        self.goodsdetail_page.click_favorites()

    #滚动找地址，点击进去再退回来
    def test_06_move_find_address(self,login_common_driver):
        self.goodsdetail_page = GoodsDetail(login_common_driver)
        if self.goodsdetail_page.roll_find_element():
            self.goodsdetail_page.click_address()
        time.sleep(2)
        self.goodsdetail_page.press_keycode_back()

    #点进购物车然后退回来
    def test_07_click_shopping_cart(self,login_common_driver):
        self.goodsdetail_page = GoodsDetail(login_common_driver)
        self.goodsdetail_page.click_shopping_cart()
        time.sleep(2)
        self.goodsdetail_page.press_keycode_back()

    #点击加入购物车，增加2个产品，点击确定,打印购物车数量
    def test_08_add_goods(self,login_common_driver):
        self.goodsdetail_page = GoodsDetail(login_common_driver)
        self.goodsdetail_page.click_add_goods_button()
        for i in range(2):
            self.goodsdetail_page.click_add_goods_num()
        time.sleep(1)
        self.goodsdetail_page.click_confirm_button()
        self.goodsdetail_page.print_shopping_cart_num()

    #点击立即购买，增加2个产品确定，然后返回
    def test_09_buy_now(self,login_common_driver):
        self.goodsdetail_page = GoodsDetail(login_common_driver)
        self.goodsdetail_page.click_buy_now()
        for i in range(2):
            self.goodsdetail_page.click_add_goods_num()
        self.goodsdetail_page.click_confirm_button()
        self.goodsdetail_page.press_keycode_back()

    def test_close_app(self,login_common_driver):
        login_common_driver.close_app()



    # def teardown(self):
    #     self.driver.quit()

if __name__ == "__main__":
    pytest.main(["-s", "test_2_goodsdetail.py"])