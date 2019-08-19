import unittest
import time,datetime
from comnon import open_broswer
from elems.pc import creatMeetings as cM
from case.PC import login_test


class CreatMeeting(unittest.TestCase):

    def test_create_nomal_meeting(self):
        '''普通会议室创建一个会议,会议室名称为普通会议室'''
        '''获取当前时间'''
        trick = time.time()

        print(trick)


        self.__driver = login_test.Login.test_login001()
        # self.__driver.click_element(cM.yuyue)
        # '''获取普通会议室所有位置'''
        # time.sleep(5)
        # divs = self.__driver.get_elements(cM.divs)
        # print(divs[0].text)
        # for i in range(len(divs)):
        #     if divs[i].text == '普通会议室':
        #
        #         cM.div += ':nth-child(%s)' % (i+1)
        #         cM.ul += ':nth-child(%s)' % (i+1)
        #         cM.li = cM.ul+' li:nth-child(6)'
        #         print(cM.li)
        #         break
        # js = 'document.querySelector(\''+cM.div+'\').scrollIntoView()'
        # self.__driver.execute_js(js)
        # self.__driver.click_element(cM.li)
        # time.sleep(5)


    def tearDown(self) -> None:
        self.__driver.exit_all_browser()


if __name__ == '__main__':
    unittest.main()