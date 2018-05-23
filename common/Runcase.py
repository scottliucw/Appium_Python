# -*- coding: utf-8 -*-

import os
import time
from common import HTMLTestRunner_appium


class RunCase:
    def __init__(self, device, port):
        self.device = device
        self.port = port

        date_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        self.test_report_path = 'D:\\test\\' + date_time + '-%s' % self.device['udid']
        if not os.path.exists(self.test_report_path):
            os.mkdir(self.test_report_path)

        self.file_name = self.test_report_path + '\\' + 'test_report.html'

    def get_path(self):
        return self.test_report_path

    def get_device(self):
        return self.device

    def get_port(self):
        return self.port

    def run(self, cases):
        fp = open(self.file_name, "wb")
        runner = HTMLTestRunner_appium.HTMLTestRunner(stream=fp,
                                                      verbosity=2,
                                                      retry=1,
                                                      title="测试报告",
                                                      description="用例执行情况",
                                                      save_last_try=True)
        runner.run(cases)
        fp.close()
