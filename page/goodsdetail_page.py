import sys, os
from appium.webdriver.common.touch_action import TouchAction
sys.path.append(os.getcwd())

from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class GoodsDetail(BaseAction):
    #被这个resource-id坑惨了，横杠是中间
    price = By.XPATH, "resource-id,com.yidejia.mall:id/tv_price,1"
    salenum = By.XPATH, "resource-id,com.yidejia.mall:id/tv_sale,1"
    goodsname = By.XPATH, "resource-id,com.yidejia.mall:id/tv_name,1"
    recommandreason = By.XPATH, "resource-id,com.yidejia.mall:id/tv_state,1"
    address = By.XPATH, "resource-id,com.yidejia.mall:id/tv_address,1"
    answer = By.XPATH, "text,客服,1"
    shopping_cart = By.XPATH, "text,购物车,1"
    shopping_cart_num = By.XPATH, "resource-id,com.yidejia.mall:id/tv_point,1"
    favorites = By.XPATH, "text,收藏,1"
    add_goods_button = By.XPATH, "resource-id,com.yidejia.mall:id/tv_add,1"
    add_goods_num = By.XPATH, "resource-id,com.yidejia.mall:id/iv_add,1"
    reduce_goods_num = By.XPATH, "resource-id,com.yidejia.mall:id/iv_cut_down,1"
    buy_now = By.XPATH, "resource-id,com.yidejia.mall:id/tv_buy,1"
    confirm_button = By.XPATH, "resource-id,com.yidejia.mall:id/tv_confirm,1"


    def __init__(self,driver):
        BaseAction.__init__(self,driver)
        #这个下面其实一般会加上其他固定步骤，比如我只要测试message，但是我需要先进入这里A点击B，就可以放这

    def print_info(self):
        print('价格是：' + str(self.find_element(self.price).text))
        print('销量是：'+str(self.find_element(self.salenum).text))
        print('商品名称是：'+str(self.find_element(self.goodsname).text))
        print('商品描述是：'+str(self.find_element(self.recommandreason).text))

    def print_shopping_cart_num(self):
        print('购物车数量是：'+str(self.find_element(self.shopping_cart_num).text))

    def click_address(self):
        self.click(self.address)
    def click_answer(self):
        self.click(self.answer)
    def click_shopping_cart(self):
        self.click(self.shopping_cart)
    def click_favorites(self):
        self.click(self.favorites)
    def click_add_goods_button(self):
        self.click(self.add_goods_button)
    def click_buy_now(self):
        self.click(self.buy_now)
    def click_confirm_button(self):
        self.click(self.confirm_button)
    def click_add_goods_num(self):
        self.click(self.add_goods_num)
    def click_reduce_goods_num(self):
        self.click(self.reduce_goods_num)


    def left_roll_3_times(self):
        for i in range(3):
            self.scroll_page_one_time('left_025')
    def right_roll_3_times(self):
        for i in range(3):
            self.scroll_page_one_time('right_025')



    #滚动找元素，找到了就返回TRUE
    def roll_find_element(self):
        while not self.is_loc_exist(self.address):
            self.scroll_page_one_time()
        return True


