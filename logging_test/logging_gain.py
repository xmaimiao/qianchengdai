import logging
# import sys
# sys.path.append("./configparser_test0316")
from test0316_1 import Conf_test

class Logging_Gain:
    def __init__(self,log_level,sc_level,form):
        self.log_level = log_level
        self.sc_level = sc_level
        self.form = form

    def logging_test(self):
        log = logging.getLogger()
        log.setLevel(self.log_level)
        formatter = logging.Formatter(self.form)
        sc = logging.StreamHandler()
        sc.setFormatter(formatter)
        sc.setLevel(self.sc_level)
        log.addHandler(sc)
        log.debug("輸出debug級別的錯誤")
        log.info("輸出info級別的錯誤")
        log.warning("輸出warning級別的錯誤")

if __name__ == '__main__':
    log_level = Conf_test('logging_conf.conf').get_steValue('formatter', 'log_level')
    sc_level = Conf_test('logging_conf.conf').get_steValue('formatter', 'sc_level')
    form = Conf_test('logging_conf.conf').get_steValue('formatter', 'form')

    Logging_Gain(log_level,sc_level,form).logging_test()
