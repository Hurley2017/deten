function ded()
{
    var text = document.getElementById('value').value;
    var doc = {'message':text};
    var jdoc = JSON.stringify(doc);
    $.ajax({
        url:"t_decrypt",
        type:"POST",
        contentType:"application/json",
        data:jdoc,
        async: false,
        success: function(msg){
            var text = createElementFromHTML(msg);
            document.getElementById('answer').innerHTML = text
                var box = document.getElementById('boxxx');
                box.style.display = 'block';
        
             }
    })
}

function createElementFromHTML(htmlString) {
    var div = document.createElement('div');
    div.innerHTML = htmlString.trim();
    return div.firstChild.innerHTML;
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