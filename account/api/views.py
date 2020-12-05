from rest_framework import status, viewsets,generics,mixins
from rest_framework.response import Response
from account.models import Profile, Social, Job
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth.models import User
from knox.models import AuthToken
from django.contrib.auth import login
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView

from .serializers import (
    UserSerializer,
    RegisterSerializer,
    ViewProfileSerializer,
    CreateProfileSerializer,
    UpdateProfileSerializer,
    ViewSocialSerializer,
    CreateSocialSerializer,
    UpdateSocialSerializer,
    ViewJobSerializer,
    CreateJobSerializer,
    UpdateJobSerializer,
)


class LoginAPI(KnoxLoginView):
    permission_classes = (AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)


class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })

    def update(self, request, pk=None):
        pass


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ViewProfileSerializer
    lookup_field = 'user'
    permission_classes = [IsAuthenticated]
    action_serializers = {
        'create': CreateProfileSerializer,
        'update': UpdateProfileSerializer,
    }
    permission_classes_by_action = {
        'list': [AllowAny],
        'create': [AllowAny],
        'retrieve': [AllowAny],
        'update': [AllowAny],
        'destroy': [AllowAny],
    }

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def update(self, request, *args, **kwargs):
        profile = self.get_object()
        if profile.user.id != request.user.id:
            return Response({"detail": "Not allowed"})
        serializer = self.get_serializer(profile, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        profile = self.get_object()
        if profile.user.id != request.user.id:
            return Response({"detail": "Not allowed"})
        self.perform_destroy(profile)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_serializer_class(self):
        if hasattr(self, 'action_serializers'):
            return self.action_serializers.get(self.action, self.serializer_class)
        return super(ViewProfileSerializer, self).get_serializer_class()

    def get_permissions(self):
        try:
            # return permission_classes depending on `action`
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            # action is not set return default permission_classes
            return [permission() for permission in self.permission_classes]


class SocialViewSet(viewsets.ModelViewSet):
    queryset = Social.objects.all()
    serializer_class = ViewSocialSerializer
    lookup_field = 'user'
    permission_classes = [IsAuthenticated]
    action_serializers = {
        'create': CreateSocialSerializer,
        'update': UpdateSocialSerializer,
    }
    permission_classes_by_action = {
        'list': [AllowAny],
        'create': [AllowAny],
        'retrieve': [AllowAny],
        'update': [AllowAny],
        'destroy': [AllowAny],
    }

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def update(self, request, *args, **kwargs):
        social = self.get_object()
        if social.user.id != request.user.id:
            return Response({"detail": "Not allowed"})
        serializer = self.get_serializer(social, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        social = self.get_object()
        if social.user.id != request.user.id:
            return Response({"detail": "Not allowed"})
        self.perform_destroy(social)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_serializer_class(self):
        if hasattr(self, 'action_serializers'):
            return self.action_serializers.get(self.action, self.serializer_class)
        return super(ViewSocialSerializer, self).get_serializer_class()

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]


class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = ViewJobSerializer
    lookup_field = 'user'
    permission_classes = [IsAuthenticated]
    action_serializers = {
        'create': CreateJobSerializer,
        'update': UpdateJobSerializer,
    }
    permission_classes_by_action = {
        'list': [AllowAny],
        'create': [AllowAny],
        'retrieve': [AllowAny],
        'update': [AllowAny],
        'destroy': [AllowAny],
    }

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def update(self, request, *args, **kwargs):
        job = self.get_object()
        if job.user.id != request.user.id:
            return Response({"detail": "Not allowed"})
        serializer = self.get_serializer(job, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        job = self.get_object()
        if job.user.id != request.user.id:
            return Response({"detail": "Not allowed"})
        self.perform_destroy(job)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_serializer_class(self):
        if hasattr(self, 'action_serializers'):
            return self.action_serializers.get(self.action, self.serializer_class)
        return super(ViewJobSerializer, self).get_serializer_class()

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]


class UserViewSet(mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  viewsets.GenericViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    permission_classes_by_action = {
        'list': [AllowAny],
        'retrieve': [AllowAny],
        'update': [AllowAny],
        'destroy': [AllowAny],
    }

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.id != request.user.id:
            return Response({"detail": "Not allowed"})
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.id != request.user.id:
            return Response({"detail": "Not allowed"})
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]