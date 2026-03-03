"""
URL configuration for Mosmak project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', views.index, name='index' ),
    path('about', views.about, name='about' ),
    path('destinations', views.destinations, name='destinations' ),
    path('gallery', views.gallery, name='gallery' ),
    path('contact/', views.contact, name='contact' ),
    path('kenya', views.kenya, name='kenya' ),
    path('tanzania', views.tanzania, name='tanzania' ),
    path('general', views.general, name='general' ),
    path('privacy', views.privacy, name='privacy_policy' ),
    path('destination-details', views.destinationdetails, name='destination-details' ),
    path('destination-details-mara', views.destinationmara, name='destination-details-mara' ),
    path('destination-details-amboseli', views.destinationamboseli, name='destination-details-amboseli' ),
    path('destination-details-tsavo-east', views.destinationtsavoeast, name='destination-details-tsavo-east' ),
    path('destination-details-tsavo-west', views.destinationtsavowest, name='destination-details-tsavo-west' ),
    path('destination-details-aberdare', views.destinationaberdare, name='destination-details-aberdare' ),
    path('destination-details-hells-gate', views.destinationhellsgate, name='destination-details-hells-gate' ),
    path('destination-details-zanzibar', views.destinationzanzibar, name='destination-details-zanzibar' ),
    
    path('inquiries/', include('inquiries.urls'))
]
