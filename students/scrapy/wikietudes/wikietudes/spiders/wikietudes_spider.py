
import scrapy
from wikietudes.items import WikietudesItem


class WikibeerSpider(scrapy.Spider):
    name = "wikietudes"
    allowed_domains = ["wikidocs.univ-lorraine.fr"]
    start_urls = [
        "https://wikidocs.univ-lorraine.fr/display/minesnancyficm",
    ]

    def parse(self, response):
        for sel in response.xpath('//table[contains(@class, "wikitable")]//tr'):

            # On vérifie qu'il ne s'agit pas du header du tableau
            cours = sel.xpath('td[1]//text()').extract()
            if not cours:
                continue

            item = WikietudesItem()
            item['cours'] = "".join(cours)
            item['enseignant'] = "".join(sel.xpath('td[2]//text()').extract())
            item['duree'] = "".join(sel.xpath('td[3]//text()').extract())
            item['ects'] = "".join(sel.xpath('td[4]//text()').extract())
            item['prerequis'] = "".join(sel.xpath('td[5]//text()').extract())
            item['objectif'] = "".join(sel.xpath('td[6]//text()').extract())
            item['description'] = "".join(sel.xpath('td[7]//text()').extract())
            item['evaluation'] = "".join(sel.xpath('td[8]//text()').extract())

            item.save()