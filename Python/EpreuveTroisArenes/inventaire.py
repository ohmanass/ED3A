class Inventaire:
    def __init__(self):
        # Dictionnaire pour stocker les items avec leurs details: quantite, prix, description
        self.items = {}

    def afficher_items(self):
        # Affiche la liste des items presentes dans l'inventaire avec leurs details
        print("Inventaire :")
        for nom, item in self.items.items():
            print(f"{nom} - Quantite: {item['quantite']}, Prix: {item['prix']}, Description: {item['description']}")

    def ajouter_item(self, nom, prix, description):
        # Ajoute un item a l'inventaire ou incremente sa quantite si deja present
        # Limitation a 2 exemplaires par item pour eviter accumulation excessive du meme article
        if nom in self.items:
            if self.items[nom]['quantite'] < 2:
                self.items[nom]['quantite'] += 1
                print(f"Un exemplaire de {nom} a ete ajoute a l'inventaire.")
            else:
                print(f"Vous ne pouvez pas avoir plus de 2 exemplaires de {nom}.")
        else:
            self.items[nom] = {'quantite': 1, 'prix': prix, 'description': description}
            print(f"{nom} a ete ajoute a l'inventaire.")