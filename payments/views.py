from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication

from payments.models import Compra

class SolicitarCompraAPIView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def post(self, request):
        url_producto = request.data.get("url")
        if not url_producto:
            return Response({"error": "La URL del producto es requerida"}, status=status.HTTP_400_BAD_REQUEST)

        user = request.user

        Compra.objects.create(usuario=user, url_producto=url_producto)

        return Response({"message": f"Compra solicitada para el producto: {url_producto} por el usuario {user.email}"}, status=status.HTTP_200_OK)
