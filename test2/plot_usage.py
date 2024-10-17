import matplotlib.pyplot as plt

# Fichiers contenant les données CPU et mémoire
CPU_LOG = "/tmp/cpu_usage.log"
MEMORY_LOG = "/tmp/memory_usage.log"

# Fonction pour lire les données CPU
def read_cpu_data(filename):
    timestamps = []
    cpu_usages = []
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split()
            timestamps.append(parts[0])
            cpu_usages.append(float(parts[1]))
    return timestamps, cpu_usages

# Fonction pour lire les données mémoire
def read_memory_data(filename):
    timestamps = []
    memory_usages = []
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split()
            timestamps.append(parts[0])
            memory_usages.append(float(parts[1]))
    return timestamps, memory_usages

# Lecture des données CPU et mémoire
cpu_timestamps, cpu_usages = read_cpu_data(CPU_LOG)
memory_timestamps, memory_usages = read_memory_data(MEMORY_LOG)

# Création des graphiques
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

# Graphique d'utilisation du CPU
ax1.plot(cpu_timestamps, cpu_usages, label="Utilisation CPU (%)", color="blue")
ax1.set_xlabel("Temps")
ax1.set_ylabel("Utilisation CPU (%)")
ax1.set_title("Utilisation CPU dans le temps")
ax1.legend()
ax1.grid(True)

# Graphique d'utilisation de la mémoire
ax2.plot(memory_timestamps, memory_usages, label="Utilisation Mémoire (%)", color="green")
ax2.set_xlabel("Temps")
ax2.set_ylabel("Utilisation Mémoire (%)")
ax2.set_title("Utilisation Mémoire dans le temps")
ax2.legend()
ax2.grid(True)

# Afficher les graphiques
plt.tight_layout()
plt.show()

