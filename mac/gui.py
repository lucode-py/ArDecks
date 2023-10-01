import serial.tools.list_ports
from PIL import Image
from customtkinter import *
from ArDeck import ArDesks

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

# Initialisez l'objet de port série


# Obtenez la liste des ports série disponibles
ports = serial.tools.list_ports.comports()

name_port = []

# Affichez les informations sur chaque port
for port in ports:
    name_port.append(port.device)

final_port = str
final_b1 = str
final_b2 = str

window = CTk()
window.geometry("920x500")
window.title("ArDecks")

def choose_port(choice):
    global final_port
    final_port = choice
    print(final_port)

def quit_func():
    window.destroy()

def chose_b1(choice):
    global final_b1
    final_b1 = choice

def chose_b2(choice):
    global final_b2
    final_b2 = choice


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
                          values=["capture d'ecran",
                                  "ouvrir une application",
                                  "augementer le son",
                                  "baisser le son",
                                  "executer une command",
                                  "écrire une phrase"
                                  ],
                          command=chose_b1)

option_b1.pack(padx=40, pady=12)

two_button_frame = CTkFrame(central_frame, corner_radius=12, height=200, width=200, fg_color="#332E30")
two_button_frame.grid(row=0, column=1,padx=30)

title_b2 = CTkLabel(two_button_frame, text="boutton 2",  font=("calibri", 25)).pack(pady=12, side=TOP, padx=30)

label_b1 = CTkLabel(two_button_frame, text="configuration du \n deuxième boutton")
label_b1.pack(padx=30, pady=30)

option_b2 = CTkOptionMenu(two_button_frame,
                          values=["capture d'ecran",
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

ArDesks(port_selected=final_port, app=window, action_b1=final_b1, action_b2=final_b2)