from scrapy import Spider
from scrapy.selector import Selector

from ..items import AresscrapeGPU, Review
from scrapy.http import Request



class NeweggGPUSpider(Spider):
    name = "newegggpu"
    allowed_domains = ['newegg.com']
    start_urls = [
        "http://www.newegg.com/Desktop-Graphics-Cards/SubCategory/ID-48/Page-%s?Tid=7709&PageSize=36&order=BESTSELLING"
        % page for page in range(5, 20)
    ]
    visitedURLs = set()

    def parse(self, response):
        products = response.xpath('//div[@class = "item-container   "]')
        for product in products:
            item = AresscrapeGPU()
            item['url'] = product.xpath('div[@class = "item-info"]/a/@href').extract()[0]
            name = product.xpath('div[@class = "item-info"]/a/text()').extract()[0]
            if 'Refurbished' in name or 'Open Box' in name:
                continue
            item['name'] = name

            prevprice = product.xpath('div[@class = "item-info"]/div[@class = "item-action"]/ul/li[@class = "price-was"]/span/text()').extract()
            intprice = product.xpath('div[@class = "item-info"]/div[@class = "item-action"]/ul/li[@class = "price-current"]/strong/text()').extract()
            centprice = product.xpath('div[@class = "item-info"]/div[@class = "item-action"]/ul/li[@class = "price-current"]/sup/text()').extract()
            # if price isnt found, skip the item.
            if not intprice:
                item['price'] = prevprice[0]
            else:
                item['price'] = intprice[0] + centprice[0]
            rating = product.xpath('div[@class = "item-info"]/div[@class = "item-branding"]/a/@title').extract()
            if rating == []:
                item['rating'] = 'None'
            else:
                item['rating'] = rating[0].split('+')[1].strip()

            urls = [product.xpath('div[@class = "item-info"]/a/@href').extract()[0]]
            for url in urls:
                if url not in self.visitedURLs:
                    request = Request(url, callback=self.boardproductpage)
                    request.meta['item'] = item
                    yield request

    def boardproductpage(self, response):

        specs = Selector(response).xpath('//*[@id="Specs"]/fieldset')
        itemdict = {}

        for i in specs:
            test = i.xpath('dl')
            for t in test:
                name = t.xpath('dt/text()').extract()
                if name == []:
                    name = t.xpath('dt/a/text()').extract()
                itemdict[name[0]] = t.xpath('dd/text()').extract()[0]
        item = response.meta['item']
        if 'Chipset Manufacturer' not in itemdict:
            yield None
        else:
            item['brand'] = itemdict['Brand'].strip()
            item['model'] = itemdict['Model'].strip()
            item['socket'] = str(itemdict.get('Chipset Manufacturer', None)).strip()
            #check reviews

            rev = Selector(response).xpath('//div[@class = "comments-cell has-side-left is-active"]')
            reviews = []
            for r in rev:

                rating = r.xpath('div[@class = "comments-cell-body"]/div[@class = "comments-cell-body-inner"]/div[@class = "comments-title"]/div[@itemprop = "reviewRating"]/span[1]/text()').extract()
                rating = rating[0]
                date = r.xpath('div[@class = "comments-cell-body"]/div[@class = "comments-cell-body-inner"]/div[@class = "comments-title"]/span[@class = "comments-text comments-time comments-time-right"]/text()').extract()
                if not date == '' or not date == []:
                    date = date[0].split()[0]
                else:
                    date = 'null'

                comment = r.xpath('div[@class = "comments-cell-body"]/div[@class = "comments-cell-body-inner"]/div[@class = "comments-cell-body"]/div[@class = "comments-cell-body-inner"]/div[@class = "comments-content"]/p')
                pros = ''
                cons = ''
                pros_other = ''
                for com in comment:
                    strong_text = com.xpath('strong/text()').extract()
                    if strong_text[0] == 'Pros:':
                        text = com.xpath('text()').extract()
                        for t in text:
                            t = t.strip()
                            if t != '':
                                pros += '. ' + t
                                pros_other += '. ' + t
                        pros.rstrip()
                    if strong_text[0] == 'Cons:':
                        text = com.xpath('text()').extract()
                        for t in text:
                            t = t.strip()
                            if t != '':
                                cons += '. ' + t

                        cons.rstrip()

                    if strong_text[0] == 'Other Thoughts:':
                        text = com.xpath('text()').extract()
                        for t in text:
                            t = t.strip()
                            if t != '':
                                pros_other+= '. ' + t

                        pros_other.rstrip()

                re_item = Review()
                re_item['cons'] = cons
                re_item['pros'] = pros
                re_item['others'] = pros_other
                re_item['rating'] = rating
                re_item['date'] = date
                reviews.append(re_item)
            item['reviews'] = reviews
            yield item
