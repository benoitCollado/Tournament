from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views
app_name = 'blog'
urlpatterns = [
  path('', views.IndexView.as_view(), name='index'),
  path('<int:pk>/', login_required(views.DetailView.as_view()), name='detail'),
  #path('int:pk/edit/', views.EditView.as_view(), name='edit'),
]