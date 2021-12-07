
window.addEventListener('load', () => {
	document.getElementById('h-form').addEventListener('submit', async (ev) => {
		ev.preventDefault();
		
		const data = {};
		const errors = [];
		const inputs = Array.from(ev.target.querySelectorAll('input:not([type="file"]), textarea, select'));

		for(let ipt of inputs) {
			data[ipt.name] = ipt.value.trim();

			if (ipt.name === 'id') continue;
			if (data[ipt.name] === '')
				errors.push(`El campo ${ipt.dataset.realName} se encuentra vacío.\n`);
		}

		if (errors.length > 0) {
			alert(''.concat(...errors))
			return;
		}
			
		// get photo
		const file = document.getElementById('fphoto').files[0];
		if (file)
			data.photo = await toBase64(file);

		$.ajax({
			url: '/casas/',
			type: data.id ? 'PUT' : 'POST',
			async: true,
			data,
			success(res) {
				if (res.Error) {
					alert(res.Error);
					return;
				}

				alert(`El inmueble se ha ${data.id ? 'actualizado' : 'añadido'} correctamente`);
				location.reload();
			},
			error(xhr, status, error) {
				alert('El inmueble no ha podido ser guardado en este momento');
			}
		});
	});
});

const toBase64 = file => new Promise((resolve, reject) => {
	const reader = new FileReader();
	
	reader.readAsDataURL(file);
	reader.onload = () => resolve(reader.result);
	reader.onerror = error => reject(error);
});