import time
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

class BaseAction(object):

    def __init__(self, driver):
        self.driver = driver

    def click(self, loc):
        self.find_element(loc).click()

    def input(self, loc, text):
        self.find_element(loc).send_keys(text)

    def find_element(self, loc, timeout=10.0, poll=0.5):
        by = loc[0]
        value = loc[1]  # "text,0"
        if by == By.XPATH:
            value = self.make_xpath_with_feature(value) # //*
            print(value)
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element(by, value))

    def find_elements(self, loc, timeout=10.0, poll=0.5):
        by = loc[0]
        value = loc[1]
        if by == By.XPATH:
            value = self.make_xpath_with_feature(value) # //*
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_elements(by, value))

    def make_xpath_with_unit_feature(self, loc):
        """
        拼接xpath中间的部分
        :param loc:
        :return:
        """
        key_index = 0
        value_index = 1
        option_index = 2

        args = loc.split(",")
        feature = ""

        if len(args) == 2:
            feature = "contains(@" + args[key_index] + ",'" + args[value_index] + "')" + "and "
        elif len(args) == 3:
            if args[option_index] == "1":
                feature = "@" + args[key_index] + "='" + args[value_index] + "'" + "and "
            elif args[option_index] == "0":
                feature = "contains(@" + args[key_index] + ",'" + args[value_index] + "')" + "and "

        return feature

    def make_xpath_with_feature(self, loc):
        feature_start = "//*["
        feature_end = "]"
        feature = ""

        if isinstance(loc, str):
            # 如果是正常的xpath
            if loc.startswith("//"):
                return loc

            # loc str
            feature = self.make_xpath_with_unit_feature(loc)
        else:
            # loc 列表
            for i in loc:
                feature += self.make_xpath_with_unit_feature(i)

        feature = feature.rstrip("and ")

        loc = feature_start + feature + feature_end

        return loc

    def find_toast(self, message, timeout=3, poll=0.1):
        """
        # message: 预期要获取的toast的部分消息
        """
        message = "//*[contains(@text,'" + message + "')]"  # 使用包含的方式定位
        element = self.find_element((By.XPATH, message), timeout, poll)
        return element.text

    def is_toast_exist(self, message, timeout=3, poll=0.1):
        try:
            self.find_toast(message, timeout, poll)
            return True
        except Exception:
            return False

    def screenshot_and_attach(self, def_name,despription_content='默认图片名'):
        #使用原方法名+时间戳拼起来给图片命名
        current_time = time.strftime("%Y%m%d_%H%M%S",time.localtime())
        filename = def_name+"_"+current_time

        #截图并且保存
        self.driver.get_screenshot_as_file("../screen/" + filename + ".png")

        #上传图片到allure报告
        file_name = '../screen/' + filename + '.png'
        with open(file_name, mode='rb') as f:
            file = f.read()
        allure.attach(file, despription_content, allure.attachment_type.PNG)


    def scroll_page_one_time(self, direction="down"):
        window_size = self.driver.get_window_size()
        window_height = window_size["height"]
        window_width = window_size["width"]
        up_y = window_height * 0.25
        down_y = up_y * 3
        left_x = window_width * 0.25
        right_x = left_x * 3
        center_x = window_width * 0.5
        center_y = window_height * 0.5
        #有些轮播图在顶部，不是在中间，需要特殊处理，在0.25y滚动一下
        center_y_025 = window_height * 0.25

        #前面的点移动到后面的点位
        if direction == "down":
            self.driver.swipe(center_x, down_y, center_x, up_y)
        elif direction == "up":
            self.driver.swipe(center_x, up_y, center_x, down_y)
        elif direction == "left":
            self.driver.swipe(left_x, center_y, right_x, center_y)
        elif direction == "right":
            self.driver.swipe(right_x, center_y, left_x, center_y)
        #这下面的就是0.25y的左右滑动
        elif direction == "left_025":
            self.driver.swipe(left_x, center_y_025, right_x, center_y_025)
        elif direction == "right_025":
            self.driver.swipe(right_x, center_y_025, left_x, center_y_025)
        else:
            raise Exception("请输入正确的direction参数 down、up、left、right")

    #home键
    def press_keycode_home(self):
        self.press_keycode(3)
    #返回键
    def press_keycode_back(self):
        self.press_keycode(4)

    def press_keycode(self, keycode):
        if "automationName" not in self.driver.capabilities.keys():
            self.driver.keyevent(keycode)
        elif self.driver.capabilities["automationName"] == "Uiautomator2":
            self.driver.press_keycode(keycode)

    #检查桌面是否有app
    def is_desktop_has_app(self, app_name, times):
        self.press_keycode_home()
        self.press_keycode_home()

        for i in range(times):
            if self.is_loc_exist((By.XPATH, "text," + app_name)):
                return True
            else:
                self.scroll_page_one_time("right")
        return False

    #检查元素是否存在
    def is_loc_exist(self, loc):
        try:
            self.find_element(loc)
            return True
        except Exception:
            return False

    #找到元素位置，输出一个list[x1,y1,x2,y2]
    def find_element_position(self,loc):
        p = self.find_element(loc).get_attribute("bounds")
        #返回的值是一个str,"[242,338][522,507]",需要下面这种处理一下
        plist = eval(p.replace("][",","))
        return plist
    #返回元素中心坐标
    def find_element_position_mid(self,loc):
        plist = self.find_element_position(loc)
        mid_x = (plist[0]+plist[2])/2
        mid_y = (plist[1]+plist[3])/2
        mid = [mid_x,mid_y]
        return mid

    #面对一个tab样式or轮播图的元素，找到中间坐标，可以进行上下左右滑动
    def scroll_page_one_time_by_mid(self,loc,direction="left"):
        mid_x = self.find_element_position_mid(loc)[0]
        mid_y = self.find_element_position_mid(loc)[1]
        window_size = self.driver.get_window_size()
        window_height = window_size["height"]
        window_width = window_size["width"]
        up_y = window_height * 0.25
        down_y = up_y * 3
        left_x = window_width * 0.25
        right_x = left_x * 3
        # 前面的点移动到后面的点位
        if direction == "down":
            self.driver.swipe(mid_x, down_y, mid_x, up_y)
        elif direction == "up":
            self.driver.swipe(mid_x, up_y, mid_x, down_y)
        elif direction == "left":
            self.driver.swipe(left_x, mid_y, right_x, mid_y)
        elif direction == "right":
            self.driver.swipe(right_x, mid_y, left_x, mid_y)
        else:
            raise Exception("请输入正确的direction参数 down、up、left、right")

    def scroll_page_one_time_constant_x(self,x,direction="down"):
        window_size = self.driver.get_window_size()
        window_height = window_size["height"]
        up_y = window_height * 0.25
        down_y = up_y * 3
        # 前面的点移动到后面的点位
        if direction == "down":
            self.driver.swipe(x, down_y, x, up_y)
        elif direction == "up":
            self.driver.swipe(x, up_y, x, down_y)
        else:
            raise Exception("请输入正确的direction参数 down、up")

    def scroll_page_one_time_constant_y(self,y,direction="right"):
        window_size = self.driver.get_window_size()
        window_width = window_size["width"]
        left_x = window_width * 0.25
        right_x = left_x * 3
        # 前面的点移动到后面的点位
        if direction == "left":
            self.driver.swipe(left_x, y, right_x, y)
        elif direction == "right":
            self.driver.swipe(right_x, y, left_x, y)
        else:
            raise Exception("请输入正确的direction参数 left、right")
