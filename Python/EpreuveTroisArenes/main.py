from pokemon import lst_pkmn_feu, lst_pkmn_eau, lst_pkmn_plante, PokemonFeu, PokemonEau, PokemonPlante, efficacite
from arene import Arene
from item import list_items
from boutique import Boutique
from dresseur import Dresseur, dresseurs_connus
from dictaciel import dictaciel_logique
import random

def couleur_pokemon(pokemon):
    return pokemon.nom

# --- Création des items et arènes ---
boutique = Boutique(list_items)
arene_feu = Arene(
    "Arène Flamme", "Feu", "Pyro", [p for p in lst_pkmn_feu[:-1]], 100, 3, "Badge Flamme"
)
arene_eau = Arene(
    "Arène Océan", "Eau", "Aqua", [p for p in lst_pkmn_eau[:-1]], 200, 3, "Badge Océan"
)
arene_plante = Arene(
    "Arène Verdure", "Plante", "Florina", [p for p in lst_pkmn_plante[:-1]], 500, 3, "Badge Feuille"
)

# --- Fonction : Choisir un dresseur ---
def choisir_dresseur():
    print("=== CHOISIS TON DRESSEUR POKÉMON ===\n")
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
    print("\n=== CHOISIS TON POKÉMON DE DÉPART ===")
    print("1. Salamèche (Feu)")
    print("2. Carapuce (Eau)")
    print("3. Bulbizarre (Plante)")
    while True:
        choix = input("Numéro de ton choix : ")
        if choix == "1":
            return lst_pkmn_feu[0]
        elif choix == "2":
            return lst_pkmn_eau[0]
        elif choix == "3":
            return lst_pkmn_plante[0]
        else:
            print("Choix invalide, réessaie.")

# --- Combat tour par tour ---
def combat(pokemon_joueur, arene, dresseur):
    print("\n" + "-" * 60)
    print(f" DÉBUT DU COMBAT DANS {arene.nom.upper()} CONTRE DES POKÉMON DE TYPE {arene.type_arene.upper()} ")
    print("-" * 60)
    # Message d'avantage de type unique
    adv = efficacite[pokemon_joueur.type][arene.type_arene]
    if adv > 1:
        print(f"\n>>> TON POKÉMON A UN AVANTAGE DE TYPE ({pokemon_joueur.type.upper()} > {arene.type_arene.upper()}) POUR CETTE ARÈNE !")
    elif adv < 1:
        print(f"\n>>> TON POKÉMON A UN DÉSAVANTAGE DE TYPE ({pokemon_joueur.type.upper()} < {arene.type_arene.upper()}) POUR CETTE ARÈNE.")
    else:
        print(f"\n>>> TYPE NEUTRE POUR CETTE ARÈNE.")

    def combat_contre(adversaire, pokemon_joueur):
        adversaire_pv_initial = adversaire.pv
        pokemon_joueur_pv_initial = pokemon_joueur.pv
        tour = 1
        while pokemon_joueur.pv > 0 and adversaire.pv > 0:
            print("\n" + "-" * 40)
            print(f"TOUR {tour}")
            print(f"{pokemon_joueur.nom.upper()} ({pokemon_joueur.type}) : {pokemon_joueur.pv} PV")
            print(f"{adversaire.nom.upper()} ({adversaire.type}) : {adversaire.pv} PV")
            print("-" * 40)
            print("TON TOUR :")
            pokemon_joueur.attaquer(adversaire)
            if adversaire.pv <= 0:
                print(f"{adversaire.nom.upper()} EST K.O.")
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
        print("\n" + "=" * 60)
        print(f" COMBAT NIVEAU {niveau_actuel} : {pokemon_joueur.nom.upper()} ({pokemon_joueur.type}) VS {adversaire.nom.upper()} ({adversaire.type}) ")
        print("=" * 60)
        victoire = combat_contre(adversaire, pokemon_joueur)
        if victoire:
            print(f"\n>>> TU AS GAGNÉ LE COMBAT NIVEAU {niveau_actuel} !")
            niveau_actuel += 1
        else:
            print(">>> TU PEUX RÉESSAYER CE NIVEAU.")

        # Menu après chaque combat
        while True:
            print("\n" + "-" * 40)
            print("QUE VEUX-TU FAIRE MAINTENANT ?")
            print("1. Continuer vers le combat suivant")
            print("2. Ouvrir la boutique")
            print("3. Afficher le dictaciel")
            print("4. Quitter le jeu")
            choix_action = input("Choisis une option (1-4) : ")
            if choix_action == "1":
                break
            elif choix_action == "2":
                menu_boutique(dresseur)
            elif choix_action == "3":
                dictaciel_logique()
            elif choix_action == "4":
                print("Tu as quitté le jeu. À bientôt !")
                exit()
            else:
                print("Choix invalide, réessaie.")

    # Combat final (niveau 5) contre le boss de l'arène
    adversaire = arene.pokemon_defense[-1]
    print("\n" + "=" * 60)
    print(f" COMBAT FINAL CONTRE LE BOSS {adversaire.nom.upper()} DANS {arene.nom.upper()} ")
    print("=" * 60)
    tour = 1
    pokemon_joueur_pv_initial = pokemon_joueur.pv
    adversaire_pv_initial = adversaire.pv
    while pokemon_joueur.pv > 0 and adversaire.pv > 0:
        print("\n" + "-" * 40)
        print(f"TOUR {tour}")
        print(f"{pokemon_joueur.nom.upper()} ({pokemon_joueur.type}) : {pokemon_joueur.pv} PV")
        print(f"{adversaire.nom.upper()} ({adversaire.type}) : {adversaire.pv} PV")
        print("-" * 40)
        print("TON TOUR :")
        pokemon_joueur.attaquer(adversaire)
        if adversaire.pv <= 0:
            print(f"{adversaire.nom.upper()} EST K.O.")
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
            print("Tu peux réessayer le combat final.")
        tour += 1
    print("-" * 40)
    # Remise à zéro des PV
    pokemon_joueur.pv = pokemon_joueur_pv_initial
    adversaire.pv = adversaire_pv_initial
    if adversaire.pv <= 0:
        print(f"\nFÉLICITATIONS ! TU AS VAINCU LE BOSS {adversaire.nom.upper()} ET OBTENU LE {arene.badge.upper()} !")
        return True
    else:
        return False

