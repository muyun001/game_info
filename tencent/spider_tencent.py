# -*- coding: utf-8 -*-
from download_center.new_spider.downloader.downloader import SpiderRequest
from download_center.new_spider.spider.basespider import BaseSpider
from extractor_tencent import TencentExtractor
from util.util import Util
import urllib
import random
import os
import time
import traceback
import sys
reload(sys)
sys.setdefaultencoding('utf8')
PROJECT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(PROJECT_PATH)


class TencentSpider(BaseSpider):
    """
    抓腾讯应用宝的游戏信息
    """
    def __init__(self):
        self.util = Util()
        super(TencentSpider, self).__init__()
        self.extractor = TencentExtractor()
        self.keywords = self.util.get_keywords()
        self.base_url = 'https://sj.qq.com/myapp/searchAjax.htm?kw={}&pns={}&sid=0'

    def get_user_password(self):
        return 'fxt', 'fxt_spider'

    def get_stores(self):
        stores = list()
        return stores

    def send_get_spider(self, request_url):
        """
        封装好 GET request请求，并发送到下载队列
        """
        basic_request = SpiderRequest(headers={"User-Agent": random.choice(self.pc_user_agents)}, urls=request_url, config={"redirect": 1})
        self.sending_queue.put_nowait(basic_request)

    def start_requests(self):
        try:
            for keyword in self.keywords:
                json_original_url = self.base_url.format(urllib.quote(keyword), '')
                request_json_url = [
                    {"url": json_original_url, "type": 1, "ext_type": 1, "media": "tencent", "keyword": keyword,
                     "unique_key": self.get_unique_key()}]
                self.send_get_spider(request_json_url)
        except:
            print('start_requests error')
            traceback.print_exc()

    def deal_response_results_status(self, task_status, url, result, request):
        try:
            if task_status == '2':
                print url['unique_key']
                page_number_stack = self.extractor.extractor_json(url, result['result'])
                if page_number_stack is not None:
                    json_url = self.base_url.format(urllib.quote(url['keyword']), page_number_stack)
                    request_json_url = [
                        {"url": json_url, "type": 1, "ext_type": 1, "media": url['media'], "keyword": url['keyword'],
                         "unique_key": self.get_unique_key()}]
                    self.send_get_spider(request_json_url)
                else:
                    request_json_url = [
                        {"url": url['url'], "type": 1, "ext_type": 1, "media": url['media'], "keyword": url['keyword'],
                         "unique_key": self.get_unique_key()}]
                    self.send_get_spider(request_json_url)
        except:
            print('deal_response_results_status error')
            traceback.print_exc()


if __name__ == '__main__':
    spider = TencentSpider()
    spider.run(1, 1, 1, 1, -1, -1, -1, -1, True)
