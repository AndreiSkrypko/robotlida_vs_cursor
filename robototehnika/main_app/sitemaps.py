# sitemaps.py

from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticViewSitemap(Sitemap):
    """
    Расширенная карта сайта с приоритетами для SEO оптимизации
    Главная и страницы курсов имеют высокий приоритет для лучшей индексации
    """
    
    # Приоритеты и частота обновлений для каждой страницы
    priorities = {
        'index': 1.0,  # Главная страница - максимальный приоритет
        'about': 0.8,  # О нас - высокий приоритет
        'courses_2_4': 0.9,  # Страницы курсов - очень высокий приоритет
        'courses_4_6': 0.9,
        'courses_6_7': 0.9,
        'courses_7_9': 0.9,
        'courses_9_11': 0.9,
        'courses_11_13': 0.9,
        'courses_13_16': 0.9,
        'courses_online': 0.8,
        'about_cookies': 0.3,  # Технические страницы - низкий приоритет
    }
    
    changefreqs = {
        'index': 'daily',  # Главная обновляется часто
        'about': 'weekly',
        'courses_2_4': 'weekly',
        'courses_4_6': 'weekly',
        'courses_6_7': 'weekly',
        'courses_7_9': 'weekly',
        'courses_9_11': 'weekly',
        'courses_11_13': 'weekly',
        'courses_13_16': 'weekly',
        'courses_online': 'weekly',
        'about_cookies': 'yearly',
    }

    def items(self):
        """Все страницы сайта для карты"""
        return [
            'index',
            'about',
            'courses_2_4',
            'courses_4_6',
            'courses_6_7',
            'courses_7_9',
            'courses_9_11',
            'courses_11_13',
            'courses_13_16',
            'courses_online',
            'about_cookies',
        ]

    def location(self, item):
        """URL страницы"""
        return reverse(item)
    
    def priority(self, item):
        """Динамический приоритет для каждой страницы"""
        return self.priorities.get(item, 0.5)
    
    def changefreq(self, item):
        """Динамическая частота изменений"""
        return self.changefreqs.get(item, 'monthly')