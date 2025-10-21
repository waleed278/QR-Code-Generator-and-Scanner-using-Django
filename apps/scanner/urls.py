from . import views
from django.urls import path

urlpatterns = [
    path('',views.home,name='home'),
    path('scanqr/',views.Scanner,name='scanqr'),
    path('generateqr/',views.Generate,name='generateqr'),
]