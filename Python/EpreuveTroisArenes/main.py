from pokemon import lst_pkmn_feu, lst_pkmn_eau, lst_pkmn_plante, PokemonFeu, PokemonEau, PokemonPlante, efficacite
from arene import Arene
from item import list_items
from boutique import Boutique
from dresseur import Dresseur, dresseurs_connus
from dictaciel import dictaciel_logique
import random
import os
import time

# Ce fichier contient la boucle principale du jeu, la logique des scenes,
# la gestion des arenes, combats, pokedex, boutique, dictaciel et menus.

# Fonction utilitaire pour afficher le nom du pokemon (sans couleur)
def couleur_pokemon(pokemon):
    return pokemon.nom

# --- Creation des items et arenes ---
# La boutique contient la liste des items disponibles a l'achat.
boutique = Boutique(list_items)
# Chaque arene est definie par un nom, un type, un champion, une liste de pokemons, une recompense, un niveau et un badge.
arene_feu = Arene(
    "Arene Flamme (Feu)", "Feu", "Pyro", [p for p in lst_pkmn_feu[:-1]], 100, 3, "Badge Flamme"
)
arene_eau = Arene(
    "Arene Ocean (Eau)", "Eau", "Aqua", [p for p in lst_pkmn_eau[:-1]], 200, 3, "Badge Ocean"
)
arene_plante = Arene(
    "Arene Verdure (Plante)", "Plante", "Florina", [p for p in lst_pkmn_plante[:-1]], 500, 3, "Badge Feuille"
)

# --- Fonction : Choisir un dresseur ---
# Permet au joueur de choisir un dresseur predefini ou d'en creer un personnalise.
def choisir_dresseur():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=" * 70)
    print(" SCENE : CHOIX DU DRESSEUR ".center(70, "="))
    print("=" * 70 + "\n")
    for i, dresseur in enumerate(dresseurs_connus, start=1):
        print(f"{i}. {dresseur.nom}")
    print("0. Creer ton propre dresseur")
    while True:
        choix = input("\nEntre le numero de ton choix : ")
        if not choix.isdigit():
            print("Merci d'entrer un numero valide.")
            continue
        choix = int(choix)
        if 1 <= choix <= len(dresseurs_connus):
            dresseur_selectionne = dresseurs_connus[choix - 1]
            print(f"\nTu as choisi : {dresseur_selectionne.nom}")
            print(f"Description : {dresseur_selectionne.description}")
            input("\nAppuie sur Entrée pour continuer...")
            return dresseur_selectionne
        elif choix == 0:
            nom = input("\nEntre le nom de ton dresseur personnalise : ")
            description = input("Entre une breve description : ")
            dresseur_perso = Dresseur(nom, description)
            print("\nTon dresseur personnalisé :")
            dresseur_perso.presentation()
            input("\nAppuie sur Entrée pour continuer...")
            return dresseur_perso
        else:
#            print("Numero invalide, reessaie.")
            print("Numero invalide, reessaie.")

# --- Fonction : Choisir son Pokemon de depart ---
# Permet au joueur de choisir son premier Pokemon parmi trois types.
def choisir_pokemon_depart():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=" * 70)
    print(" SCENE : CHOIX DU POKEMON DE DEPART ".center(70, "="))
    print("=" * 70)
    print("1. Salameche (Feu)")
    print("2. Carapuce (Eau)")
    print("3. Bulbizarre (Plante)")
    while True:
        choix = input("Numero de ton choix : ")
        if choix == "1":
            input("\nAppuie sur Entrée pour continuer...")
            return lst_pkmn_feu[0]
        elif choix == "2":
            input("\nAppuie sur Entrée pour continuer...")
            return lst_pkmn_eau[0]
        elif choix == "3":
            input("\nAppuie sur Entrée pour continuer...")
            return lst_pkmn_plante[0]
        else:
#            print("Choix invalide, reessaie.")
            print("Choix invalide, reessaie.")


