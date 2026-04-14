# ArDecks

Un projet permettant de créer des boutons configurables via Arduino et une interface web, avec un programme Python qui gère l'interaction entre le matériel et les actions système.

## Prérequis

- **Python 3.10+** (minimum 3.7, mais 3.10 ou 3.11 recommandés)
- **Arduino** (sketch fourni dans le projet)
- **pip** (gestionnaire de paquets Python)

## Installation

### 1. Créer un environnement virtuel
```bash
python -m venv ArDesk_venv
source ArDesk_venv/bin/activate  # Linux/macOS
# ou
ArDesk_venv\Scripts\activate  # Windows
```

### 2. Installer les dépendances
```bash
pip install -r requirements.txt
```

## Structure du projet

```
new_universal_gui/
├── api.py              # API pour gérer la communication
├── ArDecks.py          # Classe principale de gestion Arduino
├── flask_test.py       # Serveur Flask
├── main.py             # Point d'entrée (interface web)
└── templates/          # Fichiers HTML, CSS, JS
```

## Configuration

### Configuration Arduino
1. Téléverser le sketch depuis `ArDesks/ArDesks_sketch/ArDesks_sketch.ino`
2. Configurer le port série (ex: `/dev/ttyUSB0` sur Linux)

### Configuration des actions
Les actions configurables incluent :
- Capture d'écran
- Ouvrir une application
- Augmenter/Baisser le son
- Exécuter une commande
- Écrire du texte

## Utilisation

Lancer le serveur flask:
```bash
python new_universal_gui/flask_test.py
```

Lancer l'application :
```bash
python new_universal_gui/main.py
```

L'interface web sera accessible à `http://127.0.0.1:5000`

## Dépendances principales

- **Flask** - Framework web
- **pyserial** - Communication Arduino
- **pynput** - Contrôle clavier/souris
- **pywebview** - Interface GUI native

