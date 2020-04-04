import scrapy
from wikiemploidutemps.items import WikiemploidutempsItem


class WikiemploidutempsSpider(scrapy.Spider):
    name = "wikiemploidutemps"
    allowed_domains = ["https://www.univ-lorraine.fr/"]
    start_urls = [
        "https://ent.univ-lorraine.fr/",
    ]

    def parse(self, response):
        for sel in response.xpath('//table[contains(@class, "wikitable")]//tr'):

            # On vérifie qu'il ne s'agit pas du header du tableau
            nomducours = sel.xpath('td[1]//text()').extract()
            if not nomducours:
                continue

            item = WikiemploidutempsItem()
            item['nomducours'] = "".join(nomducours)
            item['enseignant'] = "".join(sel.xpath('td[2]//text()').extract())
            item['horaire'] = "".join(sel.xpath('td[3]//text()').extract())
            item['salle'] = "".join(sel.xpath('td[4]//text()').extract())

            item.save()