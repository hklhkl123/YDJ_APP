import sys, os

from appium.webdriver.common.touch_action import TouchAction

sys.path.append(os.getcwd())

from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class FirstPage(BaseAction):
    icon1 = By.XPATH, "text,精致护理,1"
    goods1 = By.XPATH, "text,BC31,0"


    def __init__(self,driver):
        BaseAction.__init__(self,driver)
        #这个下面其实一般会加上其他固定步骤，比如我只要测试message，但是我需要先进入这里A点击B，就可以放这

    def click_icon1(self):
        self.click(self.icon1)

    def click_goods1(self):
        self.click(self.goods1)

    #滚动找元素，找到了就返回TRUE
    def roll_find_element(self):
        while not self.is_loc_exist(self.goods1):
            self.scroll_page_one_time()
        return True


