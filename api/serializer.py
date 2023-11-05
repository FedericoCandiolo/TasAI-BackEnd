from rest_framework import serializers
from .models import *
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate


class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = '__all__'


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'


class PropiedadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Propiedad
        fields = '__all__'


class PrecioXlocalidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrecioXLocalidad
        fields = '__all__'


class TasacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasacion
        fields = '__all__'


User = get_user_model()


class RegistroUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class CambiarContraseñaSerializer(serializers.Serializer):
    contraseña_actual = serializers.CharField(write_only=True)
    nueva_contraseña = serializers.CharField(write_only=True)
    confirmar_contraseña = serializers.CharField(write_only=True)


class InicioSesionSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        user = authenticate(username=username, password=password)
        if user and user.is_active:
            return user
        raise serializers.ValidationError('Credenciales inválidas')


class IdPlanSerializer(serializers.Serializer):
    id_plan = serializers.IntegerField()


class IdPropiedadSerializer(serializers.Serializer):
    esta_guardado = serializers.BooleanField()


class IdTasacionSerializer(serializers.Serializer):
    esta_guardado = serializers.BooleanField()


class PropiedadConPrecioSerializer(serializers.ModelSerializer):
    precio = serializers.IntegerField()

    class Meta:
        model = Propiedad
        fields = '__all__'

    def to_representation(self, instance):
        # Obtenemos la representación de los datos según el serializer base
        representation = super(PropiedadConPrecioSerializer, self).to_representation(instance)

        # Agregamos el campo extra al final de la representación
        representation['precio'] = self.context.get('precio', 0)

        return representation
