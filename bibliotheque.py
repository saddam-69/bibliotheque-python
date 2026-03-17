class Bibliotheque:
    def __init__(self):
        self.livres = []
        self._compteur_id = 1

    def ajouter_livre(self, livre):
        livre.id = self._compteur_id
        self._compteur_id += 1
        self.livres.append(livre)
        print(f" '{livre.titre}' ajouté à la bibliothèque.")

    def supprimer_livre(self, id_livre):
        for livre in self.livres:
            if livre.id == id_livre:
                self.livres.remove(livre)
                print(f" '{livre.titre}' supprimé.")
                return
        print(" Livre introuvable.")

    def rechercher_livre(self, mot_cle):
        resultats = [l for l in self.livres if mot_cle.lower() in l.titre.lower() or mot_cle.lower() in l.auteur.lower()]
        if resultats:
            print(f"\n {len(resultats)} résultat(s) :")
            for l in resultats:
                print(f"  {l}")
        else:
            print(" Aucun livre trouvé.")
        return resultats

    def afficher_livres(self):
        if not self.livres:
            print(" La bibliothèque est vide.")
            return
        print("\n Catalogue de la bibliothèque :")
        print("-" * 60)
        for livre in self.livres:
            print(f"  {livre}")
        print("-" * 60 + "\n")