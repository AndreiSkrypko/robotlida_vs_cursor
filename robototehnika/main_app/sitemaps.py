# sitemaps.py

from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return [
            'index',
            'about',
            'contacts',
            'courses_online',
            'courses_2_4',
            'courses_4_6',
            'courses_6_7',
            'courses_7_9',
            'courses_9_11',
            'courses_11_13',
            'courses_13_16',
            'about_cookies',
        ]

    def location(self, item):
        return reverse(item)