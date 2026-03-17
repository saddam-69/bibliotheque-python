livres = []  

def ajouter_livre():
    id_livre = len(livres) + 1
    titre = input("Titre du livre : ")
    auteur = input("Auteur : ")
    livre = {"id": id_livre, "titre": titre, "auteur": auteur, "disponible": True}
    livres.append(livre)
    print(f" Livre '{titre}' ajouté avec succès !\n")

def afficher_livres():
    if not livres:
        print(" Aucun livre dans la bibliothèque.\n")
        return
    print("\n Liste des livres :")
    print("-" * 50)
    for livre in livres:
        dispo = "Disponible" if livre["disponible"] else "Emprunté"
        print(f"[{livre['id']}] {livre['titre']} — {livre['auteur']} ({dispo})")
    print("-" * 50 + "\n")

def rechercher_livre():
    mot = input("Rechercher (titre ou auteur) : ").lower()
    resultats = [l for l in livres if mot in l["titre"].lower() or mot in l["auteur"].lower()]
    if resultats:
        print("\n🔍 Résultats :")
        for l in resultats:
            print(f"  - {l['titre']} par {l['auteur']}")
    else:
        print(" Aucun livre trouvé.\n")

def supprimer_livre():
    afficher_livres()
    try:
        id_sup = int(input("ID du livre à supprimer : "))
        livre_trouve = None
        for l in livres:
            if l["id"] == id_sup:
                livre_trouve = l
                break
        if livre_trouve:
            livres.remove(livre_trouve)
            print(f" Livre supprimé.\n")
        else:
            print(" ID introuvable.\n")
    except ValueError:
        print(" Entrée invalide.\n")

def menu():
    while True:
        print("=== MENU BIBLIOTHÈQUE ===")
        print("1. Ajouter un livre")
        print("2. Afficher tous les livres")
        print("3. Rechercher un livre")
        print("4. Supprimer un livre")
        print("5. Quitter")
        choix = input("Votre choix : ")

        if choix == "1":
            ajouter_livre()
        elif choix == "2":
            afficher_livres()
        elif choix == "3":
            rechercher_livre()
        elif choix == "4":
            supprimer_livre()
        elif choix == "5":
            print("Au revoir !")
            break
        else:
            print(" Choix invalide.\n")

menu()