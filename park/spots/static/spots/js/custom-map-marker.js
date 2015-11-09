var infowindow;			// keep track of last opened infowindow

function CustomMarker(latlng, map, args) {
	this.latlng = latlng;	
	this.args = args;	
	this.setMap(map);	
};

CustomMarker.prototype = new google.maps.OverlayView();

CustomMarker.prototype.draw = function() {
	var self = this;
	var div = this.div;
	
	if (!div) {
		var rate = getRate(this.args);
		div = this.div = createOverlayDiv(rate);

		dict = {
			'latlng': this.latlng,
			'rate': rate,
			'id': this.args['id'],
			'start': this.args['start'],
			'end': this.args['end']
		};

		createInfoWindow(self, div, origin, dict);
		var panes = this.getPanes();
		panes.overlayImage.appendChild(div);
	}
	
	var point = this.getProjection().fromLatLngToDivPixel(this.latlng);
	
	if (point) {
		div.style.left = (point.x - 10) + 'px';
		div.style.top = (point.y - 20) + 'px';
	}
};

CustomMarker.prototype.remove = function() {
	if (this.div) {
		this.div.parentNode.removeChild(this.div);
		this.div = null;
	}	
};

CustomMarker.prototype.getPosition = function() {
	return this.latlng;	
};

function getRate(args) {
	return "$".concat(args['rate']);
};

function createOverlayDiv(rate) {
	var div = document.createElement('div');
	div.className = 'marker';
	div.innerHTML = rate;
	return div;
};

function createInfoWindow(customMarker, div, origin, dict) {
	var distance;
	var service = new google.maps.DistanceMatrixService;

	service.getDistanceMatrix({
		origins: [origin],
		destinations: [dict['latlng']],
		travelMode: google.maps.TravelMode.WALKING,
	}, function(response, status) {
		if (status !== google.maps.DistanceMatrixStatus.OK) {
			alert('Error was: ' + status);
		} else {
			var results = response.rows[0].elements;
			distance = results[0].duration.text;

			var html = createInfoWindowContent(distance, dict);
			var iw = new google.maps.InfoWindow({content: html, pixelOffset: new google.maps.Size(5,0)});
			
			google.maps.event.addDomListener(div, "click", function(event) {
				if (infowindow) infowindow.close();			// close last opened info window
				infowindow = iw;							// update last infowindow
				google.maps.event.trigger(customMarker, "click");
				iw.open(map, customMarker);
			});
		}
	});
};

function createInfoWindowContent(distance, dict) {
	var wrapper = $('<div>');
	var container = $('<div>', {class: 'iw'});
	var rate_p = $('<p>', {text: dict['rate'] + " / hr"});
	var distance_p = $('<p>', {text: distance + " away"});
	var start_p = $('<p>', {text: 'from ' + dict['start']});
	var stop_p = $('<p>', {text: 'until ' + dict['end']});

	var params = $.param(param_dict);
	var href = "/spots/book/" + dict['id'] + "?" + params
	var reserve_link = $('<a>', {href: href});
	var reserve = $('<p>', {class: 'yellow strong top-space', text: 'reserve'});;
	reserve_link.append(reserve);

	container.append(rate_p);
	container.append(distance_p);
	container.append(start_p);
	container.append(stop_p);
	container.append(reserve_link);
	wrapper.append(container);
	var content = wrapper.html();
	return content;
}





