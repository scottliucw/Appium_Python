# -*- coding: utf-8 -*-

import os

GET_ANDROID = "adb devices"


def get_devices():
    value = os.popen(GET_ANDROID)

    devices = []

    for v in value.readlines():
        desired_caps = {}
        s_value = str(v).replace("\n", "").replace("\t", "")
        if s_value.find('device') != -1 and (not s_value.startswith("List")) and s_value != "":
            desired_caps['platformName'] = 'Android'
            desired_caps['deviceName'] = s_value[:s_value.find('device')]
            desired_caps['udid'] = s_value[:s_value.find('device')]
            desired_caps['appPackage'] = 'com.snailgame.cjg'
            desired_caps['appActivity'] = 'com.snailgame.cjg.MainActivity'

            devices.append(desired_caps)

    return devices


if __name__ == '__main__':
    b = get_devices()
    print(b)
    udid = b[0]['udid']
    print(udid)

    if not len(b):
        print('测试设备未连接！')
    else:
        print('ok')
