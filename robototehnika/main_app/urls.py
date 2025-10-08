from django.urls import path
from . import views
from django.contrib.sitemaps.views import sitemap
from .sitemaps import StaticViewSitemap

sitemaps = {
    'static': StaticViewSitemap,
}

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('courses_online/', views.courses_online, name='courses_online'),
    path('courses_2_4/', views.courses_2_4, name='courses_2_4'),
    path('courses_4_6/', views.courses_4_6, name='courses_4_6'),
    path('courses_6_7/', views.courses_6_7, name='courses_6_7'),
    path('courses_7_9/', views.courses_7_9, name='courses_7_9'),
    path('courses_9_11/', views.courses_9_11, name='courses_9_11'),
    path('courses_11_13/', views.courses_11_13, name='courses_11_13'),
    path('courses_13_16/', views.courses_13_16, name='courses_13_16'),
    path('about-cookies/', views.about_cookies, name='about_cookies'),

    # Карта сайта в самом конце
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]
