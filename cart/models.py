from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class order(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    HotelId = models.CharField(max_length =16)
    roomId = models.CharField(max_length = 18)
    RoomType = models.CharField(max_length = 18)
    orderId = models.CharField(max_length=17)   # generate
    NumberOfPeople = models.IntegerField()
    NumberOfRooms = models.IntegerField()
    FromDate = models.DateField()
    ToDate =  models.DateField()
    NumberOfDays = models.IntegerField()
    Cost = models.IntegerField()
    PaidStatus = models.BooleanField()
    TransactionID = models.CharField(max_length=100)
    DatePaid = models.DateTimeField()

#orderId : od20210329t120731
#HotelId : 20210329et120731
#RoomId : not decided yet right now using "type1" , "type2" .....
#For how to handle user field view User app
