import unittest
from comnon.open_broswer import WebClient
import time
from elems.pc import meeting
from data import init
from data import login


class Login(unittest.TestCase):


    @staticmethod
    def test_login001_admin():
        __driver = WebClient(init.web)
        __driver.run_chrome()
        __driver.sendkeys_to_element(meeting.user_name, init.user_amdin+init.tenant_domain)
        __driver.sendkeys_to_element(meeting.password, init.user_pwd)

    @staticmethod
    def test_login001():
        __driver = WebClient('https://automeeting.rd.virsical.cn/meeting')
        __driver.run_chrome()
        __driver.sendkeys_to_element(meeting.user_name, login.admin)
        __driver.sendkeys_to_element(meeting.password, login.password_admin)
        __driver.click_element(meeting.login)
        # js = 'window.open("https://teststmeeting.rd.virsical.cn/meeting")'
        # self.__driver.execute_js(js)
        # handles = self.__driver.get_all_pages_handle()
        # self.__driver.switch_to_window(handles[1])
        # time.sleep(5)
        return __driver

    @staticmethod
    def test_login002_hysgly():
        __driver = WebClient(init.web)
        __driver.run_chrome()
        __driver.sendkeys_to_element(meeting.user_name, init.user_hysgly+init.tenant_domain)
        __driver.sendkeys_to_element(meeting.password, init.user_pwd)
        __driver.click_element(meeting.login)
        return __driver

    @staticmethod
    def test_login003_hygly():
        __driver = WebClient(init.web)
        __driver.run_chrome()
        __driver.sendkeys_to_element(meeting.user_name, init.user_hygly+init.tenant_domain)
        __driver.sendkeys_to_element(meeting.password, init.user_pwd)
        __driver.click_element(meeting.login)
        return __driver

    @staticmethod
    def test_login004_hyfwgly():
        __driver = WebClient(init.web)
        __driver.run_chrome()
        __driver.sendkeys_to_element(meeting.user_name, init.user_hyfwgly+init.tenant_domain)
        __driver.sendkeys_to_element(meeting.password, init.user_pwd)
        __driver.click_element(meeting.login)
        return __driver
    # def test_login002(self):
    #     ...

    def tearDown(self) -> None:
        ...


if __name__ == '__main__':
    unittest.main()
