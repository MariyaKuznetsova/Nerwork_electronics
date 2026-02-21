from django.http import HttpResponseForbidden
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from networks.models import NetworkNode
from networks.serializers import NetworkNodeSerializer
from users.permissions import IsActiveEmployee


class NetworkNodeCreateAPIView(generics.CreateAPIView):
    """Контроллер по созданию звена"""

    serializer_class = NetworkNodeSerializer
    permission_classes = (IsAuthenticated, IsActiveEmployee)

    def get(self, request):
        return HttpResponseForbidden({"message": "Только для активных сотрудников"})


class NetworkNodeListAPIView(generics.ListAPIView):
    """Контроллер по выводу списка звеньев"""

    serializer_class = NetworkNodeSerializer
    permission_classes = (IsAuthenticated, IsActiveEmployee)
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["country"]

    def get(self, request):
        return HttpResponseForbidden({"message": "Только для активных сотрудников"})


class NetworkNodeRetrieveAPIView(generics.RetrieveAPIView):
    """Контроллер по выводу звена"""

    serializer_class = NetworkNodeSerializer
    queryset = NetworkNode.objects.all()
    permission_classes = (IsAuthenticated, IsActiveEmployee)

    def get(self, request):
        return HttpResponseForbidden({"message": "Только для активных сотрудников"})


class NetworkNodeUpdateAPIView(generics.UpdateAPIView):
    """Контроллер по редактированию звена"""

    serializer_class = NetworkNodeSerializer
    queryset = NetworkNode.objects.all()
    permission_classes = (IsAuthenticated, IsActiveEmployee)

    def get(self, request):
        return HttpResponseForbidden({"message": "Только для активных сотрудников"})


class NetworkNodeDestroyAPIView(generics.DestroyAPIView):
    """Контроллер по удаления звена"""

    serializer_class = NetworkNodeSerializer
    permission_classes = (IsAuthenticated, IsActiveEmployee)
    queryset = NetworkNode.objects.all()

    def get(self, request):
        return HttpResponseForbidden({"message": "Только для активных сотрудников"})
