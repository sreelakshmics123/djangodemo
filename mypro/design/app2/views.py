from django.shortcuts import render
from app2.models import Place,Team
def home(request):
    p=Place.objects.all()
    t=Team.objects.all()
    return render(request,'home.html',{'p':p,'t':t})
