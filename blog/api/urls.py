from django.urls import path, include
from rest_framework.routers import DefaultRouter
from blog.api.views import (
    BlogViewSet,
    blog_like_view,
)

app_name = 'blog'

blog_router = DefaultRouter()
blog_router.register('post', BlogViewSet, basename='post')

urlpatterns = [
    path('', include(blog_router.urls)),
    path('<int:user>/', include(blog_router.urls)),
    path('like/<int:pk>/', blog_like_view, name='like_post'),
]
