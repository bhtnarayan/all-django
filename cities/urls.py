from django.urls import path 
from . import views 
from . views import HomePageView, SearchResultView


urlpatterns = [
    # path('home/', views.my_view, name = 'myView'),
    path('home/', HomePageView.as_view(), name = 'home'),
    path('search/', SearchResultView.as_view(), name = 'search_result'),
]