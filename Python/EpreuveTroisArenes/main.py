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

test = lst_pokemon[:5] # redefine your list 
pkm_new = [] # remove that after
for i in test: # you want to use comprehension list 

    pkm_new.append(i)
# --- Création des arènes ---
arene_feu = Arene(
    "Arène Flamme",                
    "Feu",                            
    "Pyro",                      
    pkm_new,  
    "Badge Flamme",                    
    3,                                  
    "Badge Flamme"                   
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
            pokemon_joueur.pv = pokemon_joueur_pv_initial
            adversaire.pv = adversaire_pv_initial
        else:
            print("Tu peux réessayer ce niveau.")
            pokemon_joueur.pv = pokemon_joueur_pv_initial
            adversaire.pv = adversaire_pv_initial

    # Combat final (niveau 5) contre le boss de notre arène
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

    dresseur = choisir_dresseur()

    pokedex = [] #Je créer cette variable en guise de liste contenant l'ensemble des pokémons de notre dresseur

    # Début du jeu
    while True:
        lancer = input("\nVeux-tu lancer le jeu ? (oui/non) : ").lower()
        if lancer in ["oui", "o"]:
            print(f"\nLe jeu commence avec {dresseur.nom} !")

            # Choix de notre Pokémon de départ
            pokemon_joueur = choisir_pokemon_depart()
            pokedex.append(pokemon_joueur)
            print(f"\nTu as choisi {pokemon_joueur.nom} ({pokemon_joueur.type}) ! Bonne chance !")

            # Par défaut j'ai choisi l'arène Flamme en tant que première arène 
            print("\nTu entres dans la première arène : Arène Flamme.")
            victoire = combat(pokemon_joueur, arene_feu)

            if victoire:
                # Choix d'un Pokémon supplémentaire parmi la liste des Pokémon de l'arène, excluant le boss final
                print("\nChoisis un Pokémon supplémentaire parmi la liste suivante :")
                # Exclure le boss final (dernier Pokémon de la liste)
                pokemons_choix = [pkmn for pkmn in arene_feu.pokemon_defense[:-1] if pkmn != pokemon_joueur]
                for i, pkmn in enumerate(pokemons_choix, start=1):
                    print(f"{i}. {pkmn.nom} ({pkmn.type})")

                while True:
                    choix = input("Numéro de ton choix : ")
                    if choix.isdigit():
                        choix = int(choix)
                        if 1 <= choix <= len(pokemons_choix):
                            nouveau_pokemon = pokemons_choix[choix - 1]
                            pokedex.append(nouveau_pokemon)
                            print(f"\nTu as ajouté {nouveau_pokemon.nom} à ton équipe !")
                            dresseur.deck.append(nouveau_pokemon)  # Ajoute au pokedex du dresseur
                            break
                    print("Choix invalide, réessaie.")

            # Scène boutique
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