console.log("js is working fine.");


document.querySelector("#show-login").addEventListener("click", function(){
    document.querySelector(".popup").classList.add("active");
})

document.querySelector(".popup .close-btn").addEventListener("click", function () {
    document.querySelector(".popup").classList.remove("active");
})