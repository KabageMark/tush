from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url(r'^$',views.home_page,name = 'home'),
    url(r'^shop/$',views.shop_page,name = 'shop'),
    url(r'^add/(\d+)/',views.add_to_cart,name='add'),
    url(r'^cart/',views.cart,name='cart'),
    url(r'^remove/(\d+)',views.delete_cart,name='delete'),
    url(r'^empty',views.empty,name='empty'),
    url(r'^pay',views.mobile_checkout,name='m-pesa')

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)