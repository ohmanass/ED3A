class Boutique:
    def __init__(self, items):
        self.items = items

    def afficher_items(self):
        print("\n=== Boutique Pokémon ===")
        for i, item in enumerate(self.items, 1):
            print(f"{i}. {item.nom} - Prix : {item.prix} Pokédollars - "
                  f"Restaure {item.pv_restaure} PV - {item.description}")