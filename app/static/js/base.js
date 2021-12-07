
window.addEventListener('load', () => {
	// show options by mobile menu icon
	document.querySelector('#bmenu-icon').addEventListener('click', () => {
		document.querySelectorAll(
			`.b-navbar > ul.bmenu-options, .b-navbar > ul.b-basic-options, .b-navbar > ul.b-af-options`
		).forEach(menu => {
			if(menu.classList.contains('show'))
				menu.classList.remove('show');
			else
				menu.classList.add('show');
		});
	});

	// disable inputs with empty values in the aside's form
	document.querySelector('.b-aside > .b-aform').addEventListener('submit', () => {
		document.querySelectorAll('.b-aside > .b-aform input').forEach(elm => {
			elm.value = elm.value.trim();
			
			if (elm.value === '')
				elm.disabled = true;
		});
	});

	// add redirection functionality to menu buttons
	document.querySelectorAll('li[data-bhref]').forEach(li =>
		li.addEventListener('click', ev => location.href = ev.target.dataset.bhref
	));

	// get news
	$.ajax({
		type: "GET",
		url: "/news",
		success(data) {
			const news = document.querySelector('.b-aside > .b-news > ul');

			Object.values(data).forEach(dt => 
				news.appendChild(document.createElement('li'))
					.innerText = dt.description
			);
		}
	});
});