from django.shortcuts import render
from .models import Users
# Create your views here.
def utilizatori_list(request):
    utilizatori = Users.objects.all()
    context = {
        'utilizatori': utilizatori
    }
    return render(request, 'list.html', context)