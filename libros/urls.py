from django.urls import path
from . import views

urlpatterns = [
    path('', views.libro_list_create_api_view, name='libro-list-create'),
    path('<int:pk>/', views.libro_detail_api_view, name='libro-detail'),
]