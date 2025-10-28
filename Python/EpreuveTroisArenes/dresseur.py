#Ici j'offre la possibilité à l'utilisateur de choisir un dresseur pokémon parmis ceux connues OU créer le siens !
class Dresseur:
    def __init__(self, nom, description, deck):
        self.nom = nom
        self.description = description
        self.deck = deck
        
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