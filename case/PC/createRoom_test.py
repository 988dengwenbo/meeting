#coding=utf8

import unittest
from comnon.open_broswer import WebClient
from case.PC import login_test
from elems.pc import creatRooms as cR
import time


class CreateRoom(unittest.TestCase):


    def test_create_nomal_room(self, ):
        self.__driver =login_test.Login.test_login001()
        self.__driver.click_element(cR.sys_conf)
        self.__driver.click_element(cR.room_manage)
        self.__driver.click_element(cR.add_romm)
        self.__driver.sendkeys_to_element(cR.room_name, '普通会议室')
        # self.__driver.sendkeys_to_element(cR.room_name_en, u'nomal meeting room')   #会议室英文名称
        self.__driver.sendkeys_to_element(cR.email,'123456@qq.com')
        self.__driver.click_element(cR.area_1)
        time.sleep(2)
        area_1_lis = self.__driver.get_elements(cR.area_1_lis)
        for i in range(len(area_1_lis)):
            if area_1_lis[i].text == '陕西':
                area_1_lis[i].click()
                break
            if i == len(area_1_lis):
                area_1_lis[0].click()

        self.__driver.click_element(cR.area_2)
        time.sleep(2)
        area_2_lis = self.__driver.get_elements(cR.area_2_lis)
        for i in range(len(area_2_lis)):
            if area_2_lis[i].text == '西安':
                area_2_lis[i].click()
                break
            elif i == len(area_2_lis):
                area_2_lis[0].click()

        self.__driver.click_element(cR.room_manager)
        time.sleep(2)
        room_manegers_lis = self.__driver.get_elements(cR.room_manager_lis)
        for i in range(len(room_manegers_lis)):
            if room_manegers_lis[i].text == 'hysgly':
                room_manegers_lis[i].click()
                break
            if i == len(room_manegers_lis):
                room_manegers_lis[0].click()

        self.__driver.click_element(cR.submit)
        time.sleep(10)
        self.assertEqual(self.__driver.get_element_text(cR.msg), '保存成功')

    def tearDown(self) -> None:
        self.__driver.exit_all_browser()




if __name__ == '__main__':
    unittest.main()