function showLog(id) {
    updateActiveButton(id)

    var result_sections = document.getElementsByClassName("board-result")

    for (var i=result_sections.length - 1; i>=0; i--) {
        var result_style = result_sections[i].style
        var result_id = result_sections[i].id
        if (result_id == id) {
            result_style.setProperty("display", "block")
        } else {
            result_style.setProperty("display", "none")
        }
    }
}

async function updateActiveButton(id) {
    var result_buttons = document.getElementsByClassName("board-result-button")

    for (var i=result_buttons.length - 1; i>=0; i--) {
        var button_style = result_buttons[i].style
        var result_id = result_buttons[i].id
        if (result_id == id) {
            button_style.setProperty("font-weight", "bold")
        } else {
            button_style.removeProperty("font-weight")
        }
    }
}