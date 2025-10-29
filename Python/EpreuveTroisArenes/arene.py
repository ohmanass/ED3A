from pokemon import lst_pkmn_feu, lst_pkmn_eau, lst_pkmn_plante

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
