$(document).ready(function() {
	$(".datepicker").datepicker();
	$(".timepicker").timepicker({ 'scrollDefault': 'now', 'step': 15, 'timeFormat': 'h:i A'});
	initAutocomplete();
});

var map, origin, input, searchBox;
var ZOOM = 14;

function initAutocomplete() {
	// Create the places search box and link it to the UI element.
	input = document.getElementById('address-input');
	searchBox = new google.maps.places.SearchBox(input);
	
	// Create the map
	if($('#layout-spots-map').length) {
		initMap();
	}
}

function initMap() {
	map = new google.maps.Map(document.getElementById('layout-spots-map'), {
		center: {lat: 0, lng: 0},
		zoom: ZOOM
	});

	// bias search box toward current map view
	map.addListener('bounds_changed', function() {
		searchBox.setBounds(map.getBounds());
	});

	// place a marker at the destination
	var geocoder = new google.maps.Geocoder();
	origin = document.getElementById('address-input').value;
	geocoder.geocode( { 'address': origin}, function(results, status) {
		if (status == google.maps.GeocoderStatus.OK) {
			map.setCenter(results[0].geometry.location);
			var marker = new google.maps.Marker({
				map: map,
				position: results[0].geometry.location
			});
		} else {
			alert("Geocode was not successful for the following reason: " + status);
		}	
	});

	addMarkers();
}

function addMarkers() {
	var geocoder = new google.maps.Geocoder();

	// add an overlay for each spot
	instance_list.forEach(function(instance) {
		var address = instance.spot__residence__address;
		var rate = instance.rate;
		var id = instance.id;

		geocoder.geocode( { 'address': address}, function(results, status) {
			if (status == google.maps.GeocoderStatus.OK) {
				var latlng = results[0].geometry.location;
				var overlay = new CustomMarker(latlng, map, {'id': id, 'rate': rate, 'origin': origin});
			} else {
				alert("Geocode was not successful for the following reason: " + status);
			}
		});
	});
}