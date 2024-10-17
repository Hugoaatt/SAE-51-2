#!/bin/bash

# Fichier de log pour stocker les données CPU
LOG_FILE="/tmp/cpu_usage.csv"

# Écrire l'en-tête du fichier CSV
echo "timestamp,cpu_usage" > $LOG_FILE

# Fonction pour calculer l'utilisation du CPU
get_cpu_usage() {
    local cpu_line=$(grep '^cpu ' /proc/stat)
    local cpu_values=($cpu_line)

    # Vérifier que nous avons bien assez de valeurs CPU
    if [ ${#cpu_values[@]} -lt 8 ]; then
        echo "Erreur : Impossible de lire les valeurs de CPU."
        return 1
    fi

    local user=${cpu_values[1]}
    local nice=${cpu_values[2]}
    local system=${cpu_values[3]}
    local idle=${cpu_values[4]}
    local iowait=${cpu_values[5]}
    local irq=${cpu_values[6]}
    local softirq=${cpu_values[7]}

    local total=$((user + nice + system + idle + iowait + irq + softirq))
    local total_idle=$((idle + iowait))

    echo "$total $total_idle"
}

# Obtenir l'usage CPU initial
read cpu_total_prev cpu_idle_prev < <(get_cpu_usage)
if [ $? -ne 0 ]; then
    echo "Erreur initiale de lecture CPU. Arrêt du script."
    exit 1
fi

# Boucle pour collecter les données toutes les 5 secondes
while true; do
    # Collecte CPU
    read cpu_total cpu_idle < <(get_cpu_usage)
    if [ $? -ne 0 ]; then
        echo "Erreur lors de la collecte des données CPU."
        continue
    fi

    # Vérification pour éviter la division par zéro
    if [ $((cpu_total - cpu_total_prev)) -eq 0 ]; then
        echo "Erreur : Division par zéro évitée lors du calcul CPU."
        continue
    fi

    # Calcul de l'utilisation CPU
    cpu_usage=$((100 * (cpu_total - cpu_idle - (cpu_total_prev - cpu_idle_prev)) / (cpu_total - cpu_total_prev)))
    cpu_total_prev=$cpu_total
    cpu_idle_prev=$cpu_idle

    # Écriture des données dans le fichier de log
    echo "$(date '+%Y-%m-%d %H:%M:%S'), $cpu_usage" >> $LOG_FILE

    # Pause de 5 secondes avant la prochaine collecte
    sleep 1
done

