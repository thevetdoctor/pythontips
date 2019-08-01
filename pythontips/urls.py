from django.conf.urls import  url
from . import views

urlpatterns = [
    url('home', views.index, name='index'),
    url('load', views.loadTips, name='loadTips'),
    # url('<int:tip_id>', views.showTip, name='showTip'),
    url('', views.showTip, name='showTip'),
    url('<int:tip_id>', views.showTipLinks, name='showTipLinks'),
]