# --- Combat arene (niveaux 1 a 4) ---
# Logique des combats contre les pokemons de l'arene (hors boss).
# Le joueur affronte 4 adversaires choisis aleatoirement dans l'arene.
# Les combats sont tour a tour, avec gestion des avantages de type.
# Apres chaque combat, un menu permet d'ouvrir la boutique, le dictaciel ou de quitter.
def combat_arene(pokemon_joueur, arene, dresseur):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=" * 70)
    print(f" SCENE : COMBAT DANS {arene.nom.upper()} ".center(70, "="))
    print("=" * 70)
    print(f" DEBUT DU COMBAT DANS {arene.nom.upper()} CONTRE DES POKEMON DE TYPE {arene.type_arene.upper()} ")
    print("-" * 60)
    adv = efficacite[pokemon_joueur.type][arene.type_arene]
    if adv > 1:
        print(f"\n>>> TON POKEMON A UN AVANTAGE DE TYPE ({pokemon_joueur.type.upper()} > {arene.type_arene.upper()}) POUR CETTE ARENE !")
    elif adv < 1:
        print(f"\n>>> TON POKEMON A UN DESAVANTAGE DE TYPE ({pokemon_joueur.type.upper()} < {arene.type_arene.upper()}) POUR CETTE ARENE.")
    else:
        print(f"\n>>> TYPE NEUTRE POUR CETTE ARENE.")
    input("\nAppuie sur Entree pour continuer...")

    # Fonction interne pour effectuer un combat contre un adversaire donne.
    def combat_contre(adversaire, pokemon_joueur):
        adversaire_pv_initial = adversaire.pv
        pokemon_joueur_pv_initial = pokemon_joueur.pv
        tour = 1
        while pokemon_joueur.pv > 0 and adversaire.pv > 0:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("=" * 70)
            print(f" SCENE : TOUR DE COMBAT ".center(70, "="))
            print("=" * 70)
            print(f"TOUR {tour}")
            print(f"{pokemon_joueur.nom.upper()} ({pokemon_joueur.type}) : {pokemon_joueur.pv} PV")
            print(f"{adversaire.nom.upper()} ({adversaire.type}) : {adversaire.pv} PV")
            print("-" * 40)
            print("TON TOUR :")
            pokemon_joueur.attaquer(adversaire)
            if adversaire.pv <= 0:
                print(f"{adversaire.nom.upper()} EST K.O.")
                input("\nAppuie sur Entree pour continuer...")
                break
            print("TOUR DE L'ADVERSAIRE :")
            attaque_nom, attaque_degats = random.choice(adversaire.attaques)
            mult = efficacite[adversaire.type][pokemon_joueur.type]
            degats = int(attaque_degats * mult)
            print(f"{adversaire.nom} utilise {attaque_nom} et inflige {degats} dégâts à {pokemon_joueur.nom}.")
            pokemon_joueur.pv = max(0, pokemon_joueur.pv - degats)
            print(f"{pokemon_joueur.nom} a maintenant {pokemon_joueur.pv} PV restants.")
            if pokemon_joueur.pv <= 0:
                print(f"{pokemon_joueur.nom.upper()} EST K.O. TU AS PERDU LE COMBAT.")
                input("\nAppuie sur Entree pour continuer...")
                break
            tour += 1
            input("\nAppuie sur Entree pour continuer...")
        result = adversaire.pv <= 0
        # Réinitialiser PV après combat
        pokemon_joueur.pv = pokemon_joueur_pv_initial
        adversaire.pv = adversaire_pv_initial
        print("-" * 40)
        input("\nAppuie sur Entree pour continuer...")
        return result

    niveau_actuel = 1
    while niveau_actuel < 5:
        adversaire = random.choice(arene.pokemon_defense[:-1])
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=" * 70)
        print(f" SCENE : COMBAT NIVEAU {niveau_actuel} ".center(70, "="))
        print("=" * 70)
        print(f" COMBAT NIVEAU {niveau_actuel} : {pokemon_joueur.nom.upper()} ({pokemon_joueur.type}) VS {adversaire.nom.upper()} ({adversaire.type}) ")
        print("=" * 60)
        victoire = combat_contre(adversaire, pokemon_joueur)
        if victoire:
            print(f"\n>>> TU AS GAGNE LE COMBAT NIVEAU {niveau_actuel} !")
            niveau_actuel += 1
        else:
            print(">>> TU PEUX REESSAYER CE NIVEAU.")
        input("\nAppuie sur Entree pour continuer...")

        # Menu apres chaque combat permet d'acceder a la boutique, au dictaciel ou de quitter.
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("=" * 70)
            print(" SCENE : INTERLUDE APRES COMBAT ".center(70, "="))
            print("=" * 70)
            print("QUE VEUX-TU FAIRE MAINTENANT ?")
            print("1. Continuer vers le combat suivant")
            print("2. Ouvrir la boutique")
            print("3. Afficher le dictaciel")
            print("4. Quitter le jeu")
            choix_action = input("Choisis une option (1-4) : ")
            if choix_action == "1":
                break
            elif choix_action == "2":
                scene_boutique(dresseur)
            elif choix_action == "3":
                scene_dictaciel()
            elif choix_action == "4":
                print("Tu as quitte le jeu. A bientot !")
                exit()
            else:
                print("Choix invalide, reessaie.")
    return True

