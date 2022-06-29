from django.urls import path, include
from rest_framework.routers import DefaultRouter
import ware.views

router = DefaultRouter()
router.register('ware', ware.views.WareViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
