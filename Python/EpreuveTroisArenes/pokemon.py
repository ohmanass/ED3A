class Pokemon:
    def __init__(self, nom, type_, pv, attaque):
        self.nom = nom
        self.type = type_
        self.pv = pv
        self.attaque = attaque

    def presentation(self):
        print(f"Je suis {self.nom}, de type {self.type}, avec {self.pv} PV et {self.attaque} en attaque.")

    def attaquer(self, cible):
        print(f"{self.nom} attaque {cible.nom} et lui inflige {self.attaque} dégâts 💥 !")
        cible.pv -= self.attaque
        if cible.pv < 0:
            cible.pv = 0
        print(f"{cible.nom} a maintenant {cible.pv} PV restants.\n")


class PokemonFeu(Pokemon):
    def __init__(self, nom, pv, attaque):
        super().__init__(nom, "Feu", pv, attaque)

    def special(self):
        print(f"{self.nom} lance l'attaque Lance-Flammes 🔥 !")


class PokemonEau(Pokemon):
    def __init__(self, nom, pv, attaque):
        super().__init__(nom, "Eau", pv, attaque)

    def special(self):
        print(f"{self.nom} lance l'attaque Pistolet à O 💧 !")

salameche = PokemonFeu("Salamèche", 39, 15)
carapuce = PokemonEau("Carapuce", 44, 10)

salameche.presentation()
carapuce.presentation()

print("\n--- Début du combat ---\n")

salameche.attaquer(carapuce)
carapuce.attaquer(salameche)

# --- Liste des Pokemon  ---
lst_pokemon = [

]