import sys, os
from appium.webdriver.common.touch_action import TouchAction
sys.path.append(os.getcwd())

from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class SearchGoods(BaseAction):
    #被这个resource-id坑惨了，横杠是中间
    search_inputbox_homepage = By.XPATH, "resource-id,com.yidejia.mall:id/et_search"
    search_inputbox = By.XPATH, "resource-id,com.yidejia.mall:id/etSearch"
    search_button = By.XPATH, "resource-id,com.yidejia.mall:id/tvSearch"
    clear_history_button = By.XPATH, "resource-id,com.yidejia.mall:id/ivClearHistory"
    clear_cancel = By.XPATH, "resource-id,com.yidejia.mall:id/tv_cancel"
    clear_confirm = By.XPATH, "resource-id,com.yidejia.mall:id/tv_confirm"
    clear_search_button = By.XPATH, "resource-id,com.yidejia.mall:id/ivClearSearch"
    empty_result = By.XPATH, "resource-id,com.yidejia.mall:id/tv_empty"
    # 如果是数组那么就会进行拼接
    quick_search_YS05 = By.XPATH, ["text,YS05", "resource-id,com.yidejia.mall:id/tv_title"]
    search_result_YS05 = By.XPATH,["text,YS05", "resource-id,com.yidejia.mall:id/tvTitle"]
    back_button = By.XPATH, "resource-id,com.yidejia.mall:id/ivBackNavigationBar"
    #原生也可以支持
    #back_button = By.XPATH, "//*[contains(@resource-id,'com.yidejia.yim.test:id/base_tv_left')]"

    def __init__(self,driver):
        BaseAction.__init__(self,driver)
        #这个下面其实一般会加上其他固定步骤，比如我只要测试message，但是我需要先进入这里A点击B，就可以放这

    def click_search_inputbox_homepage(self):
        self.click(self.search_inputbox_homepage)
    def input_search_inputbox(self,text):
        self.input(self.search_inputbox,text)
    def click_search_button(self):
        self.click(self.search_button)
    def click_clear_history_button(self):
        self.click(self.clear_history_button)
    def click_clear_cancel(self):
        self.click(self.clear_cancel)
    def click_clear_confirm(self):
        self.click(self.clear_confirm)
    def click_clear_search_button(self):
        self.click(self.clear_search_button)
    def click_quick_search_YS05(self):
        self.click(self.quick_search_YS05)
    def click_search_result_YS05(self):
        self.click(self.search_result_YS05)
    def click_back_button(self):
        self.click(self.back_button)

    def find_empty_result(self):
        if self.is_loc_exist(self.empty_result):
            return True
    def find_search_result_ys05(self):
        if self.is_loc_exist(self.search_result_YS05):
            return True
