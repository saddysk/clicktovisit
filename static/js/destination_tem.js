// addToCart

let id, priceId, roomType;
function AddToCart() {
    id = cid;
    priceId = priceid;
    roomType = roomtype;
}
$(document).on('submit', id, function(e){
    e.preventDefault();

    numPeople = e.target[1].id;
    numRoom = e.target[2].id;
    fromDate = e.target[3].id;
    toDate = e.target[4].id;
    hotelId = e.target[5].id;
    roomId = e.target[6].id;

    numOfPeople = document.getElementById(numPeople).value;
    numOfRoom = document.getElementById(numRoom).value;
    fDate = document.getElementById(fromDate).value;
    tDate = document.getElementById(toDate).value;

    numOfPeople = parseInt(numOfPeople, 10);
    numOfRoom = parseInt(numOfRoom, 10);

    if (numOfPeople < numOfRoom) {
        let confiramtion = prompt("You've selected too many rooms that might not be required! \n Type 'yes' to continue.");
        if (confiramtion == 'yes' )
            AjaxCall();
        else {
            document.getElementById(numPeople).value = '';
            document.getElementById(numRoom).value = '';
        }
    } else if (fDate > tDate){
        alert('to date should be after the from date');
    } else {
        AjaxCall();
    }

    function AjaxCall() {
        $.ajax({
            type: 'POST',
            url: '/cart/addtocart/',
            data: {
                numberOfPeople: numOfPeople,
                numberOfRoom: numOfRoom,
                fromDate: fDate,
                toDate: tDate,
                hotelId: document.getElementById(hotelId).value,
                roomId: document.getElementById(roomId).value,
                cost: document.getElementById(priceId).innerText,
                roomType: document.getElementById(roomType).innerText,
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
            },
            success: function () {
                alert("Item added to cart");
                
                document.getElementById(numPeople).value = '';
                document.getElementById(numRoom).value = '';
                document.getElementById(fromDate).value = '';
                document.getElementById(toDate).value = '';
            }
        })
    }
});

// send hotel ID to views.py
window.onload = function() {
    $.ajax({
        type: 'POST',
        url: '/cart/gethotel/',
        data: {
            hotelId: document.getElementById("HotelID").value,
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
        },
    });
}