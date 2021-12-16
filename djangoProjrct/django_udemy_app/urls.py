from django.urls import path
from django.urls.resolvers import URLPattern
from django_udemy_app.views import index 

urlpatterns=[
    path('',index,name='index'),
    path('index/',index,name="indexpost")
]