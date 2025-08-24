# from channels.auth import login, logout
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from VCS.models import *
from django.core.mail import send_mail

from VCS.EmailBackEnd import EmailBackEnd


def Home(request):
    return render(request, 'Hom_d/index.html')

def About(request):
    return render(request, 'Hom_d/about.html')

def Courses(request):
    return render(request, 'Hom_d/courses.html')

def Team(request):
    return render(request, 'Hom_d/team.html')

def Testimonials(request):
    return render(request, 'Hom_d/testimonial.html')

def Contact_us(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        contact = Contact (
            name = name,
            email = email,
            subject = subject,
            message = message,
        )

        # subject = subject
        # message = message
        # email_from = settings.EMAIL_HOST_USER
        # try:
        #     send_mail(subject, message, email_from, ['utrivedi180@gmail.com'])
        
        contact.save()
        return redirect('Home')
        # except:
        #     return redirect("Contact")
    return render(request, 'Hom_d/contact.html')

def loginPage(request):
    return render(request, 'login.html')


def doLogin(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        user = EmailBackEnd.authenticate(request, username=request.POST.get('email'), password=request.POST.get('password'))
        if user != None:
            login(request, user)
            user_type = user.user_type
            if user_type == '1':
                return redirect('admin_home')
                
            elif user_type == '2':
                return redirect('staff_home')
                
            elif user_type == '3':
                return redirect('student_home')
            else:
                messages.error(request, "Invalid Login!")
                return redirect('login')
        else:
            messages.error(request, "Invalid Login Credentials!")
            #return HttpResponseRedirect("/")
            return redirect('login')



def get_user_details(request):
    if request.user != None:
        return HttpResponse("User: "+request.user.email+" User Type: "+request.user.user_type)
    else:
        return HttpResponse("Please Login First")



def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')
