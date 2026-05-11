import time # Pour pouvoir faire des pauses

# 1. On pose la question à l'utilisateur
# input() attend que tu tapes quelque chose et que tu appuies sur Entrée
choix = input("Veux-tu un timer de 15 ou 20 minutes ? (Tape le nombre) : ")

# 2. On transforme ton texte en nombre (entier)
chose_minutes = int(choix)

def minuteur(minutes):

    # 3. On calcule le total de secondes
    secondes = minutes * 60
    # 4. La boucle qui compte
    while secondes > 0:
        print(f"Temps restant : {secondes} secondes")
        time.sleep(1)      # On attend 1 seconde pile
        secondes = secondes - 1 # On enlève 1 seconde au total

    print("BIIIIP ! C'est fini !")

minuteur(chose_minutes)