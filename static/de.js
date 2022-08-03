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
            document.getElementById('answer').innerHTML = msg;
        
             }
    })
}