# --- Combat boss (niveau 5) ---
# Combat contre le boss final de l'arene (dernier pokemon).
# Meme logique que combat_arene, mais contre le boss.
def combat_boss(pokemon_joueur, arene, dresseur):
    adversaire = arene.pokemon_defense[-1]
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=" * 70)
    print(f" SCENE : COMBAT FINAL CONTRE LE BOSS ".center(70, "="))
    print("=" * 70)
    print(f" COMBAT FINAL CONTRE LE BOSS {adversaire.nom.upper()} DANS {arene.nom.upper()} ")
    print("=" * 60)
    tour = 1
    pokemon_joueur_pv_initial = pokemon_joueur.pv
    adversaire_pv_initial = adversaire.pv
    boss_ko = False
    while pokemon_joueur.pv > 0 and adversaire.pv > 0:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=" * 70)
        print(f" SCENE : TOUR DE COMBAT FINAL ".center(70, "="))
        print("=" * 70)
        print(f"TOUR {tour}")
        print(f"{pokemon_joueur.nom.upper()} ({pokemon_joueur.type}) : {pokemon_joueur.pv} PV")
        print(f"{adversaire.nom.upper()} ({adversaire.type}) : {adversaire.pv} PV")
        print("-" * 40)
        print("TON TOUR :")
        pokemon_joueur.attaquer(adversaire)
        # Tester la victoire avant remise à zéro des PV
        if adversaire.pv <= 0:
            print(f"{adversaire.nom.upper()} EST K.O.")
            boss_ko = True
            input("\nAppuie sur Entree pour continuer...")
            break
        print("TOUR DE L'ADVERSAIRE :")
        attaque_nom, attaque_degats = random.choice(adversaire.attaques)
        mult = efficacite[adversaire.type][pokemon_joueur.type]
        degats = int(attaque_degats * mult)
        print(f"{adversaire.nom} utilise {attaque_nom} et inflige {degats} dégâts à {pokemon_joueur.nom}.")
        pokemon_joueur.pv = max(0, pokemon_joueur.pv - degats)
        print(f"{pokemon_joueur.nom} a maintenant {pokemon_joueur.pv} PV restants.")
        if pokemon_joueur.pv <= 0:
            print(f"{pokemon_joueur.nom.upper()} EST K.O. TU AS PERDU LE COMBAT FINAL.")
            print("Tu peux reessayer le combat final.")
        tour += 1
        input("\nAppuie sur Entree pour continuer...")
    print("-" * 40)
    # Conserver les PV initiaux pour remise à zéro après l'affichage
    pokemon_joueur.pv = pokemon_joueur_pv_initial
    adversaire.pv = adversaire_pv_initial
    if boss_ko:
        print(f"\nFELICITATIONS ! TU AS VAINCU LE BOSS {adversaire.nom.upper()} ET OBTENU LE {arene.badge.upper()} !")
        input("\nAppuie sur Entree pour continuer...")
        return True
    else:
        input("\nAppuie sur Entree pour continuer...")
        return False

