# -*- coding: utf-8 -*-
from download_center.new_spider.downloader.downloader import SpiderRequest
from download_center.new_spider.spider.basespider import BaseSpider
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
from extractor_huawei import HWExtractor
from util.util import Util


class HWSpider(BaseSpider):
    """
    抓华为的游戏信息
    """

    def __init__(self):
        self.util = Util()
        super(HWSpider, self).__init__()
        self.extractor = HWExtractor()
        self.keywords = self.util.get_keywords()
        self.url = 'http://app.hicloud.com/search/{}/{}'

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
        for keyword in self.keywords:
            url = self.url.format(urllib.quote(keyword), 1)
            request_url = [{"url": url, "type": 1, "ext_type": 0, "media": "huawei", "keyword": keyword,
                            "unique_key": self.get_unique_key()}]
            self.send_get_spider(request_url)

    def deal_response_results_status(self, task_status, url, result, request):
        try:
            if task_status == '2':
                print url['unique_key']
                ext_type = url["ext_type"]
                if ext_type == 0:
                    page_num = self.extractor.judge_page_num(result['result'])
                    for page in range(2, page_num+1):
                        next_url = self.url.format(url['keyword'], page)
                        urls = [
                            {"url": next_url, "type": 1, "ext_type": 1, "media": url['media'], "keyword": url['keyword'],
                             "unique_key": self.get_unique_key()}]
                        self.send_get_spider(urls)
                elif ext_type == 1:
                    app_url_list = self.extractor.get_each_app_url(result['result'])
                    if app_url_list:
                        for app_url in app_url_list:
                            urls = [
                                {"url": app_url, "type": 1, "ext_type": 2, "media": url['media'],
                                 "keyword": url['keyword'],
                                 "unique_key": self.get_unique_key()}]
                            self.send_get_spider(urls)
                    else:
                        url['unique_key'] = self.get_unique_key()
                        self.send_get_spider(url)
                else:
                    self.extractor.extractor_info(url, result)
        except:
            print('deal_response_results_status error')
            traceback.print_exc()


if __name__ == '__main__':
    spider = HWSpider()
    spider.run(1, 1, 1, 1, -1, -1, -1, -1, True)
