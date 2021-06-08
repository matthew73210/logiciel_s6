from django.views import generic
from django.shortcuts import render,HttpResponse
from . import models
from . import forms

def index(request):
    return render(request, 'info_base_chantier/index.html')

def export_excel(request):
    response=HttpResponse(content_type='') #add function to create excel file


class procedure_s9ListView(generic.ListView):
    model = models.procedure_s9
    form_class = forms.procedure_s9Form


class procedure_s9CreateView(generic.CreateView):
    model = models.procedure_s9
    form_class = forms.procedure_s9Form


class procedure_s9DetailView(generic.DetailView):
    model = models.procedure_s9
    form_class = forms.procedure_s9Form


class procedure_s9UpdateView(generic.UpdateView):
    model = models.procedure_s9
    form_class = forms.procedure_s9Form
    pk_url_kwarg = "pk"


class chantier_seListView(generic.ListView):
    model = models.chantier_se
    form_class = forms.chantier_seForm


class chantier_seCreateView(generic.CreateView):
    model = models.chantier_se
    form_class = forms.chantier_seForm


class chantier_seDetailView(generic.DetailView):
    model = models.chantier_se
    form_class = forms.chantier_seForm


class chantier_seUpdateView(generic.UpdateView):
    model = models.chantier_se
    form_class = forms.chantier_seForm
    pk_url_kwarg = "pk"


class ttxListView(generic.ListView):
    model = models.ttx
    form_class = forms.ttxForm


class ttxCreateView(generic.CreateView):
    model = models.ttx
    form_class = forms.ttxForm


class ttxDetailView(generic.DetailView):
    model = models.ttx
    form_class = forms.ttxForm


class ttxUpdateView(generic.UpdateView):
    model = models.ttx
    form_class = forms.ttxForm
    pk_url_kwarg = "pk"


class personelListView(generic.ListView):
    model = models.personel
    form_class = forms.personelForm


class personelCreateView(generic.CreateView):
    model = models.personel
    form_class = forms.personelForm


class personelDetailView(generic.DetailView):
    model = models.personel
    form_class = forms.personelForm


class personelUpdateView(generic.UpdateView):
    model = models.personel
    form_class = forms.personelForm
    pk_url_kwarg = "pk"


class info_chantierListView(generic.ListView):
    model = models.info_chantier
    form_class = forms.info_chantierForm


class info_chantierCreateView(generic.CreateView):
    model = models.info_chantier
    form_class = forms.info_chantierForm


class info_chantierDetailView(generic.DetailView):
    model = models.info_chantier
    form_class = forms.info_chantierForm


class info_chantierUpdateView(generic.UpdateView):
    model = models.info_chantier
    form_class = forms.info_chantierForm
    pk_url_kwarg = "pk"