# --- Menu Boutique centralise ---
# Permet au joueur d'acheter des items dans la boutique.
# Affiche le portefeuille, l'inventaire, la liste des items et gere l'achat (max 2 exemplaires).
def scene_boutique(dresseur):
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=" * 70)
        print(" SCENE : BOUTIQUE ".center(70, "="))
        print("=" * 70)
        print(f"TON PORTEFEUILLE : {dresseur.portefeuille} Pokedollars")
        print("INVENTAIRE :")
        if hasattr(dresseur.inventaire, 'items') and hasattr(dresseur.inventaire, 'items'):
            # Si items est un dict (nouvelle logique)
            if isinstance(dresseur.inventaire.items, dict):
                if dresseur.inventaire.items:
                    for it, count in dresseur.inventaire.items.items():
                        print(f"  - {it.nom} x{count}")
                else:
                    print("  (vide)")
            else:
                # fallback ancienne logique
                if dresseur.inventaire.items:
                    for it in set(dresseur.inventaire.items):
                        count = dresseur.inventaire.items.count(it)
                        print(f"  - {it.nom} x{count}")
                else:
                    print("  (vide)")
        else:
            print("  (vide)")
        boutique.afficher_items()
        choix_achat = input("Veux-tu acheter un item ? (oui/non) : ").lower()
        if choix_achat in ['oui', 'o']:
            choix_item = input("Entre le numero de l'item a acheter (ou '0' pour annuler) : ")
            if choix_item.isdigit():
                choix_item = int(choix_item)
                if choix_item == 0:
                    break
                elif 1 <= choix_item <= len(boutique.items):
                    item_choisi = boutique.items[choix_item - 1]
                    if dresseur.portefeuille < item_choisi.prix:
                        print("Tu n'as pas assez de Pokedollars pour cet item.")
                        input("\nAppuie sur Entree pour continuer...")
                    else:
                        # Nouvelle gestion via dictionnaire
                        if isinstance(dresseur.inventaire.items, dict):
                            nb_exemplaires = dresseur.inventaire.items.get(item_choisi, 0)
                            if nb_exemplaires >= 2:
                                print("Tu as deja 2 exemplaires de cet item. Tu ne peux pas en acheter plus.")
                                input("\nAppuie sur Entree pour continuer...")
                            else:
                                dresseur.portefeuille -= item_choisi.prix
                                dresseur.inventaire.items[item_choisi] = nb_exemplaires + 1
                                print(f"Tu as achete {item_choisi.nom} pour {item_choisi.prix} Pokedollars.")
                                input("\nAppuie sur Entree pour continuer...")
                        else:
                            # fallback ancienne logique (liste)
                            nb_exemplaires = dresseur.inventaire.items.count(item_choisi)
                            if nb_exemplaires >= 2:
                                print("Tu as deja 2 exemplaires de cet item. Tu ne peux pas en acheter plus.")
                                input("\nAppuie sur Entree pour continuer...")
                            else:
                                dresseur.portefeuille -= item_choisi.prix
                                dresseur.inventaire.items.append(item_choisi)
                                print(f"Tu as achete {item_choisi.nom} pour {item_choisi.prix} Pokedollars.")
                                input("\nAppuie sur Entree pour continuer...")
                else:
                    print("Numero invalide.")
                    input("\nAppuie sur Entree pour continuer...")
            else:
                print("Entree invalide.")
                input("\nAppuie sur Entree pour continuer...")
        elif choix_achat in ['non', 'n']:
            break
        else:
#            print("Reponse invalide, tape 'oui' ou 'non'.")
            print("Reponse invalide, tape 'oui' ou 'non'.")
            input("\nAppuie sur Entree pour continuer...")

# --- Dictaciel comme scene ---
# Affiche le dictaciel (aide du jeu).
def scene_dictaciel():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=" * 70)
    print(" SCENE : DICTACIEL ".center(70, "="))
    print("=" * 70)
    dictaciel_logique()
#    input("\nAppuie sur Entree pour continuer...")
    input("\nAppuie sur Entree pour continuer...")

# --- Pokedex (affichage et selection du pokemon) ---
# Affiche la liste des pokemons du joueur.
def afficher_pokedex(pokedex):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=" * 70)
    print(" SCENE : POKEDEX DU DRESSEUR ".center(70, "="))
    print("=" * 70)
    if not pokedex:
        print("Ton Pokedex est vide.")
    else:
        for i, pkmn in enumerate(pokedex, start=1):
            print(f"{i}. {pkmn.nom} ({pkmn.type})")
#    input("\nAppuie sur Entree pour revenir au menu...")
    input("\nAppuie sur Entree pour revenir au menu...")

