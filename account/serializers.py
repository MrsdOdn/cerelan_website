from django.contrib.auth.models import update_last_login
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework_simplejwt.serializers import TokenObtainSerializer
from rest_framework_simplejwt.settings import api_settings
from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken
from rest_framework_simplejwt.tokens import UntypedToken, RefreshToken

from account.models import MyUser
from ceralan_website import settings


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = MyUser(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            phone_number=validated_data['phone_number']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        password = validated_data.get('password', None)
        if password:
            instance.set_password(password)
        instance.save()
        return instance


class TokenVerifySerializer(serializers.Serializer):
    token = serializers.CharField()

    def validate(self, attrs):
        token = attrs.get("token")

        # Tokenin payload'ını al
        token_payload = UntypedToken(token).payload

        # Payload içindeki user_id'yi al
        user_id = token_payload.get('user_id')

        if not user_id:
            raise ValidationError("Invalid token: Missing user_id")

        # user_id ile kullanıcıyı sorgula
        try:
            user = MyUser.objects.get(id=user_id)
        except MyUser.DoesNotExist:
            raise ValidationError("User not found for the provided token")

        # Tokenin blacklist olup olmadığını kontrol et
        if api_settings.BLACKLIST_AFTER_ROTATION and "rest_framework_simplejwt.token_blacklist" in settings.INSTALLED_APPS:
            jti = token_payload.get(api_settings.JTI_CLAIM)
            if BlacklistedToken.objects.filter(token__jti=jti).exists():
                raise ValidationError("Token is blacklisted")

        data = {'token': attrs['token']}
        data['data'] = UserSerializer(user, context={'request': self.context.get('request')}).data
        return data


class TokenObtainPairSerializer(TokenObtainSerializer):
    token_class = RefreshToken

    def validate(self, attrs):
        data = super().validate(attrs)

        refresh = self.get_token(self.user)
        response = {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
            "isAdmin": self.user.is_superuser,
            # isAdmin değerini kullanıcının süper kullanıcı olup olmadığına göre belirleyin
            "id": self.user.id,
        }
        data['data'] = response

        if api_settings.UPDATE_LAST_LOGIN:
            update_last_login(None, self.user)

        return data


class TokenRefreshSerializer(serializers.Serializer):
    refresh = serializers.CharField()
    access = serializers.CharField(read_only=True)
    token_class = RefreshToken

    def validate(self, attrs):
        refresh = self.token_class(attrs["refresh"])

        data = {"access": str(refresh.access_token)}

        if api_settings.ROTATE_REFRESH_TOKENS:
            if api_settings.BLACKLIST_AFTER_ROTATION:
                try:
                    refresh.blacklist()
                except AttributeError:
                    pass

            refresh.set_jti()
            refresh.set_exp()
            refresh.set_iat()

            data["refresh"] = str(refresh)

        return data
