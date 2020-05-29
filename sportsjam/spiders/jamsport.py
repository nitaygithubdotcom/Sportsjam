# -*- coding: utf-8 -*-
import scrapy


class JamsportSpider(scrapy.Spider):
    name = 'jamsport'
    # allowed_domains = ['https://www.sportsjam.in/buy-dri-fit-t-shirts-online-india?PageNo=2']
    start_urls = ['https://www.sportsjam.in/buy-dri-fit-t-shirts-online-india?PageNo=2/']

    def parse(self, response):
        # print(response.xpath('//div[@class="loadmore bucketgroup"]//div[@class="bucket_left"]'))
        namexp = '(//div[@class="loadmore bucketgroup"]//div[@class="bucket_left"])[{}]/h4/text()'
        prepricexp = '(//div[@class="loadmore bucketgroup"]//div[@class="bucket_left"])[{}]/div[@class="price"]/span/label[@class="mtb-mrp"]/span[@class="sp_amt"]/text()'
        disxp = '(//div[@class="loadmore bucketgroup"]//div[@class="bucket_left"])[{}]/div[@class="dis"]/text()'
        curpricexp = '(//div[@class="loadmore bucketgroup"]//div[@class="bucket_left"])[{}]/div[@class="price"]/span/label[@class="mtb-ofr"]/span[@class="sp_amt"]/text()'
        for i in range(len(response.xpath('(//div[@class="loadmore bucketgroup"]//div[@class="bucket_left"])'))):
            namexpath = namexp.format(i+1)
            prepricexpath = prepricexp.format(i+1)
            disxpath = disxp.format(i+1)
            curpricexpath = curpricexp.format(i+1)
            name = response.xpath(namexpath).get()
            preprice = response.xpath(prepricexpath).get()
            discount = response.xpath(disxpath).get()
            curprice = response.xpath(curpricexpath).get()
            yield {name:[curprice,discount,preprice]}
