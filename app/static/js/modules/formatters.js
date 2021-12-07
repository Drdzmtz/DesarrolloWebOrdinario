
const to_phone = (query) => {
	document.querySelectorAll(query).forEach(e => 
		e.addEventListener('input', () => e.value = e.value.replace(/\D/, '')));
}

const to_name = (query) => {
	document.querySelectorAll(query).forEach(e => 
		e.addEventListener('input', () => e.value = e.value.replace(/[^a-zá-úñ ]/i, '')));
};

export {
	to_phone,
	to_name,
}