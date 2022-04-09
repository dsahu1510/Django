from django.shortcuts import render
from django.db.models import Q

# Create your views here.
from django.views.generic import TemplateView, ListView

from .models import City


class HomePageView(TemplateView):
    template_name = 'home.html'

# class SearchResultsView(ListView):
#     model = City
#     template_name = 'search_results.html'

class SearchResultsView(ListView):
    model = City
    template_name = 'search_results.html'
    # queryset = City.objects.filter(name__icontains='Boston') # new

    def get_queryset(self): # new
        query = self.request.GET.get('q')
        objects_list =  City.objects.filter(
            Q(name__icontains=query) | Q(state__icontains=query)
            )
        return objects_list