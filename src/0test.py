from util import *
from const import const
import logging


def main():
    log_file = 'log/%s.log' % datetime.strftime(datetime.now(), '%Y-%m-%d')
    log_format = '%(message)s'
    logging.basicConfig(filename=log_file, level=logging.WARNING, format=log_format)
    logger = logging.getLogger()
    logger.warning('This is a warning message!')
        

if __name__ == '__main__':
    # print('adb初始化开始')
    # util.adb('kill-server')
    # util.adb('connect 127.0.0.1:7555')
    main()
