
window.addEventListener('load', () => {
	// show options by mobile menu icon
	document.querySelector('#bmenu-icon').addEventListener('click', () => {
		document.querySelectorAll(
			'.b-navbar > ul.bmenu-options, .b-navbar > ul.b-basic-options'
		).forEach(menu => {
			if(menu.classList.contains('show'))
				menu.classList.remove('show');
			else
				menu.classList.add('show');
		});
	});
});