from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType
from store.models import Product
from tags.models import TaggedItem

def say_hello(request):
  conent_type = ContentType.objects.get_for_model(Product)

  queryset = TaggedItem.objects \
    .select_related('tag') \
    .filter(
      content_type=conent_type,
      object_id=1
    )

  return render(request, 'hello.html', {'name': 'Maximillian', 'tags': list(queryset)})
