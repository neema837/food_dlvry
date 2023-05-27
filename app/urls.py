from django.urls import path
from.import views

urlpatterns=[
    path('',views.index,name="index"),
    
    path('demoindex',views.demoindex,name="demoindex"),

]