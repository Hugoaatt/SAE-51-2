#!/bin/bash

# Fichiers temporaires pour stocker les données CPU et mémoire
CPU_LOG="/tmp/cpu_usage.log"
MEMORY_LOG="/tmp/memory_usage.log"

# Extraire les données CPU
echo "Collecte des données CPU..."
sar -u 1 5 | awk '/^[0-9]/ {print $1, 100 - $8}' > $CPU_LOG

# Extraire les données mémoire
echo "Collecte des données mémoire..."
sar -r 1 5 | awk '/^[0-9]/ {print $1, $4}' > $MEMORY_LOG

echo "Données CPU et mémoire collectées et stockées dans $CPU_LOG et $MEMORY_LOG"

