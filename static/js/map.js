// Unique Access Token for the MapBox API
mapboxgl.accessToken = `
pk.eyJ1IjoiY2xpY2t0b3Zpc2l0IiwiYSI6ImNrbG5naHhoMDA5MTQyb280djRiM2Z5ZWkifQ.UieuV8QgIkQL3-Fr2TGPuA`;

navigator.geolocation.getCurrentPosition(successLocation, errorLocation, {
  enableHighAccuracy: true,
});

// if user gives the permission to track the user's current location, use it
function successLocation(position) { setUpMap([position.coords.longitude, position.coords.latitude]);
}
// if no geolocation is found by default from the user, provide a default location of howrah
function errorLocation() {
  setUpMap([88.2636, 22.5958]);
}

function setUpMap(center) {
  // setting up the map - (creating a new map)
  const map = new mapboxgl.Map({
    container: "map",
    style: "mapbox://styles/mapbox/streets-v11",
    center: center,
    zoom: 9,
  });

  //   map navigation control - GUI
  const nav = new mapboxgl.NavigationControl();
  //   setting the position of the above field on the map
  map.addControl(nav);

  //   get direction - source/destination
  var directions = new MapboxDirections({
    accessToken: mapboxgl.accessToken,
  });
  
  //   setting the position of the above field on the map
  map.addControl(directions, "top-left");
}
