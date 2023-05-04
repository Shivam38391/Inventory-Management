from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
 path("add-stock", views.add_stock, name="add-stock"),
 path("list-stock", views.add_stock, name="add-stock"),
  path('my-view/', views.ListView.as_view(), name='my_view')
 
] 