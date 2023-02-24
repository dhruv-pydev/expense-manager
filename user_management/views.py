from rest_framework import views
from rest_framework import status
from rest_framework import viewsets
from rest_framework import response
from rest_framework import exceptions

from rest_framework.authtoken import views as auth_views
from rest_framework.authtoken import models as auth_models

from user_management import models as user_management_models
from user_management import serializers as user_management_serializers


class LoginView(auth_views.ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data,
            context={'request': request}
        )

        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, _ = auth_models.Token.objects.get_or_create(user=user)
        data = {"token": token.key}
        return response.Response(
            data=data,
            status=status.HTTP_200_OK
        )


class LogoutView(views.APIView):

    def get(self, request, format=None):
        request.user.auth_token.delete()
        return response.Response(status=status.HTTP_205_RESET_CONTENT)

    def post(self, request, format=None):
        return self.get(request, format=format)


class MainUserViewSet(viewsets.ModelViewSet):
    queryset = user_management_models.MainUser.objects.all()
    serializer_class = user_management_serializers.MainUserSerializer
