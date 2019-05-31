# -*- coding: utf-8 -*-
import scrapy
from scrapy_redis.spiders import RedisCrawlSpider
import json
import re
from zhihu.items import ZhihuItem

class ZhihuSpider(RedisCrawlSpider):
    redis_key = "redisQueue"
    name = 'zhihu'
    # allowed_domains = ['zhihu.com']
    # start_urls = ['https://www.zhihu.com/api/v4/members/ray-yang-ml/followees?include=data%5B*%5D.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics&offset=20&limit=20']


    def parse(self, response):
        temp_data = json.loads(response.body.decode("utf-8"))['data']
        count = len(temp_data)  # 多少条数据
        if count <= 20:
            pass
        else:
            # 继续调用用户本身
            page_offset = int(re.findall("&offset=(.*?)&", response.url)[0])
            new_page_offset = page_offset + 20
            next_page_url = response.url.replace("&offset=" + str(page_offset) + "&",
                                                 "&offset=" + str(new_page_offset) + "&")
        for eve_user in temp_data:
            item = ZhihuItem()
            item['name'] = eve_user['name']
            item['url_token'] = eve_user['url_token']
            item['headline'] = eve_user['headline']
            item['follower_count'] = eve_user['follower_count']
            item['answer_count'] = eve_user['answer_count']
            item['articles_count'] = eve_user['articles_count']
            item['uid'] = eve_user['id']
            item['gender'] = eve_user['gender']
            item['type'] = eve_user['type']

            with open("userinfor.txt") as f:
                user_list = f.read()

            if eve_user['url_token'] not in user_list:
                with open("userinfor.txt", "a") as f:
                    f.write(eve_user["url_token"] + "----")
            yield item

            new_url = "https://www.zhihu.com/api/v4/members/" + eve_user[
                'url_token'] + "/followees?include=data%5B*%5D.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics&offset=0&limit=20"
            yield scrapy.Request(url=new_url, callback=self.parse)



