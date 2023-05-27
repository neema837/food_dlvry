from django.urls import path
from.import views

urlpatterns=[
    path('reslogin',views.reslogin,name="reslogin"),
    path('ressignup',views.ressignup,name="ressignup"),
    path('resthome',views.resthome,name="resthome"),
    path('addmenu',views.addmenu,name="addmenu"),
    path('addcat',views.addcat,name="addcat"),
    path('newitem',views.newitem,name="newitem"),
    path('editmenu<int:pid>',views.editmenu,name="editmenu"),
   
    path('updatemenu<int:uid>',views.updatemenu,name="updatemenu"),
    path('deletemenu<int:did>',views.deletemenu,name="deletemenu"),
    path('restorder',views.restorder,name="restorder"),
    path('restfill',views.restfill,name="restfill"),
]