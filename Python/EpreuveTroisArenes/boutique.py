# Classe representant notre boutique Pokemon
class Boutique:
    def __init__(self, items):
        # Initialise la boutique avec une liste d'items disponibles à la vente
        self.items = items

    def afficher_items(self):
        # Affiche la liste des items disponibles dans la boutique avec leurs details
        print("\n=== Boutique Pokemon ===")
        for i, item in enumerate(self.items, 1):
            print(f"{i}. {item.nom} - Prix : {item.prix} Pokedollars - "
                  f"Restaure {item.pv_restaure} PV - {item.description}")

    def acheter_item(self, dresseur):
        # Permet au dresseur d'acheter un item dans la boutique
        # Affiche les items disponibles avec leurs details
        print("\n=== Acheter un item ===")
        for i, item in enumerate(self.items, 1):
            print(f"{i}. {item.nom} - Prix : {item.prix} Pokedollars - "
                  f"Restaure {item.pv_restaure} PV - {item.description}")
        try:
            # Demande a l'utilisateur de choisir un item par son numero
            choix = int(input("Choisissez le numero de l'item a acheter : "))
            if choix < 1 or choix > len(self.items):
                # Verification que le choix est dans la plage valide
                print("Choix invalide.")
                return
        except ValueError:
            # Gestion d'une entree non numerique
            print("Entree invalide.")
            return

        # Recupere l'item choisi par l'utilisateur
        item_choisi = self.items[choix - 1]
        # Compte combien d'exemplaires de cet item le dresseur possede deja
        nb_exemplaires = sum(1 for it in dresseur.inventaire.items if it.nom == item_choisi.nom)

        # Limite a 2 exemplaires du meme item dans l'inventaire
        if nb_exemplaires >= 2:
            print(f"Vous possedez deja 2 exemplaires de {item_choisi.nom}. Vous ne pouvez pas en acheter plus.")
            return

        # Verification que le dresseur a assez de fonds pour acheter l'item
        if dresseur.portefeuille < item_choisi.prix:
            print("Fonds insuffisants pour cet achat.")
            return

        # Deduit le prix de l'item du portefeuille du dresseur
        dresseur.portefeuille -= item_choisi.prix
        # Ajoute l'item achete a l'inventaire du dresseur
        dresseur.inventaire.items.append(item_choisi)
        print(f"Achat reussi : {item_choisi.nom} ajoute a votre inventaire.")