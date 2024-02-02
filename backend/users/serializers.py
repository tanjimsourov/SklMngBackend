from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from users.models import User
from users.otp import generateKey


class SuperUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=128, min_length=6, write_only=True)

    class Meta:
        model = User
        fields = ('username', 'phone', 'password', 'token')
        read_only_fields = ['token']

    def create(self, validated_data):
        return User.objects.create_superuser(**validated_data)


class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=128, min_length=6, write_only=True)

    class Meta:
        model = User
        fields = ('email', 'password', 'username', 'token')

        read_only_fields = ['token']


class AddStaffSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=128, min_length=6, write_only=True)

    class Meta:
        model = User
        fields = (
            'username', 'email', 'phone', 'gender', 'nidNumber', 'is_active', 'is_admin',
            'is_staff', 'is_verified', 'profilePic', 'nidPic'
                                                     'password', 'fullName')

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class UserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class AddTeacherSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=128, min_length=6, write_only=True)

    class Meta:
        model = User
        fields = ('username', 'profilePic', 'fullName', 'location', 'phone', 'gender',
                  'nidNumber', 'nidPic', 'is_verified', 'teacherDesignation', 'is_teacher',
                  'fname', 'mname', 'dob', 'password')

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
