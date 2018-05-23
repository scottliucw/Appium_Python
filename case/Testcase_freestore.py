# encoding: utf-8

import time
import unittest
import xlrd
from common import BasePage
import logging

logging.basicConfig(level=logging.INFO)


def execl_rows(sheet):
    workbook = xlrd.open_workbook(r'D:\test\account.xlsx')
    index = workbook.sheet_by_index(sheet)
    rows = index.nrows
    return rows


def read_excel(rowx, colx):
    workbook = xlrd.open_workbook(r'D:\test\account.xlsx')
    index = workbook.sheet_by_index(0)
    value = index.cell_value(rowx, colx)
    return value


#   def screen_shot(file_name):
#    timestr = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
#    img_name = file_name + '-' + timestr + '.png'
#    file = "D:\\test\\" + img_name
#    self.driver.get_screenshot_as_file(file)


# def error_image(func):
#    @wraps(func)
#    def wrapper(self, *args, **kwargs):
#        try:
#            print('decorator is running')
#            func(self, *args, **kwargs)
#        except AssertionError:
#            self.screen_shot(func.__name__)
#        else:
#            logging.info("%s 脚本运行正常" % func.__name__)
#
#    return wrapper


class Testcase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        #        desired_caps = {}
        #        desired_caps['platformName'] = 'Android'
        #        desired_caps['platformVersion'] = '5.1.1'
        #        desired_caps['deviceName'] = '3253ee99'
        #        desired_caps['appPackage'] = 'com.snailgame.cjg'
        #        desired_caps['appActivity'] = 'com.snailgame.cjg.MainActivity'
        #        desired_caps['unicodeKeyboard'] = 'True'
        #        desired_caps['resetKeyboard'] = 'True'
        #
        #        device = devices.Device()
        #        desired_caps = device.get_devices()
        #        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps[0])

        #        time.sleep(2)
        cls.driver = BasePage.BasePage().get_driver()

        time.sleep(5)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close_app()
        cls.driver.quit()

    def test_login_logout(self):
        # print('start login_logout')
        self.driver.find_element_by_id('com.snailgame.cjg:id/mine').click()
        self.driver.find_element_by_id('com.snailgame.cjg:id/iv_unlogin_avatar').click()
        time.sleep(1)
        self.driver.find_element_by_id('com.snailgame.cjg:id/common_login_btn').click()
        # account = read_excel(x, y)
        # print(account)
        self.driver.find_element_by_id('com.snailgame.cjg:id/account_input').send_keys('17095011949')
        self.driver.find_element_by_id('com.snailgame.cjg:id/password_input').click()
        time.sleep(1)
        self.driver.press_keycode(29, 28672)
        self.driver.press_keycode(67)
        # password = read_excel(x, y + 1)
        self.driver.find_element_by_id('com.snailgame.cjg:id/password_input').send_keys('s1234567')
        self.driver.find_element_by_id('com.snailgame.cjg:id/login_button').click()
        time.sleep(5)
        self.assertTrue(self.driver.find_element_by_name(u'退出'))
        self.driver.find_element_by_id('com.snailgame.cjg:id/tv_right_action').click()
        self.driver.find_element_by_id('com.snailgame.cjg:id/sure').click()

    def test_mian(self):
        self.driver.find_element_by_id('com.snailgame.cjg:id/tab_free_store').click()

    def test_setlocation(self):
        self.driver.find_element_by_id('com.snailgame.cjg:id/tab_home').click()
        self.driver.find_element_by_xpath("//android.widget.TextView[contains(@text, '苏州市')]").click()
        time.sleep(2)
        while self.driver.page_source.find(u'重庆市') < 0:
            BasePage.BasePage().swipe_up()
        time.sleep(2)
        self.driver.find_element_by_xpath("//android.widget.TextView[contains(@text, '重庆市')]").click()

# if __name__ == '__main__':
#    testunit = unittest.TestSuite()
#    testunit.addTest(freestore("test_login_logout"))
#    testunit.addTest(freestore("test_mian"))
#    # test_suit.addTests(map(Mydemo, ["Mytest1", "Mytest2", "Mytest3"]))
#    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
#    HtmlFile = "D:\\test\\" + now + "HTMLtemplate.html"
#    fp = open(HtmlFile, "wb")
#    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"测试报告", description=u"用例测试情况")
#    runner.run(testunit)
#
#    fp.close()