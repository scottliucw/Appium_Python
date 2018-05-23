# -*- coding: utf-8 -*-


class BasePage(object):
    @classmethod
    def set_driver(cls, dri):
        cls.driver = dri

    def get_driver(self):
        return self.driver

    def _get_windows_size(self):
        window = self.driver.get_window_size()
        y = window['height']
        x = window['width']

        return x, y

    @staticmethod
    def _get_element_size(element):
        location = element.location
        size = element.size

        x_center = location['x'] + size['width'] / 2
        y_center = location['y'] + size('height') / 2
        x_left = location['x']
        x_right = location['x'] + size['width']
        y_up = location['y']
        y_down = location['y'] + size['height']

        return x_left, y_up, x_center, y_center, x_right, y_down

    def swipe_up(self, element=None, steps=200):
        if element:
            x_left, y_up, x_center, y_center, x_right, y_down = self._get_element_size(element)

            fromX = x_center
            fromY = y_center
            toX = x_center
            toY = y_up
        else:
            print('2')
            x, y = self._get_windows_size()
            fromX = 0.5 * x
            fromY = 0.5 * y
            toX = 0.5 * x
            toY = 0.25 * y
            print(fromY, fromX, toY, toX)

        self.driver.swipe(fromX, fromY, toX, toY, steps)

    def swipe_down(self, element=None, steps=1000):
        if element:
            x_left, y_up, x_center, y_center, x_right, y_down = self._get_element_size(element)

            fromX = x_center
            fromY = y_center
            toX = x_center
            toY = y_down
        else:
            x, y = self._get_windows_size()
            fromX = 0.5 * x
            fromY = 0.5 * y
            toX = 0.5 * x
            toY = 0.75 * y

        self.driver.swipe(fromX, fromY, toX, toY, steps)

    def swipe_left(self, element=None, steps=1000):
        if element:
            x_left, y_up, x_center, y_center, x_right, y_down = self._get_element_size(element)
            fromX = x_center
            fromY = y_center
            toX = x_left
            toY = y_center
        else:
            x, y = self._get_windows_size()
            fromX = 0.5 * x
            fromY = 0.5 * y
            toX = 0.25 * x
            toY = 0.5 * y

        self.driver.swipe(fromX, fromY, toX, toY, steps)

    def swipe_right(self, element=None, steps=1000):
        if element:
            x_left, y_up, x_center, y_center, x_right, y_down = self._get_element_size(element)

            fromX = x_center
            fromY = y_center
            toX = x_right
            toY = y_center
        else:
            x, y = self._get_windows_size()
            fromX = 0.5 * x
            fromY = 0.5 * y
            toX = 0.75 * x
            toY = 0.5 * y

        self.driver.swipe(fromX, fromY, toX, toY, steps)


# dev = devices.Device().get_devices()

# driver = webdriver.Remote('http://localhost:4723/wd/hub', dev[0])
# base_page = BasePage()
# base_page.set_driver(driver)

# sleep(5)
# driver.find_element_by_name(u"发现").click()
# driver.find_element_by_id('com.snailgame.cjg:id/tv_more').click()
# while driver.page_source.find('com.snailgame.cjg:id/loadMoreProgress') < 0:
#    base_page.swipe_up()

# while driver.page_source.find('com.snailgame.cjg:id/siv_title') < 0:
#    base_page.swipe_down()