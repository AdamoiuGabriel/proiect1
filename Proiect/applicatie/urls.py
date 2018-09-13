from django.conf.urls import url
from django.urls import path, re_path

from . import views

app_name = 'applicatie'

urlpatterns = [
    re_path('^$', views.utilizatori_list, name='product_list'),
    #url(r'produs/', views.product_detail, name='product_details')
    #url(r'^(?P<categoryid>\d+)/$', views.product_list, name='product_list_by_category'),
    #url(r'^(?P<productid>\d+)/$', views.product_detail, name='product_detail'),
]
