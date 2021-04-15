from django.shortcuts import render , HttpResponse
from django.contrib import messages
from homepage.models import contactform

sample_text = "Lorem ipsum dolor sit amet consectetur adipisicing elit.Consequuntur hic odio voluptatem tenetur consequatur.Lorem ipsum dolor sit amet consectetur adipisicing elit."
comments = [{"body":sample_text , "name":"Jane Doe"} , 
            {"body":sample_text , "name":"Jane Doe"},
            {"body":sample_text , "name":"Jane Doe"} , 
            {"body":sample_text , "name":"Jane Doe"}]
destinations = [{"name" : "Destination Name" , "body" :sample_text , "URL" : "/destination" , "imgurl" : "assets/img/destination.jpg"},
                {"name" : "Destination Name" , "body" :sample_text , "URL" : "/destination", "imgurl" : "assets/img/destination.jpg"},
                {"name" : "Destination Name" , "body" :sample_text , "URL" : "/destination", "imgurl" : "assets/img/destination.jpg"},
                {"name" : "Destination Name" , "body" :sample_text , "URL" : "/destination", "imgurl" : "assets/img/destination.jpg"},
                {"name" : "Destination Name" , "body" :sample_text , "URL" : "/destination", "imgurl" : "assets/img/destination.jpg"}]

# Create your views here.
def index(request):     
    return render(request, 'index.html')


def home(request):
    context = {"commentlist" : comments , 
            "destinations" : destinations , 
            "message" : 0}

    if request.method == 'POST' :
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = ""
        c = contactform(name=name , email= email , phone= phone , message=message)
        c.save()
        context['message'] = 1
        return render(request , 'home.html' , context)

    return render(request, 'home.html',context)


def about(request):
    return render(request , 'aboutus.html')


def contact(request):
    if request.method == 'POST' :
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        c = contactform(name=name , email= email , phone= phone , message=message)
        c.save()
        context = {"message" : 1}
        return render(request , 'contactus.html' , context)

    return render(request, 'contactus.html')

def error_404(request,exception):
    return render(request,'404.html')

def error(request):
    return render(request , 'error.html')

def error_400_403(request,exception):
    return render(request , 'error.html')