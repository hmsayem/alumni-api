from rest_framework import serializers
from account.models import Profile, Social, Job
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('user', 'image', 'faculty', 'department', 'roll', 'batch', 'passing_year', 'resume')


class SocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Social
        fields = ('user', 'facebook', 'linkedin', 'github', 'instagram', 'website')


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ('user', 'title', 'company', 'start_date', 'end_date')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            self.validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email = validated_data['email'],
            password=validated_data['password']
        )
        return user
