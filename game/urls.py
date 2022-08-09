from django.urls import path
from django.conf.urls import include
from . import views
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register('scenes',SceneViewSet)


urlpatterns = [
    path('api/',include(router.urls)),
    path('', views.index, name='index'),
]
