// GetButton.io widget
(function () {
    var options = {
        whatsapp: "+917872836494", // WhatsApp number
        call_to_action: "Want help? Chat with us!", // Call to action
        position: "right", // Position may be 'right' or 'left'
        pre_filled_message: "Hey, *clicktovisit.in*, I want to know about ", // WhatsApp pre-filled message
    };
    var proto = document.location.protocol, host = "getbutton.io", url = proto + "//static." + host;
    var s = document.createElement('script'); s.type = 'text/javascript'; s.async = true; s.src = url + '/widget-send-button/js/init.js';
    s.onload = function () { WhWidgetSendButton.init(host, proto, options); };
    var x = document.getElementsByTagName('script')[0]; x.parentNode.insertBefore(s, x);
})();
//  GetButton.io widget