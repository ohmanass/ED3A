from inventaire import Inventaire # J'importe la classe inventaire qui sera un attribut du dresseur ( il aura la possibilité de choisir des items )

class Dresseur:
    def __init__(self, nom, description, deck):
        self.nom = nom
        self.description = description
        self.deck = deck
        self.inventaire = Inventaire()
        self.portefeuille = 500
        
    def presentation(self):
        print(f"👤 {self.nom} — {self.description}")
        
    def ajouter_item(self, item):
        if self.inventaire.items.get(item, 0) < 2:
            self.inventaire.ajouter(item)
        else:
            print(f"Vous avez déjà 2 exemplaires de {item}.")
            
    def afficher_inventaire(self):
        print(f"Inventaire de {self.nom} :")
        for item, quantite in self.inventaire.items.items():
            print(f"- {item} : {quantite}")
            
    def ajouter_argent(self, montant):
        self.portefeuille += montant
        
    def payer(self, montant):
        if self.portefeuille >= montant:
            self.portefeuille -= montant
            return True
        else:
            print("Fonds insuffisants pour effectuer ce paiement.")
            return False
        
    def afficher_deck(self):
        print(f"Deck de {self.nom} :")
        for pokemon in self.deck:
            print(f"- {pokemon.nom} | Type : {pokemon.type} | PV : {pokemon.pv}")


# --- Liste des dresseurs connus ---
dresseurs_connus = [
    Dresseur("Sacha (Ash Ketchum)", "Le héros principal de l’anime, originaire de Bourg Palette.", []),
    Dresseur("Ondine (Misty)", "Championne d’Azuria, spécialiste des Pokémon de type Eau.", []),
    Dresseur("Pierre (Brock)", "Champion d’Argenta, spécialiste du type Roche.", []),
    Dresseur("Serena", "Amie d’enfance de Sacha, dresseuse et performeuse Pokémon.", []),
    Dresseur("Liko", "Nouvelle protagoniste dans Pokémon Horizons.", []),
    Dresseur("Roy", "Co-protagoniste de Pokémon Horizons, curieux et motivé.", [])
]