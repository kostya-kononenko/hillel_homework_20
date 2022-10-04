from site_drf.views import UserViewSet, PostViewSet, CommentViewSet

from django.urls import path, include
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'users', UserViewSet, basename="user")
router.register(r'posts', PostViewSet, basename="post")
router.register(r'comments', CommentViewSet, basename="comment")

urlpatterns = [
    path('', include(router.urls)),
]
