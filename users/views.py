from rest_framework import generics, status, generics, permissions
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.contrib.auth import get_user_model
from .serializers import UserCreateSerializer, UserUpdateSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from decimal import Decimal
from django.db import transaction
User = get_user_model()

class UserCreateAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserCreateSerializer(user, context=self.get_serializer_context()).data,
            "message": "Usuario creado exitosamente"
        }, status=status.HTTP_201_CREATED)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_profile(request):
    user = request.user
    return Response({
        "nombre": user.nombre,
        "email": user.email,
        "fecha_nacimiento": user.fecha_nacimiento,
        "carnet": user.carnet,
        "balance": user.balance,  # ← agregado
    })
class UserUpdateAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = UserUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

@api_view(['POST'])
@permission_classes([IsAuthenticated])
@transaction.atomic
def recargar_balance(request):
    user = request.user
    try:
        monto = Decimal(str(request.data.get("monto", 0)))

        if monto <= 0:
            return Response({"error": "El monto debe ser mayor a cero."}, status=status.HTTP_400_BAD_REQUEST)

        user.balance += monto
        user.save()

        return Response({
            "mensaje": f"Recarga exitosa de {monto} USDT.",
            "nuevo_balance": float(user.balance)
        }, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)