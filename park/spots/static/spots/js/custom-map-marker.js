function CustomMarker(latlng, map, args) {
	this.latlng = latlng;	
	this.args = args;	
	this.setMap(map);	
}

var infowindow;			// keep track of last opened infowindow

CustomMarker.prototype = new google.maps.OverlayView();

CustomMarker.prototype.draw = function() {
	
	var self = this;
	
	var div = this.div;
	
	if (!div) {
	
		div = this.div = document.createElement('div');
		div.className = 'marker';
		var rate = "$".concat(this.args['rate']);
		div.innerHTML = rate;
		
		if (typeof(self.args.marker_id) !== 'undefined') {
			div.dataset.marker_id = self.args.marker_id;
		}

		var distance;
		var service = new google.maps.DistanceMatrixService;
		service.getDistanceMatrix({
			origins: [this.args['origin']],
			destinations: [this.latlng],
			travelMode: google.maps.TravelMode.WALKING,
		}, function(response, status) {
			if (status !== google.maps.DistanceMatrixStatus.OK) {
				alert('Error was: ' + status);
			} else {
				var results = response.rows[0].elements;
				distance = results[0].duration.text;

				var message = "<p>This spot costs " + rate + " per hour.</p>" + "<p>It is " + distance + " (walking) from your destination.</p>";
				var iw = new google.maps.InfoWindow({content: message, pixelOffset: new google.maps.Size(5,0)});
		
				google.maps.event.addDomListener(div, "click", function(event) {
					if (infowindow) infowindow.close();			// close last opened info window
					infowindow = iw;							// update last infowindow
					google.maps.event.trigger(self, "click");
					iw.open(map, self);
				});
			}
		});
		
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