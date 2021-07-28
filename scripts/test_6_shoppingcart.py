import time
import os,sys
import pytest
import allure

sys.path.append(os.getcwd())

from base.base_driver import init_driver
from page.shoppingcart_page import ShoppingCartPage
from page.goodsdetail_page import GoodsDetail
from page.searchgoods_page import SearchGoods

from base.base_yaml import yml_data_with_filename_and_key

class TestShoppingCart(object):
    # @pytest.mark.skipif(True, reason="已经玩过了")
    @allure.step(title="进来先点击一下购物车，发现没有商品然后点击去逛逛")
    #进来先点击一下购物车，发现没有商品然后点击“去逛逛”，就会回到首页
    def test_01_enter_shoppingcart(self,login_common_driver):
        self.shoppingcart_page = ShoppingCartPage(login_common_driver)
        self.shoppingcart_page.click_home_shopping()
        time.sleep(2)
        self.shoppingcart_page.click_shopping_wander_button()

    @allure.step(title="通过搜索产品，点击详情加入购物车")
    #通过其他page的功能调用
    def test_02_make_YS05_into_shoppingcart(self,login_common_driver):
        #继承2个page
        self.searchgoods_page = SearchGoods(login_common_driver)
        self.goodsdetail_page = GoodsDetail(login_common_driver)
        #先通过搜索找到对应的产品，点击进入详情
        self.searchgoods_page.click_search_inputbox_homepage()
        self.searchgoods_page.input_search_inputbox("YS05")
        self.searchgoods_page.click_search_button()
        self.searchgoods_page.click_search_result_YS05()
        #然后通过点击购物车填充数据
        self.goodsdetail_page.click_putinto_shopping_cart()
        self.goodsdetail_page.click_confirm_button()
        time.sleep(3)
        self.goodsdetail_page.click_back_button()
        #然后点击清除搜索记录
        self.searchgoods_page.click_clear_search_button()

    def test_03_make_E06_into_shoppingcart(self,login_common_driver):
        #继承2个page
        self.searchgoods_page = SearchGoods(login_common_driver)
        self.goodsdetail_page = GoodsDetail(login_common_driver)
        #先通过搜索找到对应的产品，点击进入详情
        self.searchgoods_page.input_search_inputbox("E06")
        self.searchgoods_page.click_search_button()
        self.searchgoods_page.click_search_result_E06()
        #然后通过点击购物车填充数据
        self.goodsdetail_page.click_putinto_shopping_cart()
        self.goodsdetail_page.click_confirm_button()
        time.sleep(3)
        self.goodsdetail_page.click_back_button()
        #然后点击清除搜索记录
        self.searchgoods_page.click_clear_search_button()

    def test_04_make_YS10_into_shoppingcart(self,login_common_driver):
        #继承2个page
        self.searchgoods_page = SearchGoods(login_common_driver)
        self.goodsdetail_page = GoodsDetail(login_common_driver)
        #先通过搜索找到对应的产品，点击进入详情
        self.searchgoods_page.input_search_inputbox("YS10")
        self.searchgoods_page.click_search_button()
        self.searchgoods_page.click_search_result_YS10()
        #然后通过点击购物车填充数据
        self.goodsdetail_page.click_putinto_shopping_cart()
        self.goodsdetail_page.click_confirm_button()
        time.sleep(3)
        self.goodsdetail_page.click_back_button()
        #然后点击清除搜索记录
        self.searchgoods_page.click_clear_search_button()

    def test_05_make_AH09_into_shoppingcart(self,login_common_driver):
        #继承2个page
        self.searchgoods_page = SearchGoods(login_common_driver)
        self.goodsdetail_page = GoodsDetail(login_common_driver)
        #先通过搜索找到对应的产品，点击进入详情
        self.searchgoods_page.input_search_inputbox("AH09")
        self.searchgoods_page.click_search_button()
        self.searchgoods_page.click_search_result_AH09()
        #然后通过点击购物车填充数据
        self.goodsdetail_page.click_putinto_shopping_cart()
        self.goodsdetail_page.click_confirm_button()
        time.sleep(3)
        self.goodsdetail_page.click_back_button()
        #然后点击清除搜索记录
        self.searchgoods_page.click_clear_search_button()

    def test_06_make_AH10_into_shoppingcart(self,login_common_driver):
        #继承2个page
        self.searchgoods_page = SearchGoods(login_common_driver)
        self.goodsdetail_page = GoodsDetail(login_common_driver)
        #先通过搜索找到对应的产品，点击进入详情
        self.searchgoods_page.input_search_inputbox("AH10")
        self.searchgoods_page.click_search_button()
        self.searchgoods_page.click_search_result_AH10()
        #然后通过点击购物车填充数据
        self.goodsdetail_page.click_putinto_shopping_cart()
        self.goodsdetail_page.click_confirm_button()
        time.sleep(3)
        self.goodsdetail_page.click_back_button()
        #然后点击清除搜索记录
        self.searchgoods_page.click_clear_search_button()

    def test_07_make_AH11_into_shoppingcart(self,login_common_driver):
        #继承2个page
        self.searchgoods_page = SearchGoods(login_common_driver)
        self.goodsdetail_page = GoodsDetail(login_common_driver)
        #先通过搜索找到对应的产品，点击进入详情
        self.searchgoods_page.input_search_inputbox("AH11")
        self.searchgoods_page.click_search_button()
        self.searchgoods_page.click_search_result_AH11()
        #然后通过点击购物车填充数据
        self.goodsdetail_page.click_putinto_shopping_cart()
        self.goodsdetail_page.click_confirm_button()
        time.sleep(3)
        self.goodsdetail_page.click_back_button()
        #然后点击清除搜索记录
        self.searchgoods_page.click_clear_search_button()

if __name__ == "__main__":
    pytest.main(["-s", "test_6_shoppingcart.py"])