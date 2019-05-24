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
from extractor_mi import MiExtractor
from util.util import Util


class MiSpider(BaseSpider):
    """
    抓小米的游戏信息
    """

    def __init__(self):
        self.util = Util()
        super(MiSpider, self).__init__()
        self.extractor = MiExtractor()
        self.keywords = self.util.get_keywords()
        self.phone_url = 'http://app.mi.com/searchAll?keywords={}&typeall=phone&page={}'
        self.pad_url = 'http://app.mi.com/searchAll?keywords={}&typeall=pad&page={}'

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
            phone_url = self.phone_url.format(urllib.quote(keyword), 1)
            pad_url = self.pad_url.format(urllib.quote(keyword), 1)
            phone_request_url = [{"url": phone_url, "type": 1, "ext_type": 1, "media": "mi", "keyword": keyword,
                            "unique_key": self.get_unique_key()}]
            pad_request_url = [{"url": pad_url, "type": 1, "ext_type": 1, "media": "mi", "keyword": keyword,
                            "unique_key": self.get_unique_key()}]
            self.send_get_spider(phone_request_url)
            self.send_get_spider(pad_request_url)

    def send_next_to_dc(self, result, urls):
        """
        将下一页发送至下载中心
        """
        try:
            next_page_href = self.extractor.get_next_page(result['result'])
            if next_page_href is not None:
                request_url = [
                    {"url": next_page_href, "type": 1, "ext_type": 1, "media": "mi", "keyword": urls['keyword'],
                     "unique_key": self.get_unique_key()}]
                self.send_get_spider(request_url)
        except:
            print "send_next_to_dc error"
            traceback.print_exc()

    def deal_response_results_status(self, task_status, url, result, request):
        try:
            if task_status == '2':
                print url['unique_key']
                ext_type = url["ext_type"]
                request_url = request.urls[0]
                if ext_type == 1:
                    self.send_next_to_dc(result, request_url)
                    app_url_list = self.extractor.get_each_app_url(result['result'])
                    if app_url_list:
                        for url in app_url_list:
                            urls = [
                                {"url": url, "type": 1, "ext_type": 2, "media": "mi",
                                 "keyword": request_url['keyword'],
                                 "unique_key": self.get_unique_key()}]
                            self.send_get_spider(urls)
                    else:
                        request_url['unique_key'] = self.get_unique_key()
                        self.send_get_spider(request_url)
                else:
                    self.extractor.extractor_info(url, result)
        except:
            print('deal_response_results_status error')
            traceback.print_exc()


if __name__ == '__main__':
    spider = MiSpider()
    spider.run(1, 1, 1, 1, -1, -1, -1, -1, True)
