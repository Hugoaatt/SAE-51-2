# Utiliser une image Python
FROM python:3.9-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier le fichier requirements.txt et installer les dépendances
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copier le script Python
COPY testgraph.py .

# Exécuter le script lors du démarrage du conteneur
CMD ["python", "testgraph.py"]