# --- Menu Boutique centralisé ---
def menu_boutique(dresseur):
    while True:
        print("\n" + "-" * 40)
        print(f"TON PORTEFEUILLE : {dresseur.portefeuille} Pokédollars")
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
            choix_item = input("Entre le numéro de l'item à acheter (ou '0' pour annuler) : ")
            if choix_item.isdigit():
                choix_item = int(choix_item)
                if choix_item == 0:
                    break
                elif 1 <= choix_item <= len(boutique.items):
                    item_choisi = boutique.items[choix_item - 1]
                    if dresseur.portefeuille < item_choisi.prix:
                        print("Tu n'as pas assez de Pokédollars pour cet item.")
                    else:
                        # Nouvelle gestion via dictionnaire
                        if isinstance(dresseur.inventaire.items, dict):
                            nb_exemplaires = dresseur.inventaire.items.get(item_choisi, 0)
                            if nb_exemplaires >= 2:
                                print("Tu as déjà 2 exemplaires de cet item. Tu ne peux pas en acheter plus.")
                            else:
                                dresseur.portefeuille -= item_choisi.prix
                                dresseur.inventaire.items[item_choisi] = nb_exemplaires + 1
                                print(f"Tu as acheté {item_choisi.nom} pour {item_choisi.prix} Pokédollars.")
                        else:
                            # fallback ancienne logique (liste)
                            nb_exemplaires = dresseur.inventaire.items.count(item_choisi)
                            if nb_exemplaires >= 2:
                                print("Tu as déjà 2 exemplaires de cet item. Tu ne peux pas en acheter plus.")
                            else:
                                dresseur.portefeuille -= item_choisi.prix
                                dresseur.inventaire.items.append(item_choisi)
                                print(f"Tu as acheté {item_choisi.nom} pour {item_choisi.prix} Pokédollars.")
                else:
                    print("Numéro invalide.")
            else:
                print("Entrée invalide.")
        elif choix_achat in ['non', 'n']:
            break
        else:
            print("Réponse invalide, tape 'oui' ou 'non'.")

