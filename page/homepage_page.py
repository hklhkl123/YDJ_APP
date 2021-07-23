import sys, os

from appium.webdriver.common.touch_action import TouchAction

sys.path.append(os.getcwd())

from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class HomePage(BaseAction):
    # 后面加1就是精准的，默认不加or加0的是模糊匹配
    icon1_jingzhi = By.XPATH, "text,精致护理,1"
    icon2_yingyang = By.XPATH, "text,营养健康,1"
    icon3_caizhuang = By.XPATH, "text,魅力彩妆,1"
    icon4_fuzhuang = By.XPATH, "text,时尚服装,1"
    icon5_muying = By.XPATH, "text,母婴宝贝,1"
    goods_BC07 = By.XPATH, "text,BC07,0"
    class_button = By.XPATH, ["text,分类,1","resource-id,com.yidejia.mall:id/tv_classify1,1"]
    back_top = By.XPATH, "resource-id,com.yidejia.mall:id/tv_back_top,1"
    nomore_button = By.XPATH, "text,没有更多了,0"
    search_button_homepage = By.XPATH, "resource-id,com.yidejia.mall:id/et_search"
    search_button = By.XPATH, "resource-id,com.yidejia.mall:id/etSearch"




    def __init__(self,driver):
        BaseAction.__init__(self,driver)
        #这个下面其实一般会加上其他固定步骤，比如我只要测试message，但是我需要先进入这里A点击B，就可以放这

    def click_icon1_jingzhi(self):
        self.click(self.icon1_jingzhi)
    def click_goods(self,name):
        self.click(self.("goods_"+name))
    def click_back_top(self):
        self.click(self.back_top)

    #滚动找元素，找到了就返回TRUE
    def roll_find_goods(self,name):
        while not self.is_loc_exist(self.("goods_"+name)):
            self.scroll_page_one_time()
        return True
    def roll_find_nomore_button(self):
        while not self.is_loc_exist(self.nomore_button):
            self.scroll_page_one_time()
        return True


