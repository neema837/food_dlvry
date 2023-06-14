from django.urls import path
from.import views

urlpatterns=[
    path('login',views.login,name="login"),
    path('ulogout',views.ulogout,name="ulogout"),
    path('signup',views.signup,name="signup"),
    path('verification',views.verification,name="verification"),
    path('userhome',views.userhome,name="userhome"),
    path('restdetails<int:rid>',views.restdetails,name="restdetails"),
    path('increment_quantity<int:cart_id>',views.increment_quantity,name="increment_quantity"),
    path('decrement_quantity<int:cart_id>',views.decrement_quantity,name="decrement_quantity"),
    path('checkout',views.checkout,name="checkout"),
    path('order_complete',views.order_complete,name="order_complete"),
    path('increment_quantit<int:cart_id>',views.increment_quantit,name="increment_quantit"),
    path('decrement_quantit<int:cart_id>',views.decrement_quantit,name="decrement_quantit"),
    path('useraddress',views.useraddress,name="useraddress"),
]