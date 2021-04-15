from django.shortcuts import render , HttpResponse , redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login , logout
from user.models import Profile
from cart.models import order
import hashlib

# Create your views here.
def signupUser(request):

    if request.method == 'POST':
        fname = request.POST['fname']
        email = request.POST['email']
        pnumber = request.POST['pnumber']
        dob = request.POST['dob']
        password = request.POST['password']
        username = hashlib.sha512(email.encode()).hexdigest()
        try:
            User.objects.get(username=username)
            return render(request , 'signup.html' , {"alert" : 1})
        except:
            user = User.objects.create_user(username = username , email = email , password = password)
            user.first_name = fname
            obj = Profile(user = user , phone = pnumber , DOB = dob)
            obj.save()
            user.save()

            return render(request , 'signup.html' , {"alert" : 0})

    return render(request , 'signup.html')

def loginUser(request):
    
    urltoredirect = ""
    try:
        value = request.COOKIES.get('lastdestinationvisit')
        urltoredirect += value
    except:
        urltoredirect = "/destination"

    if request.user.is_authenticated:
        return render(request , "signin.html" , {"alert" : 0 , "reurl" : urltoredirect})

    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        email = email.lower()
        username = hashlib.sha512(email.encode()).hexdigest()
        user = authenticate(request, username= username, password=password)
        if user is not None:
            login(request,user)
            return render(request , "signin.html" , {"alert" : 0 , "reurl" : urltoredirect})
        else:
            return render(request , "signin.html" , {"alert" : 1})        
    return render(request , 'signin.html')

def logoutUser(request):
    if request.user.is_authenticated:
        logout(request)
        return render(request , 'signout-thankyou.html')
    else:
        return redirect('/user/login')

def gettrips(request):
    if request.user.is_authenticated:
        username = request.user
        trips = order.objects.all().filter(PaidStatus=True , user= username).order_by('FromDate').reverse()
        if trips.count() == 0:
            return render(request , 'trips.html' , {"count" : 0})
        else:
            return HttpResponse("trips")
    else:
        return render(request , 'signin.html')