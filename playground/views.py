from django.shortcuts import render
from store.models import Product, Order

# Create your views here.
# request --> HttpResponse
# request handler 
# action

def say_hello(request):
  # queryset = Product.objects.prefetch_related('promotions').select_related('collection').all()

  queryset = Order.objects.select_related('customer').prefetch_related('orderitem_set__product').order_by('-placed_at')[:5]
  return render(request, 'hello.html', {'name': 'Maximillian', 'orders' : list(queryset)})
