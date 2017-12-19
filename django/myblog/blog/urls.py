from django.conf.urls import url

from . import views

urlpatterns = [
    # url(r'^', views.blog),       # （正则）所有地址
    url(r'^index/$', views.index),
    # url(r'^article/(?P<article_id>[0-9]+)/$', views.article_page),
    url(r'^article/(?P<article_id>[0-9]+)/$', views.article_page, name='article_page')
]