# Permet au joueur de choisir un pokemon de son pokedex pour le prochain combat.
def choisir_pokemon_pokedex(pokedex, pokemon_joueur):
    if not pokedex:
        print("Ton Pokedex est vide.")
        input("\nAppuie sur Entree pour continuer...")
        return pokemon_joueur
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=" * 70)
        print(" SCENE : CHOIX DU POKEMON POUR LE COMBAT ".center(70, "="))
        print("=" * 70)
        for i, pkmn in enumerate(pokedex, start=1):
            print(f"{i}. {pkmn.nom} ({pkmn.type})")
        print("0. Garder le Pokemon actuel")
        choix = input("Selectionne le numero du Pokemon a utiliser pour ce combat : ")
        if choix.isdigit():
            choix = int(choix)
            if choix == 0:
                print(f"\nTu gardes {pokemon_joueur.nom.upper()} pour ce combat.")
                input("\nAppuie sur Entree pour continuer...")
                return pokemon_joueur
            elif 1 <= choix <= len(pokedex):
                selection = pokedex[choix - 1]
                print(f"\nTu as choisi {selection.nom.upper()} pour ce combat.")
                input("\nAppuie sur Entree pour continuer...")
                return selection
#        print("Choix invalide, reessaie.")
        print("Choix invalide, reessaie.")

