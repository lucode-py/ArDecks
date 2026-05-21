import threading
import os
import sys
import webview
from PIL import Image, ImageDraw
import cairosvg
import pystray
from flask_backend import app  # On importe ton serveur Flask
import io

# Variables globales pour suivre l'état de la fenêtre
window = None
webview_started = False


def run_flask():
    """Lance le serveur Flask en arrière-plan"""
    # debug=False et use_reloader=False sont OBLIGATOIRES en mode threading
    app.run(port=5000, debug=False, use_reloader=False)


def load_svg_icon(svg_path, target_size=(64, 64)):
    """Convertit un fichier SVG en image PIL utilisable par pystray"""
    try:
        # On extrait proprement la largeur et la hauteur cibles (ex: 64 et 64)
        target_w, target_h = target_size

        # 1. On récupère le SVG à sa taille d'origine en PNG pour lire ses dimensions
        init_png = cairosvg.svg2png(url=svg_path)
        raw_img = Image.open(io.BytesIO(init_png))
        orig_w, orig_h = raw_img.size

        # 2. On calcule le ratio de redimensionnement de manière ultra-explicite
        ratio_w = float(target_w) / float(orig_w)
        ratio_h = float(target_h) / float(orig_h)
        ratio = min(ratio_w, ratio_h)

        # 3. Nouvelles dimensions proportionnelles
        new_w = int(orig_w * ratio)
        new_h = int(orig_h * ratio)

        # 4. On génère le PNG final aux bonnes proportions via CairoSVG
        png_data = cairosvg.svg2png(url=svg_path, output_width=new_w, output_height=new_h)
        resized_icon = Image.open(io.BytesIO(png_data))

        # 5. On crée le canevas carré cible ENTIÈREMENT TRANSPARENTE (RGBA)
        final_canvas = Image.new('RGBA', (target_w, target_h), (0, 0, 0, 0))

        # 6. Calcul de la position de centrage
        paste_x = (target_w - new_w) // 2
        paste_y = (target_h - new_h) // 2

        # 7. On colle le logo avec son masque de transparence
        final_canvas.paste(resized_icon, (paste_x, paste_y), resized_icon)

        return final_canvas
    except Exception as e:
        print(f"Erreur lors du chargement du SVG ({e}), retour à l'icône de secours.")
        # Icône de secours au cas où le fichier SVG est introuvable ou corrompu
        return Image.new('RGB', target_size, color=(73, 109, 137))

def show_window(icon, item):
    """Affiche la fenêtre pywebview (ou la recrée si fermée)"""
    global window, webview_started

    if window is None:
        # Création de la fenêtre
        window = webview.create_window(
            "ArDesk Configurator",
            url="http://127.0.0.1:5000",
            width=1300,
            height=900,
            resizable=False,
        )

        # On intercepte la fermeture pour ne pas tuer le script complet
        window.events.closing += on_window_closing

        # pywebview a besoin d'être démarré une première fois via start()
        if not webview_started:
            webview_started = True
            webview.start(debug=True, user_agent="ArDeskAgent")
    else:
        # Si la fenêtre existe déjà (cas des OS qui supportent show/hide)
        window.show()


def on_window_closing():
    """Fonction appelée quand l'utilisateur clique sur la croix de la fenêtre"""
    global window
    # Au lieu de fermer l'application, on cache la fenêtre
    # (ou on nettoie la variable pour la recréer au prochain clic)
    window = None
    print("Fenêtre masquée/fermée. ArDesk tourne toujours en arrière-plan.")


def quit_application(icon, item):
    """Quitte proprement toute l'application ArDesk"""
    print("Arrêt global de ArDesk...")
    icon.stop()  # Arrête l'icône de la barre des tâches
    os._exit(0)  # Force la fermeture de Flask et des ports série en arrière-plan


def setup_tray():
    """Configure et lance l'icône dans la barre des tâches"""
    # Tu pourras remplacer 'create_dummy_icon()' par Image.open("ton_logo.png")
    svg_filename = "logo.svg"
    icon_image = load_svg_icon(svg_filename)

    # Création du menu au clic droit sur l'icône
    menu = pystray.Menu(
        pystray.MenuItem("Ouvrir le configurateur", show_window, default=True),
        pystray.MenuItem("Quitter ArDesk", quit_application)
    )

    icon = pystray.Icon("ArDesk", icon_image, "ArDesk Configurator", menu)

    # Lancement de l'icône (Bloquant, devient le moteur principal de ton app)
    icon.run()


if __name__ == "__main__":
    # 1. On lance Flask dans un thread séparé (daemon=True pour qu'il meure si le main meurt)
    flask_thread = threading.Thread(target=run_flask, daemon=True)
    flask_thread.start()
    print("Backend Flask démarré sur http://127.0.0.1:5000")

    # 2. On lance l'icône de la barre des tâches sur le thread principal
    # C'est elle qui servira de point d'ancrage pour ouvrir pywebview
    setup_tray()