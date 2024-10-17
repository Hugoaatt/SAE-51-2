import matplotlib.pyplot as plt
import psutil
import time
import datetime

# Simuler la génération de logs réels à partir des ressources système
log_data = {'timestamp': [], 'cpu_usage': [], 'ram_usage': []}

# Collecter les données sur une période de 100 cycles
for _ in range(100):
    # Récupérer l'utilisation réelle du CPU (%)
    cpu_usage = psutil.cpu_percent(interval=1)  # On attend 1 seconde pour calculer l'usage CPU
    # Récupérer l'utilisation réelle de la RAM (%)
    ram_usage = psutil.virtual_memory().percent
    
    # Stocker les données avec un timestamp
    log_data['timestamp'].append(datetime.datetime.now().strftime("%H:%M:%S"))
    log_data['cpu_usage'].append(cpu_usage)
    log_data['ram_usage'].append(ram_usage)
    
    # Attendre un peu avant de collecter à nouveau
    time.sleep(0.5)  # pause de 0,5 seconde entre les collectes

# Visualisation des données avec Matplotlib
plt.figure(figsize=(10, 6))

# Graphique pour l'utilisation CPU
plt.subplot(2, 1, 1)
plt.plot(log_data['timestamp'], log_data['cpu_usage'], label='CPU Usage (%)', color='blue')
plt.title('CPU Usage Over Time')
plt.ylabel('Usage (%)')
plt.xticks(rotation=45)
plt.grid(True)

# Graphique pour l'utilisation RAM
plt.subplot(2, 1, 2)
plt.plot(log_data['timestamp'], log_data['ram_usage'], label='RAM Usage (%)', color='green')
plt.title('RAM Usage Over Time')
plt.ylabel('Usage (%)')
plt.xticks(rotation=45)
plt.grid(True)

plt.tight_layout()
plt.show()

