# -*- coding: utf-8 -*-

# Scrapy settings for rvt project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'rvt'

SPIDER_MODULES = ['rvt.spiders']
NEWSPIDER_MODULE = 'rvt.spiders'

ITEM_PIPELINES = [
        'rvt.pipelines.RVTPipeline'
]

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'rvt (+http://www.yourdomain.com)'

DOWNLOADER_MIDDLEWARES = {
    'rvt.middlewares.ProxyMiddleware': 100,
    'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 750,
}

HTTP_PROXY = "http://162.216.155.136:8089"
