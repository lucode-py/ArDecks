import serial.tools.list_ports
from PIL import Image
from ArDeck import ArDesks
import os
from customtkinter import CTk, CTkLabel, CTkEntry, CTkButton, CTkFrame, CTkImage, CTkOptionMenu
from tkinter import TOP, BOTTOM, YES

image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../asset")

one_image = CTkImage(light_image=Image.open(os.path.join(image_path, "1_dark.png")),
                     dark_image=Image.open(os.path.join(image_path, "1_white.png")),
                     size=(20, 20))

two_image = CTkImage(light_image=Image.open(os.path.join(image_path, "2_dark.png")),
                     dark_image=Image.open(os.path.join(image_path, "2_white.png")),
                     size=(20, 20))

three_image = CTkImage(light_image=Image.open(os.path.join(image_path, "3_dark.png")),
                       dark_image=Image.open(os.path.join(image_path, "3_white.png")),
                       size=(20, 20))

four_image = CTkImage(light_image=Image.open(os.path.join(image_path, "4_dark.png")),
                      dark_image=Image.open(os.path.join(image_path, "4_white.png")),
                      size=(20, 20))

# Spécifiez le port série utilisé par votre Arduino
port = '/dev/cu.usbserial-210'  # ou quelque chose comme 'COM3' sous Windows

# Obtenez la liste des ports série disponibles
ports = serial.tools.list_ports.comports()

name_port = []

# Affichez les informations sur chaque port
for port in ports:
    name_port.append(port.device)

final_port = str
final_b1 = str
final_b2 = str
user_input_apps = ["", ""]

window = CTk()
window.geometry("920x500")
window.title("ArDecks")


def choose_port(choice):
    global final_port
    final_port = choice
    print(final_port)


def quit_func():
    global final_b1, final_b2

    if final_b1 == "ouvrir une application":
        popup_app("bouton 1", 0)

    if final_b2 == "ouvrir une application":
        popup_app("bouton 2", 1)

    window.destroy()


class PopupApp:
    def __init__(self, title, nb):
        self.index = nb
        self.popup_window = CTk()
        self.popup_window.title(title)
        self.popup_window.geometry("280x100")

        label = CTkLabel(self.popup_window, text=f"entrez le chemin de l'application {title} :")
        label.pack()

        self.entry = CTkEntry(self.popup_window)
        self.entry.pack()

        ok_button = CTkButton(self.popup_window, text="OK", command=self.on_ok_click)
        ok_button.pack()

        self.popup_window.protocol("WM_DELETE_WINDOW", self.on_close)

    def on_ok_click(self):
        user_input_apps[self.index] = self.entry.get()
        print(f"Entrée utilisateur bouton {self.index + 1}:", user_input_apps[self.index])
        self.popup_window.withdraw()  # Cacher temporairement la fenêtre
        self.popup_window.destroy()  # Détruire la fenêtre

    def on_close(self):
        self.popup_window.withdraw()  # Cacher temporairement la fenêtre
        self.popup_window.destroy()  # Détruire la fenêtre


def chose_b1(choice):
    global final_b1
    final_b1 = choice


def chose_b2(choice):
    global final_b2
    final_b2 = choice


def popup_app(title, nb):
    app_popup = PopupApp(title, nb)
    app_popup.popup_window.deiconify()  # Réafficher la fenêtre


option_port = CTkOptionMenu(window, values=name_port, command=choose_port)
option_port.pack(pady=12)

central_frame = CTkFrame(window, fg_color="transparent")
central_frame.pack(expand=YES)

frame_b1 = CTkFrame(central_frame, corner_radius=12, height=200, width=200, fg_color="#332E30")
frame_b1.grid(row=0, column=0, padx=30)

title_b1 = CTkLabel(frame_b1, text="boutton 1", font=("calibri", 25)).pack(pady=12, side=TOP, padx=30)

label_b1 = CTkLabel(frame_b1, text="configuration du \n premier boutton")
label_b1.pack(padx=30, pady=30)
option_b1 = CTkOptionMenu(frame_b1,
                          values=["selectionez",
                                  "capture d'ecran",
                                  "ouvrir une application",
                                  "augementer le son",
                                  "baisser le son",
                                  "executer une command",
                                  "écrire une phrase"
                                  ],
                          command=chose_b1)

option_b1.pack(padx=40, pady=12)

two_button_frame = CTkFrame(central_frame, corner_radius=12, height=200, width=200, fg_color="#332E30")
two_button_frame.grid(row=0, column=1, padx=30)

title_b2 = CTkLabel(two_button_frame, text="boutton 2", font=("calibri", 25)).pack(pady=12, side=TOP, padx=30)

label_b1 = CTkLabel(two_button_frame, text="configuration du \n deuxième boutton")
label_b1.pack(padx=30, pady=30)

option_b2 = CTkOptionMenu(two_button_frame,
                          values=["selectionnez",
                                  "capture d'ecran",
                                  "ouvrir une application",
                                  "augementer le son",
                                  "baisser le son",
                                  "executer une command",
                                  "écrire une phrase"
                                  ],
                          command=chose_b2)
option_b2.pack(padx=40, pady=12)

done_button = CTkButton(window, text="Done", command=quit_func)
done_button.pack(side=BOTTOM, pady=12)

window.mainloop()

# Créez l'objet ArDesks après la boucle principale d'interface graphique
ArDesks(port_selected=final_port, action_b1=final_b1, action_b2=final_b2, app_path=user_input_apps)
