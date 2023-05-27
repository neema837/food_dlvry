from django.urls import path
from.import views

urlpatterns=[
    path('adlogin',views.adlogin,name="adlogin"),
    path('adsignup',views.adsignup,name="adsignup"),
    path('adminhome',views.adminhome,name="adminhome"),
    path('viewdel',views.viewdel,name="viewdel"),
    path('send_email<int:id>',views.send_email,name="send_email"),
    path('delapprove<int:id>',views.delapprove,name="delapprove"),
    path('viewrest',views.viewrest,name="viewrest"),
    path('send_restemail<int:id>',views.send_restemail,name="send_restemail"),
    path('restapprove<int:id>',views.restapprove,name="restapprove"),
]