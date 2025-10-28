# Classe Arene
class Arene:
    def __init__(self, nom, type_arene, maitre, etages, recompense):
        self.nom = nom
        self.type_arene = type_arene
        self.maitre = maitre
        self.etages = etages
        self.recompense = recompense

# --- Liste des arenes ---
lst_arenes = [
    Arene("Arène de Flamme", "Feu", "Pyro", 3, "Badge Flamme"),
    Arene("Arène Aquatique", "Eau", "Aqua", 4, "Badge Océan"),
    Arene("Arène Verdoyante", "Plante", "Florina", 2, "Badge Feuille"),
]

# Exemple d'affichage
for arene in lst_arenes:
    print(f"{arene.nom} ({arene.type_arene}) - Champion : {arene.maitre}, Étages : {arene.etages}, Récompense : {arene.recompense}")