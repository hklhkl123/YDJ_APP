import sys, os

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.touch_action import TouchAction

sys.path.append(os.getcwd())

from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class ClassPage(BaseAction):
    # 后面加1就是精准的，默认不加or加0的是模糊匹配
    class_button_1 = By.XPATH, ["text,分类,1","resource-id,com.yidejia.mall:id/tv_classify1,1"]
    class_button_2 = By.XPATH, "resource-id,com.yidejia.mall:id/tv_classify2,1"
    goods_back_button = By.XPATH, "resource-id,com.yidejia.mall:id/ivBackNavigationBar"
    search_button = By.XPATH, "resource-id,com.yidejia.mall:id/ivRightNavigationBarSearch"
    search_button_back = By.XPATH, "resource-id,com.yidejia.mall:id/ivBack"
    big_class_1 = By.XPATH, "text,营养健康"
    big_class_2 = By.XPATH, "text,精致护理"
    big_class_3 = By.XPATH, "text,魅力彩妆"
    big_class_4 = By.XPATH, "text,时尚服装"
    big_class_5 = By.XPATH, "text,母婴宝贝"
    big_class_6 = By.XPATH, "text,品牌入驻"

    class_1 = By.XPATH, "text,健康需求"
    class_2 = By.XPATH, "text,品牌系列"
    class_3 = By.XPATH, "text,组合系列"
    class_4 = By.XPATH, "text,护肤分类"
    class_5 = By.XPATH, "text,肌肤需求"
    class_6 = By.XPATH, "text,产品系列"
    class_7 = By.XPATH, "text,内调食品"
    class_10 = By.XPATH, "text,其他"

    goods_AK11 = By.XPATH, "text,AK11"
    goods_D200518 = By.XPATH, "text,D200518"



    def __init__(self,driver):
        BaseAction.__init__(self,driver)
        #这个下面其实一般会加上其他固定步骤，比如我只要测试message，但是我需要先进入这里A点击B，就可以放这

    #所有tab的类型点击
    def click_class_button_1(self):
        self.click(self.class_button_1)

    def click_class_2(self):
        #这里返回的是一个数组
        a = self.find_elements(self.class_2)
        #先判断长度，如果1个就直接点了，2个就找x坐标是0的点
        if len(a) == 1:
            a[0].click()
        else:
            #取出元素的坐标，变成一个list，如果list[0]==0，那么就点击这个
            if eval(a[0].get_attribute("bounds").replace("][", ","))[0] == 0:
                a[0].click()
            else:
                a[1].click()

    def click_class_10(self):
        #这里返回的是一个数组
        a = self.find_elements(self.class_10)
        #先判断长度，如果1个就直接点了，2个就找x坐标是0的点
        if len(a) == 1:
            a[0].click()
        else:
            #取出元素的坐标，变成一个list，如果list[0]==0，那么就点击这个
            if eval(a[0].get_attribute("bounds").replace("][", ","))[0] == 0:
                a[0].click()
            else:
                a[1].click()

    def click_goods_D200518(self):
        self.click(self.goods_D200518)

    def click_goods_back_button(self):
        self.click(self.goods_back_button)

    #滚动找元素，找到了就点击
    def roll_find_goods_and_click_goods_D200518(self,direction = "up"):
        while not self.is_loc_exist(self.goods_D200518):
            self.scroll_page_one_time(direction)
        self.click(self.goods_D200518)

    # def roll_find_nomore_button(self):
    #     while not self.is_loc_exist(self.nomore_button):
    #         self.scroll_page_one_time()
    #     return True

    #直接找到元素x坐标
    def find_big_class1_positon_x(self):
        p = self.find_element_position(self.big_class_1)
        x =p[0]
        return x

    #通过一个元素的x或y中心位置，来选中移动【上下左右】
    def roll_bigclass_find_big_class_6(self,x,direction = "down"):
        while not self.is_loc_exist(self.big_class_6):
            self.scroll_page_one_time_constant_x(x,direction)






