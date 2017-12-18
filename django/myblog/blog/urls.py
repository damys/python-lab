from django.conf.urls import url

from . import views

urlpatterns = [
    # url(r'^', views.index)       # （正则）所有地址
    url(r'^index/', views.index)
]
