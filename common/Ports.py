# -*- coding: utf-8 -*-

import os


class Ports:
    @staticmethod
    def is_using(port):
        """判断端口号是否被占用"""
        cmd = "netstat -an | findstr %s" % port

        if os.popen(cmd).readlines():
            return True
        else:
            return False

    def get_ports(self, count):
        """获得4723端口后的可以用端口"""
        port = 4723
        port_list = []
        port_p_bp = []
        sum1 = count * 2
        while sum1 > 0:
            sum2 = 2
            while sum2 > 0:
                _port_list = []
                for each in port_list:
                    for each in each:
                        _port_list.append(each)
                if not self.is_using(port) and (port not in _port_list):
                    port_p_bp.append(port)
                    sum1 -= 1
                    sum2 -= 1
                    port += 1
                else:
                    port += 1
            port_list.append(port_p_bp)
            port_p_bp = []

        return port_list


if __name__ == '__main__':

    ports = Ports().get_ports(6)
    print(ports)