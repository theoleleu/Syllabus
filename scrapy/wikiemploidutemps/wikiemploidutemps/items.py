# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

from scrapy_djangoitem import DjangoItem
from emploidutemps.models import Emploidutemps

class WikiemploidutempsItem(DjangoItem):
    django_model = Emploidutemps
