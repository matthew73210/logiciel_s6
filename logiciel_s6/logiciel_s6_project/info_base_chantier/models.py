from django.db import models
from django.urls import reverse


class procedure_s9(models.Model):

    # Fields
    N_prog_jour = models.IntegerField()
    nom_phase = models.CharField(max_length=30)
    trx_nuit = models.BooleanField()
    DFV = models.BooleanField()
    continuite_elec = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True, editable=False)
    active = models.BooleanField()
    h_fin = models.TimeField()
    date_debut_trx = models.DateField()
    pk_fin = models.DecimalField(max_digits=10, decimal_places=2)
    Ct_Tx = models.CharField(max_length=30)
    etat_surface_rail = models.BooleanField()
    pk_debut = models.DecimalField(max_digits=10, decimal_places=2)
    h_debut = models.TimeField()
    GEq = models.BooleanField()
    RCT = models.BooleanField()
    indice_CtTx = models.CharField(max_length=30)
    Voie = models.CharField(max_length=30)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("info_base_chantier_procedure_s9_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("info_base_chantier_procedure_s9_update", args=(self.pk,))


class chantier_se(models.Model):

    # Fields
    created = models.DateTimeField(auto_now_add=True, editable=False)
    pk_depose_debut = models.IntegerField()
    pk_depose_fin = models.IntegerField()
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("info_base_chantier_chantier_se_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("info_base_chantier_chantier_se_update", args=(self.pk,))


class ttx(models.Model):

    # Fields
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    pk_fin = models.IntegerField()
    fonction = models.TextField(max_length=100)
    pk_deput = models.IntegerField()
    nom_ttx = models.TextField(max_length=100)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    pk_engagment = models.IntegerField()
    pk_degagment = models.IntegerField()

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("info_base_chantier_ttx_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("info_base_chantier_ttx_update", args=(self.pk,))


class personel(models.Model):

    # Fields
    created = models.DateTimeField(auto_now_add=True, editable=False)
    telephone = models.TextField(max_length=100)
    prenom = models.TextField(max_length=100)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    habilitation = models.TextField(max_length=100)
    nom = models.TextField(max_length=100)
    date_depart = models.DateField()
    date_arrive = models.DateField()
    fonction = models.TextField(max_length=100)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("info_base_chantier_personel_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("info_base_chantier_personel_update", args=(self.pk,))


class info_chantier(models.Model):

    # Fields
    numero_ligne = models.CharField(max_length=30)
    nbr_voies_travail = models.TextField(max_length=100)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    date_debut_chantier = models.DateField()
    date_fin_chantier = models.DateField()

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("info_base_chantier_info_chantier_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("info_base_chantier_info_chantier_update", args=(self.pk,))
