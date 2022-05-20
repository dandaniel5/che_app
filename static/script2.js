
jQuery('document').ready(function () {
let value1 = document.getElementById("theId").innerHTML;
let value2 = document.getElementById("theData").innerHTML;
$('input:checkbox').click(function () {
var checked = [value1, value2];
$('input:checkbox').each(function () {
    if ($(this).is(':checked')) {
        xxx = "checked";
    } else {
        xxx = "unchecked"
    };
    let total = checked.push($(this).attr('name'), xxx);
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

