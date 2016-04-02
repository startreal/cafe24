# -*- coding: utf-8 -*-
import requests
import lxml.html
import time
from flask import jsonify

class CafeCrawler():

    def crawl_cafe_list(self, index_from, crawl_size):
        base_url = 'http://map.naver.com/search2/local.nhn?sm=hty&searchCoord=127.0279266%3B37.5408227&isFirstSearch=true&query=%EC%B9%B4%ED%8E%98&menu=location&boundary=126.6964629%3B37.2941247%3B127.3566661%3B37.7875801&type=SITE_1&mpx=09200113%3A37.5408227%2C127.0279266%3AZ6%3A0.6602032%2C0.4934554http://map.naver.com/search2/local.nhn?sm=hty&searchCoord=127.0279266%3B37.5408227&isFirstSearch=true&query=%EC%B9%B4%ED%8E%98&menu=location&boundary=126.6964629%3B37.2941247%3B127.3566661%3B37.7875801&type=SITE_1&mpx=09200113%3A37.5408227%2C127.0279266%3AZ6%3A0.6602032%2C0.4934554'
        # base_url = 'http://www.schoolxcess.com/index.php?q=aHR0cDovL21hcC5uYXZlci5jb20vc2VhcmNoMi9nZXRTaXRlSW5mby5uaG4%2FaWQ9cD'
        headers = {'Accept':'application/json, text/javascript, */*; q=0.01',
        'Cookie':'npic=hYUj/pMm6E1SBw5s1x6P+88lny/2PROPZqtZQem1zK+bwlLKu5fg5pA9Ibiads3tCA==; JSESSIONID=4DFD0063192949CD42F954245F9DF86C; NNB=OXTVIJMXQP7FM; page_uid=SYIvplpydS4ssuWHVAhssssss5h-426828; _naver_usersession_=CZoemydaqoSlDlTZzbwDXQ==npic=hYUj/pMm6E1SBw5s1x6P+88lny/2PROPZqtZQem1zK+bwlLKu5fg5pA9Ibiads3tCA==; JSESSIONID=4DFD0063192949CD42F954245F9DF86C; NNB=OXTVIJMXQP7FM; page_uid=SYIvplpydS4ssuWHVAhssssss5h-426828; _naver_usersession_=CZoemydaqoSlDlTZzbwDXQ==',
        'Host':'map.naver.com',
        'Referer':'http://map.naver.com/',
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36',
        'X-Requested-With':'XMLHttpRequest'}

        result_list = []
        start = time.time()

        for idx in range(index_from, index_from+crawl_size):
            url = base_url+'&page='+str(idx+1)
            print url
            res = requests.get(url, headers=headers)
            res_json = res.json()

            try:
                if 'result' in res_json:
                    result = res.json()['result']['site']['list']
                    result_list.extend(result)
                else:
                    pass
            except Exception as e:
                print e
        end = time.time()
        print end - start
        return result_list

    def crawl_cafe_page(self, cafe_id):
        base_url = 'http://map.naver.com/local/siteview.nhn?code='
        # base_url = 'http://www.schoolxcess.com/index.php?q=aHR0cDovL21hcC5uYXZlci5jb20vc2VhcmNoMi9nZXRTaXRlSW5mby5uaG4%2FaWQ9cD'
        headers = {'Accept':'application/json, text/javascript, */*; q=0.01',
        'Cookie':'npic=hYUj/pMm6E1SBw5s1x6P+88lny/2PROPZqtZQem1zK+bwlLKu5fg5pA9Ibiads3tCA==; JSESSIONID=4DFD0063192949CD42F954245F9DF86C; NNB=OXTVIJMXQP7FM; page_uid=SYIvplpydS4ssuWHVAhssssss5h-426828; _naver_usersession_=CZoemydaqoSlDlTZzbwDXQ==npic=hYUj/pMm6E1SBw5s1x6P+88lny/2PROPZqtZQem1zK+bwlLKu5fg5pA9Ibiads3tCA==; JSESSIONID=4DFD0063192949CD42F954245F9DF86C; NNB=OXTVIJMXQP7FM; page_uid=SYIvplpydS4ssuWHVAhssssss5h-426828; _naver_usersession_=CZoemydaqoSlDlTZzbwDXQ==',
        'Host':'map.naver.com',
        'Referer':'http://map.naver.com/',
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36',
        'X-Requested-With':'XMLHttpRequest'}

        start = time.time()
        url = base_url+str(cafe_id)
        print url
        res = requests.get(url, headers=headers)


        root = lxml.html.fromstring(res.content)
        open_dict_list = []
        for el in root.cssselect("#_baseInfo > div.section.section_detail > dl > dd.section_detail_time > ul > li"):
            open_label_obj = next(iter(el.cssselect("strong")), None)
            open_label_text = open_label_obj.text if open_label_obj is not None else None
            open_time_obj = next(iter(el.cssselect("span")), None)
            open_time_text = open_time_obj.text if open_time_obj is not None else None
            print open_label_text
            print open_time_text
            open_dict_list.append({
                'label':open_label_text,
                'time':open_time_text
            })
        end = time.time()
        print end - start
        return open_dict_list

    def crawl(self, start_page, page_number):
        result_list = self.crawl_cafe_list(int(start_page), int(page_number))
        for each_cafe in result_list:
            cafe_id = each_cafe['id'][1:]
            each_cafe['open'] = self.crawl_cafe_page(cafe_id)
        return result_list

