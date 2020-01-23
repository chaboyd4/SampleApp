from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse
from sample_app.models import AppUser

# Create your views here.

#STEP 2 - FUNCTION

def home(request):
    data = dict() #context comes in form of a dictionary
    data['help'] = 'This is totally crazy'
    data['yelp'] = "A website for reviews"
    import datetime
    data['date'] = datetime.date.today()
    people = [["John","New York"],
              ["Qing","Boston"],
              ["Jill","Oslo"],
              ['Raja', 'Stockholm']]
    data['persons'] = people
    data['banjo'] = "Yes"
    return render(request, "home.html", context = data) #everything must be clearly specified!  render function contains these three components

def login(request):
    return render(request, "registration/login.html")

# def new_user_register(request):
#     return render(request, "register.html")

def guest(request):
    return render(request, "guest.html")

def loggedIn(request):
    context = dict()
    return render(request, "loggedIn.html", context=context)

def process_guest(request):
    try:
        request.GET['cancel']
        return home(request)
    except:
        pass

    try:
        name = request.GET['name']
        dob = request.GET['dob']
        email = request.GET['email']
    except:
        return render(request, 'guest.html')
    import datetime
    today = datetime.date.today()
    then = datetime.datetime.strptime(dob, "%Y-%m-%d")
    print(today, then)
    diff = today - then.date()
    context = dict()
    context['name'] = name
    context['dob'] = dob
    context['age'] = diff.days
    context['email'] = email
    alive = today - datetime.datetime.strptime(dob,"%Y-%m-%d").date()
    return render(request, "guest_stuff.html", context=context)


def new_user_register(request):
    context = dict()
    form = UserCreationForm(request.POST)
    if form.is_valid():
        print("Inside if")
        new_user = form.save()
        email = request.POST['email']
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        new_user.first_name = first_name
        new_user.last_name = last_name
        new_user.email = email
        new_user.save()
        acct_holder = AppUser(user=new_user)
        acct_holder.points = 1000
        acct_holder.save()
        print("User created")
        return HttpResponseRedirect(reverse("login"))
    else:
        print("User not created")
        form = UserCreationForm()
        context['form'] = form
        return render(request,"registration/register.html", context)


def resort_finder(request):
    from sample_app.support_funcs import get_resorts
    context = dict()
    resorts = get_resorts()
    context['data'] = resorts
    return render(request,"resorts.html",context=context)
