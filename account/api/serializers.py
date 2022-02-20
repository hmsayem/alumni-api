from rest_framework import serializers
from account.models import Profile, Social, Job
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email')
        extra_kwargs = {'username': {'required': False}}

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
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user


class ViewProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('user', 'about', 'image', 'faculty', 'department', 'roll', 'batch', 'passing_year', 'resume')


class CreateProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('user', 'image', 'about', 'faculty', 'department', 'roll', 'batch', 'passing_year', 'resume')
        extra_kwargs = {'user': {'required': False}}


class UpdateProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('user', 'image', 'about', 'faculty', 'department', 'roll', 'batch', 'passing_year', 'resume')
        extra_kwargs = {'faculty': {'required': False}, 'department': {'required': False}, 'passing_year': {'required': False},}
        read_only_fields = ['user']


class ViewSocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Social
        fields = ('user', 'facebook', 'linkedin', 'github', 'instagram', 'website')


class CreateSocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Social
        fields = ('user', 'facebook', 'linkedin', 'github', 'instagram', 'website')
        extra_kwargs = {'user': {'required': False}}


class UpdateSocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Social
        fields = ('user', 'facebook', 'linkedin', 'github', 'instagram', 'website')
        read_only_fields = ['user']


class ViewJobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ('user', 'title', 'company', 'start_date', 'end_date')


class CreateJobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ('user', 'title', 'company', 'start_date', 'end_date')
        extra_kwargs = {'user': {'required': False}}


class UpdateJobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ('user', 'title', 'company', 'start_date', 'end_date')
        extra_kwargs = {'title': {'required': False}, 'company': {'required': False}, 'start_date': {'required': False},}
        read_only_fields = ['user']
