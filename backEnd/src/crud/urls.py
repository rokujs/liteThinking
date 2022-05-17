from django.urls import path
from . import views

urlpatterns = [
  path('', views.start, name='start'),
  path('api', views.enterprise_api, name='enterprise_api'),
  path('api/<int:id>', views.enterprise_api, name='enterprise_api'),
  ]