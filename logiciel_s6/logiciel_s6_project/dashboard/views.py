from django.shortcuts import render
from info_base_chantier.models import info_chantier

# Create your views here.

def index(request):
    info_chantier_dashboard = info_chantier.objects.all()
    
    args = {'info_chantier_dashboard' : info_chantier_dashboard}
    #print(args)
    return render(request, 'dashboard/index.html', args)