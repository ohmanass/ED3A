class Inventaire:
    def __init__(self):
        self.items = {}

    def afficher_items(self):
        print("Inventaire :")
        for nom, item in self.items.items():
            print(f"{nom} - Quantité: {item['quantite']}, Prix: {item['prix']}, Description: {item['description']}")

    def ajouter_item(self, nom, prix, description):
        if nom in self.items:
            if self.items[nom]['quantite'] < 2:
                self.items[nom]['quantite'] += 1
                print(f"Un exemplaire de {nom} a été ajouté à l'inventaire.")
            else:
                print(f"Vous ne pouvez pas avoir plus de 2 exemplaires de {nom}.")
        else:
            self.items[nom] = {'quantite': 1, 'prix': prix, 'description': description}
            print(f"{nom} a été ajouté à l'inventaire.")