# --- Menu principal ---
# Menu principal du jeu. Permet de lancer le dictaciel, de choisir le dresseur,
# puis de gerer la progression dans les arenes, combats, boutique, pokedex et dictaciel.
def menu_principal():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("#" * 70)
    print("#" + " " * 68 + "#")
    print("#" + " " * 20 + "POKEMON : LE COMBAT DES TROIS ARENES" + " " * 7 + "#")
    print("#" + " " * 68 + "#")
    print("#" * 70)
    print("\nPREPARE-TOI POUR UNE AVENTURE INCROYABLE ET PLEINE DE DEFIS !")
    print("-" * 70 + "\n")
    dictaciel = input("Veux-tu lancer le dictaciel ? (oui/non) : ").lower()
    if dictaciel in ["oui", "o"]:
        scene_dictaciel()
    dresseur = choisir_dresseur()
    pokedex = []
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=" * 70)
        print(" SCENE : LANCEMENT DU JEU ".center(70, "="))
        print("=" * 70)
        lancer = input("Veux-tu lancer le jeu ? (oui/non) : ").lower()
        if lancer in ["oui", "o"]:
            print(f"\nLe jeu commence avec {dresseur.nom} !")
            input("\nAppuie sur Entree pour continuer...")
            pokemon_joueur = choisir_pokemon_depart()
            pokedex.append(pokemon_joueur)
            dresseur.deck.append(pokemon_joueur)
            print(f"\nTU AS CHOISI {pokemon_joueur.nom.upper()} ({pokemon_joueur.type}) ! BONNE CHANCE !")
            print("\nTU ENTRE DANS LA PREMIERE ARENE : ARENE FLAMME.")
            input("\nAppuie sur Entree pour continuer...")
            # Liste des arenes a parcourir
            arenes = [
                ("Arene Flamme (Feu)", arene_feu),
                ("Arene Ocean (Eau)", arene_eau),
                ("Arene Verdure (Plante)", arene_plante)
            ]
            arene_index = 0
            continuer_jeu = True
            while arene_index < len(arenes) and continuer_jeu:
                nom_arene, arene_courante = arenes[arene_index]
                # Menu avant arène
                while True:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("=" * 70)
                    print(f" SCENE : MENU AVANT COMBAT ({nom_arene.upper()}) ".center(70, "="))
                    print("=" * 70)
                    print("1. Lancer le combat")
                    print("2. Accéder à la boutique")
                    print("3. Afficher le dictaciel")
                    print("4. Consulter le Pokédex")
                    print("5. Quitter le jeu")
                    choix_menu = input("Choisis une option (1-5) : ")
                    if choix_menu == "1":
                        # Proposer de choisir un Pokémon du Pokédex avant le combat
                        pokemon_joueur = choisir_pokemon_pokedex(pokedex, pokemon_joueur)
                        # Combats arène niveaux 1 à 4
                        victoire_niveaux = combat_arene(pokemon_joueur, arene_courante, dresseur)
                        if not victoire_niveaux:
                            print("TU N'AS PAS REUSSI A VAINCRE L'ARENE. TU PEUX REESSAYER.")
                            input("\nAppuie sur Entree pour continuer...")
                            continue
                        # Combat boss
                        victoire_boss = False
                        while not victoire_boss:
                            victoire_boss = combat_boss(pokemon_joueur, arene_courante, dresseur)
                            if not victoire_boss:
                                print("TU N'AS PAS REUSSI A VAINCRE LE BOSS. TU PEUX REESSAYER.")
                                input("\nAppuie sur Entree pour continuer...")
                        # Récompense
                        dresseur.portefeuille += arene_courante.recompense
                        print(f"\n>>> TU AS RECU {arene_courante.recompense} POKEDOLLARS EN RECOMPENSE !")
                        boss_final = arene_courante.pokemon_defense[-1]
                        if boss_final not in pokedex:
                            pokedex.append(boss_final)
                            dresseur.deck.append(boss_final)
                        print("\nCHOISIS UN POKEMON SUPPLEMENTAIRE PARMI LA LISTE SUIVANTE :")
                        pokemons_choix = [pkmn for pkmn in arene_courante.pokemon_defense[:-1] if pkmn not in pokedex]
                        if not pokemons_choix:
                            print("(Tous les Pokemon de cette arene sont deja dans ton Pokedex.)")
                            input("\nAppuie sur Entree pour continuer...")
                        else:
                            for i, pkmn in enumerate(pokemons_choix, start=1):
                                print(f"{i}. {pkmn.nom} ({pkmn.type})")
                            while True:
                                choix = input("Numero de ton choix : ")
                                if choix.isdigit():
                                    choix = int(choix)
                                    if 1 <= choix <= len(pokemons_choix):
                                        nouveau_pokemon = pokemons_choix[choix - 1]
                                        if nouveau_pokemon not in pokedex:
                                            pokedex.append(nouveau_pokemon)
                                            dresseur.deck.append(nouveau_pokemon)
                                        print(f"\nTU AS AJOUTE {nouveau_pokemon.nom.upper()} A TON EQUIPE !")
                                        input("\nAppuie sur Entree pour continuer...")
                                        break
                                print("Choix invalide, reessaie.")
                        # Menu post-victoire arene/boss
                        while True:
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print("=" * 70)
                            print(" SCENE : APRES VICTOIRE D'ARENE ".center(70, "="))
                            print("=" * 70)
                            print("QUE VEUX-TU FAIRE MAINTENANT ?")
                            if arene_index < len(arenes) - 1:
                                print("1. Continuer vers la prochaine arene")
                            else:
                                print("1. Terminer le jeu")
                            print("2. Aller à la boutique")
                            print("3. Afficher le dictaciel")
                            print("4. Quitter le jeu")
                            choix_post = input("Choisis une option (1-4) : ")
                            if choix_post == "1":
                                if arene_index < len(arenes) - 1:
                                    arene_index += 1
                                    print(f"\nTU TE DIRIGES VERS LA PROCHAINE ARENE : {arenes[arene_index][0].upper()}")
                                    input("\nAppuie sur Entree pour continuer...")
                                    break
                                else:
                                    print("\nBRAVO, TU AS TERMINE TOUTES LES ARENES ! MERCI D'AVOIR JOUE !")
                                    input("\nAppuie sur Entree pour continuer...")
                                    continuer_jeu = False
                                    break
                            elif choix_post == "2":
                                scene_boutique(dresseur)
                            elif choix_post == "3":
                                scene_dictaciel()
                            elif choix_post == "4":
                                print("\nTU AS QUITTE LE JEU. A BIENTOT !")
                                exit()
                            else:
                                print("Choix invalide, reessaie.")
                        break
                    elif choix_menu == "2":
                        scene_boutique(dresseur)
                    elif choix_menu == "3":
                        scene_dictaciel()
                    elif choix_menu == "4":
                        afficher_pokedex(pokedex)
                        # Après consultation du Pokédex, proposer de choisir un Pokémon pour le combat
                        pokemon_joueur = choisir_pokemon_pokedex(pokedex, pokemon_joueur)
                    elif choix_menu == "5":
                        print("\nTU AS QUITTE LE JEU. A BIENTOT !")
                        exit()
                    else:
                        print("Choix invalide, reessaie.")
            break
        elif lancer in ["non", "n"]:
            print("\nLe jeu est annule. A bientot !")
            exit()
        else:
            print("Reponse non valide, tape 'oui' ou 'non'.")

# --- Execution principale ---
if __name__ == "__main__":
    menu_principal()