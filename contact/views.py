from django.shortcuts import render
from .models import Info
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def send_message(request):
    myinfo = Info.objects.first()
    if request.method == 'POST':
        subject = request.POST['subject']
        email = request.POST['email']
        message = request.POST['message']
        send_mail(
            subject,
            message,
            email,
            [settings.EMAIL_HOST_USER],
        )
    else:
        pass
    
    return render(request,'contact/contact.html',{'myinfo':myinfo})
