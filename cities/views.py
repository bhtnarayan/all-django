from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
# Create your views here.
from django.db.models import Q
from . models import City 
# import asyncio

class HomePageView(TemplateView):
    template_name = 'home.html'

# async def my_view(request):
#     await asyncio.sleep(3)
#     return HttpResponse('Hello World This is for waiting time.') 

class SearchResultView(ListView):
    model = City 
    template_name = 'search_results.html'
    # queryset = City.objects.filter(name__icontains = 'Butwal')

    # def get_queryset(self):
    #     return City.objects.filter(name__icontains = 'Kathmandu')


    # def get_queryset(self):
    #     return City.objects.filter(
    #         Q(name__icontains = 'Kathmandu') | Q(state__icontains = 'Lumbini')
    #     )

    def get_queryset(self):
        query = self.request.GET.get('query')
        object_list = City.objects.filter(
            Q(name__icontains = query) | Q(state__icontains = query) 
        )
        return object_list 