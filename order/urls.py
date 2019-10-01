from django.conf.urls import url
from order import views
from django.urls import path

app_name = 'order'
urlpatterns = [
    path('order_page/', views.OrderPage, name='order_page'),
    path('order/', views.createpost, name='createpost'),
    ]