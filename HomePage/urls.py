from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [ 
    path('', views.home_page),
    path('info', views.explore),
    # path('all-analytics', views.all_analytics),
    # # path('short_url',views.analy),

    
    # path('<slug:short_url>', views.redirect_url)
]
