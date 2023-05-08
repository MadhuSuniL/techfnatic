from .views import *
from django.urls import path


urlpatterns = [
    path('', Home, name='home'),
    path('cus_admin', AdminPage, name='admin'),
    path('add_product',AddProduct,name='add_product'),
    path('delete_product/<int:pk>',ProductDelete,name='delete_product'),
    path('update_intro',UpdateIntro,name='intro'),
    path('update_introsub',UpdateIntroSub,name='introsub'),
    path('update_about',UpdateAbout,name='about'),
    path('update_email',UpdateEmail,name='email'),
    path('update_address',UpdateAddress,name='address'),
]