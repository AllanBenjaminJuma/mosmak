from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings

from django.http import HttpResponse

# Create your views here.

def contact(request):
    
    return render(request, 'contact.html')

def inquiry_view(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        
        full_message = f"""
        New Safari Inquiry
        
        Name: {name}
        Email: {email}
        Subject: {subject}
        
        Message:
        {message}
        """
        
        send_mail(
            subject = f"Tour Inquiry:{subject}",
            message = full_message,
            from_email= settings.DEFAULT_FROM_EMAIL,
            recipient_list = ["info@mosmak.co.ke"],
        )
        return render(request, "contact.html", {"success": True})
    
    return redirect(contact)

# Test View to test that emails are sent.
def test_email(request):
    send_mail(
        subject="Mosmak SMTP Test",
        message="This is a test email from your Django application.",
        from_email="info@mosmak.co.ke",
        recipient_list=["info@mosmak.co.ke"],
        fail_silently=False,
    )
    return HttpResponse("Test mail sent successfully")
