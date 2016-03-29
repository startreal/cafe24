# -*- coding: utf-8 -*-
import requests
import lxml.html
import time


class CafeCrawler():

    def crawl_cafe_list(self, index_from, crawl_size):
        base_url = 'http://map.naver.com/search2/local.nhn?query=%EC%B9%B4%ED%8E%98&type=SITE_1&queryRank=1&siteSort=0&menu=location&searchCoord=127.0018354%3B37.5560745&sm=clk&boundary=126.9246437%3B37.4944333%3B127.078899%3B37.617808&mpx=09140580%3A37.5560745%2C127.0018354%3AZ8%3A0.1542553%2C0.1233747'
        # base_url = 'http://www.schoolxcess.com/index.php?q=aHR0cDovL21hcC5uYXZlci5jb20vc2VhcmNoMi9nZXRTaXRlSW5mby5uaG4%2FaWQ9cD'
        headers = {'Accept':'application/json, text/javascript, */*; q=0.01',
        'Cookie':'npic=IhHf0sIV2sNKzQWajD4MaBwbICouHNRqL1nNOqO2UonEKdRkaylWM4W4CeiWb7PVCA==; NNB=5FIFGLS5NDWFG; WMONID=ZzV3T54OUA2; nsr_acl=1; BMR=s=1431578263011&r=http%3A%2F%2Ftvcast.naver.com%2Fv%2F368791%2Flist%2F33215&r2=http%3A%2F%2Ftvcast.naver.com%2Fv%2F366519; nid_inf=611665233; NID_AUT=9QZuR23S9LQ7QBjvLANeSh0M1EZ3+agZ/9aMV50PEtWhNBjpjMnae3Nn+cp9dARD; NID_SES=AAABThR1q17xHlztdAbeV9JamitaH1MHMr5F8HnuchL0JKOFaYBhzkycsGNFKqKnSfG3eYZeycNv28ELaNO9ueFAJC5fGjcw0mK3uxd5UInjv+nB7/2FmJGxCBIkoZZ8RiJNxea7RL6DVV/4xWkjwX0ym8I6zDf2nt4b8JjIlvG3S4SHzTZqb7R2lXEMrdy0ixXq1+zUm3EtOp/UC/NS5wxcX513F0gl8TNtEzEbjpD4oKBw8aIYj8+QQ+//CxkK3XItDBagxXMZ4F33AEK9XrK6iNVdI4+9fWM3fDphClhgy5K0M/8bvgajppPyt39fOEFpsV3pEQuMSkatFm7ioS52hdhKhVDI3oQXDPar37Yy41svh7lGvF46XHXr6GWuwrndUahdrKtC0FJ5iWBr9HcgmImq+FZ8J9r9qCMAV8/ecUjxzP1Q6nNFfskzlwUru56+Ow==; ns_load_time=1431690925387; ns_sid=45dc8c80-faf9-11e4-823e-836f0b3835a6; JSESSIONID=918A0B13C8717968F0C70A2B5FADFD9E; page_uid=SSUPrwpyLjRssa60D5RssssssZw-166244; _naver_usersession_=sMJVm/9grSbKBn0vg2lFzg==',
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
        'Cookie':'npic=jynufvucroCs0fFerOfSXwhRrh1zUweOzhA//z++D3Ls/imab7yCjHQ+sHNrmiukCA==; NNB=5YGIIJLAA7ZVK; __gads=ID=24b7cc66d1cc27d1:T=1450847420:S=ALNI_MZBNrYxOxnBLApu96Dn2r9FbzhoAw; nx_ssl=2; _ga=GA1.2.242297725.1452759455; nid_inf=-648798361; BMR=s=1459053435540&r=http%3A%2F%2Fpost.naver.com%2Fviewer%2FpostView.nhn%3FvolumeNo%3D3863751%26memberNo%3D19627&r2=http%3A%2F%2Fwww.naver.com%2F; nid_iplevel=-1; page_uid=SYpJslpydShsss+ZaN0ssssssSs-362969; _naver_usersession_=FAeJb/WluobqoSX/Z5ycbQ==; JSESSIONID=6C433A583FD9D49DEA02EAF65FBD4057',
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

