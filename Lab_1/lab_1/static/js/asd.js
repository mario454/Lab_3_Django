// alert("Hello from JS")

var footer = document.getElementById("footer");

if (document.body.scrollHeight <= window.innerHeight) {
    footer.classList.add("footer_normal");
} else {
    footer.classList.add("footer_exceed");
}

window.addEventListener("resize", () => {
        if (document.body.scrollHeight <= window.innerHeight) {
            footer.classList.add("footer_normal");
            footer.classList.remove("footer_exceed");
        } else {
            footer.classList.add("footer_exceed");
            footer.classList.remove("footer_normal");
        }
    });