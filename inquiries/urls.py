from django.urls import path
from .views import inquiry_view, test_email

urlpatterns = [
     path("", inquiry_view, name="inquiries"),
     
     # Testing url for emails
     path("testemail/", test_email, name="testemail"), 
]
