from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import PostDetail, PostList, UserList, UserDetail, PostViewSet, UserViewSet
from rest_framework.schemas import get_schema_view

router = SimpleRouter()
router.register('posts', PostViewSet, basename='posts')
router.register('users', UserViewSet, basename='users')
urlpatterns = router.urls
