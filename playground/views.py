from django.shortcuts import render
from django.db import transaction, connection
from django.contrib.contenttypes.models import ContentType
from store.models import Product, Order, OrderItem, Collection
from tags.models import TaggedItem

def say_hello(request):
  with connection.cursor() as cursor:
    cursor.callproc('get_customers', [1,2,'a'])

  return render(request, 'hello.html', {'name': 'Maximillian', 'result': list(queryset)})
