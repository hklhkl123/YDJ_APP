import sys, os

from appium.webdriver.common.touch_action import TouchAction

sys.path.append(os.getcwd())

from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class HomePage(BaseAction):
    # 后面加1就是精准的，默认不加or加0的是模糊匹配
    icon0_jingxuan = By.XPATH, "text,精选,1"
    icon1_jingzhihuli = By.XPATH, "text,精致护理,1"
    icon2_yingyang = By.XPATH, "text,营养健康,1"
    icon3_caizhuang = By.XPATH, "text,魅力彩妆,1"
    icon4_fuzhuang = By.XPATH, "text,时尚服装,1"
    icon5_muying = By.XPATH, "text,母婴宝贝,1"
    goods_BC07 = By.XPATH, "text,BC07,0"
    class_button_1 = By.XPATH, ["text,分类,1","resource-id,com.yidejia.mall:id/tv_classify1,1"]
    class_button_2 = By.XPATH, "resource-id,com.yidejia.mall:id/tv_classify2,1"
    back_top = By.XPATH, "resource-id,com.yidejia.mall:id/tv_back_top,1"
    nomore_button = By.XPATH, "text,没有更多了,0"
    search_button_homepage = By.XPATH, "resource-id,com.yidejia.mall:id/et_search"
    search_button = By.XPATH, "resource-id,com.yidejia.mall:id/etSearch"
    class_back_button = By.XPATH, "resource-id,com.yidejia.mall:id/ivBackNavigationBar"
    goods_back_button = By.XPATH, "resource-id,com.yidejia.mall:id/ivBackNavigationBar"





    def __init__(self,driver):
        BaseAction.__init__(self,driver)
        #这个下面其实一般会加上其他固定步骤，比如我只要测试message，但是我需要先进入这里A点击B，就可以放这

    #所有tab的类型点击
    def click_icon0_jingxuan(self):
        self.click(self.icon0_jingxuan)
    def click_icon1_jingzhihuli(self):
        self.click(self.icon1_jingzhihuli)
    def click_icon2_yingyang(self):
        self.click(self.icon2_yingyang)
    def click_icon3_caizhuang(self):
        self.click(self.icon3_caizhuang)
    def click_icon4_fuzhuang(self):
        self.click(self.icon4_fuzhuang)
    def click_icon5_muying(self):
        self.click(self.icon5_muying)
    #2个分类按键的不同入口
    def click_class_button_1(self):
        self.click(self.class_button_1)
    def click_class_button_2(self):
        self.click(self.class_button_2)

    def click_goods(self,name="BC07"):
        #这种是错误的，不能用
        # self.click(self.("goods_%s"%(name)))
        self.click(self.goods_BC07)
    def click_back_top(self):
        self.click(self.back_top)
    def click_class_back_button(self):
        self.click(self.class_back_button)
    def click_goods_back_button(self):
        self.click(self.goods_back_button)

    #滚动找元素，找到了就返回TRUE
    def roll_find_goods(self,name="BC07"):
        while not self.is_loc_exist(self.goods_BC07):
            self.scroll_page_one_time()
        return True
    def roll_find_nomore_button(self):
        while not self.is_loc_exist(self.nomore_button):
            self.scroll_page_one_time()
        return True
    #通过一个元素的x或y中心位置，来选中移动【上下左右】
    def roll_tab_icon5_muying(self,direction):
        self.scroll_page_one_time_by_mid(self.icon5_muying,direction)
    def roll_tab_icon1_jingzhihuli(self,direction):
        self.scroll_page_one_time_by_mid(self.icon1_jingzhihuli,direction)




