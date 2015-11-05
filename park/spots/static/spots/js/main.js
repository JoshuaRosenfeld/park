$(document).ready(function() {
	$(".datepicker").datepicker();
	$(".timepicker").timepicker({ 'scrollDefault': 'now', 'step': 15, 'timeFormat': 'h:i A'});
});

function initAutocomplete() {
	// Create the places search box and link it to the UI element.
	var input = document.getElementById('address-input');
	var searchBox = new google.maps.places.SearchBox(input);
	var map = new google.maps.Map(document.getElementById('layout-map'), {
		center: {lat: 41.31, lng: -72.93},
		zoom: 14
	});
}