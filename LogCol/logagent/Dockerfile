# Utiliser une image de base compatible avec logagent
FROM sematext/logagent:latest

# Copier le fichier de configuration
COPY logagent.conf /etc/logagent.conf

# Exécuter logagent avec le fichier de configuration
CMD ["logagent", "-c", "/etc/logagent.conf"]

