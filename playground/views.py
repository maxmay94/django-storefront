from django.shortcuts import render
from django.db.models.aggregates import Count, Max, Min, Sum, Avg
from store.models import Product, Order

# Create your views here.
# request --> HttpResponse
# request handler 
# action

def say_hello(request):
  # queryset = Product.objects.prefetch_related('promotions').select_related('collection').all()
  result = Product.objects.filter(collection_id=3).aggregate(count = Count('id'),min_price=Min('unit_price'), max_price=Max('unit_price'), avg_price=Avg('unit_price'))

  return render(request, 'hello.html', {'name': 'Maximillian', 'result': result})
