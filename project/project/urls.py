
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from post_app.views import PostViewSet

router = DefaultRouter()
router.register("posts", PostViewSet, basename="posts")

urlpatterns = [
    path('admin/', admin.site.urls),
    path("auth/", include("auth_app.urls")),
    path("api/", include(router.urls)),
]
