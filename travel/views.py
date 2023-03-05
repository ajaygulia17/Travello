from django.shortcuts import render
from .models import Destination

# Create your views here.
def index(request):
    # dest1  = Destination()
    # dest1.name = "Bali"
    # dest1.desc = "Nulla pretium tincidunt felis, nec."
    # dest1.img = "destination_1.jpg"
    # dest1.price = 700
    # dest1.special = False

    # dests = [dest1, dest2, dest3]
    dests = Destination.objects.all()
    dests = dests[:6]

    return render(request, "index.html", {'dests':dests})

def destinations(request):
    dests = Destination.objects.all()
    return render(request, "destination.html", {'dests':dests})