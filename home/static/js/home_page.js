const buttons = Array.from(document.getElementsByClassName("portfolio-item-caption"))
buttons.forEach(button => {
    button.addEventListener("click", (e) => {
        window.location.href = e.target.attributes.link.value
    })
})
