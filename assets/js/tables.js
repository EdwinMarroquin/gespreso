(async () => {
    await document.querySelectorAll(".tableId").forEach(async function (t) {
        console.log(t)
        await t.addEventListener('click', async function (e) {
            el = e.target;
            if (el.attributes["aria-label"].value == "showBody") {
                await t.childNodes[2].classList.toggle('hide')
            }
        })
    })
})()

