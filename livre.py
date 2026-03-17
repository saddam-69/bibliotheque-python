class Livre:
    def __init__(self, id, titre, auteur):
        self.id = id
        self.titre = titre
        self.auteur = auteur
        self.disponible = True

    def emprunter(self):
        if self.disponible:
            self.disponible = False
            print(f" '{self.titre}' a été emprunté.")
        else:
            print(f" '{self.titre}' est déjà emprunté.")

    def retourner(self):
        if not self.disponible:
            self.disponible = True
            print(f" '{self.titre}' a été retourné.")
        else:
            print(f" '{self.titre}' n'était pas emprunté.")

    def __str__(self):
        dispo = "Disponible" if self.disponible else "Emprunté"
        return f"[{self.id}] {self.titre} — {self.auteur} ({dispo}) [Type: {self.type_livre()}]"

    def type_livre(self):
        return "Livre classique"


class LivreAudio(Livre):
    def __init__(self, id, titre, auteur, duree_minutes):
        super().__init__(id, titre, auteur)
        self.duree_minutes = duree_minutes

    def type_livre(self):
        return f"Livre Audio ({self.duree_minutes} min)"


class BandeDessinee(Livre):
    def __init__(self, id, titre, auteur, nb_pages):
        super().__init__(id, titre, auteur)
        self.nb_pages = nb_pages

    def type_livre(self):
        return f"Bande Dessinée ({self.nb_pages} pages)"


class Ebook(Livre):
    def __init__(self, id, titre, auteur, format_fichier):
        super().__init__(id, titre, auteur)
        self.format_fichier = format_fichier

    def type_livre(self):
        return f"Ebook ({self.format_fichier})"