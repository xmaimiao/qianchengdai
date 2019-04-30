import logging
from UseExcel.common import contants
from UseExcel.common.config import  config

def get_logger(name):                       #執行日誌的用例都是不同的，故要傳入名字，不傳就會統一用root，重複輸出日誌信息
    logger = logging.getLogger(name)
    fmt = '%(asctime)s-%(levelname)s-%(name)s-日誌信息:%(message)s-[%(filename)s:%(lineno)d]'
    formatter = logging.Formatter(fmt)
    logger.setLevel(config.get('data','logger_level'))


    console_logger = logging.StreamHandler()
    console_logger.setFormatter(formatter)
    console_logger.setLevel(config.get('data','console_level'))

    file_logger = logging.FileHandler(contants.log_dir + '/case.log')
    file_logger.setFormatter(formatter)
    file_logger.setLevel(config.get('data','file_level'))

    logger.addHandler(console_logger)
    logger.addHandler(file_logger)
    return logger



