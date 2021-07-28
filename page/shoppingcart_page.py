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
    reduce_num = By.XPATH, "resource-id,com.com.yidejia.mall:id/ll_sub"
    add_num = By.XPATH, "resource-id,com.yidejia.mall:id/ll_add"
    click_num = By.XPATH, "resource-id,com.yidejia.mall:id/et_num"
    input_num = By.XPATH, "resource-id,com.yidejia.mall:id/et_input"
    cancel_button = By.XPATH, ["text,取消","resource-id,com.yidejia.mall:id/tv_cancel"]
    confirm_button = By.XPATH, ["text,确认","esource-id,com.yidejia.mall:id/tv_confirm"]
    select_button = By.XPATH, "resource-id,com.yidejia.mall:id/iv_select"
    all_select_button = By.XPATH, "resource-id,com.yidejia.mall:id/iv_allSelect"
    settlement_button = By.XPATH, ["text,结算", "resource-id,com.yidejia.mall:id/tv_settlement,1"]
    del_button = By.XPATH, "resource-id,com.yidejia.mall:id/tv_del"
    removeInvalid_button = By.XPATH, ["text,移除失效","resource-id,com.yidejia.mall:id/tv_removeInvalid"]

    def click_home_shopping(self):
        self.click(self.home_shopping)
    def click_shopping_wander_button(self):
        self.click(self.shopping_wander_button)