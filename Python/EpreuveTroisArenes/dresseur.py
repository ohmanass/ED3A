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


# --- Liste des dresseurs connus ---
dresseurs_connus = [
    Dresseur("Sacha (Ash Ketchum)", "Le héros principal de l’anime, originaire de Bourg Palette.", []),
    Dresseur("Ondine (Misty)", "Championne d’Azuria, spécialiste des Pokémon de type Eau.", []),
    Dresseur("Pierre (Brock)", "Champion d’Argenta, spécialiste du type Roche.", []),
    Dresseur("Serena", "Amie d’enfance de Sacha, dresseuse et performeuse Pokémon.", []),
    Dresseur("Liko", "Nouvelle protagoniste dans Pokémon Horizons.", []),
    Dresseur("Roy", "Co-protagoniste de Pokémon Horizons, curieux et motivé.", [])
]