from django.shortcuts import render , HttpResponse
from destinations import mongodbconn
from destinations import mongodb2conn

# Create your views here.
def destinations(request):
    destination = mongodbconn.fetch_All()
    context = {"destinationlist" : destination}
    return render(request , 'destination.html',context)

def destination(request , id = 0):
    #\d{8}\w[et]\d{6}
    full_des = mongodb2conn.fetch_one(id)
    if(full_des == None):
        return render(request , '404.html')
    context = full_des
    response = render(request , 'destination_template.html' , context) 
    response.set_cookie(key="lastdestinationvisit" , value= full_des['id'] , httponly=True)
    return response