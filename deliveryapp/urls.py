from django.urls import path
from.import views

urlpatterns=[
    path('dlogin',views.adlogin,name="dlogin"),
    path('dsignup',views.adsignup,name="dsignup"),
    
]