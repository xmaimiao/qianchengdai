from configparser import ConfigParser
from UseExcel.common import contants

class Config:

    def __init__(self):
        self.config = ConfigParser()
        self.config.read(contants.global_dir,encoding='utf-8')
        # self.switch = self.config.get('global','switch')   #這樣寫只會拿到str類型數據，不為空永遠為真
        self.switch = self.config.getboolean('global','switch')
        print(type(self.switch))
        if self.switch:
            self.con = self.config.read(contants.online_dir,encoding='utf-8')
        else:
            self.url = self.config.read(contants.test_dir, encoding='utf-8')

    def get(self,section,option):
        return self.config.get(section,option)

config = Config()

# if __name__ == '__main__':
#     config = Config().get('api','pre_url')
#     print(config)