from django.shortcuts import render
from.models import *
# Create your views here.

def table(request):
    task = Task.objects.all()
    return render(request, 'app2/table.html',{'task':task})
