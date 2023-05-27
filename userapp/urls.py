from django.urls import path
from.import views

urlpatterns=[
    path('login',views.login,name="login"),
    path('signup',views.signup,name="signup"),
    path('verification',views.verification,name="verification"),
    path('userhome',views.userhome,name="userhome"),
    path('restdetails<int:rid>',views.restdetails,name="restdetails"),
    path('increment_quantity<int:cart_id>',views.increment_quantity,name="increment_quantity"),
    path('decrement_quantity<int:cart_id>',views.decrement_quantity,name="decrement_quantity"),
    path('checkout',views.checkout,name="checkout"),
    
]