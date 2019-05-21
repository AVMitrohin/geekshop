from django.conf.urls import url
import ordersapp.views as ordersapp

app_name = 'ordersapp'

urlpatterns = [
    url(r'^$', ordersapp.OrderList.as_view(), name='index'),
    url(r'^order/create/$', ordersapp.OrderItemsCreate.as_view(), name='order_create'),
    url(r'^forming/complete/(?P<pk>\d+)/$', ordersapp.order_forming_complete, name='order_forming_complete'),
    url(r'^read/(?P<pk>\d+)/$', ordersapp.OrderRead.as_view(), name='order_read'),
    url(r'^update/(?P<pk>\d+)/$', ordersapp.OrderItemsUpdate.as_view(), name='order_update'),
    url(r'^delete/(?P<pk>\d+)/$', ordersapp.OrderItemsDelete.as_view(), name='order_delete'),
]
