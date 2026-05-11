import webview



window = webview.create_window(
    "ArDesk Configurator",
    url="http://127.0.0.1:5000",
    width=1300,
    height=900,
    resizable=False,
)

webview.start(debug=True)
