from flask import Flask, render_template, request, jsonify
from ArDecks import ArDesks
import threading

app = Flask(__name__)

OPTIONS = [
    "selectionez",
    "capture d'ecran",
    "ouvrir une application",
    "augementer le son",
    "baisser le son",
    "executer une command",
    "écrire une phrase",
]

# Instance globale d'ArDesks pour pouvoir l'arrêter
ar_desks_instance = None

@app.route("/")
def index():
    return render_template("index.html", options=OPTIONS)

@app.route("/save", methods=["POST"])
def save():
    global ar_desks_instance
    data = request.json

    # data ressemble à :
    # {
    #   "0": {"action": "écrire une phrase", "value": "bonjour"},
    #   "1": {"action": "capture d'ecran"},
    #   ...
    # }

    print("Données reçues :", data)

    # Arrêter l'instance précédente si elle existe
    if ar_desks_instance:
        ar_desks_instance.exit()
    
    # Créer une nouvelle instance et la lancer dans un thread
    ar_desks_instance = ArDesks(
        port_selected="/dev/ttyUSB0",
        action=data  # Passer directement le JSON avec le mapping
    )
    
    # Lancer ArDesks dans un thread pour ne pas bloquer Flask
    thread = threading.Thread(target=ar_desks_instance.start_listening, daemon=True)
    thread.start()
    
    return jsonify({"status": "success", "received": data})


if __name__ == "__main__":
    app.run(debug=True)
