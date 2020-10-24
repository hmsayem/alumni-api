from django.urls import path, include
from knox import views as knox_views
from rest_framework.routers import DefaultRouter
from account.api.views import (

    ProfileViewSet,
    JobViewSet,
    SocialViewSet,
    RegisterAPI,
    LoginAPI
)

app_name = 'account'

profile_router = DefaultRouter()
profile_router.register('profile', ProfileViewSet, basename='profile')

job_router = DefaultRouter()
job_router.register('job', JobViewSet, basename='job')

social_router = DefaultRouter()
social_router.register('social', SocialViewSet, basename='social')

urlpatterns = [

    path('', include(profile_router.urls)),
    path('<int:user>', include(profile_router.urls)),
    path('', include(job_router.urls)),
    path('<int:user>', include(job_router.urls)),
    path('', include(social_router.urls)),
    path('<int:user>', include(social_router.urls)),
    path('register', RegisterAPI.as_view(), name='register'),
    path('login/', LoginAPI.as_view(), name='login'),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
]
