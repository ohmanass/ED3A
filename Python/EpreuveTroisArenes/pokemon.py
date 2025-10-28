# Tableau des multiplicateurs de dégâts en fonction du type selon les règles de bases du Jeu
efficacite = {
    "Feu": {"Feu": 1, "Eau": 0.5, "Plante": 2},
    "Eau": {"Feu": 2, "Eau": 1, "Plante": 0.5},
    "Plante": {"Feu": 0.5, "Eau": 2, "Plante": 1}
}

class Pokemon:
    def __init__(self, nom, type_, pv, attaque, attaque_spe, description=""):
        self.nom = nom
        self.type = type_
        self.pv = pv
        self.attaque = attaque
        self.attaque_spe = attaque_spe
        self.description = description

    def presentation(self):
        print(f"Je suis {self.nom}, de type {self.type}, avec {self.pv} PV et attaque spéciale : {self.attaque_spe} ({self.attaque} dégâts).")
        if self.description:
            print(f"Description : {self.description}")

    def attaquer(self, cible):
            mult = efficacite[self.type][cible.type]
            degats = int(self.attaque * mult)
            
            if mult > 1:
                print("C'est super efficace ! ⚡")
            elif mult < 1:
                print("Ce n'est pas très efficace… 😕")
            
            print(f"{self.nom} attaque {cible.nom} avec {self.attaque_spe} et inflige {degats} dégâts 💥 !")
            cible.pv -= degats
            if cible.pv < 0:
                cible.pv = 0
            print(f"{cible.nom} a maintenant {cible.pv} PV restants.\n")


class PokemonFeu(Pokemon):
    def __init__(self, nom, pv, attaque, attaque_spe, description=""):
        super().__init__(nom, "Feu", pv, attaque, attaque_spe, description)

    def special(self):
        print(f"{self.nom} lance l'attaque {self.attaque_spe} 🔥 !")


class PokemonEau(Pokemon):
    def __init__(self, nom, pv, attaque, attaque_spe, description=""):
        super().__init__(nom, "Eau", pv, attaque, attaque_spe, description)

    def special(self):
        print(f"{self.nom} lance {self.attaque_spe} 💧 !")


class PokemonPlante(Pokemon):
    def __init__(self, nom, pv, attaque, attaque_spe, description=""):
        super().__init__(nom, "Plante", pv, attaque, attaque_spe, description)

    def special(self):
        print(f"{self.nom} lance l'attaque {self.attaque_spe} 🌱 !")


# --- Exemple de combat ---
salameche = PokemonFeu("Salamèche", 39, 15, "Flammèche")
carapuce = PokemonEau("Carapuce", 44, 12, "Pistolet à O")

salameche.presentation()
carapuce.presentation()

print("\n--- Début du combat ---\n")
salameche.attaquer(carapuce)
carapuce.attaquer(salameche)


# --- Liste des Pokémon ---
lst_pokemon = [
    PokemonEau("Carapuce", 44, 12, "Pistolet à O", "Petite tortue bipède de couleur bleue avec une carapace brune. Elle lance des jets d’écume pour se défendre."),
    PokemonEau("Magicarpe", 20, 5, "Trempette", "Faible au début, mais peut évoluer en Léviator."),
    PokemonEau("Stari", 30, 10, "Écume", "Étoile de mer qui peut apprendre des attaques de type Eau et Psy."),
    PokemonEau("Tartard", 60, 18, "Hydrocanon", "Amphibien puissant avec de bonnes attaques Eau et Combat."),
    PokemonEau("Lokhlass", 260, 25, "Laser Glace", "Grand Pokémon marin, mélange Eau et Glace, très résistant."),

    PokemonFeu("Salameche", 39, 15, "Flammèche", "Pokémon de départ Feu, rapide et offensif."),
    PokemonFeu("Ponyta", 50, 18, "Flamme", "Cheval enflammé très rapide, attaque par flammes et coups de sabot."),
    PokemonFeu("Goupix", 38, 14, "Boule de Feu", "Petit renard de feu, peut évoluer en Feunard."),
    PokemonFeu("Arcanin", 90, 25, "Déflagration", "Rapide et puissant, idéal pour les attaques physiques."),
    PokemonFeu("Magmar", 65, 20, "Poing Feu", "Pokémon de type Feu aux attaques spéciales puissantes."),

    PokemonPlante("Bulbizarre", 45, 12, "Fouet Lianes", "Petit dinosaure avec un bulbe sur son dos qui grandit en une plante."),
    PokemonPlante("Mystherbe", 60, 15, "Vampigraine", "Plante herbeuse qui peut évoluer en Ortide."),
    PokemonPlante("Chetiflor", 60, 16, "Tranch'Herbe", "Plante carnivore qui peut évoluer en Empiflor."),
    PokemonPlante("Arcko", 40, 12, "Poing de Feuille", "Petit lézard agile, spécialisé dans les attaques précises de type Plante."),
    PokemonPlante("Joliflor", 60, 18, "Giga-Sangsue", "Plante élégante et robuste, évoluée de Chétiflor.")
]