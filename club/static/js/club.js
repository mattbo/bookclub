$( document ).ready(function() {

	$(".toggle_form").on("click", function(){
	  var button_id = $(this)[0].id; 
		var form = $('#' + button_id + '_form');
		form.toggle();
	});
});
