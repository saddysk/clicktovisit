var cards = document.getElementsByClassName("card");
for(var i=0; i < cards.length ; i++) 
{
    cards[i].onclick = function(i){
        var id = this.id;
        url = "/destination/"+id;
        window.open(url, '_blank').focus()
    };
}