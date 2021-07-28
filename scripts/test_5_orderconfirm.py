import time
import os,sys
import pytest
import allure

sys.path.append(os.getcwd())

from base.base_driver import init_driver
from page.orderconfirm_page import ConfirmPage
from page.searchgoods_page import SearchGoods
from page.goodsdetail_page import GoodsDetail
from base.base_yaml import yml_data_with_filename_and_key

class TestOrderConfirm(object):
    # @pytest.mark.skipif(True, reason="已经玩过了")
    @allure.step(title="搜索YS05产品，点击到产品界面")
    def test_01_enter_orderconfirm(self,login_common_driver):
        self.searchgoods_page = SearchGoods(login_common_driver)
        self.searchgoods_page.click_search_inputbox_homepage()
        self.searchgoods_page.input_search_inputbox("YS05")
        self.searchgoods_page.click_search_button()
        self.searchgoods_page.click_search_result_YS05()

    @allure.step(title="进入界面后，点击立即付款进入到确认订单界面")
    def test_02_buy_now(self, login_common_driver):
        self.goodsdetail_page = GoodsDetail(login_common_driver)
        self.goodsdetail_page.click_buy_now()
        #点击确定按键
        self.goodsdetail_page.click_confirm_button()
        time.sleep(1)

    @allure.step(title="点击一下地址返回")
    def test_03_check_address(self,login_common_driver):
        self.orderconfirm_page = ConfirmPage(login_common_driver)
        self.orderconfirm_page.click_address()
        time.sleep(3)
        self.orderconfirm_page.click_back_button()
        # self.orderconfirm_page.press_keycode_back()

    @allure.step(title="点击2次运费，一次点击我知道了，一次点击x关闭")
    def test_04_check_freight(self,login_common_driver):
        self.orderconfirm_page = ConfirmPage(login_common_driver)
        #这里用到滚动找到点击，避免购买数量过长导致没找到
        #这是打开后点击“我知道了”
        self.orderconfirm_page.roll_find_and_click_freight()
        self.orderconfirm_page.click_iknow_button()
        #这是打开后点击关
        self.orderconfirm_page.roll_find_and_click_freight()
        self.orderconfirm_page.click_close_button()

    @allure.step(title="点击常规换购，然后点击返回")
    def test_05_check_exchange_pay_button(self,login_common_driver):
        self.orderconfirm_page = ConfirmPage(login_common_driver)
        self.orderconfirm_page.roll_find_and_exchange_pay_button()
        time.sleep(3)
        self.orderconfirm_page.click_back_button()

    @allure.step(title="验证结算按键")
    def test_06_check_settlement(self,login_common_driver):
        self.orderconfirm_page = ConfirmPage(login_common_driver)
        self.orderconfirm_page.click_settlement_button()
        #先点击阿里，再点击微信支付
        self.orderconfirm_page.click_pay_ali()
        self.orderconfirm_page.click_pay_wx()
        #点击X,弹出点击立即支付
        self.orderconfirm_page.click_close_button()
        self.orderconfirm_page.click_pay_continue()
        # 再次点击X,弹出点击暂时放弃
        self.orderconfirm_page.click_close_button()
        self.orderconfirm_page.click_pay_cancel()

if __name__ == "__main__":
    pytest.main(["-s", "test_5_orderconfirm.py"])


