from django.urls import path, include
from rest_framework.routers import DefaultRouter # default router가 기능이 많음, simple router는 기능이 적음
from .views import *

router = DefaultRouter()
router.register('', BookViewSet)

urlpatterns = [
    path('', include(router.urls)), 
]