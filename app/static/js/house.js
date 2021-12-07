
window.addEventListener('load', () => {
	initMap();

	document.querySelector('#ephoto img').addEventListener('click', ev => ev.target.parentElement.className = '');
	document.getElementById('photo').addEventListener('click', () => 
		document.getElementById('ephoto').classList.add('show'));
});


const initMap = () => {
	const lat  = document.getElementById('lat') .value;
	const long = document.getElementById('long').value;

	var map = L.map('map').setView([long, lat], 13);
	L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
		attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
	}).addTo(map);
			
	L.marker([long, lat])
		.addTo(map)
		.bindPopup('Ubicación de la vivienda')
		.openPopup();
};