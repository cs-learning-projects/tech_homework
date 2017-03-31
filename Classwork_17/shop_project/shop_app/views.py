from django.shortcuts import render
from shop_app.models import Visit
from django.db.models import Count
# Create your views here.


def index(request):
    if request.method == 'GET':
        # visit = Visit()
        # visit.url = '/some-url'
        # visit.save()
        # second option of the above code
        # Visit.objects.create(url='/some-url')
        # visits = Visit.objects.all() # возращает все визиты, которые были сделаны, передаем их в темлейт
        # return render(request, 'shop_app/index.html', {
        #     'visits' : visits,
        # })
        Visit.objects.create(url=request.path)
        # urls = Visit.objects.values('url').distinct().annotate(count=Count('id')).order_by('count').reverse()
        urls = Visit.objects.values('url').distinct().annotate(count=Count('id')).order_by('count')
        return render(request, 'shop_app/index.html', {'urls': urls}, )

