jQuery('document').ready(function(){

$('input:checkbox').click(function(){


var checked = [];
$('input:checkbox').each(function() {
if ($(this).is(':checked')) {xxx="checked";}
else {xxx="unchecked";}
var total = checked.push($(this).attr('name'), xxx);
});
$.ajax({
    url: '/chb',
    type: 'POST',
    data: JSON.stringify(checked),
    contentType: 'application/json; charset=utf-8',
    dataType: 'json',
    async: false,
    success: alert('отправлено')
});
});
});