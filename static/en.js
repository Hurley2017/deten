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

            }
             }
    })
}