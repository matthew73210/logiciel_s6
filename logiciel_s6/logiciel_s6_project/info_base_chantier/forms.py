from django import forms
from . import models


class procedure_s9Form(forms.ModelForm):
    class Meta:
        model = models.procedure_s9
        fields = [
            "N_prog_jour",
            "nom_phase",
            "trx_nuit",
            "DFV",
            "continuite_elec",
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
        ]


class chantier_seForm(forms.ModelForm):
    class Meta:
        model = models.chantier_se
        fields = [
            "pk_depose_debut",
            "pk_depose_fin",
        ]


class ttxForm(forms.ModelForm):
    class Meta:
        model = models.ttx
        fields = [
            "pk_fin",
            "fonction",
            "pk_deput",
            "nom_ttx",
            "pk_engagment",
            "pk_degagment",
        ]


class personelForm(forms.ModelForm):
    class Meta:
        model = models.personel
        fields = [
            "telephone",
            "prenom",
            "habilitation",
            "nom",
            "date_depart",
            "date_arrive",
            "fonction",
        ]


class info_chantierForm(forms.ModelForm):
    class Meta:
        model = models.info_chantier
        fields = [
            "numero_ligne",
            "nbr_voies_travail",
            "date_debut_chantier",
            "date_fin_chantier",
        ]
