import subprocess
import serial
import serial.tools.list_ports
import os
import sys


class ArDesks:
    def __init__(self, port_selected, action):
        """""
        action: dict JSON avec la structure:
        {
            "0": {"action": "ouvrir une application", "value": "appname"},
            "1": {"action": "capture d'ecran"},
            "2": {"action": "écrire une phrase", "value": "texte"},
            ...
        }
        """
        self.port_selected = port_selected
        self.action_map = action  # Stocker le mapping complet
        self.keyboard = None  # Initialisé tardivement
        self.running = True
        
        # Mapping des actions texte aux méthodes
        self.action_handlers = {
            "ouvrir une application": self.open_app,
            "capture d'ecran": self.screen_capture,
            "écrire une phrase": self.type_text,
            "executer une command": self.execute_command,
            "augementer le son": self.increase_volume,
            "baisser le son": self.decrease_volume,
        }
        
        self.start_listening()

    def start_listening(self):
        """Écoute le port série et déclenche les actions"""
        # Importer pynput seulement quand nécessaire
        try:
            from pynput.keyboard import Controller
            self.keyboard = Controller()
        except ImportError as e:
            print(f"Avertissement: pynput non disponible: {e}")
            self.keyboard = None
        
        try:
            ser = serial.Serial(self.port_selected, baudrate=9600, timeout=1)
        except Exception as e:
            print(f"Erreur: impossible d'ouvrir le port {self.port_selected}: {e}")
            return

        while self.running:
            try:
                data = ser.readline().decode('utf-8').strip()
                if data in self.action_map:
                    action_info = self.action_map[data]
                    action_type = action_info.get("action")
                    value = action_info.get("value")
                    
                    if action_type in self.action_handlers:
                        handler = self.action_handlers[action_type]
                        if value:
                            handler(value)
                        else:
                            handler()
                    else:
                        print(f"Action non reconnue: {action_type}")
                else:
                    print(f"Clé non reconnue: {data}")
            except KeyboardInterrupt:
                print("Arrêt de la lecture.")
                break
            except Exception as e:
                print(f"Erreur lors de la lecture: {e}")

        # Fermez le port série à la fin
        ser.close()
        
    def open_app(self, app_name):
        """Ouvre une application"""
        try:
            if sys.platform == "darwin":  # macOS
                cmd = f'open -a "{app_name}"'
            elif sys.platform == "linux":  # Linux
                cmd = app_name
            elif sys.platform == "win32":  # Windows
                cmd = f'start {app_name}'
            
            print(f"Exécution: {cmd}")
            subprocess.run(cmd, shell=True, universal_newlines=True)
        except Exception as e:
            print(f"Erreur lors de l'ouverture de l'app: {e}")

    def screen_capture(self):
        """Prend une capture d'écran"""
        try:
            if sys.platform == "darwin":  # macOS
                subprocess.run('open /System/Applications/Utilities/Screenshot.app', 
                             shell=True, universal_newliukgugugnes=True)
            elif sys.platform == "linux":  # Linux
                subprocess.run('gnome-screenshot', shell=True, universal_newlines=True)
            elif sys.platform == "win32":  # Windows
                subprocess.run('screencapture -c', shell=True, universal_newlines=True)
        except Exception as e:
            print(f"Erreur capture d'écran: {e}")

    def type_text(self, text):
        """Écrit un texte via le clavier"""
        try:
            if self.keyboard is None:
                print("Erreur: clavier non disponible")
                return
            self.keyboard.type(text)
            print(f"Texte écrit: {text}")
        except Exception as e:
            print(f"Erreur lors de l'écriture: {e}")

    def execute_command(self, command):
        """Exécute une commande shell"""
        try:
            result = subprocess.run(command, shell=True, 
                                  universal_newlines=True, 
                                  capture_output=True)
            print(f"Commande exécutée: {command}")
            print(f"Sortie: {result.stdout}")
            if result.stderr:
                print(f"Erreur: {result.stderr}")
        except Exception as e:
            print(f"Erreur lors de l'exécution: {e}")

    def increase_volume(self):
        """Augmente le volume"""
        try:
            if sys.platform == "darwin":
                subprocess.run('osascript -e "set volume output volume (output volume of (get volume settings) + 5)"', 
                             shell=True)
            elif sys.platform == "linux":
                subprocess.run('pactl set-sink-volume @DEFAULT_SINK@ +5%', shell=True)
        except Exception as e:
            print(f"Erreur volume: {e}")

    def decrease_volume(self):
        """Baisse le volume"""
        try:
            if sys.platform == "darwin":
                subprocess.run('osascript -e "set volume output volume (output volume of (get volume settings) - 5)"', 
                             shell=True)
            elif sys.platform == "linux":
                subprocess.run('pactl set-sink-volume @DEFAULT_SINK@ -5%', shell=True)
        except Exception as e:
            print(f"Erreur volume: {e}")

    def exit(self):
        """Arrête l'écoute"""
        self.running = False