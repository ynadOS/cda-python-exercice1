# définir la classe livre avec titre, auteur et date de parution __init__
# définir affichage avec __str__
# faire une liste de livres (tableau vide)
# fonction ajouter un livre
# fonction afficher les livres
# fonctioin pour rechercher des livres par leur titre
# supprimer un livre avec remove()
# faire une liste avec les actions à faire

class Livre:
    def __init__(self, titre, auteur, date_parution):
        self.titre = titre
        self.auteur = auteur
        self.date_parution = date_parution
    def __str__(self):
        return (f"Le livre {self.titre}, écrit par {self.auteur}, qui a été publié en {self.date_parution}")

class Bibliotheque:
    def __init__(self):
        self.liste_livres = []

    def ajouter_livre(self, titre, auteur, date_parution):
        nouveau_livre = Livre(titre, auteur, date_parution)
        self.liste_livres.append(nouveau_livre)
        print(f"Le livre {titre} a bien été ajouté !")

    def afficher_livres(self):
        print("Voici la liste des livres :")
        for index, livre in enumerate(self.liste_livres):
            print(index, livre)

    def supprimer_livre(self, index):
            livre_supprime = self.liste_livres[index]
            self.liste_livres.remove(livre_supprime)
            print(f"Le livre '{livre_supprime.titre}' a été supprimé avec succès.")

    # def cherher_livre(self):


def afficher_menu():
    print("Que voulez-vous faire ?")
    print("1. Ajouter un livre")
    print("2. Afficher des livres")
    print("3. Rechercher un livre par son titre")
    print("4. Supprimer un livre")
    print("5. Quitter")

ma_bibliotheque = Bibliotheque()

while True:
    afficher_menu()
    choix = int((input("Tapez le numéro de votre choix : ")))
    if choix == 1:
        titre = input("Saisir titre : ")
        auteur = input("Saisir auteur : ")
        date_parution = input("Saisir date : ")
        ma_bibliotheque.ajouter_livre(titre, auteur, date_parution)
    elif choix == 2:
        print("choix 2 pour afficher des livres")
        ma_bibliotheque.afficher_livres()
    elif choix == 3:
        print("choix 3 pour rechercher un livre")
    elif choix == 4:
        ma_bibliotheque.afficher_livres()
        livre_effacer = int(input("Quel livre voulez-vous supprimer ? Mettre son numéro : "))
        print("choix 4 pour supprimer un livre")
        ma_bibliotheque.supprimer_livre(livre_effacer)
        print("Voici la liste mise à jour")

    elif choix == 5:
        print("choix 5 pour sortir de l'app")
        break
    else:
        print("Ça n'existe pas ça, mets un numéro qui existe quand même !")






# ma_bibliotheque.afficher_livres()