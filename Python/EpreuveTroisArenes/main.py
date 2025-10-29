from pokemon import lst_pkmn_feu, lst_pkmn_eau, lst_pkmn_plante, PokemonFeu, PokemonEau, PokemonPlante, efficacite
from arene import Arene
from item import list_items
from boutique import Boutique
from dresseur import Dresseur, dresseurs_connus
from dictaciel import dictaciel_logique
import random

def couleur_pokemon(pokemon):
    return pokemon.nom

# --- Création des items ---
boutique = Boutique(list_items)

# --- Création des arènes ---
arene_feu = Arene(
    "Arène Flamme",
    "Feu",
    "Pyro",
    [p for p in lst_pkmn_feu[:-1]],   # tous sauf le dernier
    100,
    3,
    "Badge Flamme"
)

arene_eau = Arene(
    "Arène Océan",
    "Eau",
    "Aqua",
    [p for p in lst_pkmn_eau[:-1]],   # tous sauf le dernier
    200,
    3,
    "Badge Océan"
)

arene_plante = Arene(
    "Arène Verdure",
    "Plante",
    "Florina",
    [p for p in lst_pkmn_plante[:-1]],  # tous sauf le dernier
    500,
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
            return lst_pkmn_feu[0]  # Salameche
        elif choix == "2":
            return lst_pkmn_eau[0]  # Carapuce
        elif choix == "3":
            return lst_pkmn_plante[0] # Bulbizarre
        else:
            print("Choix invalide, réessaie.")

# --- Combat tour par tour ---
def combat(pokemon_joueur, arene):
    print("\n" + "-" * 50)
    print(f"DÉBUT DU COMBAT dans {arene.nom} contre les Pokémon de type {arene.type_arene}")
    print("-" * 50)

    def combat_contre(adversaire, pokemon_joueur):
        adversaire_pv_initial = adversaire.pv
        pokemon_joueur_pv_initial = pokemon_joueur.pv
        tour = 1
        while pokemon_joueur.pv > 0 and adversaire.pv > 0:
            print("\n" + "-" * 40)
            print(f"TOUR {tour}")
            print(f"{pokemon_joueur.nom} ({pokemon_joueur.type}) : {pokemon_joueur.pv} PV")
            print(f"{adversaire.nom} ({adversaire.type}) : {adversaire.pv} PV")
            print("-" * 40)
            print("Ton tour :")
            pokemon_joueur.attaquer(adversaire)
            if adversaire.pv <= 0:
                print(f"{adversaire.nom} est K.O.")
                break

            print("Tour de l'adversaire :")
            attaque_nom, attaque_degats = random.choice(adversaire.attaques)
            mult = efficacite[adversaire.type][pokemon_joueur.type]
            degats = int(attaque_degats * mult)
            if mult > 1:
                print("C’est super efficace !")
            elif mult < 1:
                print("Ce n’est pas très efficace.")
            print(f"{adversaire.nom} utilise {attaque_nom} et inflige {degats} dégâts à {pokemon_joueur.nom}.")
            pokemon_joueur.pv = max(0, pokemon_joueur.pv - degats)
            print(f"{pokemon_joueur.nom} a maintenant {pokemon_joueur.pv} PV restants.")
            if pokemon_joueur.pv <= 0:
                print(f"{pokemon_joueur.nom} est K.O. Tu as perdu le combat.")
                break
            tour += 1
        result = adversaire.pv <= 0
        pokemon_joueur.pv = pokemon_joueur_pv_initial
        adversaire.pv = adversaire_pv_initial
        print("-" * 40)
        return result

    niveau_actuel = 1
    while niveau_actuel < 5:
        adversaire = random.choice(arene.pokemon_defense)
        print("\n" + "=" * 50)
        print(f"COMBAT NIVEAU {niveau_actuel} : {pokemon_joueur.nom} ({pokemon_joueur.type}) VS {adversaire.nom} ({adversaire.type})")
        print("=" * 50)
        victoire = combat_contre(adversaire, pokemon_joueur)
        if victoire:
            print(f"Tu as gagné le combat niveau {niveau_actuel}.\n")
            niveau_actuel += 1
        else:
            print("Tu peux réessayer ce niveau.")

    # Combat final (niveau 5) contre le boss de notre arène
    adversaire = arene.pokemon_defense[-1]
    print("\n" + "=" * 50)
    print(f"COMBAT FINAL contre le boss {adversaire.nom} dans {arene.nom}")
    print("=" * 50)
    tour = 1
    while pokemon_joueur.pv > 0 and adversaire.pv > 0:
        print("\n" + "-" * 40)
        print(f"TOUR {tour}")
        print(f"{pokemon_joueur.nom} ({pokemon_joueur.type}) : {pokemon_joueur.pv} PV")
        print(f"{adversaire.nom} ({adversaire.type}) : {adversaire.pv} PV")
        print("-" * 40)
        print("Ton tour :")
        pokemon_joueur.attaquer(adversaire)
        if adversaire.pv <= 0:
            print(f"{adversaire.nom} est K.O.")
            break
        print("Tour de l'adversaire :")
        attaque_nom, attaque_degats = random.choice(adversaire.attaques)
        mult = efficacite[adversaire.type][pokemon_joueur.type]
        degats = int(attaque_degats * mult)
        if mult > 1:
            print("C’est super efficace !")
        elif mult < 1:
            print("Ce n’est pas très efficace.")
        print(f"{adversaire.nom} utilise {attaque_nom} et inflige {degats} dégâts à {pokemon_joueur.nom}.")
        pokemon_joueur.pv = max(0, pokemon_joueur.pv - degats)
        print(f"{pokemon_joueur.nom} a maintenant {pokemon_joueur.pv} PV restants.")
        if pokemon_joueur.pv <= 0:
            print(f"{pokemon_joueur.nom} est K.O. Tu as perdu le combat final.")
            print("Tu peux réessayer le combat final.")
            # Les PV sont gérés par la boucle
        tour += 1
    print("-" * 40)
    if adversaire.pv <= 0:
        print(f"\nFÉLICITATIONS ! Tu as vaincu le boss {adversaire.nom} et obtenu le {arene.badge} !")
        return True
    else:
        return False

# --- Menu principal ---
def menu_principal():
    print("Bienvenue dans Pokémon : Le combat des trois arènes !")
    print("Prépare-toi pour une aventure incroyable.\n")
    dictaciel = input("\Veux tu lancer le dictaciel ? (oui/non) : ").lower()
    if dictaciel in ["oui", "o"]:
        dictaciel_logique()

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
            dresseur.deck.append(pokemon_joueur)
            print(f"\nTu as choisi {pokemon_joueur.nom} ({pokemon_joueur.type}) ! Bonne chance !")

            # Par défaut j'ai choisi l'arène Flamme en tant que première arène 
            print("\nTu entres dans la première arène : Arène Flamme.")

            while True:
                print("\nMenu avant combat :")
                print("1. Lancer le combat")
                print("2. Accéder à la boutique")
                print("3. Quitter le jeu")
                choix_menu = input("Choisis une option (1-3) : ")
                if choix_menu == "1":
                    victoire = combat(pokemon_joueur, arene_feu)
                    if victoire:
                        # Ajout de la récompense de l'arène au portefeuille du dresseur
                        dresseur.portefeuille += arene_feu.recompense
                        print(f"\nTu as reçu {arene_feu.recompense} Pokédollars en récompense !")
                        # Ajout du boss final au pokedex et deck
                        boss_final = arene_feu.pokemon_defense[-1]
                        if boss_final not in pokedex:
                            pokedex.append(boss_final)
                            dresseur.deck.append(boss_final)

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
                                    if nouveau_pokemon not in pokedex:
                                        pokedex.append(nouveau_pokemon)
                                        dresseur.deck.append(nouveau_pokemon)  # Ajoute au pokedex du dresseur
                                    print(f"\nTu as ajouté {nouveau_pokemon.nom} à ton équipe !")
                                    break
                            print("Choix invalide, réessaie.")
                    else:
                        print("Tu n'as pas réussi à vaincre l'arène. Tu peux réessayer.")
                    # Après combat ou tentative, sortir de la menu boucle
                    break
                elif choix_menu == "2":
                    while True:
                        boutique.afficher_items()
                        choix_achat = input("Veux-tu acheter un item ? (oui/non) : ").lower()
                        if choix_achat in ['oui', 'o']:
                            choix_item = input("Entre le numéro de l'item à acheter (ou '0' pour annuler) : ")
                            if choix_item.isdigit():
                                choix_item = int(choix_item)
                                if choix_item == 0:
                                    break
                                elif 1 <= choix_item <= len(boutique.items):
                                    item_choisi = boutique.items[choix_item - 1]
                                    # Vérifier si le dresseur a assez d'argent
                                    if dresseur.portefeuille < item_choisi.prix:
                                        print("Tu n'as pas assez de Pokédollars pour cet item.")
                                    else:
                                        # Vérifier la limite de 2 exemplaires
                                        nb_exemplaires = dresseur.inventaire.count(item_choisi)
                                        if nb_exemplaires >= 2:
                                            print("Tu as déjà 2 exemplaires de cet item. Tu ne peux pas en acheter plus.")
                                        else:
                                            dresseur.portefeuille -= item_choisi.prix
                                            dresseur.inventaire.append(item_choisi)
                                            print(f"Tu as acheté {item_choisi.nom} pour {item_choisi.prix} Pokédollars.")
                                else:
                                    print("Numéro invalide.")
                            else:
                                print("Entrée invalide.")
                        elif choix_achat in ['non', 'n']:
                            break
                        else:
                            print("Réponse invalide, tape 'oui' ou 'non'.")
                elif choix_menu == "3":
                    print("\nTu as quitté le jeu. À bientôt !")
                    exit()
                else:
                    print("Choix invalide, réessaie.")

            # Scène boutique
            print("\nBravo pour ce combat ! Bienvenue dans la boutique Pokémon !!")
            boutique_pkmn = input("Veux-tu y accéder ? (oui/non) ").lower()
            if boutique_pkmn in ["oui", "o"]:
                while True:
                    boutique.afficher_items()
                    choix_achat = input("Veux-tu acheter un item ? (oui/non) : ").lower()
                    if choix_achat in ['oui', 'o']:
                        choix_item = input("Entre le numéro de l'item à acheter (ou '0' pour annuler) : ")
                        if choix_item.isdigit():
                            choix_item = int(choix_item)
                            if choix_item == 0:
                                break
                            elif 1 <= choix_item <= len(boutique.items):
                                item_choisi = boutique.items[choix_item - 1]
                                # Vérifier si le dresseur a assez d'argent
                                if dresseur.portefeuille < item_choisi.prix:
                                    print("Tu n'as pas assez de Pokédollars pour cet item.")
                                else:
                                    # Vérifier la limite de 2 exemplaires
                                    nb_exemplaires = dresseur.inventaire.count(item_choisi)
                                    if nb_exemplaires >= 2:
                                        print("Tu as déjà 2 exemplaires de cet item. Tu ne peux pas en acheter plus.")
                                    else:
                                        dresseur.portefeuille -= item_choisi.prix
                                        dresseur.inventaire.append(item_choisi)
                                        print(f"Tu as acheté {item_choisi.nom} pour {item_choisi.prix} Pokédollars.")
                            else:
                                print("Numéro invalide.")
                        else:
                            print("Entrée invalide.")
                    elif choix_achat in ['non', 'n']:
                        break
                    else:
                        print("Réponse invalide, tape 'oui' ou 'non'.")
            break

        elif lancer in ["non", "n"]:
            print("\nLe jeu est annulé. À bientôt !")
            exit()
        else:
            print("Réponse non valide, tape 'oui' ou 'non'.")

# --- Exécution principale ---
if __name__ == "__main__":
    menu_principal()