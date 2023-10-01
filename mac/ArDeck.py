import subprocess
import serial
import serial.tools.list_ports
from pynput.keyboard import Key, Controller




class ArDesks:
    def __init__(self, port_selected, app, action_b1, action_b2):
        app.quit()

        ser = serial.Serial(port_selected, baudrate=9600, timeout=1)

        self.keyboard = Controller()

        while True:
            try:
                data = ser.readline().decode('utf-8')
                print(data)
                """try:
                    volume = float(data)
                    print(volume)
                    def_volume = f'osascript -e "set volume output volume {volume}"'
        
                    os.system(def_volume)
                except ValueError:"""
                # Lisez les données du port série

                if data.strip() == "S1":
                    if action_b1 == "ouvrir une application":
                        self.open_app(NB=1)
                    elif action_b1 == "capture d'ecran":
                        self.screen_capture()
                    elif action_b1 == "écrire une phrase":
                        self.type_caratere(NB=1)

                if data.strip() == "S2":
                    if action_b2 == "ouvrir une application":
                        self.open_app(NB=2)
                    elif action_b1 == "capture d'ecran":
                        self.screen_capture()
                    elif action_b2 == "écrire une phrase":
                        self.type_caratere(NB=2)

            except KeyboardInterrupt:
                print("Arrêt de la lecture.")
                break

        # Fermez le port série à la fin
        ser.close()

    def open_app(self, NB):
        if NB == 1:
            commandeB1 = 'open /Applications/Discord.app'
            subprocess.run(commandeB1, shell=True, universal_newlines=True)
        elif NB == 2:
            commandeB2: str = 'open /System/Applications/Utilities/Terminal.app'
            subprocess.run(commandeB2, shell=True, universal_newlines=True)

    def type_caratere(self, NB):
        if NB == 1:
            self.keyboard.type("≥")
        elif NB == 2:
            self.keyboard.type("≥")

    def screen_capture(self):
        commandescreen = 'open /System/Applications/Utilities/Screenshot.app'
        subprocess.run(commandescreen, shell=True, universal_newlines=True)