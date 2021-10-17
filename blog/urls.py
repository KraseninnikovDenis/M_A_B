from django.urls import path
from . import views

urlpatterns=[

    path('', views.showeblog, name='showeblog'),
    path('<int:post_id>/', views.specific_post, name='specific'),

]