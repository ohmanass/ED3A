from pokemon import lst_pokemon

# Classe Arene
class Arene:
    def __init__(self, nom, type_arene, maitre, pokemon_defense, recompense, niveau, badge):
        self.nom = nom
        self.type_arene = type_arene
        self.maitre = maitre
        self.pokemon_defense = pokemon_defense
        self.recompense = recompense
        self.niveau = niveau
        self.badge = badge

    def presentation(self):
        print(f"{self.nom} ({self.type_arene}) - Champion : {self.maitre}, "
              f"Niveau : {self.niveau}, Récompense : {self.recompense} pièces/victoire.")
        print("Pokémon défenseurs :")
        for pokemon in self.pokemon_defense:
            print(f"  - {pokemon.nom} (PV : {pokemon.pv})")

# --- Liste des arènes ---
lst_arenes = [
    Arene("Arène de Flamme", "Feu", "Pyro", [lst_pokemon[0], lst_pokemon[1], lst_pokemon[6], lst_pokemon[7]], 100, 3, "Badge de l'arène de Flamme"),
    Arene("Arène Aquatique", "Eau", "Aqua", [lst_pokemon[2], lst_pokemon[3], lst_pokemon[8], lst_pokemon[9]], 200, 4, "Badge de l'arène Aquatique"),
    Arene("Arène Verdoyante", "Plante", "Florina", [lst_pokemon[4], lst_pokemon[5], lst_pokemon[10], lst_pokemon[11]], 400, 2, "Badge de l'arène Verdoyante"),
]


# Exemple d'affichage uniquement si le fichier est exécuté directement
if __name__ == "__main__":
    for arene in lst_arenes:
        arene.presentation()