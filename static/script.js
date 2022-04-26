jQuery('document').ready(function(){
//    jQuery('#chb1').click(function() {
//    var chb1,chb2,chb3,chb4
//
//    chb1 = jQuery('#chb1').is(':checked');
//    chb2 = jQuery('#chb2').is(':checked');
//    chb3 = jQuery('#chb3').is(':checked');
//    chb4 = jQuery('#chb4').is(':checked');
//    var arr = {boxes:{ "chb1":chb1, "chb2":chb2, "chb3":chb3, "chb4":chb4 }};
//
//$.ajax({
//    url: '/chb',
//    type: 'POST',
//    data: JSON.stringify(arr),
//    contentType: 'application/json; charset=utf-8',
//    dataType: 'json',
//    async: false,
//    success: alert('отправлено')
//});
//});
//    jQuery('#chb2').click(function() {
//    var chb1,chb2,chb3,chb4
//
//    chb1 = jQuery('#chb1').is(':checked');
//    chb2 = jQuery('#chb2').is(':checked');
//    chb3 = jQuery('#chb3').is(':checked');
//    chb4 = jQuery('#chb4').is(':checked');
//    var arr = {boxes:{ "chb1":chb1, "chb2":chb2, "chb3":chb3, "chb4":chb4 }};
//
//$.ajax({
//    url: '/chb',
//    type: 'POST',
//    data: JSON.stringify(arr),
//    contentType: 'application/json; charset=utf-8',
//    dataType: 'json',
//    async: false,
//    success: alert('отправлено')
//});
//});
//jQuery('#chb3').click(function() {
//    var chb1,chb2,chb3,chb4
//
//    chb1 = jQuery('#chb1').is(':checked');
//    chb2 = jQuery('#chb2').is(':checked');
//    chb3 = jQuery('#chb3').is(':checked');
//    chb4 = jQuery('#chb4').is(':checked');
//    var arr = {boxes:{ "chb1":chb1, "chb2":chb2, "chb3":chb3, "chb4":chb4 }};
//
//$.ajax({
//    url: '/chb',
//    type: 'POST',
//    data: JSON.stringify(arr),
//    contentType: 'application/json; charset=utf-8',
//    dataType: 'json',
//    async: false,
//    success: alert('отправлено')
//});
//});
//jQuery('#chb4').click(function() {
//    var chb1,chb2,chb3,chb4
//
//    chb1 = jQuery('#chb1').is(':checked');
//    chb2 = jQuery('#chb2').is(':checked');
//    chb3 = jQuery('#chb3').is(':checked');
//    chb4 = jQuery('#chb4').is(':checked');
//    var arr = {boxes:{ "chb1":chb1, "chb2":chb2, "chb3":chb3, "chb4":chb4 }};
//
//$.ajax({
//    url: '/chb',
//    type: 'POST',
//    data: JSON.stringify(arr),
//    contentType: 'application/json; charset=utf-8',
//    dataType: 'json',
//    async: false,
//    success: alert('отправлено')
//});
//});

$('input:checkbox').click(function(){
if ($(this).is(':checked')) {
		var chb1,chb2,chb3,chb4

    chb1 = jQuery('#chb1').is(':checked');
    chb1text = jQuery('#chb1text').val();
    chb2 = jQuery('#chb2').is(':checked');
    chb2text = jQuery('#chb2text').val();
    chb3 = jQuery('#chb3').is(':checked');
    chb3text = jQuery('#chb3text').val();
    chb4 = jQuery('#chb4').is(':checked');
    chb4text = jQuery('#ch41text').val();
    var arr = {boxes:{ chb1text:chb1, chb2text:chb2, chb3text:chb3, chb4text:chb4 }};
$.ajax({
    url: '/chb',
    type: 'POST',
    data: JSON.stringify(arr),
    contentType: 'application/json; charset=utf-8',
    dataType: 'json',
    async: false,
    success: alert('отправлено')
});
	}
	 else {
	var chb1,chb2,chb3,chb4

    chb1 = jQuery('#chb1').is(':checked');
    chb1text = jQuery('#chb1text').val();
    chb2 = jQuery('#chb2').is(':checked');
    chb2text = jQuery('#chb2text').val();
    chb3 = jQuery('#chb3').is(':checked');
    chb3text = jQuery('#chb3text').val();
    chb4 = jQuery('#chb4').is(':checked');
    chb4text = jQuery('#ch41text').val();
    var arr = {boxes:{ chb1text:chb1, chb2text:chb2, chb3text:chb3, chb4text:chb4 }};
$.ajax({
    url: '/chb',
    type: 'POST',
    data: JSON.stringify(arr),
    contentType: 'application/json; charset=utf-8',
    dataType: 'json',
    async: false,
    success: alert('отправлено')
});



	}
});
});