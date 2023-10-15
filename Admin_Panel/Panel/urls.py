from django.urls import path

from Panel.views import show_index_page, show_orders, show_employees, show_clients

urlpatterns = [
    path('', show_index_page, name='index'),
    path('orders/<str:status>/', show_orders, name='orders'),
    path('employees/<str:status>/', show_employees, name='employees'),
    path('clients/', show_clients, name='clients'),
]
