# -*- coding:utf-8 -*-
'''
Created on 2018年3月1日

@author:
'''
import time, os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
# from selenium.common import NoSuchElementException
from selenium.webdriver.common import keys
from selenium.webdriver.common.action_chains import ActionChains
from comnon import com_module
from comnon import time_module as tm


'''
http://npm.taobao.org/mirrors/chromedriver/
'''


class WebClient():
    __driver = None

    def __init__(self, url):
        self.url = url
        self.time_out = 10
        '''如果是windows系统，使用chrome最大化；如果是其他系统，则全屏'''
        if com_module.is_windows():
            abspath = os.path.abspath(r"C:\Users\wafer\AppData\Local\Google\Chrome\Application\chromedriver.exe")
            self.__driver = webdriver.Chrome(abspath)
            self.__driver.maximize_window()
        else:
            # executable_path = os.path.abspath(r"chromedriver")

            options = Options()
            # options.add_argument("start-fullscreen")
            options.add_argument('lang=zh_CN.UTF-8')
            # self.__driver = webdriver.Chrome(executable_path, chrome_options=options)
            self.__driver = webdriver.Chrome('/usr/local/chromedriver', chrome_options=options)

    '''启动chrome浏览器'''

    def run_chrome(self):

        self.__driver.get(self.url)

    '''启动浏览器，模拟访问手机网页'''

    def run_chrome_iphone(self):
        mobileEmulation = {'deviceName': 'iPhone 6'}  # 模拟iphone X
        #         mobileEmulation = {'deviceName' : 'Galaxy S5'} #模拟Galaxy S5
        if com_module.is_windows():
            executable_path = os.path.abspath(r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
            options = webdriver.ChromeOptions()
            options.add_experimental_option('mobileEmulation', mobileEmulation)  # 在浏览器网页中模拟访问手机网页
            self.__driver = webdriver.Chrome(executable_path, chrome_options=options)
            self.__driver.maximize_window()
        else:
            executable_path = os.path.abspath('/Users/liujun/Downloads/chromedriver')
            options = Options()
            options.add_argument('lang=zh_CN.UTF-8')
            options.add_experimental_option('mobileEmulation', mobileEmulation)
            self.__driver = webdriver.Chrome(executable_path, chrome_options=options)
        self.__driver.get(self.url)


    '''启动浏览器，模拟访问ipad网页'''

    def run_chrome_ipad(self):
        WIDTH = 1024
        HEIGHT = 768
        mobileEmulation = {
            'deviceMetrics': {'width': WIDTH, 'height': HEIGHT}
        }  # 模拟ipad横屏
        #         mobileEmulation = {'deviceName': 'iPad'} # 模拟ipad
        #         mobileEmulation = {'deviceName' : 'iPad Pro'} #模拟ipad Pro
        if com_module.is_windows():
            abspath = os.path.abspath(r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
            options = webdriver.ChromeOptions()
            options.add_experimental_option('mobileEmulation', mobileEmulation)  # 在浏览器网页中模拟访问手机网页
            self.__driver = webdriver.Chrome(abspath, chrome_options=options)
            self.__driver.maximize_window()
        else:
            chrome_options = Options()
            chrome_options.add_experimental_option('mobileEmulation', mobileEmulation)
            chrome_options.add_argument("start-fullscreen")
            self.__driver = webdriver.Chrome(chrome_options=chrome_options)
        self.__driver.get(self.url)


    '''退出浏览器'''

    def exit_all_browser(self):
        if self.__driver:
            self.__driver.quit()

    '''清除缓存'''

    def clear_all_cookies(self):
        if self.__driver:
            self.__driver.delete_all_cookies()

    '''获取当前浏览页句柄'''

    def get_current_page_handle(self):
        current_page_handle = self.__driver.current_window_handle
        return current_page_handle

    '''获取打开的所有浏览页的句柄'''

    def get_all_pages_handle(self):
        all_pages_handle = self.__driver.window_handles
        return all_pages_handle

    '''
       切换浏览页tab
       0--切换
       1--不切换
    '''

    def switch_page_handle(self, current_page_handle, all_pages_handle, flage=1):
        for handle in all_pages_handle:
            if 1 == flage:
                if handle == current_page_handle:
                    self.__driver.switch_to_window(handle)
            if 0 == flage:
                if handle != current_page_handle:
                    self.__driver.switch_to_window(handle)

    '''ִ执行js脚本'''

    def execute_js(self, js):
        self.__driver.execute_script(js)

    '''获取单个元素'''

    def get_element(self, element_selector, find_by=By.CSS_SELECTOR):
        return self.__driver.find_element(find_by, element_selector)

    '''获取一组元素'''

    def get_elements(self, element_selector, find_by=By.CSS_SELECTOR):
        return self.__driver.find_elements(find_by, element_selector)

    '''获取元素属性值ֵ'''

    def get_element_attribute_value(self, element_selector, attr_name, find_by=By.CSS_SELECTOR):
        attribute_value = self.get_element(element_selector, find_by).get_attribute(attr_name)
        return attribute_value

    '''获取文本内容'''

    def get_element_text(self, element_selector, find_by=By.CSS_SELECTOR):
        return self.get_element(element_selector, find_by).text

    '''获取一组中某个元素的文本内容'''

    def get_elements_text(self, element_selector, number, find_by=By.CSS_SELECTOR):
        l = self.get_elements(element_selector, find_by)
        return l[number].text

    '''获取一组中某个元素的属性值'''

    def get_elements_attribute_value(self, element_selector, attr_name, number, find_by=By.CSS_SELECTOR):
        l = self.get_elements(element_selector, find_by)
        return l[number].get_attribute(attr_name)

    '''
    选择元素，按住不放，然后移动到固定坐标位置，最后松开鼠标，完成拖拽
    xOffset 为负数，表示横坐标向左移动，yOffset 为负数表示纵坐标向上移动
    '''

    def drag_and_drop_by_offset(self, element_selector, xOffset, yOffset, find_by=By.CSS_SELECTOR):
        dragElement = self.get_element(element_selector, find_by)
        Action = ActionChains(self.__driver)
        Action.drag_and_drop_by_offset(dragElement, xOffset, yOffset).perform()
        self.sleep_one_sec()

    '''将浏览器滚动条滚动到目标元素'''

    def scroll_into_view(self, element_selector, find_by=By.CSS_SELECTOR):
        target = self.get_element(element_selector, find_by)
        time.sleep(5)
        self.__driver.execute_script("arguments[0].scrollIntoView();", target)

    '''将浏览器滚动条滚动到最底部'''

    def scroll_to_bottom(self):
        js = 'window.scrollTo(0, document.body.scrollHeight)'
        self.__driver.execute_script(js)

    '''将浏览器滚动条滚动到最顶部'''

    def scroll_to_top(self):
        js = 'document.body.scrollTop=0;'
        self.__driver.execute_script(js)

    '''按百分比滚动滚动条'''

    def scroll_into_persent(self, percent):
        self.__driver.execute_script("window.scrollTo(0,document.body.scrollHeight*" + percent + ");")

    '''等待一秒钟'''



    '''强制等待'''

    def sleep(self, seconds):
        time.sleep(seconds)

    '''隐式等待'''

    def implicitly_wait(self, timeout):
        self.__driver.implicitly_wait(timeout)

    '''显性等待，等待控件加载完成'''

    def wait_until_elem(self, element_selector, find_by=By.CSS_SELECTOR):
        try:
            WebDriverWait(self.__driver, 10).until(
                EC.presence_of_element_located((find_by, element_selector)))
        except :
            raise Exception("\nElementLoadingError:can't find element!")

    '''点击元素'''

    def click_element(self, element_selector, find_by=By.CSS_SELECTOR):
        self.wait_until_elem(element_selector, find_by)
        elem = self.get_element(element_selector, find_by)
        try:
            elem.click()
        except:
            print('-----------元素点击异常，等待10秒再次点击----------%s' % elem)
            time.sleep(self.time_out)
            elem.click()




    '''向控件中输入值'''

    def sendkeys_to_element(self, element_selector, msg, find_by=By.CSS_SELECTOR):
        self.wait_until_elem(element_selector, find_by)
        self.get_element(element_selector, find_by).send_keys(msg)

    '''清除控件文本内容'''

    def clear_elem_text(self, element_selector, find_by=By.CSS_SELECTOR):
        self.wait_until_elem(element_selector, find_by)
        elem = self.get_element(element_selector, find_by)
        elem.clear()

    '''将控件中的文本内容全选'''

    def check_all_text(self, element_selector, find_by=By.CSS_SELECTOR):
        elem = self.get_element(element_selector, find_by)
        elem.send_keys(keys.CONTROL, 'a')

    '''删除控件中的文本内容'''

    def delete_elem_text(self, element_selector, find_by=By.CSS_SELECTOR):
        elem = self.get_element(element_selector, find_by)
        elem.send_keys(keys.BACK_SPACE)

    '''输入框等，回车键'''

    def enter_key(self, element_selector, find_by=By.CSS_SELECTOR):
        elem = self.get_element(element_selector, find_by)
        elem.send_keys(keys.ENTER)

    '''根据text在由ant组件实现的下拉列表中选择'''



    '''将鼠标移动到元素上'''

    def mouse_move_to_elem(self, element_selector, find_by=By.CSS_SELECTOR):
        self.wait_until_elem(element_selector, find_by)
        to_element = self.get_element(element_selector, find_by)
        ActionChains(self.__driver).move_to_element(to_element).perform()

    '''鼠标单击'''

    def mouse_single_click_elem(self, element_selector, find_by=By.CSS_SELECTOR):
        self.wait_until_elem(element_selector, find_by)
        elem = self.get_element(element_selector, find_by)
        ActionChains(self.__driver).move_to_element(elem).click(elem).perform()


    '''鼠标双击'''

    def mouse_double_click_elem(self, element_selector, find_by=By.CSS_SELECTOR):
        self.wait_until_elem(element_selector, find_by)
        elem = self.get_element(element_selector, find_by)
        ActionChains(self.__driver).move_to_element(elem).double_click(elem).perform()


    '''鼠标单击后保持'''

    def mouse_click_and_hold_elem(self, element_selector, find_by=By.CSS_SELECTOR):
        self.wait_until_elem(element_selector, find_by)
        elem = self.get_element(element_selector, find_by)
        ActionChains.click_and_hold(self, elem).perform()

    '''将元素按住拖拽到目标元素'''

    def mouse_drag_and_drop_to_elem(self, source_element, target_element, find_by=By.CSS_SELECTOR):
        self.wait_until_elem(source_element, find_by)
        self.wait_until_elem(target_element, find_by)
        source_elem = self.get_element(source_element, find_by)
        target_elem = self.get_element(target_element, find_by)
        ActionChains(self.__driver).click_and_hold(source_elem).drag_and_drop(source_elem, target_elem).perform()

    '''鼠标按住控件拖拽'''

    def mouse_exact_drag_ang_drop(self, source_element, target_element, find_by=By.CSS_SELECTOR):
        self.wait_until_elem(source_element, find_by)
        self.wait_until_elem(target_element, find_by)
        source_elem = self.get_element(source_element, find_by)
        target_elem = self.get_element(target_element, find_by)
        ActionChains(self.__driver).move_to_element(source_elem).click_and_hold(source_elem)
        ActionChains(self.__driver).move_to_element(target_elem).release().perform()

    '''将元素拖拽到目标元素'''

    def mouse_drag_and_drop_to_position(self, source_element, xoffset, yoffset, find_by=By.CSS_SELECTOR):
        self.wait_until_elem(source_element, find_by)
        source_elem = self.get_element(source_element, find_by)
        ActionChains(self.__driver).drag_and_drop_by_offset(source_elem, xoffset, yoffset).perform()

    '''断言字符'''

    def assert_equal_msg(self, actual_msg, expect_msg):
        assert actual_msg == expect_msg

    '''断言传入的文本值在包含控件的文本内容中'''

    def assert_mark_msg(self, element_selector, msg, find_by=By.CSS_SELECTOR):
        self.wait_until_elem(element_selector, find_by)
        txt_msg = self.get_element(element_selector, find_by).text
        print(txt_msg)
        assert msg in txt_msg

    '''断言传入的文本值在一组中某个元素的文本内容中'''

    def assert_mark_msgs(self, element_selector, msg, number, find_by=By.CSS_SELECTOR):
        self.wait_until_elem(element_selector, find_by)
        txt_msg = self.get_elements_text(element_selector, number, find_by)
        print(txt_msg)
        assert msg in txt_msg

    '''断言传入的文本值在一组中某个元素的属性值中'''

    def assert_mark_attrs(self, element_selector, msg, attr_name, number, find_by=By.CSS_SELECTOR):
        self.wait_until_elem(element_selector, find_by)
        txt_msg = self.get_elements_attribute_value(element_selector, attr_name, number, find_by)
        print(txt_msg)
        assert msg in txt_msg

    '''
       断言元素显示，默认显示
       1---显示
       0---不显示
    '''

    def assert_element_is_displayed(self, element_selector, flage=1, find_by=By.CSS_SELECTOR):
        if 1 == flage:
            tmp = self.get_element(element_selector, find_by).is_displayed()
            assert tmp == True
        else:
            try:
                self.get_element(element_selector, find_by).is_displayed()
            except NoSuchElementException:
                print("The element doesn't exist!")

    '''
       断言控件可用，默认可用
       1---可用
       0---不可用
    '''

    def assert_element_is_enabled(self, element_selector, flage=1, find_by=By.CSS_SELECTOR):
        self.wait_until_elem(element_selector, find_by)
        tmp = self.get_element(element_selector, find_by).is_enabled()
        if flage == 1:
            assert tmp == True
        else:
            assert tmp == False

    '''
        断言控件被选中，默认选中
        1---选中
        0---未选中
    '''

    def assert_element_is_selected(self, element_selector, flage=1, find_by=By.CSS_SELECTOR):
        self.wait_until_elem(element_selector, find_by)
        tmp = self.get_element(element_selector, find_by).is_selected()
        if 1 == flage:
            assert tmp == True
        else:
            assert tmp == False

    '''断言元素属性值'''

    def assert_attribute_msg(self, element_selector, attr, msg, find_by=By.CSS_SELECTOR):
        self.wait_until_elem(element_selector, find_by)
        attrmsg = self.get_element(element_selector, find_by).get_attribute(attr)
        assert msg in attrmsg

    '展板立即预订会议后，需要等待最多一分钟的时间会议才开始：动态断言会议开始'

    def dynamic_wait(self, element_selector, text, find_by=By.CSS_SELECTOR):
        WebDriverWait(self.__driver, 60).until(
            EC.text_to_be_present_in_element((find_by, element_selector), text))

    '''输入URL'''

    def send_url(self, url):
        self.__driver.get(url)

    def frequency_click(self, times, element_selector, find_by=By.CSS_SELECTOR):
        while times > 0:
            elem = self.get_element(element_selector, find_by)
            elem.click()
            times = times - 1

    '''插件列表中查找指定内容的元素'''
    def sle_item_in_list(self, element_selector, msg):
        lists = self.get_elements(element_selector, find_by=By.CSS_SELECTOR)
        for item in lists:
            if item.text == msg:
                print(item.text)
                item.click()
                return item

    def switch_to_window(self,handle):
        self.__driver.switch_to_window(handle)

    '''
    localtime[0]:2008
    localtime[1]:1-12
    localtime[2]:1-31
    localtime[3]:0-23
    localtime[4]:0-59
    localtime[5]:0-61 (60或61 是闰秒)
    localtime[6]:0-6 (0是周一)
    localtime[7]:1-366
    '''
    @staticmethod
    def date_to_num():
        localtime = time.localtime(time.time())
        print(localtime)
        day = tm.pc_time_module_week(localtime[6])
        hour = tm.get_time_module_day(localtime[3], localtime[4])
        return [day, hour]





