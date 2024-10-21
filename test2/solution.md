# Surveillance de l'Utilisation du CPU en Temps Réel

## Introduction

Ce projet contient deux scripts :
1. **Un script Bash** pour surveiller l'utilisation du CPU et enregistrer les données dans un fichier CSV.
2. **Un script Python** pour visualiser les données du fichier CSV sous forme de graphique en temps réel à l'aide de Matplotlib.

---

## Prérequis

Avant d'utiliser ces scripts, assurez-vous d'avoir installé les logiciels suivants sur votre machine :
- **Python 3.x** avec les bibliothèques :
  - `pandas`
  - `matplotlib`

Pour installer les dépendances Python, utilisez la commande suivante :

```bash
pip install pandas matplotlib
```
---
### Script 1 : Surveillance de l'Utilisation du CPU (Bash)

Le script Bash collect_cpu_mem.sh collecte les données de l'utilisation du CPU à intervalles réguliers (1 seconde par défaut) et enregistre ces données dans un fichier CSV.

#### Utilisation

1. Rendez le script exécutable avec la commande suivante :
```Bash
chmod +x collect_cpu_mem.sh
```
2. Exécutez le script pour commencer la collecte des données CPU :
```Bash
./collect_cpu_mem.sh
```

---
### Script 2 : Visualisation de l'Utilisation du CPU (Python)

Le script Python lit les données collectées dans le fichier CSV et les affiche sous forme de graphique en temps réel. Il utilise la bibliothèque matplotlib pour tracer les données.

#### Utilisation

1. Assurez-vous d'avoir les bibliothèques Python nécessaires en exécutant :
```Bash
pip install pandas matplotlib
```
2. Exécutez le script Python pour visualiser l'utilisation du CPU en temps réel :
```Bash
python3 cpu_plot.py
```
Le script mettra à jour le graphique en temps réel, en affichant les nouvelles données collectées à chaque seconde.

---
### Résumé

Script Bash : Collecte les données CPU et les enregistre dans un fichier CSV.

Script Python : Utilise matplotlib pour lire les données du fichier CSV et afficher un graphique en temps réel avec l'utilisation du CPU.
