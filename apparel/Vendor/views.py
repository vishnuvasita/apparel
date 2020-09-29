from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages
# Create your views here.

def register(request):
    template = 'Vendor/signup.html'
    if request.method == 'POST':
        r_form = RegisterForm(request.POST or None, request.FILES or None)
        if r_form.is_valid():
            register =r_form.save(commit=False)
            name = request.POST.get('v_name')
            email = request.POST.get('v_email')
            password = request.POST.get('v_password')
            c_password = request.POST.get('v_r_password')
            if(password==c_password):
                register.save()
                request.session["vendor_email"]=email
                request.session["vendor_name"]=name
                # email for welcome
                subject = "Ronak Nandanwar, apparel"
                message = "Hello" + name + ". Welcome to appael. Please verify your email id::--> http://127.0.0.1:8000/Vendor/verification"
                email_from = settings.EMAIL_HOST_USER
                email_to =[email,]
                send_mail(subject, message, email_from, email_to)
                return redirect("Vendor:Please_verify")
    else:
        messages.error(request, 'Please correct error below')
        r_form = RegisterForm()

    return render(request, template, {'register_form':r_form})