from django.shortcuts import render

# Create your views here.

#STEP 2 - FUNCTION

def home(request):
    data = dict() #context comes in form of a dictionary
    data['help'] = 'This is totally crazy'
    data['yelp'] = "A website for reviews"
    import datetime
    data['date'] = datetime.date.today()
    return render(request, "home.html", context = data) #everything must be clearly specified!  render function contains these three components
