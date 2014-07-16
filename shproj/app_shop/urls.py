from django.conf.urls import patterns, url

from app_shop import views

urlpatterns = patterns('',
    #url(r'^$', shop_main_page_function, name='shop_main_page_function')
    url(r'^$', views.index, name='index'),
)