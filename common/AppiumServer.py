# -*- coding: utf-8 -*-

from multiprocessing import Pool
import os


class AppiumServer:
    def __init__(self, runs):
        self._runs = runs

    def start_server(self):
        pool = Pool(processes=len(self._runs))
        for run in self._runs:
            pool.apply_async(self.run_server, args=(run,))
        pool.close()
        # pool.join()

    def run_server(self, run):
        port = run.get_port()
        cmd = str('appium -p %s -bp %s') % (port[0], port[1])
        os.system(cmd)

    def kill_server(self):
        os.system('taskkill /f /im  node.exe')
