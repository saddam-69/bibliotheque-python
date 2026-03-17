class Utilisateur:
    def __init__(self, nom):
        self.nom = nom
        self.livres_empruntes = []

    def emprunter_livre(self, livre):
        if livre.disponible:
            livre.emprunter()
            self.livres_empruntes.append(livre)
            print(f" {self.nom} a emprunté '{livre.titre}'.")
        else:
            print(f" '{livre.titre}' n'est pas disponible.")

    def retourner_livre(self, livre):
        if livre in self.livres_empruntes:
            livre.retourner()
            self.livres_empruntes.remove(livre)
            print(f" {self.nom} a retourné '{livre.titre}'.")
        else:
            print(f" {self.nom} n'a pas ce livre.")

    def afficher_emprunts(self):
        if not self.livres_empruntes:
            print(f" {self.nom} n'a aucun livre emprunté.")
        else:
            print(f" Livres empruntés par {self.nom} :")
            for l in self.livres_empruntes:
                print(f"  - {l.titre}")