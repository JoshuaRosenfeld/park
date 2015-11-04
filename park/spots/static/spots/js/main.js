$(document).ready(function() {
	$(".datepicker").datepicker();
	$(".timepicker").timepicker({ 'scrollDefault': 'now', 'step': 15 });
});

function initAutocomplete() {
	// Create the places search box and link it to the UI element.
	var input = document.getElementById('address-input');
	var searchBox = new google.maps.places.SearchBox(input);

	var map = new google.maps.Map($('#layout-map'), {
		center: {lat: -34.397, lng: 150.644},
		zoom: 8
	});
}