import matplotlib.pyplot as plt
import pandas as pd
import time

# Chemin vers le fichier de log
LOG_FILE = '/tmp/cpu_usage.csv'

# Initialisation des listes pour stocker les timestamps et les valeurs de CPU
timestamps = []
cpu_usages = []

# Configuration de la figure
plt.ion()  # Mode interactif
fig, ax = plt.subplots()
line, = ax.plot(timestamps, cpu_usages, marker='o', linestyle='-')
ax.set_title('Utilisation du CPU en Temps Réel')
ax.set_xlabel('Temps')
ax.set_ylabel('Utilisation CPU (%)')
ax.grid()

# Boucle pour lire les logs en temps réel
while True:
    # Lire les dernières données à partir du fichier CSV
    try:
        data = pd.read_csv(LOG_FILE)
        # Obtenir le dernier timestamp et l'utilisation du CPU
        last_entry = data.iloc[-1]
        timestamp = last_entry['timestamp']
        cpu_usage = last_entry['cpu_usage']

        # Ajouter les nouvelles données aux listes
        timestamps.append(pd.to_datetime(timestamp))
        cpu_usages.append(cpu_usage)

        # Mettre à jour le graphique
        line.set_xdata(timestamps)
        line.set_ydata(cpu_usages)
        ax.relim()  # Réajuster les limites
        ax.autoscale_view()  # Auto-scaling des axes
        plt.draw()
        plt.pause(0.1)  # Pause pour permettre le rafraîchissement du graphique
    except Exception as e:
        print(f"Erreur lors de la lecture du fichier : {e}")

    # Pause pour éviter une lecture trop fréquente
    time.sleep(1)

