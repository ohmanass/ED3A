# 🎮 ED3A — Le jeu des 3 Arènes

## 📝 Description
**ED3A** est un projet développé en **Python** dans le cadre du **Master 1 à H3 Hitema**.  
Il s’agit d’une version **textuelle du jeu de combat Pokémon**, intitulée *Le jeu des 3 Arènes*.

Le joueur affronte plusieurs dresseurs dans trois arènes successives, en gérant ses Pokémon, leurs points de vie et leurs attaques.  
Chaque combat repose sur la stratégie, la gestion des ressources et le choix du bon Pokémon au bon moment.

---

## 🚀 Installation et exécution

### 1️⃣ Cloner le projet
```bash
git clone https://github.com/ohmanass/ED3A.git
cd ED3A
```

### 2️⃣ Créer un environnement virtuel (optionnel mais recommandé)
```bash
python -m venv venv
```

### 3️⃣ Activer l'environnement virtuel
- **Windows :**
  ```bash
  venv\Scripts\activate
  ```
- **macOS / Linux :**
  ```bash
  source venv/bin/activate
  ```

### 4️⃣ Installer les dépendances
Si un fichier `requirements.txt` existe :
```bash
pip install -r requirements.txt
```

Sinon, le jeu ne dépend que de la **librairie standard de Python 3.10+**.

### 5️⃣ Lancer le jeu
```bash
python main.py
```

> 🔧 Remplace `main.py` par le nom de ton fichier principal (par exemple `arene.py` ou `dresseur.py` si c’est ton point d’entrée).

---

## ⚔️ Fonctionnalités principales
- Système de **combat tour par tour**
- Gestion des **Pokémon**, **attaques** et **points de vie**
- **Trois arènes** de difficulté croissante
- Système d’achat via une **boutique** pour gérer l’équipement
- Affichage **textuel clair et immersif**

---

## 🧩 Technologies utilisées
- **Python 3.10+**
- Aucun framework externe requis

---

## 📈 Améliorations possibles
- Ajout d’une **interface graphique** (via Tkinter ou PyQt)
- Implémentation d’une **IA avancée** pour les dresseurs
- Sauvegarde des parties (système de fichiers ou base de données)
- Extension avec de nouvelles arènes et Pokémon

---

## 👨‍💻 Auteur
**Nassim Touissi**  
Étudiant en Master 1 Développement & Data à **H3 Hitema**  
🔗 [GitHub : ohmanass](https://github.com/ohmanass)

---

## 📄 Licence
Projet réalisé dans un cadre académique.  
Libre d’utilisation à des fins pédagogiques et personnelles.
