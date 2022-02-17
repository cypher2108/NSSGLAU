console.log("js is working fine.");


// document.querySelector("#show-login").addEventListener("click", function(){
//     document.querySelector(".popup").classList.add("active");
// })

// document.querySelector(".popup .close-btn").addEventListener("click", function () {
//     document.querySelector(".popup").classList.remove("active");
// })

$(function () {
	$('.btn-link[aria-expanded="true"]').closest('.accordion-item').addClass('active');
	$('.collapse').on('show.bs.collapse', function () {
		$(this).closest('.accordion-item').addClass('active');
	});
	$('.collapse').on('hidden.bs.collapse', function () {
		$(this).closest('.accordion-item').removeClass('active');
	});
});