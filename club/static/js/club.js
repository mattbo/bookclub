$( document ).ready(function() {

	$(".toggle_form").on("click", function(){
          console.log("hi");
	  var button_id = $(this)[0].id; 
		var form = $('#' + button_id + '_form');
		form.toggle();
	});
        //turn on the datepickers
        $('.datepicker').datepicker();
});
