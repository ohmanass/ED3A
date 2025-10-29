# Classe representant notre dictaciel ( presentation de notre jeu )

def dictaciel_logique():
    print("\n" + "="*60)
    print(" " * 15 + "DICTACIEL LOGIQUE DU JEU POKÉMON")
    print("="*60 + "\n")

    print("Le combat des trois arènes est simple. Voici la logique de fonctionnement :\n")

    print("1. Choix du dresseur :")
    print("   - Tu peux choisir un dresseur connu ou créer le tien.")
    print("   - Chaque dresseur possède un deck de Pokémon et un inventaire d'items.")
    print("   - Chaque dresseur a aussi un portefeuille pour gérer ton argent.\n")

    print("2. Choix du Pokémon de départ :")
    print("   - Trois choix possibles : Salamèche (Feu), Carapuce (Eau), Bulbizarre (Plante).")
    print("   - Ce Pokémon est ajouté à ton deck et sera ton premier combattant.\n")

    print("3. Combat dans l'arène :")
    print("   - Chaque arène a un type (Feu, Eau, Plante) et un boss final.")
    print("   - Les combats se déroulent en niveaux de 1 à 5.")
    print("   - Niveaux 1 à 4 : tu affrontes un Pokémon aléatoire parmi les défenseurs.")
    print("   - Niveau 5 : combat final contre le boss de l'arène.")
    print("   - Les PV sont gérés pour chaque combat, et les multiplicateurs de type s'appliquent.")
    print("   - Si tu perds, tu peux réessayer le même niveau sans perdre ta progression.\n")

    print("4. Récompenses après victoire dans l'arène :")
    print("   - Le boss vaincu est automatiquement ajouté à ton deck.")
    print("   - Tu peux choisir un Pokémon supplémentaire parmi les défenseurs de l'arène (hors boss et starter).")
    print("   - Tu obtiens le badge de l'arène après avoir vaincu le boss final.\n")

    print("5. Boutique Pokémon :")
    print("   - Après chaque combat, tu peux accéder à la boutique.")
    print("   - Chaque item a un prix et une quantité maximale de 2 par dresseur.")
    print("   - Les items restaurent des PV fixes ou en pourcentage, ou réaniment les Pokémon K.O.")
    print("   - Ton argent est géré via ton portefeuille.\n")

    print("6. Fin du jeu :")
    print("   - Le jeu peut continuer sur d'autres arènes après la première.")
    print("   - Ton objectif est de collecter tous les badges et Pokémon puissants.")
    print("   - Tu construis progressivement ton Pokédex et ton deck.\n")

    print("="*60)
    print(" " * 20 + "FIN DU DICTACIEL")
    print("="*60 + "\n")