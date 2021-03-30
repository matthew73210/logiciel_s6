from django.urls import path, include
from rest_framework import routers

from . import api
from . import views


router = routers.DefaultRouter()
router.register("procedure_s9", api.procedure_s9ViewSet)
router.register("chantier_se", api.chantier_seViewSet)
router.register("ttx", api.ttxViewSet)
router.register("personel", api.personelViewSet)
router.register("info_chantier", api.info_chantierViewSet)

urlpatterns = (
    path('', views.index, name="info_base_chantier"),
    path("api/v1/", include(router.urls)),
    path("info_base_chantier/procedure_s9/", views.procedure_s9ListView.as_view(), name="info_base_chantier_procedure_s9_list"),
    path("info_base_chantier/procedure_s9/create/", views.procedure_s9CreateView.as_view(), name="info_base_chantier_procedure_s9_create"),
    path("info_base_chantier/procedure_s9/detail/<int:pk>/", views.procedure_s9DetailView.as_view(), name="info_base_chantier_procedure_s9_detail"),
    path("info_base_chantier/procedure_s9/update/<int:pk>/", views.procedure_s9UpdateView.as_view(), name="info_base_chantier_procedure_s9_update"),
    path("info_base_chantier/chantier_se/", views.chantier_seListView.as_view(), name="info_base_chantier_chantier_se_list"),
    path("info_base_chantier/chantier_se/create/", views.chantier_seCreateView.as_view(), name="info_base_chantier_chantier_se_create"),
    path("info_base_chantier/chantier_se/detail/<int:pk>/", views.chantier_seDetailView.as_view(), name="info_base_chantier_chantier_se_detail"),
    path("info_base_chantier/chantier_se/update/<int:pk>/", views.chantier_seUpdateView.as_view(), name="info_base_chantier_chantier_se_update"),
    path("info_base_chantier/ttx/", views.ttxListView.as_view(), name="info_base_chantier_ttx_list"),
    path("info_base_chantier/ttx/create/", views.ttxCreateView.as_view(), name="info_base_chantier_ttx_create"),
    path("info_base_chantier/ttx/detail/<int:pk>/", views.ttxDetailView.as_view(), name="info_base_chantier_ttx_detail"),
    path("info_base_chantier/ttx/update/<int:pk>/", views.ttxUpdateView.as_view(), name="info_base_chantier_ttx_update"),
    path("info_base_chantier/personel/", views.personelListView.as_view(), name="info_base_chantier_personel_list"),
    path("info_base_chantier/personel/create/", views.personelCreateView.as_view(), name="info_base_chantier_personel_create"),
    path("info_base_chantier/personel/detail/<int:pk>/", views.personelDetailView.as_view(), name="info_base_chantier_personel_detail"),
    path("info_base_chantier/personel/update/<int:pk>/", views.personelUpdateView.as_view(), name="info_base_chantier_personel_update"),
    path("info_base_chantier/info_chantier/", views.info_chantierListView.as_view(), name="info_base_chantier_info_chantier_list"),
    path("info_base_chantier/info_chantier/create/", views.info_chantierCreateView.as_view(), name="info_base_chantier_info_chantier_create"),
    path("info_base_chantier/info_chantier/detail/<int:pk>/", views.info_chantierDetailView.as_view(), name="info_base_chantier_info_chantier_detail"),
    path("info_base_chantier/info_chantier/update/<int:pk>/", views.info_chantierUpdateView.as_view(), name="info_base_chantier_info_chantier_update"),
)
