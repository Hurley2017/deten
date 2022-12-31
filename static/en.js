function end()
{
    var text = document.getElementById('value').value;
    text = '<xmp>' + text + '</xmp>'
    var doc = {'message':text};
    var jdoc = JSON.stringify(doc);
    $.ajax({
        url:"t_encrypt",
        type:"POST",
        contentType:"application/json",
        data:jdoc,
        async: false,
        success: function(msg){
            if(msg == '0')
            {
                end();
            }
            else
            {
                document.getElementById('answer').innerHTML = msg;
                var box = document.getElementById('boxxx');
                box.style.display = 'block';

            }
             }
    })
}

var copyButton = document.getElementById("copy-button");
var msg = document.getElementById("msg");
copyButton.addEventListener("click", function(event) {
  copyToClipboardMsg(document.getElementById("answer"));
});

function copyToClipboardMsg(elem ) {
    copyToClipboard(elem);
   
    msg.innerHTML = "Copied!";
    setTimeout(function() {
        msg.innerHTML = "Copy";
    }, 2000);
    }

function copyToClipboard(elem) {
    console.log(elem);
    navigator.clipboard.writeText(elem.innerHTML);
}