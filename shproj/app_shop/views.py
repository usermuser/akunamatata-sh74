#! -*- coding:utf-8 -*-
from django.shortcuts import render
from app_shop.models import Product, Catalog

def index(request):
    latest_product_list = Product.objects.all().order_by('-name')#[:5]
    latest_catalog_list = Catalog.objects.all().order_by('-name')#[:5]
    context = {'latest_product_list': latest_product_list, 'latest_catalog_list':latest_catalog_list}
    return render(request, 'app_shop/index.html', context)



################################################################################
#def get_herofunc(request, heroname):                            #get_herofunc - функция перехватывает имя героя
#    try:
#        tryvar=Hero.objects.get(name=heroname)                  #пытается найти обьект с именем героя, которого перехватила функция
#    except Hero.DoesNotExist:                                   #исключения, если такого героя не существует
#        return HttpResponse('Героя с таким именем нет!')        #выводим страничку с ошибкой
#
#    return render_to_response('base.html',{'tryvar': tryvar})


#########################################################

#It’s a very common idiom to load a template, fill a context and return an HttpResponse object with the result of the rendered template.
#Django provides a shortcut. Here’s the full index() view, rewritten:

#from django.shortcuts import render

#from polls.models import Poll

#def index(request):
#    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
#    context = {'latest_poll_list': latest_poll_list}
#    return render(request, 'polls/index.html', context)
#Note that once we’ve done this in all these views, we no longer need to import loader, RequestContext and HttpResponse
#(you’ll want to keep HttpResponse if you still have the stub methods for detail, results, and vote).

#The render() function takes the request object as its first argument, a template name as its second argument and a dictionary as its optional third argument.
#It returns an HttpResponse object of the given template rendered with the given context."

#########################################################