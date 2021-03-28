from rest_framework import viewsets, permissions

from . import serializers
from . import models


class procedure_s9ViewSet(viewsets.ModelViewSet):
    """ViewSet for the procedure_s9 class"""

    queryset = models.procedure_s9.objects.all()
    serializer_class = serializers.procedure_s9Serializer
    permission_classes = [permissions.IsAuthenticated]


class chantier_seViewSet(viewsets.ModelViewSet):
    """ViewSet for the chantier_se class"""

    queryset = models.chantier_se.objects.all()
    serializer_class = serializers.chantier_seSerializer
    permission_classes = [permissions.IsAuthenticated]


class ttxViewSet(viewsets.ModelViewSet):
    """ViewSet for the ttx class"""

    queryset = models.ttx.objects.all()
    serializer_class = serializers.ttxSerializer
    permission_classes = [permissions.IsAuthenticated]


class personelViewSet(viewsets.ModelViewSet):
    """ViewSet for the personel class"""

    queryset = models.personel.objects.all()
    serializer_class = serializers.personelSerializer
    permission_classes = [permissions.IsAuthenticated]


class info_chantierViewSet(viewsets.ModelViewSet):
    """ViewSet for the info_chantier class"""

    queryset = models.info_chantier.objects.all()
    serializer_class = serializers.info_chantierSerializer
    permission_classes = [permissions.IsAuthenticated]
