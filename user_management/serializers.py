from rest_framework import exceptions
from rest_framework import serializers

from django.contrib.auth import models as auth_models

from user_management import models


class UserSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(required=False, allow_null=True)
    last_name = serializers.CharField(required=False, allow_null=True)
    email = serializers.EmailField(required=False)
    password = serializers.CharField(required=False)

    class Meta:
        model = auth_models.User
        fields = "__all__"


class MainUserSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(required=False, allow_null=True)
    last_name = serializers.CharField(required=False, allow_null=True)
    username = serializers.CharField(required=False, allow_null=False)
    email = serializers.EmailField(required=False, allow_null=False)
    password = serializers.CharField(
        required=False,
        write_only=True,
        allow_null=False
    )
    contact_number = serializers.CharField(required=False)

    class Meta:
        model = models.MainUser
        exclude = ["user", "created_at"]
        read_only_fields = ["id", ]

    def validate(self, attrs):
        password = attrs.get("password", None)
        email = attrs.get("email", None)

        if not self.instance:
            if not password:
                raise exceptions.ValidationError({
                    "password": "This field is required"
                })

            if not email:
                raise exceptions.ValidationError({
                    "email": "This field is required"
                })

        return super().validate(attrs)

    def create(self, validated_data):
        user_data = {
            "first_name": validated_data.pop("first_name"),
            "last_name": validated_data.pop("last_name"),
            "username": validated_data.pop("username"),
            "email": validated_data.pop("email"),
        }

        user_serializer = UserSerializer(data=user_data)
        if user_serializer.is_valid():
            user = user_serializer.save()
            user.set_password(validated_data.pop("password"))
            user.save()

            validated_data["user"] = user
            return super().create(validated_data)

        else:
            raise serializers.ValidationError(user_serializer.errors)

    def update(self, instance, validated_data):
        first_name = validated_data.pop("first_name", instance.first_name)
        last_name = validated_data.pop("last_name", instance.last_name)
        username = validated_data.pop("username", instance.username)
        email = validated_data.pop("email", instance.email)
        password = validated_data.pop("password", None)

        user_data = {
            "first_name": first_name,
            "last_name": last_name,
            "username": username,
            "email": email,
        }

        user_serializer = UserSerializer(
            instance=instance.user,
            data=user_data,
            partial=True
        )

        if user_serializer.is_valid():
            user = user_serializer.save()
            if password:
                user.set_password(password)
                user.save()
            validated_data["user"] = user
        else:
            raise serializers.ValidationError(user_serializer.errors)
        return super().update(instance, validated_data)
