# Dockerfile pour Logagent
FROM node:14-alpine

# Installer Logagent
RUN npm install -g @sematext/logagent

# Copier le fichier de configuration
COPY logagent.conf /etc/logagent.conf

# Commande d'exécution de Logagent avec le fichier de configuration
CMD ["logagent", "--config", "/etc/logagent.conf"]

