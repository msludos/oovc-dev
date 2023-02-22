var map = L.map('map').setView([50, 0], 3);

L.tileLayer('https://stamen-tiles-{s}.a.ssl.fastly.net/terrain-background/{z}/{x}/{y}.png', {
	attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> &copy; <a href="https://carto.com/attributions">CARTO</a>',
    subdomains: 'abcd',
	maxZoom: 6,
    minZoom: 2
}).addTo(map);

var point_marker = L.icon({
    iconUrl: '/static/imgs/map/point_marker.png',
    iconSize: [16, 16]
});

var capital_point_marker = L.icon({
    iconUrl: '/static/imgs/map/capital_point_marker.png',
    iconSize: [16, 16]
});

function setMapJson(json, id, flag, name) {
    json.forEach(element => {
        L.geoJSON(element, {
            style: {
                fillColor: element.properties.fill,
                color: element.properties.stroke
            },
            pointToLayer: function(feature, latlng) {
                let icon_f = capital_point_marker;
                try {
                    if (feature.properties.type.toLowerCase() == "city") icon_f = point_marker; 
                    else icon_f = capital_point_marker;
                } catch (e) {
                    try {
                        if (feature.properties.Type.toLowerCase() == "city") icon_f = point_marker; 
                        else icon_f = capital_point_marker;
                    } catch (ex) {
                        console.log(e, ex);
                    }
                }

                try {
                    if (feature.properties.Name != (undefined || null)) feature.properties.name = feature.properties.Name;
                } catch (e) {
                    console.log(e);
                }

                return L.marker(latlng, 
                {icon: icon_f}).bindPopup(feature.properties.name);
            },
            onEachFeature: function (feature, latlng) {
                if (feature.geometry.type != "Point") latlng.bindPopup(`
		<div class="popup-country"><img src="${flag}"><hr><a href="/sections/countries/country.html?id=${id}">${name}❯</a><script>console.log("a");</script></div>
		`);
            }
        }).addTo(map);
    });
}

window.onload = function() {
    ids.ids.forEach(element => {
        console.log(element);
        $.get(`https://oovc-dev.vercel.app/redirect/geo?id=${element}`, function(data) {
            console.log(data)
            setMapJson(JSON.parse(data.split("~")[0]).features, element, data.split("~")[1], data.split("~")[2]);     
        });
    });
    document.querySelector(".leaflet-attribution-flag").remove();
}
