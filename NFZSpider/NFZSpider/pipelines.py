# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class NfzspiderPipeline(object):
    def process_item(self, item, spider):
        return 'http://kolejki.nfz.gov.pl/Informator/PobierzPlikXLS?term='+item
