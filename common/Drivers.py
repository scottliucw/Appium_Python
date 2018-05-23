# -*- coding: utf-8 -*-

from multiprocessing import Pool
from common import Ports
from common import Devices
from appium import webdriver
from common import Runcase
from common import AppiumServer
from common import BasePage
import unittest
from case import Testcase_freestore
import os


class Driver:
    @staticmethod
    def _run_cases(run, cases):
        driver = webdriver.Remote(str('http://localhost:%s/wd/hub') % run.get_port()[0], run.get_device())

        base_page = BasePage.BasePage()
        base_page.set_driver(driver)

        # run.run(cases)
        run.run(cases)

    def run_driver(self):
        device = Devices.get_devices()
        port = Ports.Ports().get_ports(len(device))
        print(port)

        if not len(device):
            print('测试设备未连接！')
            return

        runs = []
        for i in range(len(device)):
            runs.append(Runcase.RunCase(device[i], port[i]))

        Appium_server = AppiumServer.AppiumServer(runs)
        Appium_server.start_server()
        print('good')

        # 多机用例
        suites = []
        suite = unittest.TestSuite()
        suite.addTest(Testcase_freestore.Testcase("test_mian"))
        suites.append(suite)
        suite1 = unittest.TestSuite()
        suite1.addTest(Testcase_freestore.Testcase("test_login_logout"))
        suites.append(suite1)
        print(suites)

        # suites = []
        # suite = unittest.TestLoader().loadTestsFromTestCase(Testcase_freestore.Testcase)
        # suites.append(suite)
        # suites.append(suite)

        pool = Pool(processes=len(runs))
        for run in runs:
            pool.apply_async(self._run_cases, args=(run, suites[runs.index(run)]))
        pool.close()
        pool.join()

        Appium_server.kill_server()


if __name__ == '__main__':
    a = Driver()
    a.run_driver()
    # os.system('taskkill /f /im  node.exe')

