from pokemon import lst_pkmn_feu, lst_pkmn_eau, lst_pkmn_plante

# Classe Arene
class Arene:
    def __init__(self, nom, type_arene, maitre, pokemon_defense, recompense, vague, badge):
        self.nom = nom
        self.type_arene = type_arene
        self.maitre = maitre
        self.pokemon_defense = pokemon_defense
        self.recompense = recompense
        self.vague = vague
        self.badge = badge

    def boss_final(self):
        return self.pokemon_defense[-1] if self.pokemon_defense else None

    def presentation(self):
        print("="*40)
        print(f"Arene : {self.nom} ({self.type_arene})")
        print(f"Champion : {self.maitre}")
        print(f"Vague : {self.vague}")
        print(f"Récompense : {self.recompense} pièces/victoire")
        print("-"*40)
        print("Pokémon défenseurs :")
        for pokemon in self.pokemon_defense:
            print(f"  - {pokemon.nom} (Type : {pokemon.type}, PV : {pokemon.pv})")
        print("="*40)
