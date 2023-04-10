from django.shortcuts import render
from django.db.models import Value, F, Func, Count
from django.db.models.functions import Concat
from store.models import Product, Order, Customer

# Create your views here.
# request --> HttpResponse
# request handler 
# action

def say_hello(request):
  # queryset = Customer.objects.annotate(
  #   full_name = Func(F('first_name'), Value(' '), F('last_name'), function='CONCAT')
  # )
  # queryset = Customer.objects.annotate(
  #   full_name = Concat('first_name', Value(' '), 'last_name')
  # )
  queryset = Customer.objects.annotate(
    orders_count=Count('order')
  )

  return render(request, 'hello.html', {'name': 'Maximillian', 'result': list(queryset)})
