# -*- coding: utf-8 -*-
import os
import codecs


class Util(object):

    def __init__(self):
        self.read_path = r''
        self.save_path = r'../data/result.csv'
        # self.judge_path()
        self.write = codecs.open(self.save_path, 'a', encoding='utf8')
        # self.write_data(u'游戏名, 包名, 类型, 公司名, orgame, apkCode, appId, 媒体, 关键词')

    def get_keywords(self):
        """
        读取关键词
        """
        return ['英雄爱三国']

    def judge_path(self):
        """
        执行之前将前文件删除
        """
        if os.path.exists(self.save_path):
            os.remove(self.save_path)

    def write_data(self, content):
        """
        将数据写入文件
        """
        self.write.write(content + '\n')
        print('write data to csv succeed: ', content)


if __name__ == '__main__':
    util = Util()
    util.write_data('aaa')