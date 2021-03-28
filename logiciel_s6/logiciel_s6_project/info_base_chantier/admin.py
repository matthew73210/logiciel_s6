from django.contrib import admin
from django import forms

from . import models


class procedure_s9AdminForm(forms.ModelForm):

    class Meta:
        model = models.procedure_s9
        fields = "__all__"


class procedure_s9Admin(admin.ModelAdmin):
    form = procedure_s9AdminForm
    list_display = [
        "N_prog_jour",
        "nom_phase",
        "trx_nuit",
        "DFV",
        "continuite_elec",
        "created",
        "active",
        "h_fin",
        "date_debut_trx",
        "pk_fin",
        "Ct_Tx",
        "etat_surface_rail",
        "pk_debut",
        "h_debut",
        "GEq",
        "RCT",
        "indice_CtTx",
        "Voie",
        "last_updated",
    ]
    readonly_fields = [
        "N_prog_jour",
        "nom_phase",
        "trx_nuit",
        "DFV",
        "continuite_elec",
        "created",
        "active",
        "h_fin",
        "date_debut_trx",
        "pk_fin",
        "Ct_Tx",
        "etat_surface_rail",
        "pk_debut",
        "h_debut",
        "GEq",
        "RCT",
        "indice_CtTx",
        "Voie",
        "last_updated",
    ]


class chantier_seAdminForm(forms.ModelForm):

    class Meta:
        model = models.chantier_se
        fields = "__all__"


class chantier_seAdmin(admin.ModelAdmin):
    form = chantier_seAdminForm
    list_display = [
        "created",
        "pk_depose_debut",
        "pk_depose_fin",
        "last_updated",
    ]
    readonly_fields = [
        "created",
        "pk_depose_debut",
        "pk_depose_fin",
        "last_updated",
    ]


class ttxAdminForm(forms.ModelForm):

    class Meta:
        model = models.ttx
        fields = "__all__"


class ttxAdmin(admin.ModelAdmin):
    form = ttxAdminForm
    list_display = [
        "last_updated",
        "pk_fin",
        "fonction",
        "pk_deput",
        "nom_ttx",
        "created",
        "pk_engagment",
        "pk_degagment",
    ]
    readonly_fields = [
        "last_updated",
        "pk_fin",
        "fonction",
        "pk_deput",
        "nom_ttx",
        "created",
        "pk_engagment",
        "pk_degagment",
    ]


class personelAdminForm(forms.ModelForm):

    class Meta:
        model = models.personel
        fields = "__all__"


class personelAdmin(admin.ModelAdmin):
    form = personelAdminForm
    list_display = [
        "created",
        "telephone",
        "prenom",
        "last_updated",
        "habilitation",
        "nom",
        "date_depart",
        "date_arrive",
        "fonction",
    ]
    readonly_fields = [
        "created",
        "telephone",
        "prenom",
        "last_updated",
        "habilitation",
        "nom",
        "date_depart",
        "date_arrive",
        "fonction",
    ]


class info_chantierAdminForm(forms.ModelForm):

    class Meta:
        model = models.info_chantier
        fields = "__all__"


class info_chantierAdmin(admin.ModelAdmin):
    form = info_chantierAdminForm
    list_display = [
        "numero_ligne",
        "nbr_voies_travail",
        "created",
        "last_updated",
        "date_debut_chantier",
        "date_fin_chantier",
    ]
    readonly_fields = [
        "numero_ligne",
        "nbr_voies_travail",
        "created",
        "last_updated",
        "date_debut_chantier",
        "date_fin_chantier",
    ]


admin.site.register(models.procedure_s9, procedure_s9Admin)
admin.site.register(models.chantier_se, chantier_seAdmin)
admin.site.register(models.ttx, ttxAdmin)
admin.site.register(models.personel, personelAdmin)
admin.site.register(models.info_chantier, info_chantierAdmin)
