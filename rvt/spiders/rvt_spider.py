import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor

from rvt.items import RVItem


def get_text_nl(selector):
    result = ""
    for chunk in selector.xpath('text() | br'):
        result += chunk.extract().replace('<br>', '\n')
    return result.strip('\n')


class RVTSpider(CrawlSpider):

    name = "rvt"
    allowed_domains = ["rvt.com"]
    start_urls = [
        "http://www.rvt.com/New-and-Used-Foretravel-Motorcoach-RVs-For-Sale-On-RVT.com/results?manu=Foretravel+Motorcoach&searchtype=browse",
    ]

    rules = [
        Rule(
            LinkExtractor(
                restrict_xpaths='//li[@itemtype="http://schema.org/Product"]',
                deny=('pop-up-login\.php',
                      'contact_seller_pop\.php',
                      'rv-video\.php',
                      'results\?manu')
            ),
            callback="parse_item"
        ),
    ]

    def parse_start_url(self, response):
        nxt = response.xpath('//ul[@class="p-nation"]//a[@rel="next"]/@href').extract()
        if nxt:
            yield scrapy.Request(nxt[0])

    def parse_item(self, response):
        item = RVItem()
        item['url'] = response.url
        # Parse header
        header = response.xpath('//h1[@itemprop="name"]')
        year = header.xpath('text()').re(r"(\d+)")
        if year:
            item['year'] = year[0]
        item['model'] = header.xpath('span[@itemprop="model"]/text()').re(r"(.+)\sfor\ssale")[0]
        item['price'] = response.xpath('//span[@class="rvd-price"]/text()').re(r"\$([\d,]+)")[0]
        # Parse detail block 1
        detail_01 = response.xpath('//div[@class="detail-01"]')
        phones = detail_01.xpath('.//div[@class="rvd-phone"]/text()').re(r"([\d-]+)")
        if phones:
            item['phone1'] = phones[0]
        main_photo = detail_01.xpath('.//a[@class="main-photo"]/@href').extract()
        if main_photo:
            item['main_photo'] = "http://www.rvt.com/" + main_photo[0]
        item['photos'] = []
        for photo in detail_01.xpath('div[@class="rv-photos"]//a[@rel="view-photos"]/@href'):
            item['photos'].append("http://www.rvt.com/" + photo.extract())
        info_01 = detail_01.xpath('div[@class="rv-info-01"]')
        contact_person = info_01.xpath('a[@class="dealer-logo"]/img/@alt').re(r"More\sListings\sfrom\s(.+)")
        if contact_person:
            item['contact_person'] = contact_person[0]
        item['address'] = get_text_nl(info_01.xpath('address'))
        # Parse detail block 2
        detail_02 = response.xpath('//div[@class="detail-02"]')
        item['description'] = get_text_nl(detail_02.xpath('div[@itemprop="description"]'))
        info_02 = detail_02.xpath('div[@class="rv-info-02"]')
        item['product_uid'] = info_02.xpath('.//span[@class="rv-item-data"]/text()').extract()[2]
        item['length'] = info_02.xpath('.//span[@class="rv-item-data"]/text()').extract()[6]
        yield item
