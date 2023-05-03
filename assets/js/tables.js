let tables = document.querySelectorAll(".tableId")
tables.forEach(function (t) {
    t.addEventListener('click', function (e) {
        el = e.target;
        if (el.attributes["aria-label"].value == "showBody") {
            t.childNodes[2].classList.toggle('hide')
        }
    })
})
