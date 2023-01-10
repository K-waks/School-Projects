from django.shortcuts import render
from datetime import datetime

def index(request):
    return render(request, 'index.html', {'today':datetime.today()})