from django.shortcuts import render
from .models import Student, Dojo

# Create your views here.
def index(request):
    context = {
        'all_dojos': Dojo.objects.all(),
        'all_students': Student.objects.all()
    }
    return render(request, 'index.html', context)