from django.shortcuts import render
from django.db.models import Value, F
from store.models import Product, Order, Customer

# Create your views here.
# request --> HttpResponse
# request handler 
# action

def say_hello(request):
  queryset = Customer.objects.annotate(new_id=F('id') + 1)

  return render(request, 'hello.html', {'name': 'Maximillian', 'result': list(queryset)})
