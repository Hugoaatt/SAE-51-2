#!/bin/bash

# Fichier de log pour stocker les données CPU et mémoire
LOG_FILE="/tmp/cpu_memory_usage.log"

# Fonction pour calculer l'utilisation du CPU
get_cpu_usage() {
    # Lire les statistiques CPU à partir de /proc/stat
    local cpu_line=$(grep '^cpu ' /proc/stat)
    local cpu_values=($cpu_line)

    # Vérifiez que la ligne CPU contient bien des valeurs suffisantes
    if [ ${#cpu_values[@]} -lt 8 ]; then
        echo "Erreur : Impossible de lire les valeurs de CPU."
        return 1
    fi

    # Extraire les valeurs d'utilisation
    local user=${cpu_values[1]}
    local nice=${cpu_values[2]}
    local system=${cpu_values[3]}
    local idle=${cpu_values[4]}
    local iowait=${cpu_values[5]}
    local irq=${cpu_values[6]}
    local softirq=${cpu_values[7]}

    # Calculer l'utilisation totale et l'idle
    local total=$((user + nice + system + idle + iowait + irq + softirq))
    local total_idle=$((idle + iowait))

    echo "$total $total_idle"
}

# Fonction pour calculer l'utilisation de la mémoire
get_memory_usage() {
    # Lire les informations de mémoire à partir de /proc/meminfo
    local mem_total=$(grep 'MemTotal:' /proc/meminfo | awk '{print $2}')
    local mem_free=$(grep 'MemFree:' /proc/meminfo | awk '{print $2}')
    local buffers=$(grep 'Buffers:' /proc/meminfo | awk '{print $2}')
    local cached=$(grep 'Cached:' /proc/meminfo | awk '{print $2}')

    # Vérifiez que les valeurs ne sont pas nulles pour éviter la division par zéro
    if [ -z "$mem_total" ] || [ "$mem_total" -eq 0 ]; then
        echo "Erreur : Impossible de lire la mémoire totale ou valeur nulle."
        return 1
    fi

    # Calculer la mémoire utilisée
    local mem_used=$((mem_total - mem_free - buffers - cached))
    echo "$mem_total $mem_used"
}

# Initialiser les valeurs CPU pour le calcul de l'utilisation
read cpu_total_prev cpu_idle_prev < <(get_cpu_usage)

# Vérifier si les valeurs CPU initiales sont valides
if [ $? -ne 0 ]; then
    echo "Erreur initiale de lecture CPU. Arrêt du script."
    exit 1
fi

# Collecte des données toutes les 5 secondes
while true; do
    # Calculer l'utilisation CPU
    read cpu_total cpu_idle < <(get_cpu_usage)
    if [ $? -ne 0 ]; then
        echo "Erreur lors de la collecte des données CPU."
        continue
    fi

    # Calcul de l'utilisation du CPU en pourcentage
    cpu_usage=$((100 * (cpu_total - cpu_idle - (cpu_total_prev - cpu_idle_prev)) / (cpu_total - cpu_total_prev)))
    cpu_total_prev=$cpu_total
    cpu_idle_prev=$cpu_idle

    # Calculer l'utilisation mémoire
    read mem_total mem_used < <(get_memory_usage)
    if [ $? -ne 0 ]; then
        echo "Erreur lors de la collecte des données mémoire."
        continue
    fi

    # Calcul de l'utilisation mémoire en pourcentage
    mem_usage=$((100 * mem_used / mem_total))

    # Écrire les résultats dans le fichier de log avec l'horodatage
    echo "$(date '+%Y-%m-%d %H:%M:%S'), CPU: $cpu_usage%, Memory: $mem_usage%" >> $LOG_FILE

    # Attendre 5 secondes avant la prochaine mesure
    sleep 5
done

