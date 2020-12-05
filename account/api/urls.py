from django.urls import path, include
from knox import views as knox_views
from rest_framework.routers import DefaultRouter
from account.api.views import (
    UserViewSet,
    ProfileViewSet,
    JobViewSet,
    SocialViewSet,
    RegisterAPI,
    LoginAPI
)

app_name = 'account'

account_router = DefaultRouter()
account_router.register('user', UserViewSet, basename='user')
account_router.register('profile', ProfileViewSet, basename='profile')
account_router.register('job', JobViewSet, basename='job')
account_router.register('social', SocialViewSet, basename='social')

urlpatterns = [

    path('', include(account_router.urls)),
    path('<int:user>', include(account_router.urls)),
    path('', include(account_router.urls)),
    path('<int:user>', include(account_router.urls)),
    path('register', RegisterAPI.as_view(), name='register'),
    path('login/', LoginAPI.as_view(), name='login'),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
]
