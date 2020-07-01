from django.urls import path
from .viewsets import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'shows', ShowSerializerViewSet, basename='SHOWS')
router.register(r'seasons', SeasonSerializerViewSet, basename='SEASONS')
router.register(r'episodes', EpisodeSerializerViewSet, basename='EPISODES')

urlpatterns = router.urls