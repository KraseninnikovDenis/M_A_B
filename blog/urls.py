from django.urls import path
from . import views

urlpatterns=[

    path('', views.showeblog, name='showeblog'),

]