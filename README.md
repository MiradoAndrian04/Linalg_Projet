# Projet d'Algèbre Linéaire

Ce projet est une implémentation en Python de l'Analyse en Composantes Principales (ACP) pour l'analyse et la visualisation de données. Il inclut des fonctionnalités pour charger des ensembles de données, effectuer une ACP et visualiser les résultats à travers divers graphiques.

## Structure du Projet

```
Linalg_Projet
│
├── README.md                # Documentation du projet
├── requirements.txt         # Dépendances Python
├── data/                    # Dossier contenant des ensembles de données d'exemple
│   ├── data_jouets.csv
│   ├── iris.csv
│   ├── notes_etudiants.csv
│   ├── notes_sim.csv
│   └── score_sim.csv
├── notebooks/               # Dossier pour les notebooks Jupyter
│   └── dataset.py
├── results/                 # Dossier pour stocker les résultats
│   └── figures/             # Graphiques générés
│       ├── bar_variance.png
│       ├── color_by_value.png
│       ├── line_cumulative.png
│       └── scatter_projection.png
├── src/                     # Code source
│   ├── algorithme.py        # Implémentation de l'ACP
│   ├── data_loader.py       # Utilitaires de chargement des données
│   ├── linalg_utils.py      # Utilitaires d'algèbre linéaire
│   ├── main.py              # Script principal pour exécuter le projet
│   └── utils/               # Fonctions utilitaires
│       └── visualisation.py # Utilitaires de visualisation
```

## Fonctionnalités

1. **Chargement des Données** : Charger des fichiers CSV depuis le dossier `data/` et les prétraiter pour l'analyse.
2. **Analyse en Composantes Principales (ACP)** : Effectuer une ACP pour réduire la dimensionnalité des ensembles de données.
3. **Visualisation des Données** : Générer divers graphiques pour visualiser les résultats de l'ACP, y compris :
   - Nuage de points des données originales vs projetées
   - Diagramme en barres de la variance expliquée par les composantes principales
   - Graphique en ligne de la variance cumulée
   - Nuage de points avec des points colorés selon leur valeur

## Installation

1. Clonez le dépôt :
   ```bash
   git clone <repository-url>
   cd Linalg_Projet
   ```

2. Installez les dépendances requises :
   ```bash
   pip install -r requirements.txt
   ```

## Utilisation

1. Exécutez le script principal :
   ```bash
   python src/main.py
   ```

2. Suivez les instructions pour sélectionner un ensemble de données dans le dossier `data/`.

3. Le script :
   - Charge et prétraite l'ensemble de données sélectionné.
   - Effectue une ACP pour réduire la dimensionnalité des données.
   - Affiche les valeurs propres et les composantes principales.
   - Génère et enregistre les visualisations dans le dossier `results/figures/`.

## Dépendances

Le projet nécessite les bibliothèques Python suivantes :
- `numpy`
- `scipy`
- `matplotlib`
- `pandas`

Ces bibliothèques peuvent être installées à l'aide du fichier `requirements.txt`.

## Données

Le dossier `data/` contient des ensembles de données d'exemple pour tester l'implémentation de l'ACP. Vous pouvez ajouter vos propres fichiers CSV à ce dossier pour analyser des ensembles de données personnalisés.

## Résultats

Les résultats de l'analyse ACP, y compris les visualisations, sont enregistrés dans le dossier `results/figures/`. Les graphiques suivants sont générés :
- `scatter_projection.png` : Nuage de points des données originales vs projetées.
- `bar_variance.png` : Diagramme en barres de la variance expliquée par les composantes principales.
- `line_cumulative.png` : Graphique en ligne de la variance cumulée.
- `color_by_value.png` : Nuage de points avec des points colorés selon leur valeur.

## Contribution

Les contributions sont les bienvenues ! N'hésitez pas à forker ce dépôt et à soumettre des pull requests.

## Licence

Ce projet est sous licence MIT.