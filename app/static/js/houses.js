
window.addEventListener('load', () => {
	document.getElementById('filter').addEventListener('submit', loadHouses);
	document.getElementById('btn-clear').addEventListener('click', () => 
		document.querySelectorAll('#filter input').forEach(ipt => ipt.value = ''));

	document.querySelector('#filter button[type="submit"]').click();
});

const loadHouses = (ev) => {
	ev.preventDefault();

	// get input without empty values
	const inputs = Array.from(ev.target.querySelectorAll('input'))
		.filter(ipt => {
			ipt.value = ipt.value.trim();

			return ipt.value !== '';
		});

	// convert form into jquery ajax data
	const data = {};
	for(const ipt of inputs)
		data[ipt.name] = ipt.value;

	const msg = document.querySelector('.h-message');
	msg.innerText = '';
	
	$.ajax({
		url: '/casas',
		type: 'GET',
		async: true,
		data,
		success(res) {
			if (res.error) {
				alert(res.error);
				return;
			}

			const ul = document.querySelector('ul.h-list');
			const data = Object.values(res);

			ul.innerHTML = '';
			if (data.length == 0) {
				msg.innerHTML = 'No se encontraron inmuebles en este momento...';
				return
			}

			data.forEach(dt => {
				ul.appendChild(document.createElement('li')).innerHTML = `
					<img src="${dt.photo}">
			
					<div class="h-info">
						<ul>
							<li><i class="material-icons">${(dt.type === 'TERRENO') ? 'terrain' : 'home'}</i> ${dt.type}</li>
							<li><i>${dt.city}, ${dt.state}</i></li>
							<li><b>${dt.rooms} Habitacion(es)</b></li>
							<li><b>${dt.bathrooms} Baño(s)</b></li>
						</ul>
			
						<ul>
							<li><i class="material-icons">${(dt.status === 'EN VENTA') ? 'attach_money' : 'money_off'}</i> ${dt.status}</li>
							<li><b>${dt.price} MXN</b></li>
						</ul>
					</div>
				`;
			});			
		},
		error(xhr, status, error) {
			alert('Las casas no están disponibles en este momento');
		}
	});
};