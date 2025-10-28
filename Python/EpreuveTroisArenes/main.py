from pokemon import lst_pokemon, PokemonFeu, PokemonEau, PokemonPlante, efficacite
from arene import Arene
from item import Item
from boutique import Boutique
from dresseur import Dresseur, dresseurs_connus
import random

# --- Création des items ---
potion = Item("Potion", 20, 300, "Restaure 20 PV.")
super_potion = Item("Super Potion", 50, 700, "Restaure 50 PV.")
boutique = Boutique([potion, super_potion])

# --- Création des arènes ---
# Les indices utilisés dans lst_pokemon doivent correspondre à des Pokémon existants de chaque type.
# Arguments requis : nom, type_arene, maitre, pokemon_defense, recompense, niveau, badge
arene_feu = Arene(
    "Arène Flamme",                     # nom
    "Feu",                              # type_arene
    "Pyro",                             # maitre
    [lst_pokemon[3], lst_pokemon[4]],   # pokemon_defense (existant dans lst_pokemon)
    "Badge Flamme",                     # recompense
    3,                                  # niveau
    "Badge Flamme"                      # badge
)
arene_eau = Arene(
    "Arène Océan",
    "Eau",
    "Aqua",
    [lst_pokemon[6], lst_pokemon[7]],
    "Badge Océan",
    3,
    "Badge Océan"
)
arene_plante = Arene(
    "Arène Verdure",
    "Plante",
    "Florina",
    [lst_pokemon[12], lst_pokemon[13]],
    "Badge Feuille",
    3,
    "Badge Feuille"
)

# --- Fonction : Choisir un dresseur ---
def choisir_dresseur():
    print("=== Choisis ton dresseur Pokémon ===\n")
    for i, dresseur in enumerate(dresseurs_connus, start=1):
        print(f"{i}. {dresseur.nom}")
    print("0. Créer ton propre dresseur")

    while True:
        choix = input("\nEntre le numéro de ton choix : ")
        if not choix.isdigit():
            print("Merci d’entrer un numéro valide.")
            continue
        choix = int(choix)
        if 1 <= choix <= len(dresseurs_connus):
            dresseur_selectionne = dresseurs_connus[choix - 1]
            print(f"\nTu as choisi : {dresseur_selectionne.nom}")
            print(f"Description : {dresseur_selectionne.description}")
            return dresseur_selectionne
        elif choix == 0:
            nom = input("\nEntre le nom de ton dresseur personnalisé : ")
            description = input("Entre une brève description : ")
            dresseur_perso = Dresseur(nom, description)
            print("\nTon dresseur personnalisé :")
            dresseur_perso.presentation()
            return dresseur_perso
        else:
            print("Numéro invalide, réessaie.")

# --- Fonction : Choisir son Pokémon de départ ---
def choisir_pokemon_depart():
    print("\n=== Choisis ton Pokémon de départ ===")
    print("1. Salamèche (Feu)")
    print("2. Carapuce (Eau)")
    print("3. Bulbizarre (Plante)")

    while True:
        choix = input("Numéro de ton choix : ")
        if choix == "1":
            return lst_pokemon[0]  # Salameche
        elif choix == "2":
            return lst_pokemon[5]  # Carapuce
        elif choix == "3":
            return lst_pokemon[10] # Bulbizarre
        else:
            print("Choix invalide, réessaie.")

