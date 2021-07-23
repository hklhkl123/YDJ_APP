import time
import os,sys
import pytest
import allure

sys.path.append(os.getcwd())

from base.base_driver import init_driver
from page.searchgoods_page import SearchGoods
from base.base_yaml import yml_data_with_filename_and_key

class TestSearchGoods():

    #先进到搜索界面来
    def test_01_enter_search_interface(self,login_common_driver):
        self.searchgoods_page = SearchGoods(login_common_driver)
        self.searchgoods_page.click_search_inputbox_homepage()

    #默认搜索一下，然后点击X
    def test_02_search_default(self,login_common_driver):
        self.searchgoods_page = SearchGoods(login_common_driver)
        self.searchgoods_page.click_search_button()
        self.searchgoods_page.click_clear_search_button()
    #点击清空历史，先取消再点击，再确定
    def test_03_clear_history(self,login_common_driver):
        self.searchgoods_page = SearchGoods(login_common_driver)
        self.searchgoods_page.click_clear_history_button()
        self.searchgoods_page.click_clear_cancel()
        self.searchgoods_page.click_clear_history_button()
        self.searchgoods_page.click_clear_confirm()
    #搜索不存在的商品，截图然后清掉记录
    def test_04_search_empty_result(self,login_common_driver):
        self.searchgoods_page = SearchGoods(login_common_driver)
        self.searchgoods_page.input_search_inputbox("不存在的商品")
        self.searchgoods_page.click_search_button()
        if self.searchgoods_page.find_empty_result():
            self.searchgoods_page.screenshot_and_attach("test_04_search_empty_result", despription_content='搜索空结果后截图')
        self.searchgoods_page.click_clear_search_button()

    #搜索存在的商品YS05，然后点击进去然后返回，清除掉文本
    def test_05_search_result_ys05(self,login_common_driver):
        self.searchgoods_page = SearchGoods(login_common_driver)
        self.searchgoods_page.input_search_inputbox("YS05")
        self.searchgoods_page.click_search_button()
        if self.searchgoods_page.find_search_result_ys05():
            self.searchgoods_page.screenshot_and_attach("test_05_search_result_ys05", despription_content='搜索YS05结果后截图')
        self.searchgoods_page.click_search_result_YS05()
        time.sleep(2)
        self.searchgoods_page.click_back_button()
        self.searchgoods_page.click_clear_search_button()

    #通过历史搜索点击进行搜索,点击进去再回来
    def test_05_quick_search_YS05(self,login_common_driver):
        self.searchgoods_page = SearchGoods(login_common_driver)
        self.searchgoods_page.click_quick_search_YS05()
        self.searchgoods_page.click_search_result_YS05()
        self.searchgoods_page.click_back_button()
        self.searchgoods_page.click_clear_search_button()

    def test_close_app(self,login_common_driver):
        login_common_driver.close_app()







if __name__ == "__main__":
    pytest.main(["-s", "test_3_searchgoods.py"])