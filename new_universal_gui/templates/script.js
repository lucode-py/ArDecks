function updateOption(buttonId, value) {
    pywebview.api.set_option(buttonId, value)
        .then(response => {
            console.log("Python a répondu :", response);
        });
}

// Afficher une variable envoyée par Python
function updateFromPython(data) {
    document.getElementById("py-data").innerText = JSON.stringify(data);
}
