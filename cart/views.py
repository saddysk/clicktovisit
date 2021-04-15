from django.shortcuts import render
from django.http import HttpResponse
from datetime import date, datetime
from cart.models import order
from destinations import mongodb2conn

# Create your views here.
def AddToCart(request):
    if request.method == 'POST':
        hotelId = request.POST['hotelId']
        roomId = request.POST['roomId']
        numberOfPeople = request.POST['numberOfPeople']
        numberOfRoom = request.POST['numberOfRoom']
        fromDate = request.POST['fromDate']
        toDate = request.POST['toDate']
        cost = request.POST['cost']
        roomType = request.POST['roomType']

        # calculating number of days
        fdate = fromDate.split('-')
        tdate = toDate.split('-')
        DateFrom = date(int(fdate[0]), int(fdate[1].lstrip("0")), int(fdate[2].lstrip("0")))
        DateTo = date(int(tdate[0]), int(tdate[1].lstrip("0")), int(tdate[2].lstrip("0")))
        numberOfDays = ((DateTo - DateFrom).days)

        # loading current date time for generating below id's
        curDateTime = datetime.now()
        # Order Id > FORMAT: od20210329t120731
        orderId = 'od' + curDateTime.strftime("%x").replace('/', '') + 't' + curDateTime.strftime("%X").replace(':', '')

        # calculating total cost
        totalCost = int(cost) * int(numberOfDays) * int(numberOfPeople)

        # getting user
        username = request.user

        # DatePaid : fromDate > from the bank
        # PaidStatus : False > True after successful payment
        # TransactionID : 'xxx' > from the bank
        
        myOrder = order(user=username, HotelId=hotelId,  roomId=roomId, orderId=orderId, NumberOfPeople=numberOfPeople, NumberOfRooms=numberOfRoom, FromDate=fromDate, ToDate=toDate, NumberOfDays=numberOfDays, Cost=totalCost, PaidStatus=False, TransactionID="xxx", DatePaid=fromDate, RoomType=roomType)

        myOrder.save()

        return HttpResponse('')


# handling cart
def getHotel(request):
    global hotelID
    hotelID = request.POST['hotelId']
    return HttpResponse('')

def MyCart(request, id = 0):
    if request.user.is_authenticated:
        full_des = mongodb2conn.fetch_one(hotelID)
        orderDetails = order.objects.all().filter(PaidStatus=False, user = request.user)

        context = {
            "orderDetails": orderDetails,
            "full_des": full_des
        }
        if orderDetails.count() == 0:
            return render(request, 'cart.html', {"data": 0})
        else:
            return render(request, 'cart.html', context)
            # return render(request, 'cart.html', {"orderDetails": orderDetails})
    else:
        return render(request , 'signin.html')

# delete Order from cart
def DeleteBooking(request):
    if request.method == 'POST':
        OrderId = request.POST['OrderId']
        orderDetails = order.objects.all().filter(PaidStatus=False, orderId = OrderId)
        orderDetails.delete()

        return HttpResponse('')
        