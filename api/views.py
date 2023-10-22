from datetime import datetime

from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from .serializer import *
from .models import *
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import update_session_auth_hash
from sklearn.ensemble import RandomForestRegressor
import joblib
import math

modelo = joblib.load("forest_model.joblib")


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


class PlanViewSet(viewsets.ModelViewSet):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer


class PropiedadViewSet(viewsets.ModelViewSet):
    queryset = Propiedad.objects.all()
    serializer_class = PropiedadSerializer


class TasacionViewSet(viewsets.ModelViewSet):
    queryset = Tasacion.objects.all()
    serializer_class = TasacionSerializer


class ActualizarPlan(APIView):
    @staticmethod
    @swagger_auto_schema(request_body=IdPlanSerializer)
    def patch(request, user_id):
        try:
            usuario = Usuario.objects.get(id=user_id)
            plan = Plan.objects.get(id=request.data.get('id_plan'))
            usuario.id_plan = plan
            usuario.save()
            # serializer = UsuarioSerializer(usuario)
            return Response(status=status.HTTP_200_OK)
        except Usuario.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except Plan.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class EstaGuardadoPropiedad(APIView):
    @staticmethod
    @swagger_auto_schema(request_body=IdPropiedadSerializer)
    def patch(request, id_propiedad):
        try:
            propiedad = Propiedad.objects.get(id=id_propiedad)
            esta_guardado = request.data.get('esta_guardado')
            propiedad.esta_guardado = esta_guardado
            propiedad.save()
            return Response(status=status.HTTP_200_OK)
        except Propiedad.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class EstaGuardadoTasacion(APIView):
    @staticmethod
    @swagger_auto_schema(request_body=IdTasacionSerializer)
    def patch(request, id_tasacion):
        try:
            tasacion = Tasacion.objects.get(id=id_tasacion)
            esta_guardado = request.data.get('esta_guardado')
            tasacion.esta_guardado = esta_guardado
            tasacion.save()
            return Response(status=status.HTTP_200_OK)
        except Propiedad.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class TasacionConPropiedadNueva(APIView):
    @staticmethod
    @swagger_auto_schema(request_body=PropiedadSerializer)
    def post(request):

        datos_propiedad = request.data

        propiedad_serializer = PropiedadSerializer(data=datos_propiedad)
        if propiedad_serializer.is_valid():
            propiedad = propiedad_serializer.save()
        else:
            return Response(propiedad_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        datos_tasacion = calcular_datos_de_tasacion(propiedad)

        tasacion_serializer = TasacionSerializer(data=datos_tasacion)
        if tasacion_serializer.is_valid():
            tasacion = tasacion_serializer.save()
            return Response(TasacionSerializer(tasacion).data, status=status.HTTP_201_CREATED)
        else:
            return Response(tasacion_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TasacionConPropiedadExistente(APIView):
    @staticmethod
    @swagger_auto_schema()
    def post(request, propiedad_id):
        try:
            propiedad = Propiedad.objects.get(id=propiedad_id)

            datos_tasacion = calcular_datos_de_tasacion(propiedad)
            print(datos_tasacion)

            tasacion_serializer = TasacionSerializer(data=datos_tasacion)
            if tasacion_serializer.is_valid():
                tasacion = tasacion_serializer.save()
                return Response(TasacionSerializer(tasacion).data, status=status.HTTP_201_CREATED)
            else:
                return Response(tasacion_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Propiedad.DoesNotExist:
            return Response({'message': 'La propiedad no existe'}, status=status.HTTP_404_NOT_FOUND)


class GuardarPropiedad(APIView):
    @staticmethod
    @swagger_auto_schema(request_body=PropiedadSerializer)
    def post(request):

        datos_propiedad = request.data

        propiedad_serializer = PropiedadSerializer(data=datos_propiedad)
        if propiedad_serializer.is_valid():
            propiedad_serializer.save()
            return Response(propiedad_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(propiedad_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetAllPropiedades(APIView):
    @staticmethod
    @swagger_auto_schema()
    def get(request, user_id):
        propiedades = Propiedad.objects.filter(id_usuario=user_id)

        serializer = PropiedadSerializer(propiedades, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class GetPropiedadesSimilares(APIView):
    @staticmethod
    @swagger_auto_schema()
    def get(request, propiedad_id):
        propiedad_actual = Propiedad.objects.filter(id=propiedad_id)
        ultima_tasacion_actual = Tasacion.objects.filter(id_propiedad=propiedad_id).order_by("fecha_tasacion").last()

        ultima_tasacion_actual_max = ultima_tasacion_actual.precio * 1.1
        ultima_tasacion_actual_min = ultima_tasacion_actual.precio * 0.9

        propiedades = Propiedad.objects.filter(tasacion__precio__gte=ultima_tasacion_actual_min,
                                               tasacion__precio__lte=ultima_tasacion_actual_max)
        propiedades_filtradas = []
        # Calcular distancias y agregarlas a las propiedades
        for propiedad_bd in propiedades:
            distancia = calcular_distancia(propiedad_actual.get().latitud, propiedad_actual.get().longitud,
                                           propiedad_bd.latitud, propiedad_bd.longitud)

            ultima_tasacion_bd = Tasacion.objects.filter(id_propiedad=propiedad_bd.id).order_by("fecha_tasacion").last()

            if not ultima_tasacion_bd:
                break;

            if (0 < distancia <= 600):
                propiedades_filtradas.append(propiedad_bd)

        if not propiedades_filtradas:
            return Response({'message': 'No existen propiedades similares'}, status=status.HTTP_404_NOT_FOUND)

        serializer = PropiedadSerializer(propiedades_filtradas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class GetOnePropiedad(APIView):
    @staticmethod
    @swagger_auto_schema()
    def get(request, propiedad_id):
        try:
            propiedad = Propiedad.objects.get(id=propiedad_id)
            serializer = PropiedadSerializer(propiedad)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Propiedad.DoesNotExist:
            return Response({'message': 'La propiedad no existe'}, status=status.HTTP_404_NOT_FOUND)


class TasacionesDeUsuario(APIView):
    @staticmethod
    @swagger_auto_schema()
    def get(request, user_id):
        tasaciones = Tasacion.objects.filter(id_usuario=user_id)
        serializer = TasacionSerializer(tasaciones, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class RegistroUsuario(APIView):
    @staticmethod
    @swagger_auto_schema(request_body=RegistroUsuarioSerializer)
    def post(request):
        serializer = RegistroUsuarioSerializer(data=request.data)
        if serializer.is_valid():
            usuario = serializer.save()
            response_data = {
                'message': 'Registro exitoso',
                'user_id': usuario.id
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class IniciarSesion(APIView):
    @staticmethod
    @swagger_auto_schema(request_body=InicioSesionSerializer)
    def post(request):
        serializer = InicioSesionSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key, 'id_usuario': user.id, 'id_plan': user.id_plan.id},
                            status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CambiarContraseña(APIView):
    @swagger_auto_schema(request_body=CambiarContraseñaSerializer)
    def post(self, request):
        serializer = CambiarContraseñaSerializer(data=request.data)
        if serializer.is_valid():
            user = self.request.user
            contraseña_actual = serializer.validated_data['contraseña_actual']
            nueva_contraseña = serializer.validated_data['nueva_contraseña']
            confirmar_contraseña = serializer.validated_data['confirmar_contraseña']

            if user.check_password(contraseña_actual) and nueva_contraseña == confirmar_contraseña:
                user.set_password(nueva_contraseña)
                user.save()
                # Actualizar la sesión de autenticación para evitar que el usuario sea desconectado
                update_session_auth_hash(self.request, user)
                return Response({'message': 'Contraseña cambiada con éxito'}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Contraseña actual incorrecta o no coincide con la nueva contraseña'},
                                status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def calcular_datos_de_tasacion(propiedad):
    datos_tasacion = {
        'id_propiedad': propiedad.id,
        'id_usuario': propiedad.id_usuario_id,
        'fecha_tasacion': datetime.now(),
        'precio': calcular_valor_tasacion(propiedad),
    }
    return datos_tasacion


def calcular_valor_tasacion(propiedad):
    # var = [200, 6, 3, 0, 4, 1478, 0, 0, 0, 0, 0, 0, 0]
    propiedad_array = [propiedad.metros, propiedad.ambientes, propiedad.baños, propiedad.cochera, propiedad.dormitorios,
                       propiedad.precioxLocalidad, propiedad.parrilla, propiedad.jardin, propiedad.lavadero,
                       propiedad.toilette, propiedad.AC, propiedad.balcon, propiedad.pileta]

    predict = modelo.predict([propiedad_array])
    predict = int(predict/1000)*1000
    return predict
    #return round(predict[0],0)
    # return 300000


def calcular_distancia(lat1, lon1, lat2, lon2):
    # Fórmula de distancia haversine
    radius = 6371000  # Radio de la Tierra en Metros
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = (math.sin(dlat / 2) ** 2) + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * (
            math.sin(dlon / 2) ** 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distancia = radius * c
    return distancia
