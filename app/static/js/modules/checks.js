
const check = (id, cname, ...checks) => {
	let control = document.getElementById(id);

	for(let ch of checks) {
		let err = ch(cname, control, control.value);

		if (err)
			return err;
	}

	return "";
}

const try_match = (v, m, err) => !m.test(v.trim()) ? `${err}\n` : "";

const is_blank = (n, c, v) =>
	!v.trim() ? `El campo ${n} se encuentra vacío\n` : "";

const is_email = (n, c, v) =>
	try_match(v, /^[\w\d._-]+@\w+(?:\.\w+)+$/, `El campo ${n} no tiene un email válido`);

const is_phone = (n, c, v) =>
	try_match(v, /^\d{10}$/, `El campo ${n} no tiene un número de telefono válido`);

export {
	check,
	try_match,
	is_blank,
	is_email,
	is_phone,
};