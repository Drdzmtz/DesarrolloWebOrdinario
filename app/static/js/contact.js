window.addEventListener('load', () => {
	document.getElementById('contact-form').addEventListener('submit', contactAdmin);
});

const clearData = () => {
	[
		'ffull_name',
		'femail',
		'fmessage',
		'fphone_number',
	]
	.forEach(id => document.getElementById(id).value = '');
};


const contactAdmin = (ev) => {
	ev.preventDefault();

	// get input without empty values
	var inputs = Array.from(ev.target.querySelectorAll('input'))
		.filter(ipt => {
			ipt.value = ipt.value.trim();

			return ipt.value !== '';
		});

    inputs = inputs.concat(Array.from(ev.target.querySelectorAll('textarea'))
    .filter(ipt => {
        ipt.value = ipt.value.trim();

        return ipt.value !== '';
    }));

	// convert form into jquery ajax data
	const data = {};
	for(const ipt of inputs)
		data[ipt.name] = ipt.value;
	
	$.ajax({
		url: '/contacto/send-mail',
		type: 'POST',
		async: true,
		data,
		success(res) {
			if (res.error) {
				alert(res.error);
				return;
			}

			const data = Object.values(res);
            console.log(data);
		
		},
		error(xhr, status, error) {
			alert('No se pudo contactar a los administradores');
		}
	});

    clearData();
};
