from django.shortcuts import render, redirect
from .models import Destination, Packages

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
    for d in dests:
        packages = Packages.objects.filter(destination = d).values()
        mn = 100000000
        for p in packages:
            mn = min(mn, p['price'])
            # print(p)
        if mn!=100000000:
            d.price = mn
    # dests = dests[:6]

    return render(request, "index.html", {'dests':dests})

def destinations(request):
    d = request.GET['id']
    packages = Packages.objects.filter(destination = d).values()
    return render(request, "destination.html", {'packages':packages})

def about(request):
    return render(request, "about.html")

def news(request):
    return render(request, "news.html")

def contact(request):
    return render(request, "contact.html")

def package(request):
    dests = Destination.objects.all()
    return render(request, "packages.html", {'dests': dests})

def addpackage(request):
    name=request.POST['name']
    demo=request.POST['demo']
    existingDestination=request.POST['existingDestination']
    destination=request.POST['destination']
    desc=request.POST['desc']
    duration=request.POST['duration']
    # img=request.POST['img']
    price=request.POST['price']
    image = request.FILES['img']
    sp = False
    if 'special' in request.POST:
        sp = True
    
    if demo=="One":
        p = Packages.objects.create(name=name, destination_id=existingDestination, img=image, duration=duration, price=price, special=sp)
        p.save()
    else:
        d = Destination.objects.create(name=destination, img = image, desc=desc, price=price, special=sp)
        d.save()
        d_id = d.id
        p = Packages.objects.create(name=name, destination_id=d_id, img=image, duration=duration, price=price, special=sp)
        p.save()
    # print(name, demo, existingDestination, destination, desc, duration, price, image)
    return redirect("/package")