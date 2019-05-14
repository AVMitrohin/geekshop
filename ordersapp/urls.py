from django.conf.urls import url
import ordersapp.views as ordersapp

app_name = 'ordersapp'

urlpatterns = [
    url(r'^$', ordersapp.OrderList.as_view(), name='index'),
    url(r'^order/create/$', ordersapp.OrderItemsCreate.as_view(), name='order_create'),
]
