from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('product/', ProductViewset)


urlpatterns = [
    path('data_values/',HomeData.as_view()),
    path('update_data_values',UpdateData.as_view()),
    path('',include(router.urls)),

]