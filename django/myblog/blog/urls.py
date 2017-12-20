from django.conf.urls import url

from . import views

urlpatterns = [
    # （正则）所有地址
    # url(r'^', views.blog),
    url(r'^index/$', views.index, name='index'),
    # url(r'^article/(?P<article_id>[0-9]+)/$', views.article_page),
    url(r'^article/(?P<article_id>[0-9]+)/$', views.article_page, name='article_page'),

    # add edit
    # url(r'^edit/$', views.edit_page, name='edit_page'),

    # add edit article_id
    url(r'^edit/(?P<article_id>[0-9]+)/$', views.edit_page, name='edit_page'),
    url(r'^edit/action$', views.edit_action, name='edit_action')
]
