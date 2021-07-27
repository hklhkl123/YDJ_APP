import sys, os

from appium.webdriver.common.touch_action import TouchAction

sys.path.append(os.getcwd())

from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class ConfirmPage(BaseAction):
    # 后面加1就是精准的，默认不加or加0的是模糊匹配
    #这是搜索需要的，产品结果
    search_inputbox_homepage = By.XPATH, "resource-id,com.yidejia.mall:id/et_search"
    search_inputbox = By.XPATH, "resource-id,com.yidejia.mall:id/etSearch"
    search_button = By.XPATH, "resource-id,com.yidejia.mall:id/tvSearch"
    search_result_YS05 = By.XPATH, ["text,YS05", "resource-id,com.yidejia.mall:id/tvTitle"]
    #这个是立即购买和确定
    buy_now = By.XPATH, "resource-id,com.yidejia.mall:id/tv_buy,1"
    confirm_button_1 = By.XPATH, ["text,确定","resource-id,com.yidejia.mall:id/tv_confirm,1"]

    address = By.XPATH, "resource-id,com.yidejia.mall:id/cl_address,1"
    #运费
    freight = By.XPATH, "resource-id,com.yidejia.mall:id/tv_freight,1"
    back_button = By.XPATH, "resource-id,com.yidejia.mall:id/ivBackNavigationBar,1"
    iknow_button = By.XPATH, "resource-id,com.yidejia.mall:id/tv_know,1"
    close_button = By.XPATH, "resource-id,com.yidejia.mall:id/iv_close,1"
    #金币兑换
    exchange_pay_button = By.XPATH, "resource-id,com.yidejia.mall:id/ll_exchange_pay,1"
    #多优惠券使用
    ll_coupons_button = By.XPATH, "resource-id,com.yidejia.mall:id/ll_coupons,1"
    #结算
    settlement_button = By.XPATH, ["text,结算","resource-id,com.yidejia.mall:id/tv_settlement,1"]
    confirm_button = By.XPATH, ["text,立即付款","resource-id,com.yidejia.mall:id/tv_confirm,1"]
    pay_wx = By.XPATH, ["text,微信支付","resource-id,com.yidejia.mall:id/tv_pay_wx,1"]
    pay_ali = By.XPATH, ["text,支付宝支付","resource-id,com.yidejia.mall:id/tv_pay_ali,1"]
    pay_cancel = By.XPATH, ["text,暂时放弃", "resource-id,com.yidejia.mall:id/tv_cancel,1"]
    pay_continue = By.XPATH, ["text,继续支付", "resource-id,com.yidejia.mall:id/tv_confirm,1"]


    #这是搜索数据
    def click_search_inputbox_homepage(self):
        self.click(self.search_inputbox_homepage)
    def input_search_inputbox(self,text):
        self.input(self.search_inputbox,text)
    def click_search_button(self):
        self.click(self.search_button)
    def click_search_result_YS05(self):
        self.click(self.search_result_YS05)
    #这是立即购买和确定
    def click_buy_now(self):
        self.click(self.buy_now)
    def click_confirm_button_1(self):
        self.click(self.confirm_button_1)

    #这是确定订单需要的按键
    def click_address(self):
        self.click(self.address)
    def click_back_button(self):
        self.click(self.back_button)
    def click_iknow_button(self):
        self.click(self.iknow_button)
    def click_close_button(self):
        self.click(self.close_button)
    #下面的都是支付相关
    def click_settlement_button(self):
        self.click(self.settlement_button)
    def click_confirm_button(self):
        self.click(self.confirm_button)
    def click_pay_wx(self):
        self.click(self.pay_wx)
    def click_pay_ali(self):
        self.click(self.pay_ali)
    def click_pay_cancel(self):
        self.click(self.pay_cancel)
    def click_pay_continue(self):
        self.click(self.pay_continue)

    #滚动找元素"运费"，找到了就点击
    def roll_find_and_click_freight(self,direction = "down"):
        while not self.is_loc_exist(self.freight):
            self.scroll_page_one_time(direction)
        self.click(self.freight)

    #滚动找元素"常规金币兑换"，找到了就点击
    def roll_find_and_exchange_pay_button(self,direction = "down"):
        while not self.is_loc_exist(self.exchange_pay_button):
            self.scroll_page_one_time(direction)
        self.click(self.exchange_pay_button)
