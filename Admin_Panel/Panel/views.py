from django.shortcuts import render
from Panel.models import *
from django.db.models import Sum
from django.utils import timezone
from datetime import timedelta


# Create your views here.
def show_index_page(request):
    stock_objects = Stock.objects.all()
    bootle_count = 0
    for stock in stock_objects:
        bootle_count += stock.quantity

    orders_not_delivered = Order.objects.exclude(order_status='Delivered').count()
    orders_delivered = Order.objects.filter(order_status='Delivered').count()
    clients = Client.objects.all().count()

    today = timezone.now().date()

    start_of_week = today - timedelta(days=today.weekday())
    end_of_week = start_of_week + timedelta(days=6)

    start_of_month = today.replace(day=1)
    end_of_month = start_of_month.replace(month=start_of_month.month % 12 + 1) - timedelta(days=1)

    revenue_day = Order.objects.filter(order_date=today, order_status='Delivered').aggregate(Sum('items__price'))[
                      'items__price__sum'] or 0
    revenue_week = \
        Order.objects.filter(order_date__range=[start_of_week, end_of_week], order_status='Delivered').aggregate(
            Sum('items__price'))['items__price__sum'] or 0

    revenue_month = \
        Order.objects.filter(order_date__range=[start_of_month, end_of_month], order_status='Delivered').aggregate(
            Sum('items__price'))['items__price__sum'] or 0

    context = {'bootle_count': bootle_count, 'orders_not_delivered': orders_not_delivered,
               'orders_delivered': orders_delivered, 'clients': clients, 'revenue_day': revenue_day,
               'revenue_week': revenue_week, 'revenue_month': revenue_month}
    return render(request, 'Panel/index.html', context=context)


def show_orders(request, status):
    if status == 'Delivered':
        orders = Order.objects.filter(order_status='Delivered')
    else:
        orders = Order.objects.exclude(order_status='Delivered')
    return render(request, 'Panel/orders.html', context={'orders': orders})


def show_employees(request, status):
    if status == 'True':
        employees = Employee.objects.filter(is_available=True)
    else:
        employees = Employee.objects.exclude(is_available=True)
    return render(request, 'Panel/employees.html', context={'employees': employees})


def show_clients(request):
    clients = Client.objects.all()
    return render(request, 'Panel/clients.html', context={'clients': clients})
