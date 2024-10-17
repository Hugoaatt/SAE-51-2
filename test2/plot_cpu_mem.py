import matplotlib.pyplot as plt
import datetime

# Fichier de log généré par le script Bash
LOG_FILE = "/tmp/cpu_memory_usage.log"

# Listes pour stocker les données de temps, CPU et mémoire
timestamps = []
cpu_usages = []
memory_usages = []

# Lecture du fichier de log
with open(LOG_FILE, 'r') as file:
    for line in file:
        parts = line.strip().split(", ")
        timestamp_str = parts[0]
        cpu_usage_str = parts[1].split(": ")[1].replace("%", "")
        memory_usage_str = parts[2].split(": ")[1].replace("%", "")
        
        # Conversion des données en formats appropriés
        timestamp = datetime.datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")
        cpu_usage = float(cpu_usage_str)
        memory_usage = float(memory_usage_str)
        
        timestamps.append(timestamp)
        cpu_usages.append(cpu_usage)
        memory_usages.append(memory_usage)

# Création des graphiques
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

# Graphique d'utilisation du CPU
ax1.plot(timestamps, cpu_usages, label="Utilisation CPU (%)", color="blue")
ax1.set_xlabel("Temps")
ax1.set_ylabel("Utilisation CPU (%)")
ax1.set_title("Utilisation CPU dans le temps")
ax1.legend()
ax1.grid(True)

# Graphique d'utilisation de la mémoire
ax2.plot(timestamps, memory_usages, label="Utilisation Mémoire (%)", color="green")
ax2.set_xlabel("Temps")
ax2.set_ylabel("Utilisation Mémoire (%)")
ax2.set_title("Utilisation Mémoire dans le temps")
ax2.legend()
ax2.grid(True)

# Afficher les graphiques
plt.tight_layout()
plt.show()

