# Classe de tous les items du jeu
class Item:
    def __init__(self, nom, pv_restaure, prix, description):
        # Nom de l'item
        self.nom = nom
        # Points de vie que l'item restaure
        # Peut etre un nombre fixe, un pourcentage (entre 0 et 1), ou -1 pour restauration complete
        self.pv_restaure = pv_restaure
        # Prix de l'item en monnaie du jeu
        self.prix = prix
        # Description textuelle de l'effet de l'item
        self.description = description

    def calculer_pv_restaures(self, pv_max_pokemon):
        """
        Calcule le nombre de points de vie restaures par l'item en fonction du maximum de PV du pokemon.
        
        Types de restauration :
        - Restauration complete : si pv_restaure == -1, on restaure tous les PV (pv_max_pokemon)
        - Restauration en pourcentage : si 0 < pv_restaure < 1, on restaure un pourcentage des PV max
        - Restauration fixe : sinon, on restaure une valeur fixe de PV
        """
        if self.pv_restaure == -1:  # Restauration complete
            return pv_max_pokemon
        elif 0 < self.pv_restaure < 1:  # Pourcentage du max
            return int(pv_max_pokemon * self.pv_restaure)
        else:  # Valeur fixe
            return self.pv_restaure

list_items = [
    Item("Potion", 20, 300, "Restaure 20 PV du Pokemon."),
    Item("Super Potion", 50, 700, "Restaure 50 PV du Pokemon."),
    Item("Hyper Potion", 200, 1200, "Restaure 200 PV du Pokemon."),
    Item("Rappel Max", -1, 3000, "Restaure tous les PV d'un Pokemon KO."),
    Item("Baie Oran", 10, 50, "Restaure 10 PV lorsque le Pokemon est touche."),
    Item("Baie Sitrus", 0.25, 200, "Restaure 25 % des PV max lorsque le Pokemon a moins de 50 % de ses PV."),
    Item("Rappel", 0.5, 1500, "Restaure la moitie des PV d'un Pokemon KO.")
]