# --- Menu principal ---
def menu_principal():
    print("\n" + "#" * 70)
    print("#" + " " * 68 + "#")
    print("#" + " " * 20 + "POKÉMON : LE COMBAT DES TROIS ARÈNES" + " " * 7 + "#")
    print("#" + " " * 68 + "#")
    print("#" * 70)
    print("\nPRÉPARE-TOI POUR UNE AVENTURE INCROYABLE ET PLEINE DE DÉFIS !")
    print("-" * 70 + "\n")
    dictaciel = input("Veux-tu lancer le dictaciel ? (oui/non) : ").lower()
    if dictaciel in ["oui", "o"]:
        dictaciel_logique()
    dresseur = choisir_dresseur()
    pokedex = []
    while True:
        lancer = input("\nVeux-tu lancer le jeu ? (oui/non) : ").lower()
        if lancer in ["oui", "o"]:
            print(f"\nLe jeu commence avec {dresseur.nom} !")
            pokemon_joueur = choisir_pokemon_depart()
            pokedex.append(pokemon_joueur)
            dresseur.deck.append(pokemon_joueur)
            print(f"\nTU AS CHOISI {pokemon_joueur.nom.upper()} ({pokemon_joueur.type}) ! BONNE CHANCE !")
            print("\nTU ENTRE DANS LA PREMIÈRE ARÈNE : ARÈNE FLAMME.")
            arenes = [
                ("Arène Flamme", arene_feu),
                ("Arène Océan", arene_eau),
                ("Arène Verdure", arene_plante)
            ]
            arene_index = 0
            continuer_jeu = True
            while arene_index < len(arenes) and continuer_jeu:
                nom_arene, arene_courante = arenes[arene_index]
                while True:
                    print("\n" + "=" * 60)
                    print(f"MENU AVANT COMBAT ({nom_arene.upper()}) :")
                    print("1. Lancer le combat")
                    print("2. Accéder à la boutique")
                    print("3. Afficher le dictaciel")
                    print("4. Quitter le jeu")
                    choix_menu = input("Choisis une option (1-4) : ")
                    if choix_menu == "1":
                        victoire = combat(pokemon_joueur, arene_courante, dresseur)
                        if victoire:
                            dresseur.portefeuille += arene_courante.recompense
                            print(f"\n>>> TU AS REÇU {arene_courante.recompense} POKÉDOLLARS EN RÉCOMPENSE !")
                            boss_final = arene_courante.pokemon_defense[-1]
                            if boss_final not in pokedex:
                                pokedex.append(boss_final)
                                dresseur.deck.append(boss_final)
                            print("\nCHOISIS UN POKÉMON SUPPLÉMENTAIRE PARMI LA LISTE SUIVANTE :")
                            pokemons_choix = [pkmn for pkmn in arene_courante.pokemon_defense[:-1] if pkmn != pokemon_joueur]
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
                                            dresseur.deck.append(nouveau_pokemon)
                                        print(f"\nTU AS AJOUTÉ {nouveau_pokemon.nom.upper()} À TON ÉQUIPE !")
                                        break
                                print("Choix invalide, réessaie.")
                            # Menu post-victoire arène
                            while True:
                                print("\n" + "-" * 40)
                                print("QUE VEUX-TU FAIRE MAINTENANT ?")
                                if arene_index < len(arenes) - 1:
                                    print("1. Continuer vers la prochaine arène")
                                else:
                                    print("1. Terminer le jeu")
                                print("2. Aller à la boutique")
                                print("3. Afficher le dictaciel")
                                print("4. Quitter le jeu")
                                choix_post = input("Choisis une option (1-4) : ")
                                if choix_post == "1":
                                    if arene_index < len(arenes) - 1:
                                        arene_index += 1
                                        print(f"\nTU TE DIRIGES VERS LA PROCHAINE ARÈNE : {arenes[arene_index][0].upper()}")
                                        break
                                    else:
                                        print("\nBRAVO, TU AS TERMINÉ TOUTES LES ARÈNES ! MERCI D'AVOIR JOUÉ !")
                                        continuer_jeu = False
                                        break
                                elif choix_post == "2":
                                    menu_boutique(dresseur)
                                elif choix_post == "3":
                                    dictaciel_logique()
                                elif choix_post == "4":
                                    print("\nTU AS QUITTÉ LE JEU. À BIENTÔT !")
                                    exit()
                                else:
                                    print("Choix invalide, réessaie.")
                            break
                        else:
                            print("TU N'AS PAS RÉUSSI À VAINCRE L'ARÈNE. TU PEUX RÉESSAYER.")
                    elif choix_menu == "2":
                        menu_boutique(dresseur)
                    elif choix_menu == "3":
                        dictaciel_logique()
                    elif choix_menu == "4":
                        print("\nTU AS QUITTÉ LE JEU. À BIENTÔT !")
                        exit()
                    else:
                        print("Choix invalide, réessaie.")
            break
        elif lancer in ["non", "n"]:
            print("\nLe jeu est annulé. À bientôt !")
            exit()
        else:
            print("Réponse non valide, tape 'oui' ou 'non'.")

# --- Exécution principale ---
if __name__ == "__main__":
    menu_principal()