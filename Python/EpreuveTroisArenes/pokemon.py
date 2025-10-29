from random import choice

# --- Tableau d'efficacité entre types ---
efficacite = {
    "Feu": {"Feu": 1, "Eau": 0.5, "Plante": 2},
    "Eau": {"Feu": 2, "Eau": 1, "Plante": 0.5},
    "Plante": {"Feu": 0.5, "Eau": 2, "Plante": 1}
}


# --- Classe de base ---
class Pokemon:
    def __init__(self, nom, type_, pv, attaques):
        self.nom = nom
        self.type = type_
        self.pv = pv
        self.attaques = attaques  # liste de tuples (nom, dégâts)

    def presentation(self):
        print(f"{self.nom} ({self.type}) - {self.pv} PV")
        print("Attaques :")
        for i, (nom, degats) in enumerate(self.attaques, 1):
            print(f"  {i}. {nom} ({degats} dégâts)")

    def attaquer(self, cible):
        print(f"\nChoisis une attaque pour {self.nom} :")
        for i, (nom, degats) in enumerate(self.attaques, 1):
            print(f"{i}. {nom} ({degats} dégâts)")

        while True:
            choix = input("Numéro de l'attaque : ")
            if choix.isdigit() and 1 <= int(choix) <= len(self.attaques):
                attaque_nom, attaque_degats = self.attaques[int(choix) - 1]
                break
            print("Choix invalide, réessaie.")

        mult = efficacite[self.type][cible.type]
        degats = int(attaque_degats * mult)

        if mult > 1:
            print("C’est super efficace !")
        elif mult < 1:
            print("Ce n’est pas très efficace…")

        print(f"{self.nom} utilise {attaque_nom} sur {cible.nom} et inflige {degats} dégâts !")
        cible.pv = max(0, cible.pv - degats)
        print(f"{cible.nom} a maintenant {cible.pv} PV restants.\n")


# --- Sous-classes par type ---
class PokemonFeu(Pokemon):
    def __init__(self, nom, pv, attaques):
        super().__init__(nom, "Feu", pv, attaques)


class PokemonEau(Pokemon):
    def __init__(self, nom, pv, attaques):
        super().__init__(nom, "Eau", pv, attaques)


class PokemonPlante(Pokemon):
    def __init__(self, nom, pv, attaques):
        super().__init__(nom, "Plante", pv, attaques)


# --- Liste complète de Pokémon ---
lst_pkmn_feu = [
    PokemonFeu("Salamèche", 39, [("Flammèche", 15), ("Griffe", 10), ("Lance-Flammes", 25)]),
    PokemonFeu("Ponyta", 50, [("Charge", 10), ("Roue de Feu", 20), ("Flamme Ultime", 30)]),
    PokemonFeu("Goupix", 38, [("Vive-Attaque", 8), ("Flammèche", 15), ("Déflagration", 28)]),
    PokemonFeu("Arcanin", 90, [("Crocs Feu", 22), ("Morsure", 18), ("Lance-Flammes", 30)]),
    PokemonFeu("Magmar", 65, [("Poing Feu", 20), ("Jet de Flamme", 25), ("Explosion", 35)]),
    PokemonFeu("Pyroli", 80, [("Flammèche", 25), ("Lance-Flammes", 35), ("Éclat Feu", 30)])  # Boss final
]

lst_pkmn_eau = [
    PokemonEau("Carapuce", 44, [("Pistolet à O", 12), ("Charge", 8), ("Hydrocanon", 25)]),
    PokemonEau("Magicarpe", 20, [("Trempette", 1), ("Rebond", 8), ("Fléau", 10)]),
    PokemonEau("Stari", 30, [("Écume", 10), ("Laser Glace", 20), ("Bulles d’O", 15)]),
    PokemonEau("Tartard", 60, [("Hydrocanon", 25), ("Coup de Poing", 15), ("Cascade", 20)]),
    PokemonEau("Lokhlass", 130, [("Surf", 25), ("Laser Glace", 28), ("Onde Boréale", 30)]),
    PokemonEau("Léviator", 150, [("Hydrocanon", 40), ("Morsure", 25), ("Draco-Rage", 35)])  # Boss final
]

lst_pkmn_plante = [
    PokemonPlante("Bulbizarre", 45, [("Fouet Lianes", 15), ("Tranch’Herbe", 12), ("Canon Graine", 20)]),
    PokemonPlante("Mystherbe", 60, [("Vampigraine", 12), ("Acide", 10), ("Méga-Sangsue", 18)]),
    PokemonPlante("Chétiflor", 60, [("Tranch’Herbe", 14), ("Fouet Lianes", 12), ("Poudre Dodo", 10)]),
    PokemonPlante("Arcko", 40, [("Vive-Attaque", 10), ("Lame Feuille", 18), ("Griffe", 8)]),
    PokemonPlante("Joliflor", 60, [("Giga-Sangsue", 20), ("Tranch’Herbe", 15), ("Canon Graine", 18)]),
    PokemonPlante("Jardinelle", 90, [("Canon Graine", 25), ("Tranch’Herbe", 20), ("Fouet Lianes", 15)])  # Boss final
]