# -*- coding: utf-8 -*-

# Scrapy settings for zhihu project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html
from zhihu.proxy import *


BOT_NAME = 'zhihu'

SPIDER_MODULES = ['zhihu.spiders']
NEWSPIDER_MODULE = 'zhihu.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
  ':authority': 'www.zhihu.com',
  ':method':'GET',
  ':path':"/api/v4/members/hua-wei-62-16/followees?include=data%5B*%5D.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics&offset=0&limit=20",
  ':scheme': 'https',
  'accept': '*/*',
  'accept-language': "zh-CN,zh;q=0.9,en;q=0.8",
  'cookie': '_xsrf=PUofKRq227TS1FDQ6phwWwjNbCAH5RbE; _zap=e431bf8b-97cb-4c2d-b905-126652ed139e; q_c1=756c52b4d652449aa3318f492934da4f|1548994477000|1548994477000; d_c0="APChKKzk6Q6PTsqDgrHFyMY35E1PiG15xSM=|1548994479"; __utma=51854390.1767450546.1548994479.1548994479.1548994479.1; __utmz=51854390.1548994479.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmv=51854390.000--|3=entry_date=20190201=1; tgw_l7_route=a37704a413efa26cf3f23813004f1a3b; capsion_ticket="2|1:0|10:1559144731|14:capsion_ticket|44:ZmJlOGFlNGM2YTMzNDhkYjljODZiZjIzMzg1ZWQ2Zjk=|518fddc3a14dd1252d947465c5c3ef16f70978a89af30508d0ccea04588bdafc"',
  'referer': 'https://www.zhihu.com/org/hua-wei-62-16/following',
  'x-ab-param': "li_price_test=1;pf_newguide_vertical=0;tp_qa_metacard=1;top_gr_ab=0;se_rewrite=0;top_rank=0;top_reason=1;tp_time_information=0;ug_newtag=0;zr_infinity_rec_num=close;tp_discussion_feed_type_android=2;tp_sft_v2= a;li_lt_tp_score=1;se_lottery=0;se_ltr_v002=0;se_new_topic=0;se_topicdirect=2;zr_km_slot_style=event_card;zr_km_answer=open_cvr;li_album_liutongab=0;se_ri=0;se_rr=0;se_search_feed=N;soc_update=1;pf_noti_entry_num=0;se_webmajorob=0;se_zu_recommend=0;top_recall_deep_user=1;li_qa_cover=old;top_ebook=0;top_ydyq=X;pf_feed=1;se_site_onebox=0;top_hotcommerce=1;top_vipconsume=1;se_featured=1;top_v_album=1;ug_follow_answerer_0=0;ug_zero_follow_0=0;li_mceb=0;li_tjys_ec_ab=0;qa_answerlist_ad=0;se_p_slideshow=0;tp_meta_card=0;li_se_ebook_chapter=1;pf_foltopic_usernum=50;se_likebutton=0;se_payconsult=0;top_root=0;li_ebook_detail=1;ls_fmp4=0;se_title_only=0;se_whitelist=0;tp_sft=a;soc_bignew=1;soc_special=0;top_test_4_liguangyi=1;li_se_intervene=1;li_ts_sample=old;pf_creator_card=1;se_backsearch=0;tp_top_sticky=0;tsp_childbillboard=1;se_famous=1;top_universalebook=1;tp_m_intro_re_topic=1;tp_sticky_android=0;zr_ans_rec=gbrank;qa_web_answerlist_ad=1;se_zu_onebox=0;soc_bigone=0;top_user_cluster=0;ug_goodcomment=0;se_amovietab=0;se_auto_syn=0;ug_follow_answerer=0;se_colorfultab=0;ug_fw_answ_aut_1=0;zr_ebook_chapter=0;li_hot_score_ab=0;se_expired_ob=0;se_ios_spb309=0;ug_follow_topic_1=2;li_album3_ab=0;pf_fuceng=1;se_preset_tech=0;se_wannasearch=0;se_webtimebox=0;se_movietab=0;se_terminate=0;tp_qa_toast=1;ug_goodcomment_0=0;qa_test=0;top_native_answer=1;top_recall_exp_v2=1;tp_header_style=1;li_filter_ttl=2;se_spb309=0;se_websearch=3;zr_se_footer=1;zr_art_rec=base;zr_video_rec_weight=close;top_recall_exp_v1=1;ug_zero_follow=0;zr_km_xgb_model=old;se_km_ad_locate=1;se_time_threshold=1.5;top_quality=0;se_subtext=0;se_ad_index=10;se_se_index=1;se_timebox_num=3;zr_rel_search=base;se_billboardsearch=0;se_page_limit_20=1;top_new_feed=5;tp_qa_metacard_top=top;tsp_lastread=0;se_agency= 0;se_webrs=1",
  'x-requested-with': "fetch",
  'x-zse-83': "3_2.0",
  'x-zse-84': "1LFqeT9ye_2xbLYqmTH0ge90r_FXFqSqYXYyrHuySMYpcTO0Z9O0Uvuyc7YxeHYy",
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'zhihu.middlewares.ZhihuSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'zhihu.middlewares.ZhihuDownloaderMiddleware': 543,
#}
DOWNLOADER_MIDDLEWARES = {
    'zhihu.middlewares.ProxyMiddleware': 543,
}
# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'zhihu.pipelines.ZhihuPipeline': 300,
}
# ITEM_PIPELINES = {
#   'scrapy_redis.pipelines.RedisPipeline': 400,
#   }

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

MONGODB_HOST = "192.168.1.104"
# MONGODB 端口号
MONGODB_PORT = 27017
# 数据库名称
MONGODB_DBNAME = "zhihu-redis"
# 存放数据的表名称
MONGODB_SHEETNAME = "userinfor_redis"


PROXIES = x


REDIS_HOST = '192.168.1.104'
REDIS_PORT = 6379
REDIS_ENCODING = 'utf-8'
# REDIS_PARAMS = {‘password’:’123456’}

# 使用scrapy-redis组件的去重队列（过滤）
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
# 使用scrapy-redis组件自己的调度器(核心代码共享调度器)
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
# 是否允许暂停
SCHEDULER_PERSIST = True

