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
from operator import itemgetter
from django.core.mail import send_mail
from django.utils.crypto import get_random_string

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

        id_usuario = datos_propiedad.get('id_usuario')

        guardados_actuales = Propiedad.objects.filter(id_usuario_id=id_usuario).count()
        tasaciones_actuales = Tasacion.objects.filter(id_usuario_id=id_usuario).count()

        usuario = Usuario.objects.get(id=id_usuario)
        plan = Plan.objects.filter(id=usuario.id_plan.id)

        tasaciones_plan = plan.get().tasaciones_maximas
        guardados_plan = plan.get().guardados_maximos

        if guardados_actuales > guardados_plan:
            return Response({'message': 'Guardados maximos de plan alcanzados'}, status=status.HTTP_406_NOT_ACCEPTABLE)
        if tasaciones_actuales > tasaciones_plan:
            return Response({'message': 'Tasaciones maximas de plan alcanzados'}, status=status.HTTP_406_NOT_ACCEPTABLE)

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

            id_usuario = propiedad.id_usuario_id

            tasaciones_actuales = Tasacion.objects.filter(id_usuario_id=id_usuario).count()

            usuario = Usuario.objects.get(id=id_usuario)
            plan = Plan.objects.filter(id=usuario.id_plan.id)

            tasaciones_plan = plan.get().tasaciones_maximas

            if tasaciones_actuales > tasaciones_plan:
                return Response({'message': 'Tasaciones maximas de plan alcanzadas'},
                                status=status.HTTP_406_NOT_ACCEPTABLE)

            datos_tasacion = calcular_datos_de_tasacion(propiedad)

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

        id_usuario = datos_propiedad.get('id_usuario')

        guardados_actuales = Propiedad.objects.filter(id_usuario_id=id_usuario).count()

        usuario = Usuario.objects.get(id=id_usuario)
        plan = Plan.objects.filter(id=usuario.id_plan.id)

        guardados_plan = plan.get().guardados_maximos

        if guardados_actuales > guardados_plan:
            return Response({'message': 'Guardados maximos de plan alcanzados'}, status=status.HTTP_406_NOT_ACCEPTABLE)

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

        ultima_tasacion_actual_max = ultima_tasacion_actual.precio * 1.2
        ultima_tasacion_actual_min = ultima_tasacion_actual.precio * 0.8

        propiedades = Propiedad.objects.filter(tasacion__precio__gte=ultima_tasacion_actual_min,
                                               tasacion__precio__lte=ultima_tasacion_actual_max)
        propiedades_filtradas = []
        distancias_propiedades = []
        # Calcular distancias y agregarlas a las propiedades
        for propiedad_bd in propiedades:
            distancia = calcular_distancia(propiedad_actual.get().latitud, propiedad_actual.get().longitud,
                                           propiedad_bd.latitud, propiedad_bd.longitud)

            ultima_tasacion_bd = Tasacion.objects.filter(id_propiedad=propiedad_bd.id).order_by("fecha_tasacion").last()

            if not ultima_tasacion_bd:
                break;

            propiedad_precio = armar_propiedad_precio(propiedad_bd, ultima_tasacion_bd.precio)

            serializer = PropiedadConPrecioSerializer(propiedad_precio,
                                                      context={'precio': ultima_tasacion_bd.precio})

            if 0 < distancia <= 2000:
                propiedades_filtradas.append(serializer.data)
                distancias_propiedades.append(round(distancia))

        if not propiedades_filtradas:
            return Response({'message': 'No existen propiedades similares'}, status=status.HTTP_404_NOT_FOUND)

        # Ordenar las propiedades y las distancias juntas
        propiedades_distancias_ordenadas = sorted(zip(propiedades_filtradas, distancias_propiedades), key=itemgetter(1))
        propiedades_ordenadas, distancias_ordenadas = zip(*propiedades_distancias_ordenadas)

        return Response(propiedades_ordenadas, status=status.HTTP_200_OK)


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


class CambioContraseñaMail(APIView):
    @staticmethod
    @swagger_auto_schema()
    def post(request, usuario_name):

        try:
            usuario = Usuario.objects.get(username=usuario_name)
            nueva_contrasena = get_random_string(length=15)  # Genera una nueva contraseña

            # Asigna la nueva contraseña al usuario
            usuario.set_password(nueva_contrasena)
            usuario.save()

            # Envia la nueva contraseña por correo
            send_mail(
                'Nueva contraseña',
                f'Tu nueva contraseña es: {nueva_contrasena}',
                'tasai.noreply@gmail.com',
                [usuario.email],
                fail_silently=False,
            )

            return Response({'message': 'Se ha generado una nueva contraseña y enviado al correo del usuario.'},
                            status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({'error': 'El usuario no existe'}, status=status.HTTP_404_NOT_FOUND)


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

    precio_x_localidad_actual = PrecioXLocalidad.objects.get(ciudad=propiedad.ciudad)
    if precio_x_localidad_actual:
        precio = precio_x_localidad_actual.precioxLocalidad
    else:
        precio = 1500

    propiedad_array = [propiedad.metros, propiedad.ambientes, propiedad.baños, propiedad.cochera, propiedad.dormitorios,
                       precio, propiedad.parrilla, propiedad.jardin,
                       propiedad.lavadero, propiedad.toilette, propiedad.AC, propiedad.balcon, propiedad.pileta]

    predict = modelo.predict([propiedad_array])
    predict = int(predict / 1000) * 1000
    return predict


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


def armar_propiedad_precio(propiedad, precio):
    propiedad_precio = {
        'id': propiedad.id,
        'id_usuario': propiedad.id_usuario,
        'calle': propiedad.calle,
        'numero': propiedad.numero,
        'ambientes': propiedad.ambientes,
        'baños': propiedad.baños,
        'dormitorios': propiedad.dormitorios,
        'pileta': propiedad.pileta,
        'parrilla': propiedad.parrilla,
        'jardin': propiedad.jardin,
        'latitud': propiedad.latitud,
        'longitud': propiedad.longitud,
        'esta_guardado': propiedad.esta_guardado,
        'metros': propiedad.metros,
        'cochera': propiedad.cochera,
        'ciudad': propiedad.ciudad,
        'toilette': propiedad.toilette,
        'lavadero': propiedad.lavadero,
        'AC': propiedad.AC,
        'balcon': propiedad.balcon,
        'precio': precio
    }

    return propiedad_precio
