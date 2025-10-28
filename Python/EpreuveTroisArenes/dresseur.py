#Ici j'offre la possibilité à l'utilisateur de choisir un dresseur pokémon parmis ceux connues OU créer le siens !
class Dresseur:
    def __init__(self, nom, description):
        self.nom = nom
        self.description = description

    def presentation(self):
        print(f"👤 {self.nom} — {self.description}")


# --- Liste des dresseurs connus ---
dresseurs_connus = [
    Dresseur("Sacha (Ash Ketchum)", "Le héros principal de l’anime, originaire de Bourg Palette."),
    Dresseur("Ondine (Misty)", "Championne d’Azuria, spécialiste des Pokémon de type Eau."),
    Dresseur("Pierre (Brock)", "Champion d’Argenta, spécialiste du type Roche."),
    Dresseur("Serena", "Amie d’enfance de Sacha, dresseuse et performeuse Pokémon."),
    Dresseur("Liko", "Nouvelle protagoniste dans Pokémon Horizons."),
    Dresseur("Roy", "Co-protagoniste de Pokémon Horizons, curieux et motivé.")
]


# --- Affichage du menu ---
print("=== Choisis ton dresseur Pokémon ===\n")

for i, dresseur in enumerate(dresseurs_connus, start=1):
    print(f"{i}. {dresseur.nom}")

print("0. 🔧 Créer ton propre dresseur")

# --- Saisie du choix ---
while True:
    choix = input("\nEntre le numéro de ton choix : ")

    if not choix.isdigit():
        print("❌ Merci d’entrer un numéro valide.")
        continue

    choix = int(choix)

    if 1 <= choix <= len(dresseurs_connus):
        dresseur_selectionne = dresseurs_connus[choix - 1]
        print(f"\n✅ Tu as choisi : {dresseur_selectionne.nom}")
        print(f"ℹ️  Description : {dresseur_selectionne.description}")
        break

    elif choix == 0:
        nom = input("\nEntre le nom de ton dresseur personnalisé : ")
        description = input("Entre une brève description : ")
        dresseur_perso = Dresseur(nom, description)
        print("\n✨ Ton dresseur personnalisé :")
        dresseur_perso.presentation()
        break

    else:
        print("❌ Numéro invalide, réessaie.")