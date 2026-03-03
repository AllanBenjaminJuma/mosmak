from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def destinations(request):
    return render(request, "destinations.html")

def gallery(request):
    return render(request, "gallery.html")

def kenya(request):
    return render(request, "kenya.html")

def tanzania(request):
    return render(request, "tanzania.html")

def general(request):
    return render(request, "general.html")

def contact(request):
    return render(request, "contact.html")

def privacy(request):
    return render(request, "privacy.html")

def destinationdetails(request):
    return render(request, "destination-details.html")

def destinationmara(request):
    return render(request, "destination-details-mara.html")

def destinationamboseli(request):
    return render(request, "destination-details-amboseli.html")

def destinationtsavoeast(request):
    return render(request, "destination-details-tsavo-east.html")
def destinationtsavowest(request):
    return render(request, "destination-details-tsavo-west.html")

def destinationaberdare(request):
    return render(request, "destination-details-aberdare.html")

def destinationhellsgate(request):
    return render(request, "destination-details-hells-gate.html")

def destinationzanzibar(request):
    return render(request, "destination-details-zanzibar.html")