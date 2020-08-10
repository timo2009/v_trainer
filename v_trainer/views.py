from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import EnglischesWort, DeutschesWort



#def index(request):
	#return HttpResponse("Hallo, ich bin Timo.")


def index(request):
	deutsche_woerter=DeutschesWort.objects.all()
	englische_woerter=EnglischesWort.objects.all()
	return render(request, 'v_trainer/index.html', {"name":"Moin", "deutsche_woerter":deutsche_woerter, "englische_woerter":englische_woerter})


