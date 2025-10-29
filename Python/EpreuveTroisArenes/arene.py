from pokemon import lst_pkmn_feu, lst_pkmn_eau, lst_pkmn_plante

# Classe representant une arene Pokemon
class Arene:
    # Constructeur de la classe
    def __init__(self, nom, type_arene, maitre, pokemon_defense, recompense, vague, badge):
        self.nom = nom                  # Nom de l'arene
        self.type_arene = type_arene    # Type de l'arene (Feu, Eau, Plante)
        self.maitre = maitre            # Nom du champion de l'arene
        self.pokemon_defense = pokemon_defense  # Liste de Pokemon defendants dans l'arene
        self.recompense = recompense    # Nombre de pieces gagnees par victoire
        self.vague = vague              # Nombre de vagues ou niveaux avant le boss
        self.badge = badge              # Nom du badge obtenu apres victoire

    # Retourne le Pokemon boss de l'arene (dernier de la liste)
    def boss_final(self):
        return self.pokemon_defense[-1] if self.pokemon_defense else None

    # Affiche les informations de l'arene de maniere lisible
    def presentation(self):
        print("="*40)
        print(f"Arene : {self.nom} ({self.type_arene})")        # Affiche nom et type
        print(f"Champion : {self.maitre}")                     # Affiche le champion
        print(f"Vague : {self.vague}")                         # Affiche le nombre de vagues
        print(f"Recompense : {self.recompense} pieces/victoire")  # Affiche la recompense
        print("-"*40)
        print("Pokemon defenseurs :")                          # Liste des Pokemon dans l'arene
        for pokemon in self.pokemon_defense:
            # Affiche chaque Pokemon avec type et PV
            print(f"  - {pokemon.nom} (Type : {pokemon.type}, PV : {pokemon.pv})")
        print("="*40)