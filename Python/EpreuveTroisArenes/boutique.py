class Boutique:
    def __init__(self, items):
        self.items = items

    def afficher_items(self):
        print("\n=== Boutique Pokémon ===")
        for i, item in enumerate(self.items, 1):
            print(f"{i}. {item.nom} - Prix : {item.prix} Pokédollars - "
                  f"Restaure {item.pv_restaure} PV - {item.description}")

    def acheter_item(self, dresseur):
        print("\n=== Acheter un item ===")
        for i, item in enumerate(self.items, 1):
            print(f"{i}. {item.nom} - Prix : {item.prix} Pokédollars - "
                  f"Restaure {item.pv_restaure} PV - {item.description}")
        try:
            choix = int(input("Choisissez le numéro de l'item à acheter : "))
            if choix < 1 or choix > len(self.items):
                print("Choix invalide.")
                return
        except ValueError:
            print("Entrée invalide.")
            return

        item_choisi = self.items[choix - 1]
        nb_exemplaires = sum(1 for it in dresseur.inventaire.items if it.nom == item_choisi.nom)

        if nb_exemplaires >= 2:
            print(f"Vous possédez déjà 2 exemplaires de {item_choisi.nom}. Vous ne pouvez pas en acheter plus.")
            return

        if dresseur.portefeuille < item_choisi.prix:
            print("Fonds insuffisants pour cet achat.")
            return

        dresseur.portefeuille -= item_choisi.prix
        dresseur.inventaire.items.append(item_choisi)
        print(f"Achat réussi : {item_choisi.nom} ajouté à votre inventaire.")