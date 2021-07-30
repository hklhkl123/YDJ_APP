import sys, os

from appium.webdriver.common.touch_action import TouchAction

sys.path.append(os.getcwd())

from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class ShoppingCartPage(BaseAction):
    # 后面加1就是精准的，默认不加or加0的是模糊匹配

    home_shopping = By.XPATH, "resource-id,com.yidejia.mall:id/home_shopping"
    shopping_wander_button = By.XPATH, ["text,去逛逛吧","resource-id,com.yidejia.mall:id/tv_wander"]
    operate_button = By.XPATH, ["text,管理","resource-id,com.yidejia.mall:id/tv_operate"]
    finish_button = By.XPATH, ["text,完成", "resource-id,com.yidejia.mall:id/tv_operate"]
    reduce_num = By.XPATH, "resource-id,com.yidejia.mall:id/ll_sub"
    add_num = By.XPATH, "resource-id,com.yidejia.mall:id/ll_add"
    click_num = By.XPATH, "resource-id,com.yidejia.mall:id/et_num"
    input_num = By.XPATH, "resource-id,com.yidejia.mall:id/et_input"
    cancel_button = By.XPATH, ["text,取消","resource-id,com.yidejia.mall:id/tv_cancel"]
    confirm_button = By.XPATH, ["text,确认","resource-id,com.yidejia.mall:id/tv_confirm"]
    single_select_button = By.XPATH, "resource-id,com.yidejia.mall:id/iv_select"
    all_select_button = By.XPATH, "resource-id,com.yidejia.mall:id/iv_allSelect"
    settlement_button = By.XPATH, ["text,结算", "resource-id,com.yidejia.mall:id/tv_settlement,1"]
    del_button = By.XPATH, "resource-id,com.yidejia.mall:id/tv_del"
    removeInvalid_button = By.XPATH, ["text,移除失效","resource-id,com.yidejia.mall:id/tv_removeInvalid"]

    def click_home_shopping(self):
        self.click(self.home_shopping)
    def click_shopping_wander_button(self):
        self.click(self.shopping_wander_button)
    def click_operate_button(self):
        self.click(self.operate_button)
    def click_finish_button(self):
        self.click(self.finish_button)

    #改造一下,点击第n个元素
    def click_add_num_n(self,n=1):
        ele = self.find_add_num_n(n)
        #元素后直接点击
        ele.click()
    def click_reduce_num_n(self,n=1):
        ele = self.find_reduce_num_n(n)
        ele.click()
    def click_single_select_button_n(self,n=1):
        ele = self.find_single_select_button_n(n)
        ele.click()
    def click_click_num_n(self,n=1):
        ele = self.find_click_num_n(n)
        ele.click()
    #第x个元素连续点n次+,n次-
    def click_add_num_xele_ntimes(self,n,times=3):
        for i in range(times):
            self.click_add_num_n(n)
    def click_reduce_num_xele_ntimes(self,n,times=3):
        for i in range(times):
            self.click_reduce_num_n(n)
    #用findelements加角标来显示,找到第n个+元素
    def find_add_num_n(self,num):
        x = self.find_elements(self.add_num)
        x_num_ele = x[int(num)-1]
        return x_num_ele
    def find_reduce_num_n(self,num):
        x = self.find_elements(self.reduce_num)
        x_num_ele = x[int(num)-1]
        return x_num_ele
    def find_single_select_button_n(self,num):
        x = self.find_elements(self.single_select_button)
        x_num = x[int(num)-1]
        return x_num
    def find_click_num_n(self,num):
        x = self.find_elements(self.click_num)
        x_num = x[int(num)-1]
        return x_num

    #点击输入框后，可以直接输入数字
    def clear_input_num(self):
        self.clear_input(self.input_num)
    def input_goods_num(self,num):
        self.input(self.input_num,num)
    def click_cancel_button(self):
        self.click(self.cancel_button)
    def click_confirm_button(self):
        self.click(self.confirm_button)
    #点击管理后可以出现的按键
    def click_all_select_button(self):
        self.click(self.all_select_button)
    def click_settlement_button(self):
        self.click(self.settlement_button)
    def click_del_button(self):
        self.click(self.del_button)
    def click_removeInvalid_button(self):
        self.click(self.removeInvalid_button)