# --- Combat tour par tour ---
def combat(pokemon_joueur, arene):
    print(f"\nDébut du combat dans {arene.nom} contre les Pokémon de type {arene.type_arene}.")

    niveau_actuel = 1
    while niveau_actuel < 5:
        adversaire = random.choice(arene.pokemon_defense)
        print(f"\nCombat niveau {niveau_actuel} : {pokemon_joueur.nom} ({pokemon_joueur.type}) contre {adversaire.nom} ({adversaire.type})")

        adversaire_pv_initial = adversaire.pv
        pokemon_joueur_pv_initial = pokemon_joueur.pv

        while pokemon_joueur.pv > 0 and adversaire.pv > 0:
            print("\n--- Ton tour ---")
            pokemon_joueur.attaquer(adversaire)
            if adversaire.pv <= 0:
                print(f"\n{adversaire.nom} est K.O.")
                break

            print("\n--- Tour de l'adversaire ---")
            attaque_nom, attaque_degats = random.choice(adversaire.attaques)
            mult = efficacite[adversaire.type][pokemon_joueur.type]
            degats = int(attaque_degats * mult)

            if mult > 1:
                print("C’est super efficace.")
            elif mult < 1:
                print("Ce n’est pas très efficace.")

            print(f"{adversaire.nom} utilise {attaque_nom} et inflige {degats} dégâts.")
            pokemon_joueur.pv = max(0, pokemon_joueur.pv - degats)
            print(f"{pokemon_joueur.nom} a maintenant {pokemon_joueur.pv} PV restants.")

            if pokemon_joueur.pv <= 0:
                print(f"\n{pokemon_joueur.nom} est K.O. Tu as perdu le combat.")
                break

        if adversaire.pv <= 0:
            print(f"Tu as gagné le combat niveau {niveau_actuel}.\n")
            niveau_actuel += 1
            # Restaure les PV du joueur pour le prochain combat
            pokemon_joueur.pv = pokemon_joueur_pv_initial
            # Restaure les PV de l'adversaire pour le cas où il serait choisi à nouveau
            adversaire.pv = adversaire_pv_initial
        else:
            print("Tu peux réessayer ce niveau.")
            # Restaure les PV du joueur pour réessayer le même niveau
            pokemon_joueur.pv = pokemon_joueur_pv_initial
            adversaire.pv = adversaire_pv_initial
            # Ne pas incrémenter niveau_actuel pour rester au même étage

    # Combat final (niveau 5) contre le boss
    adversaire = arene.pokemon_defense[-1]
    print(f"\nCombat final contre le boss {adversaire.nom} dans {arene.nom}.")

    adversaire_pv_initial = adversaire.pv
    pokemon_joueur_pv_initial = pokemon_joueur.pv

    while pokemon_joueur.pv > 0 and adversaire.pv > 0:
        print("\n--- Ton tour ---")
        pokemon_joueur.attaquer(adversaire)
        if adversaire.pv <= 0:
            print(f"\n{adversaire.nom} est K.O.")
            break

        print("\n--- Tour de l'adversaire ---")
        attaque_nom, attaque_degats = random.choice(adversaire.attaques)
        mult = efficacite[adversaire.type][pokemon_joueur.type]
        degats = int(attaque_degats * mult)

        if mult > 1:
            print("C’est super efficace.")
        elif mult < 1:
            print("Ce n’est pas très efficace.")

        print(f"{adversaire.nom} utilise {attaque_nom} et inflige {degats} dégâts.")
        pokemon_joueur.pv = max(0, pokemon_joueur.pv - degats)
        print(f"{pokemon_joueur.nom} a maintenant {pokemon_joueur.pv} PV restants.")

        if pokemon_joueur.pv <= 0:
            print(f"\n{pokemon_joueur.nom} est K.O. Tu as perdu le combat final.")
            print("Tu peux réessayer le combat final.")
            # Restaure les PV du joueur et du boss pour réessayer
            pokemon_joueur.pv = pokemon_joueur_pv_initial
            adversaire.pv = adversaire_pv_initial

    if adversaire.pv <= 0:
        print(f"\nFélicitations ! Tu as vaincu le boss {adversaire.nom} et obtenu le {arene.badge} !")
        return True
    else:
        return False

# --- Menu principal ---
def menu_principal():
    print("Bienvenue dans le monde des Pokémon !")
    print("Prépare-toi pour une aventure incroyable.\n")

    # Étape 1 : Choix du dresseur
    dresseur = choisir_dresseur()

    # Variable pour stocker les Pokémon du joueur
    pokemons_joueur = []

    # Étape 2 : Confirmation pour lancer le jeu
    while True:
        lancer = input("\nVeux-tu lancer le jeu ? (oui/non) : ").lower()
        if lancer in ["oui", "o"]:
            print(f"\nLe jeu commence avec {dresseur.nom} !")

            # Étape 3 : Choix du Pokémon de départ
            pokemon_joueur = choisir_pokemon_depart()
            pokemons_joueur.append(pokemon_joueur)
            print(f"\nTu as choisi {pokemon_joueur.nom} ({pokemon_joueur.type}) ! Bonne chance !")

            # Étape 4 : Premier combat dans l'Arène Feu
            print("\nTu entres dans la première arène : Arène Flamme.")
            victoire = combat(pokemon_joueur, arene_feu)

            if victoire:
                # Choix d'un Pokémon supplémentaire parmi la liste des Pokémon de l'arène, excluant le boss final
                print("\nChoisis un Pokémon supplémentaire parmi la liste suivante :")
                pokemons_disponibles = arene_feu.pokemon_defense[:-1]  # Exclure le boss final
                for i, pkmn in enumerate(pokemons_disponibles, start=1):
                    print(f"{i}. {pkmn.nom} ({pkmn.type})")

                while True:
                    choix = input("Numéro de ton choix : ")
                    if choix.isdigit():
                        choix = int(choix)
                        if 1 <= choix <= len(pokemons_disponibles):
                            nouveau_pokemon = pokemons_disponibles[choix - 1]
                            pokemons_joueur.append(nouveau_pokemon)
                            print(f"\nTu as ajouté {nouveau_pokemon.nom} à ton équipe !")
                            break
                    print("Choix invalide, réessaie.")

            # Étape 5 : Boutique
            print("\nAprès le combat, tu découvres la boutique.")
            boutique.afficher_items()
            break

        elif lancer in ["non", "n"]:
            print("\nLe jeu est annulé. À bientôt !")
            exit()
        else:
            print("Réponse non valide, tape 'oui' ou 'non'.")

# --- Exécution principale ---
if __name__ == "__main__":
    menu_principal()