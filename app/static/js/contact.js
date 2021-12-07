import * as Checks from './modules/checks.js';
import * as Format from './modules/formatters.js';

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

	// Format fields
	Format.to_name("#ffull_name");
	Format.to_phone("#fphone_number");

	// Check fields
	let errs = "".concat(...[
		Checks.check("ffull_name",     	"Nombre del cliente", 	Checks.is_blank),
		Checks.check("femail",       	"Correo",               Checks.is_blank, Checks.is_email),
		Checks.check("fmessage",       	"Mensaje",            	Checks.is_blank),
		Checks.check("fphone_number", 	"Numero de telefono",   Checks.is_blank, Checks.is_phone),
	]);

	if(errs) {
		alert(errs);
		return;
	}

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
            alert("Mensaje Enviado con Exito");
		
		},
		error(xhr, status, error) {
			alert('No se pudo contactar a los administradores');
		}
	});

    clearData();
};
