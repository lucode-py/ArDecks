from PIL import ImageGrab

print("--- MENU CAPTURE D'ÉCRAN ---")
print("1. Prendre une capture maintenant")
print("2. Quitter")

reponse = input("Fais ton choix : ")

if reponse == "1":
    capture = ImageGrab.grab()
    capture.save("ma_capture.png")
    print("Capture reussie !")
    print("Regarde dans la liste de tes fichiers sur la gauche !")

elif reponse == "2":
    print("Fin du programme.")

else:
    print("Tu n'as pas tape 1 ou 2.")