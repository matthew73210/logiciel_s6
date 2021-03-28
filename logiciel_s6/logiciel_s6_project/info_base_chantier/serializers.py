from rest_framework import serializers

from . import models


class procedure_s9Serializer(serializers.ModelSerializer):

    class Meta:
        model = models.procedure_s9
        fields = [
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

class chantier_seSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.chantier_se
        fields = [
            "created",
            "pk_depose_debut",
            "pk_depose_fin",
            "last_updated",
        ]

class ttxSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ttx
        fields = [
            "last_updated",
            "pk_fin",
            "fonction",
            "pk_deput",
            "nom_ttx",
            "created",
            "pk_engagment",
            "pk_degagment",
        ]

class personelSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.personel
        fields = [
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

class info_chantierSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.info_chantier
        fields = [
            "numero_ligne",
            "nbr_voies_travail",
            "created",
            "last_updated",
            "date_debut_chantier",
            "date_fin_chantier",
        ]
