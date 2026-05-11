import tkinter as tk

fenetre = tk.Tk()
fenetre.withdraw()

print("--- MENU COLLAGE ---")
print("1. Afficher mon texte")
print("2. Quitter")

reponse = input("Fais ton choix : ")

if reponse == "1":
    resultat = fenetre.clipboard_get()
    print("Le texte colle est :")
    print(resultat)

elif reponse == "2":
    print("Fin du programme.")

else:
    print("Tu n'as pas tape 1 ou 2.")

fenetre.destroy()