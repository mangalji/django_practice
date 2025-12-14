from django.urls import path
from . import views

# now if anyone use localhost:8000/chai he saw the all_chai.html page
urlpatterns = [
    path('',views.all_chai, name='all_chai'),
]