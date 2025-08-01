from rest_framework.routers import SimpleRouter

from post import views

router = SimpleRouter()
router.register('posts', views.PostViewSet, basename='posts')
urlpatterns = router.urls
