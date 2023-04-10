from django.shortcuts import render
from store.models import Product

# Create your views here.
# request --> HttpResponse
# request handler 
# action

def say_hello(request):
  queryset = Product.objects.prefetch_related('promotions').all()
  return render(request, 'hello.html', {'name': 'Maximillian', 'products' : list(queryset)})
