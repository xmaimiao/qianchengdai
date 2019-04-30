from configparser import ConfigParser

class Conf_test:

    def __init__(self,filename):
        self.conf = ConfigParser()
        self.conf.read(filename, encoding='utf-8')

    def conf_resd(self):
        list = self.conf.sections()
        return list

    def get_steValue(self,section,option):
        value = self.conf.get(section,option)
        print('在{}中,{}对应的值是：{}'.format(section,option,value))
        return value


    def getint(self,section,option):
        value = self.conf.get(section, option)
        print('在{}中,{}对应的值是：{}'.format(section, option, value))

    def getflost(self,section,option):
        value = self.conf.get(section, option)
        print('在{}中,{}对应的值是：{}'.format(section, option, value))

    def getbool(self,section,option):
        value = self.conf.get(section,option)
        print('在{}中,{}对应的值是：{}'.format(section, option, value))

    def options(self,section):
        options = self.conf.options(section)
        print('区间{}中获取所有的options为:{}'.format(section,options))
        return options

if __name__ == '__main__':
    # sections = Conf_test().conf_resd()
    # print(sections)
    # options = Conf_test().options('favorite_books')
    Conf_test('py_test0318.conf').get_steValue('favorite_books','book1')
    # Conf_test().getint(sections[0], options[1])
    # options = Conf_test().options(sections[1])
    # Conf_test().getbool(sections[1],options[3])
    # options = Conf_test().options(sections[2])
    # Conf_test().getflost(sections[2],options[2])
