from django.urls import path

from networks.apps import NetworksConfig
from networks.views import (NetworkNodeCreateAPIView,
                            NetworkNodeDestroyAPIView, NetworkNodeListAPIView,
                            NetworkNodeRetrieveAPIView,
                            NetworkNodeUpdateAPIView)

app_name = NetworksConfig.name

urlpatterns = [
    path("networks/", NetworkNodeListAPIView.as_view(), name="network_list"),
    path(
        "networks/<int:pk>/",
        NetworkNodeRetrieveAPIView.as_view(),
        name="network_detail",
    ),
    path("networks/create/", NetworkNodeCreateAPIView.as_view(), name="network_create"),
    path(
        "networks/update/<int:pk>/",
        NetworkNodeUpdateAPIView.as_view(),
        name="network_update",
    ),
    path(
        "networks/delete/<int:pk>/",
        NetworkNodeDestroyAPIView.as_view(),
        name="network_delete",
    ),
]
