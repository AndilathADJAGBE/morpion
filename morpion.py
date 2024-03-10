import random

def creer_plateau():
    """
    Crée un plateau de jeu vide.
    """
    return [[" "]*3 for _ in range(3)]

def afficher_plateau(plateau):
    """
    Affiche le plateau de jeu.
    """
    for ligne in plateau:
        print("|".join(ligne))
        print("-" * 5)

def placer_pion(plateau, ligne, colonne, symbole):
    """
    Place un pion sur le plateau à la position spécifiée.
    """
    plateau[ligne][colonne] = symbole

def est_emplacement_vide(plateau, ligne, colonne):
    """
    Vérifie si l'emplacement spécifié sur le plateau est vide.
    """
    return plateau[ligne][colonne] == " "

def tour_joueur(plateau):
    """
    Gère le tour du joueur humain.
    """
    while True:
        try:
            ligne = int(input("Entrez le numéro de ligne (0, 1, 2) : "))
            colonne = int(input("Entrez le numéro de colonne (0, 1, 2) : "))

            if 0 <= ligne < 3 and 0 <= colonne < 3 and est_emplacement_vide(plateau, ligne, colonne):
                placer_pion(plateau, ligne, colonne, "X")
                break
            else:
                print("Position invalide, réessayez.")
        except ValueError:
            print("Veuillez entrer un nombre valide.")

def tour_adversaire(plateau):
    """
    Gère le tour de l'adversaire (ordinateur).
    """
    while True:
        ligne = random.randint(0, 2)
        colonne = random.randint(0, 2)

        if est_emplacement_vide(plateau, ligne, colonne):
            placer_pion(plateau, ligne, colonne, "O")
            break

def verifier_victoire(plateau, symbole):
    """
    Vérifie s'il y a une victoire pour le symbole spécifié.
    """
    # Vérification des lignes et colonnes
    for i in range(3):
        if all(plateau[i][j] == symbole for j in range(3)) or all(plateau[j][i] == symbole for j in range(3)):
            return True

    # Vérification des diagonales
    if all(plateau[i][i] == symbole for i in range(3)) or all(plateau[i][2 - i] == symbole for i in range(3)):
        return True

    return False

def jeu():
    """
    Fonction principale pour exécuter le jeu.
    """
    while True:
        plateau = creer_plateau()
        tour = 0

        while True:
            afficher_plateau(plateau)

            if tour % 2 == 0:
                print("Tour du joueur (X)")
                tour_joueur(plateau)
            else:
                print("Tour de l'adversaire (O)")
                tour_adversaire(plateau)

            if verifier_victoire(plateau, "X"):
                afficher_plateau(plateau)
                print("Félicitations ! Vous avez gagné.")
                break
            elif verifier_victoire(plateau, "O"):
                afficher_plateau(plateau)
                print("Dommage ! Vous avez perdu.")
                break
            elif all(plateau[i][j] != " " for i in range(3) for j in range(3)):
                afficher_plateau(plateau)
                print("Match nul !")
                break

            tour += 1

        rejouer = input("Voulez-vous rejouer ? (Oui/Non) : ")
        if rejouer.lower() != "oui":
            break

if __name__ == "__main__":
    jeu()
