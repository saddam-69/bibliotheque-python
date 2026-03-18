from livre import Livre, LivreAudio, BandeDessinee, Ebook
from bibliotheque import Bibliotheque
from utilisateur import Utilisateur

bibli = Bibliotheque()
utilisateurs = []

def creer_livre():
    print("\nType de livre :")
    print("1. Classique  2. Audio  3. BD  4. Ebook")
    choix = input("Choix : ")
    titre = input("Titre : ")
    auteur = input("Auteur : ")
    id_temp = 0  

    if choix == "1":
        return Livre(id_temp, titre, auteur)
    elif choix == "2":
        duree = int(input("Durée (minutes) : "))
        return LivreAudio(id_temp, titre, auteur, duree)
    elif choix == "3":
        pages = int(input("Nombre de pages : "))
        return BandeDessinee(id_temp, titre, auteur, pages)
    elif choix == "4":
        fmt = input("Format (PDF/EPUB/MOBI) : ")
        return Ebook(id_temp, titre, auteur, fmt)
    else:
        print("Type invalide, livre classique créé par défaut.")
        return Livre(id_temp, titre, auteur)

def menu_utilisateur():
    nom = input("Nom de l'utilisateur : ")
    user = next((u for u in utilisateurs if u.nom == nom), None)
    if not user:
        user = Utilisateur(nom)
        utilisateurs.append(user)
        print(f" Nouvel utilisateur '{nom}' créé.")

    while True:
        print(f"\n--- Menu utilisateur : {nom} ---")
        print("1. Emprunter un livre")
        print("2. Retourner un livre")
        print("3. Voir mes emprunts")
        print("4. Retour")
        choix = input("Choix : ")

        if choix == "1":
            bibli.afficher_livres()
            try:
                id_l = int(input("ID du livre à emprunter : "))
                livre = next((l for l in bibli.livres if l.id == id_l), None)
                if livre:
                    user.emprunter_livre(livre)
                else:
                    print(" ID introuvable.")
            except ValueError:
                print(" Entrée invalide.")

        elif choix == "2":
            user.afficher_emprunts()
            try:
                id_l = int(input("ID du livre à retourner : "))
                livre = next((l for l in user.livres_empruntes if l.id == id_l), None)
                if livre:
                    user.retourner_livre(livre)
                else:
                    print(" Vous n'avez pas ce livre.")
            except ValueError:
                print(" Entrée invalide.")

        elif choix == "3":
            user.afficher_emprunts()

        elif choix == "4":
            break

def menu_principal():
    while True:
        print("\n====== BIBLIOTHÈQUE — Menu Principal ======")
        print("1. Ajouter un livre")
        print("2. Afficher tous les livres")
        print("3. Rechercher un livre")
        print("4. Supprimer un livre")
        print("5. Espace utilisateur (emprunts)")
        print("6. Quitter")
        choix = input("Votre choix : ")

        if choix == "1":
            livre = creer_livre()
            bibli.ajouter_livre(livre)
        elif choix == "2":
            bibli.afficher_livres()
        elif choix == "3":
            mot = input("Mot-clé : ")
            bibli.rechercher_livre(mot)
        elif choix == "4":
            bibli.afficher_livres()
            try:
                id_sup = int(input("ID à supprimer : "))
                bibli.supprimer_livre(id_sup)
            except ValueError:
                print(" Entrée invalide.")
        elif choix == "5":
            menu_utilisateur()
        elif choix == "6":
            print(" Au revoir !")
            break
        else:
            print(" Choix invalide.")
menu_principal()