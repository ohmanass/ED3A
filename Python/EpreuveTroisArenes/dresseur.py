from inventaire import Inventaire # J'importe la classe inventaire qui sera un attribut du dresseur ( il aura la possibilite de choisir des items )

class Dresseur:
    def __init__(self, nom, description, deck=None):
        """
        Initialise un dresseur avec un nom, une description, un deck de pokemons,
        un inventaire d'items et un portefeuille d'argent.
        """
        if deck is None:
            deck = []
        self.nom = nom  # Nom du dresseur
        self.description = description  # Description du dresseur
        self.deck = deck  # Liste des pokemons dans le deck du dresseur
        self.inventaire = Inventaire()  # Inventaire des items possedes par le dresseur
        self.portefeuille = 500  # Argent disponible pour le dresseur
        
    def presentation(self):
        """
        Affiche une presentation simple du dresseur avec son nom et sa description.
        """
        print(f"👤 {self.nom} — {self.description}")
        
    def ajouter_item(self, item):
        """
        Ajoute un item a l'inventaire si le dresseur en possede moins de 2 exemplaires.
        """
        if self.inventaire.items.get(item, 0) < 2:
            self.inventaire.ajouter(item)
        else:
            print(f"Vous avez deja 2 exemplaires de {item}.")
            
    def afficher_inventaire(self):
        """
        Affiche le contenu de l'inventaire du dresseur avec les quantites de chaque item.
        """
        print(f"Inventaire de {self.nom} :")
        for item, quantite in self.inventaire.items.items():
            print(f"- {item} : {quantite}")
            
    def ajouter_argent(self, montant):
        """
        Ajoute une somme d'argent au portefeuille du dresseur.
        """
        self.portefeuille += montant
        
    def payer(self, montant):
        """
        Tente de payer une somme d'argent. Retourne True si le paiement est possible,
        False sinon avec un message d'erreur.
        """
        if self.portefeuille >= montant:
            self.portefeuille -= montant
            return True
        else:
            print("Fonds insuffisants pour effectuer ce paiement.")
            return False
        
    def afficher_deck(self):
        """
        Affiche les pokemons presents dans le deck du dresseur avec leurs details.
        """
        print(f"Deck de {self.nom} :")
        for pokemon in self.deck:
            print(f"- {pokemon.nom} | Type : {pokemon.type} | PV : {pokemon.pv}")

# Cette liste contient des instances predefinies de dresseurs celebres ou protagonistes
# de la serie Pokemon, avec leur nom, une description concise et un deck initial vide.
dresseurs_connus = [
    Dresseur("Sacha (Ash Ketchum)", "Le heros principal de l'anime, originaire de Bourg Palette.", []),
    Dresseur("Ondine (Misty)", "Champione d'Azuria, specialiste des Pokemon de type Eau.", []),
    Dresseur("Pierre (Brock)", "Champion d'Argenta, specialiste du type Roche.", []),
    Dresseur("Serena", "Amie d'enfance de Sacha, dresseuse et performeuse Pokemon.", []),
    Dresseur("Liko", "Nouvelle protagonista dans Pokemon Horizons.", []),
    Dresseur("Roy", "Co-protagoniste de Pokemon Horizons, curieux et motive.", [])
]