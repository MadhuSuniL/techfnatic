from django.urls import path
from .views import Registration,Login,AdminList,SendInvitation
from rest_framework_simplejwt.views import TokenRefreshView
urlpatterns = [
    path('register',Registration.as_view()),    
    path('login',Login.as_view())   , 
    path('refresh',TokenRefreshView.as_view())   , 
    path('admins/',AdminList.as_view())   , 
    path('invite',SendInvitation.as_view())   , 
]