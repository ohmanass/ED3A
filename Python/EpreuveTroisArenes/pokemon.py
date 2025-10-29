from random import choice

# Tableau d'efficacite entre types
# Contient les multiplicateurs de degats selon les types d'attaques et de cibles
# Par exemple, une attaque de type "Feu" inflige 2 fois plus de degats a un Pokemon de type "Plante"
efficacite = {
    "Feu": {"Feu": 1, "Eau": 0.5, "Plante": 2},
    "Eau": {"Feu": 2, "Eau": 1, "Plante": 0.5},
    "Plante": {"Feu": 0.5, "Eau": 2, "Plante": 1}
}

# Classe de base representant un Pokemon generique
class Pokemon:
    # Constructeur
    # nom : nom du Pokemon
    # type_ : type elementaire ("Feu", "Eau", "Plante")
    # pv : points de vie
    # attaques : liste de tuples (nom attaque, degats)
    def __init__(self, nom, type_, pv, attaques):
        self.nom = nom
        self.type = type_
        self.pv = pv
        self.attaques = attaques  # liste de tuples (nom, degats)

    # Affiche les informations du Pokemon et ses attaques
    def presentation(self):
        print(f"{self.nom} ({self.type}) - {self.pv} PV")
        print("Attaques :")
        for i, (nom, degats) in enumerate(self.attaques, 1):
            print(f"  {i}. {nom} ({degats} degats)")

    # Dictionnaire pour afficher une seule fois le message d'avantage par paire de Pokemon
    _avantage_message_shown = {}

    # Methode pour attaquer un autre Pokemon
    def attaquer(self, cible):
        # Cle unique pour identifier la paire (attaquant, cible)
        key = (id(self), id(cible))
        mult = efficacite[self.type][cible.type]

        # Affichage du message d'avantage une seule fois par combat et par paire
        if key not in Pokemon._avantage_message_shown:
            if mult > 1:
                print(f"{self.nom} ({self.type}) a l'avantage sur {cible.nom} ({cible.type}) !")
            elif mult < 1:
                print(f"{cible.nom} ({cible.type}) a l'avantage sur {self.nom} ({self.type}) !")
            Pokemon._avantage_message_shown[key] = True

        # Demande a l'utilisateur de choisir une attaque
        print(f"\nChoisis une attaque pour {self.nom} :")
        for i, (nom, degats) in enumerate(self.attaques, 1):
            print(f"{i}. {nom} ({degats} degats)")

        while True:
            choix = input("Numero de l'attaque : ")
            if choix.isdigit() and 1 <= int(choix) <= len(self.attaques):
                attaque_nom, attaque_degats = self.attaques[int(choix) - 1]
                break
            print("Choix invalide, reessaie.")

        # Calcul des degats en appliquant le multiplicateur de type
        degats = int(attaque_degats * mult)

        # Affiche le resultat de l'attaque et met a jour les PV de la cible
        print(f"{self.nom} utilise {attaque_nom} sur {cible.nom} et inflige {degats} degats !")
        cible.pv = max(0, cible.pv - degats)
        print(f"{cible.nom} a maintenant {cible.pv} PV restants.\n")


# Sous-classes pour chaque type de Pokemon
class PokemonFeu(Pokemon):
    # Constructeur fixe le type a "Feu"
    def __init__(self, nom, pv, attaques):
        super().__init__(nom, "Feu", pv, attaques)

class PokemonEau(Pokemon):
    # Constructeur fixe le type a "Eau"
    def __init__(self, nom, pv, attaques):
        super().__init__(nom, "Eau", pv, attaques)

class PokemonPlante(Pokemon):
    # Constructeur fixe le type a "Plante"
    def __init__(self, nom, pv, attaques):
        super().__init__(nom, "Plante", pv, attaques)


# Listes de Pokemon par type
# Les derniers Pokemon de chaque liste sont des boss finaux
lst_pkmn_feu = [
    PokemonFeu("Salameche", 39, [("Flammeche", 15), ("Griffe", 10), ("Lance-Flammes", 25)]),
    PokemonFeu("Ponyta", 50, [("Charge", 10), ("Roue de Feu", 20), ("Flamme Ultime", 30)]),
    PokemonFeu("Goupix", 38, [("Vive-Attaque", 8), ("Flammeche", 15), ("Deflagration", 28)]),
    PokemonFeu("Arcanin", 90, [("Crocs Feu", 22), ("Morsure", 18), ("Lance-Flammes", 30)]),
    PokemonFeu("Magmar", 65, [("Poing Feu", 20), ("Jet de Flamme", 25), ("Explosion", 35)]),
    PokemonFeu("Pyroli", 80, [("Flammeche", 25), ("Lance-Flammes", 35), ("Eclat Feu", 30)])  # Boss final
]

lst_pkmn_eau = [
    PokemonEau("Carapuce", 44, [("Pistolet a O", 12), ("Charge", 8), ("Hydrocanon", 25)]),
    PokemonEau("Magicarpe", 20, [("Trempette", 1), ("Rebond", 8), ("Fleau", 10)]),
    PokemonEau("Stari", 30, [("Ecume", 10), ("Laser Glace", 20), ("Bulles d’O", 15)]),
    PokemonEau("Tartard", 60, [("Hydrocanon", 25), ("Coup de Poing", 15), ("Cascade", 20)]),
    PokemonEau("Lokhlass", 130, [("Surf", 25), ("Laser Glace", 28), ("Onde Boreale", 30)]),
    PokemonEau("Leviator", 150, [("Hydrocanon", 40), ("Morsure", 25), ("Draco-Rage", 35)])  # Boss final
]

lst_pkmn_plante = [
    PokemonPlante("Bulbizarre", 45, [("Fouet Lianes", 15), ("Tranch'Herbe", 12), ("Canon Graine", 20)]),
    PokemonPlante("Mystherbe", 60, [("Vampigraine", 12), ("Acide", 10), ("Mega-Sangsue", 18)]),
    PokemonPlante("Chetiflor", 60, [("Tranch'Herbe", 14), ("Fouet Lianes", 12), ("Poudre Dodo", 10)]),
    PokemonPlante("Arcko", 40, [("Vive-Attaque", 10), ("Lame Feuille", 18), ("Griffe", 8)]),
    PokemonPlante("Joliflor", 60, [("Giga-Sangsue", 20), ("Tranch'Herbe", 15), ("Canon Graine", 18)]),
    PokemonPlante("Jardinelle", 90, [("Canon Graine", 25), ("Tranch'Herbe", 20), ("Fouet Lianes", 15)])  # Boss final
]