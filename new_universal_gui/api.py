import serial.tools.list_ports
from ArDecks import ArDesks

class API:
    def __init__(self):
        self.config = {
            "port": None,
            "action_b1": "",
            "action_b2": "",
            "app1_path": "",
            "app2_path": ""
        }

    def get_serial_ports(self):
        """Retourne la liste des ports disponibles"""
        ports = serial.tools.list_ports.comports()
        return [p.device for p in ports]

    def set_config(self, key, value):
        """Stocke les paramètres envoyés depuis l'interface"""
        self.config[key] = value
        return True

    def start_ardesk(self):
        """Lance l'objet ArDesks"""
        print("Démarrage ArDesks avec config :", self.config)

        ArDesks(
            port_selected=self.config["port"],
            action_b1=self.config["action_b1"],
            action_b2=self.config["action_b2"],
            app_path=[
                self.config["app1_path"],
                self.config["app2_path"]
            ]
        )

        return "ArDesks lancé"
