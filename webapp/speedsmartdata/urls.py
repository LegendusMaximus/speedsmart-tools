from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("sortdown/",views.sortdown,name="sortdown"),
    path("sortup/",views.sortup,name="sortup"),
    path("fulllength/",views.fulllength,name="fulllength"),
    path("sorted/",views.sorted,name="sorted"),
    path("averages/",views.averages,name="averages"),
]