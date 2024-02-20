from django.shortcuts import render

from .forms import ContactForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from django.core.mail import EmailMessage
from django.template.loader import get_template


def backend(request):
    return render(request, "Home/index.html")

def homeindex(request):
    return render(request, "Home/index.html")

def signup(request):

    if request.method=="POST":
        username = request.POST.get("username")
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        email = request.POST.get("email")
        pass1 = request.POST.get("pass1")
        pass2 = request.POST.get("pass2")

        myuser =User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, "Your account has been created")
        return redirect('signin')

    return render(request, "Home/signup.html")

def signin(request):

    if request.method=="POST":
      username = request.POST.get("username")        
      pass1 = request.POST.get("pass1")       
      user = authenticate(username=username, password=pass1)
      if user is not None:
          login(request, user)
          fname=user.first_name
          return render(request, "Home/index.html", {'fname': fname})
      else :
          messages.error(request,"Bad Credentials" )
          return redirect ('index')

    return render(request, "Home/signin.html")

def signout(request):
    logout(request)
    messages.success(request, "Loggedout Successfully")
    return redirect('backend')




def about(request):
    return render(request, "Home/about.html")

def contact(request):
    form_class = ContactForm
    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            your_contact_name = request.POST.get('your_contact_name', '')
            your_email_address = request.POST.get('your_contact_name', '')
            your_organisation_ = request.POST.get('your_organisation_', '')
            your_query_details = request.POST.get('your_query_details', '')

            # Email the profile with the
            # contact information
            template =get_template('Home/contact_template.txt')
            context = {
                'your_contact_name': your_contact_name,
                'your_email_address': your_email_address,
                'your_organisation_': your_organisation_,
                'your_query_details': your_query_details,
            }
            content = template.render(context)

            email = EmailMessage(
                "New contact form submission",
                content,
                "Your website" +'',
                ['santhanawelladvisor@gmail.com'],
                headers = {'Reply-To': your_email_address }
            )
            email.send()
            return redirect('contact')

    return render(request, 'Home/contact.html', {
        'form': form_class,
    })



def register(request):
    return render(request, "Home/register.html")

def leftsidenavi(request):
    return render(request, "Home/leftsidenavi.html")

def topandside(request):
    return render(request, "Home/base.html")

def lefttop1(request):
    return render(request, "Home/lefttop1.html")


