# -*- coding: utf-8 -*-
import scrapy


class QueuespiderSpider(scrapy.Spider):
    name = "QueueSpider"
    allowed_domains = ["http://kolejki.nfz.gov.pl"]
    start_urls = (
        'http://kolejki.nfz.gov.pl/Informator/PobierzDane/Index/',
    )

    def parse(self, response):
            hash_list = response.xpath('//span[contains(@class, "hashcode")]/text()').extract()
            yield({'hash_list':hash_list})
            pass
