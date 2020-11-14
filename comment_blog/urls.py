from django.urls import path 
from . import views 
from . views import PostView, PostUpdateView, PostDeleteView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('home/', views.blog_index, name = 'blog_index'),
    path('<int:pk>/', views.blog_detail, name = 'blog_detail') ,
    path('<category>/', views.blog_category, name = "blog_category"),
    path('', login_required(PostView.as_view()), name = "post_details"),
    path('<int:pk>/update/', login_required(PostUpdateView.as_view()), name = "post_update"),
    path('<int:pk>/delete/', login_required(PostDeleteView.as_view()), name = "post_delete"),
]
